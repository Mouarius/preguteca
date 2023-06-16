from rest_framework import generics

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
