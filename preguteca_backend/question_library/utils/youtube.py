from __future__ import annotations

import re

import requests

from preguteca_backend import settings

from googleapiclient import discovery


def extract_video_id_from_url(youtube_url: str) -> str | None:
    # video url is likely in this form : https://www.youtube.com/watch?v=[VIDEO_ID]&[SOME_OTHER_THINGS]
    if not youtube_url:
        return None
    pattern = re.compile("youtube\.com\/watch\?v=([0-9a-zA-Z\-_]{11})")
    if not pattern:
        return None
    video_id_match_list = re.findall(pattern, youtube_url)
    if not video_id_match_list:
        return None
    return video_id_match_list[0]


def get_youtube_videos_snippet_list(id_list: list[str]):
    batch_list = [id_list[i:i+50] for i in range(0, len(id_list), 50)]
    items = []
    for batch in batch_list:
        id_string = ",".join(batch)
        print(f"Fetching the data for {id_string}")
        query_url = f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id={id_string}&key={settings.YOUTUBE_API_KEY}"
        response = requests.get(query_url)
        print(f"Got ", response.status_code)
        data = response.json()
        if data["items"]:
            items = items + data["items"]

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
