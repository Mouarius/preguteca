from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from googleapiclient.discovery import build
from rest_framework import viewsets, permissions
from urllib3.exceptions import HTTPError

from preguteca_backend.settings import YOUTUBE_API_KEY
from .models import Category, extract_video_id_from_url
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def category_list(request):
    categories = Category.objects.all()
    template = loader.get_template("question_library/category_list.html")
    context = {"categories": categories}
    return HttpResponse(template.render(context, request))


def category_details(request, category_name):
    category = get_object_or_404(
        Category,
        name__startswith=category_name,
    )
    video_entries = category.video_entries.all()
    last_comments = category.comment_set.all()[:5]
    video_data_list = []

    if video_entries:
        video_id_list = [
            extract_video_id_from_url(video.url) for video in list(video_entries)
        ]
        video_data_list = fetchYoutubeVideoData(video_id_list)

    context = {
        "category": category,
        "video_entries": video_entries,
        "last_comments": last_comments,
        "video_data_list": video_data_list,
    }

    return render(request, "question_library/category_detail.html", context=context)


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
