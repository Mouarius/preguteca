from django.contrib import admin

from .models import Category, Comment, VideoEntry, VideoType

admin.site.register([Comment, VideoType])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ("name", "full_name", "video_entries")
    filter_horizontal = ("video_entries",)


@admin.register(VideoEntry)
class VideoEntryAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "questions",
        "video_url",
        "views",
        "language",
        "video_types",
        "youtube_id",
    )
    readonly_fields = ("youtube_id",)
    filter_horizontal = ("video_types",)
