from rest_framework import generics
from django.views.generic import TemplateView

from .models import Category, MenuPage, Post, VideoEntry, HomePage
from .serializers import (
    CategorySerializer,
    MenuPageSerializer,
    VideoEntrySerializer,
    HomePageSerializer,
)


class DefaultView(TemplateView):
    template_name = "question_library/index.html"


class HomePageView(generics.ListAPIView):
    queryset = HomePage.objects.filter(active=True)
    serializer_class = HomePageSerializer


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


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()


class MenuPageList(generics.ListAPIView):
    queryset = MenuPage.objects.filter(is_active=True)
    serializer_class = MenuPageSerializer
    lookup_field = "slug"
