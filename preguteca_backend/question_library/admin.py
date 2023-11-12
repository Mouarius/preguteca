from django.contrib import admin
from django.http.request import HttpRequest

from .models import (
    Category,
    Comment,
    TextPost,
    VideoEntry,
    VideoPost,
    VideoType,
    HomePage,
)

admin.site.register(
    [
        Comment,
        VideoType,
    ]
)


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ("month_category", "active", "created_at", "modified_at")
    autocomplete_fields = ("highlighted_video",)
    filter_horizontal = ("text_posts", "video_posts")


class HomepageBasePostAdmin(admin.ModelAdmin):
    header_fieldsets = (
        ("Header", {"fields": ("header_title", "header_supplementary_information")}),
    )
    footer_fieldsets = (
        (
            "Footer",
            {
                "fields": (
                    ("footer_left_name", "footer_left_value"),
                    ("footer_right_name", "footer_right_value"),
                )
            },
        ),
    )

    def get_fieldsets(self, request: HttpRequest, obj):
        fieldsets = super().get_fieldsets(request, obj)
        return [*self.header_fieldsets, *fieldsets, *self.footer_fieldsets]


@admin.register(TextPost)
class HomepageTextPostAdmin(HomepageBasePostAdmin):
    fieldsets = [
        ("Content", {"fields": ("content",)}),
    ]


@admin.register(VideoPost)
class HomepageVideoPostAdmin(HomepageBasePostAdmin):
    fieldsets = [("Content", {"fields": ("video","content")})]


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
