from __future__ import annotations

import re
from typing import cast

import requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from preguteca_backend import settings
from question_library.types import (
    YoutubeApiResponse,
    YoutubeApiResponseItem,
    YoutubeApiSnippet,
)


def extract_video_id_from_url(youtube_url: str) -> str | None:
    # video url is likely in this form : https://www.youtube.com/watch?v=[VIDEO_ID]&[SOME_OTHER_THINGS]
    if not youtube_url:
        return None
    pattern = re.compile(
        r"(?:youtu\.be/|youtube\.com/(?:watch\?(?:.*&)?v=|(?:embed|v)/))([^/?]{11})"
    )
    if not pattern:
        return None
    video_id_match_list = re.findall(pattern, youtube_url)
    if not video_id_match_list:
        return None
    return video_id_match_list[0]


# DEPRECATED
def get_youtube_videos_snippet_list(id_list: list[str]) -> list[YoutubeApiSnippet]:
    batch_list = [id_list[i : i + 50] for i in range(0, len(id_list), 50)]
    items = []
    for batch in batch_list:
        id_string = ",".join(batch)
        print(f"Fetching the data for {id_string}")
        query_url = f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id={id_string}&key={settings.YOUTUBE_API_KEY}"
        response = requests.get(query_url)
        print("Got ", response.status_code)
        data: YoutubeApiResponse = response.json()
        if data["items"]:
            items = items + data["items"]
    return items


def get_youtube_videos_information_list(
    id_list: list[str],
) -> list[YoutubeApiResponseItem]:
    youtube = build("youtube", "v3", developerKey=settings.YOUTUBE_API_KEY)
    batch_list = [id_list[i : i + 50] for i in range(0, len(id_list), 50)]
    items: list[YoutubeApiResponseItem] = []
    for batch in batch_list:
        id_string = ",".join(batch)
        request = youtube.videos().list(part="snippet,contentDetails", id=id_string)
        try:
            response = cast(YoutubeApiResponse, request.execute())
            if response["items"]:
                items = items + response["items"]
        except HttpError as e:
            print(
                f"Error response status code : {e.status_code}, reason : {e.error_details}"
            )
    return items


def get_youtube_video_snippet(youtube_id: str) -> str | None:
    if not youtube_id:
        return None

    query_url = f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id={youtube_id}&key={settings.YOUTUBE_API_KEY}"

    response = requests.get(query_url)
    data = response.json()
    if data["items"]:
        video_info = data["items"][0]
        return video_info["snippet"]


def get_youtube_video_channel_id_list(video_id_list: list[str]) -> tuple[str, str]:
    if not video_id_list:
        return None
    information_list = get_youtube_videos_information_list(video_id_list)
    channel_id_list = []
    for info in information_list:
        channel_id_list.append((info["id"], info["snippet"]["channelId"]))
    return channel_id_list


def get_youtube_channel_information_list(channel_id_list: list[str]):
    youtube = build("youtube", "v3", developerKey=settings.YOUTUBE_API_KEY)
    batch_list = [
        channel_id_list[i : i + 50] for i in range(0, len(channel_id_list), 50)
    ]
    items = []
    for batch in batch_list:
        id_string = ",".join(batch)
        request = youtube.channels().list(
            part="snippet,contentDetails,contentOwnerDetails", id=id_string
        )
        try:
            response = request.execute()
            if response["items"]:
                items = items + response["items"]
        except HttpError as e:
            print(
                f"Error response status code : {e.status_code}, reason : {e.error_details}"
            )
    return items


def create_embed_url(youtube_id: str):
    return f"https://www.youtube.com/embed/{youtube_id}"
