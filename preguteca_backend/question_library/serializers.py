from rest_framework import serializers

from question_library.models import (
    Category,
    TextPost,
    VideoEntry,
    VideoPost,
    VideoType,
    HomePage,
)


class VideoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoType
        fields = "__all__"


class VideoEntrySerializer(serializers.ModelSerializer):
    video_types = VideoTypeSerializer(many=True, read_only=True)

    class Meta:
        model = VideoEntry
        fields = [
            "id",
            "title",
            "author",
            "questions",
            "video_url",
            "video_embed_url",
            "views",
            "language",
            "youtube_id",
            "yt_channel_title",
            "yt_channel_id",
            "yt_publish_time",
            "duration",
            "video_types",
            "thumbnail_url",
        ]


class CategorySerializer(serializers.ModelSerializer):
    video_entries = VideoEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "full_name", "description", "video_entries", "keywords"]
        lookup_field = "name"


class HomepageTextPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPost
        fields = "__all__"

class HomepageVideoPostSerializer(serializers.ModelSerializer):
    video = VideoEntrySerializer(read_only = True)
    class Meta:
        model = VideoPost
        fields = "__all__"

class HomepagePostSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        if isinstance(instance, TextPost):
            return HomepageTextPostSerializer().to_representation(instance)
        return HomepageVideoPostSerializer().to_representation(instance)
    

class HomePageSerializer(serializers.ModelSerializer):
    month_category = CategorySerializer(read_only=True)
    highlighted_video = VideoEntrySerializer(read_only=True)
    posts = HomepagePostSerializer(many=True, read_only=True)
    text_posts = HomepageTextPostSerializer(many=True, read_only=True)
    video_posts = HomepageVideoPostSerializer(many=True, read_only=True)

    class Meta:
        model = HomePage
        fields = "__all__"
