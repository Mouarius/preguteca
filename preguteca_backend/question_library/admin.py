from django.contrib import admin

from .models import (
    Category,
    Comment,
    VideoEntry,
    VideoType,
    HomePage,
    HomePageInformationCard,
)

admin.site.register([Comment, VideoType])


@admin.register(HomePageInformationCard)
class HomePageInformationCardAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "modified_at"]


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ("month_category", "active", "created_at", "modified_at")
    autocomplete_fields = ("highlighted_video",)
    filter_horizontal = ("information_cards",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["full_name", "name"]
    search_fields = ["full_name"]
    fields = ("name", "full_name", "description", "keywords", "video_entries")
    filter_horizontal = ("video_entries",)


@admin.register(VideoEntry)
class VideoEntryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "visible", "video_url"]
    search_fields = ["title", "youtube_id", "author"]
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
