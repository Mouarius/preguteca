from django.contrib import admin
from django.db import models
from django.http.request import HttpRequest
from django.utils.html import format_html
from django.forms import TextInput

from .models import (
    Category,
    Comment,
    MenuPage,
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
    list_display = ("identifier", "active", "created_at", "modified_at")
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
    fieldsets = [("Content", {"fields": ("video", "content")})]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["full_name", "name"]
    search_fields = ["full_name"]
    fields = ("name", "full_name", "description", "keywords", "video_entries")
    filter_horizontal = ("video_entries",)


@admin.register(VideoEntry)
class VideoEntryAdmin(admin.ModelAdmin):
    list_display = ["id", "trimmed_title", "categories", "visible"]
    search_fields = ["title", "youtube_id", "author"]
    empty_value_display = "???"

    list_filter = (
        "visible",
        "category",
    )

    @admin.display
    def trimmed_title(self, obj):
        return format_html(
            f"<span style='width: 100%; display:flex; justify-content:space-between'>{obj.title[:40]}... <a href='{obj.video_url}'>(link)</a></span>"
        )


    @admin.display
    def categories(self, obj):
        return list(obj.category_set.values_list("full_name", flat=True))

    fields = (
        "title",
        "visible",
        "author",
        "questions",
        ("video_url", "video_embed_url"),
        "thumbnail_url",
        "views",
        "language",
        "video_types",
        "youtube_id",
    )

    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 80})}}
    readonly_fields = ("youtube_id",)
    filter_horizontal = ("video_types",)


@admin.register(MenuPage)
class MenuPageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    fields = ("is_active", ("title", "slug"), "content")

    prepopulated_fields = {"slug": ["title"]}
