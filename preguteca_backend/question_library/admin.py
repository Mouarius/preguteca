from django.contrib import admin
from django.db import models
from django.http.request import HttpRequest
from django.utils.html import format_html
from django.forms import (
    TextInput,
)
from adminsortable2.admin import (
    SortableAdminBase,
    SortableInlineAdminMixin,
)

from .models import (
    Category,
    Comment,
    MenuPage,
    Post,
    VideoEntry,
    VideoType,
    HomePage,
)

admin.site.register([Comment, VideoType])


class OrderedPostInline(SortableInlineAdminMixin, admin.TabularInline):
    model = HomePage.ordered_posts.through
    raw_id_fields = ["post"]
    extra = 0


@admin.register(HomePage)
class HomePageAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("identifier", "active", "created_at", "modified_at")
    autocomplete_fields = ("highlighted_video",)
    inlines = [OrderedPostInline]


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


@admin.register(Post)
class PostAdmin(HomepageBasePostAdmin):
    raw_id_fields = ["video"]
    fieldsets = [
        ("Content", {"fields": ("content", "video")}),
    ]

class OrderedVideoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Category.ordered_videos.through
    raw_id_fields = ["video_entry"]
    extra = 0


@admin.register(Category)
class CategoryAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ["full_name", "name"]
    search_fields = ["full_name"]
    readonly_fields = ["name"]
    fields = (
        ("full_name", "name"),
        "description",
        "keywords",
    )
    inlines = [OrderedVideoInline]


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
