from googleapiclient.discovery import build
from rest_framework import generics
from urllib3.exceptions import HTTPError

from preguteca_backend.settings import YOUTUBE_API_KEY
from .models import Category, VideoEntry
from .serializers import CategorySerializer, VideoEntrySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all().order_by("name").prefetch_related("video_entries")
    serializer_class = CategorySerializer
    lookup_field = "name"


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "name"


class VideoEntryList(generics.ListAPIView):
    queryset = VideoEntry.objects.all().order_by("id")
    serializer_class = VideoEntrySerializer


class VideoEntryDetail(generics.RetrieveAPIView):
    queryset = VideoEntry.objects.all()
    serializer_class = VideoEntrySerializer


def fetchYoutubeVideoData(video_id_list):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    videos = youtube.videos()
    req = videos.list(
        part="snippet,contentDetails,statistics",
        id=video_id_list,
        access_token=YOUTUBE_API_KEY,
        fields="items(id, snippet, statistics)",
    )
    video_data_list = []
    try:
        res = req.execute()
        video_data_list = res["items"]

    except HTTPError as e:
        print(
            "Error response status code : {0}, reason : {1}".format(
                e.status_code, e.error_details
            )
        )

    youtube.close()
    return video_data_list
