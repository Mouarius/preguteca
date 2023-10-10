from django.contrib import admin

from .models import Category, Comment, VideoEntry, VideoType

admin.site.register([Comment, VideoType])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "full_name"]
    fields = ("name", "full_name", "description", "video_entries")
    filter_horizontal = ("video_entries",)


@admin.register(VideoEntry)
class VideoEntryAdmin(admin.ModelAdmin):
    list_display = ["video_title", "visible", "video_url"]
    search_fields = ["youtube_id", "author"]
    empty_value_display = "???"

    @admin.display(empty_value="???")
    def video_title(self, obj):
        if not obj.title:
            return "???"
        return obj.title

    fields = (
        (
            "title",
            "visible",
        ),
        "author",
        "questions",
        ("video_url", "video_embed_url"),
        "thumbnail_url",
        "views",
        "language",
        "video_types",
        "youtube_id",
    )
    readonly_fields = ("youtube_id",)
    filter_horizontal = ("video_types",)
