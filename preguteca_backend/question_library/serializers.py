from rest_framework import serializers

from question_library.models import (
    Category,
    MenuPage,
    Post,
    VideoEntry,
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
    class Meta:
        model = Category
        fields = ["id", "name", "full_name"]
        lookup_field = "name"


class CategoryDetailedSerializer(serializers.ModelSerializer):
    video_entries = serializers.SerializerMethodField()

    def get_video_entries(self, obj):
        videos = obj.ordered_videos.order_by("videoentrywithposition__position")
        return VideoEntrySerializer(videos, many=True).data

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "full_name",
            "description",
            "video_entries",
            "keywords",
        ]
        lookup_field = "name"


class HomepagePostSerializer(serializers.ModelSerializer):
    video = VideoEntrySerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class HomePageSerializer(serializers.ModelSerializer):
    month_category = CategoryDetailedSerializer(read_only=True)
    posts = serializers.SerializerMethodField()

    def get_posts(self, obj):
        posts = obj.posts.order_by("postwithposition__position")
        return HomepagePostSerializer(posts, many=True).data

    class Meta:
        model = HomePage
        fields = [
            "active",
            "identifier",
            "modified_at",
            "created_at",
            "month_category",
            "month_questions",
            "day_question",
            "posts"
        ]


class MenuPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPage
        fields = "__all__"
