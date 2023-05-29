from rest_framework import serializers

from question_library.models import Category, VideoEntry


class VideoEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoEntry
        fields = ["id", "title", "questions", "video_url", "views", "youtube_id", "language"]


class CategorySerializer(serializers.ModelSerializer):
    video_entries = VideoEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "full_name", "video_entries"]
        lookup_field = "name"
