from __future__ import annotations


from django.db import models
from question_library.utils.common import iso8601_to_duration, to_snake_case
from question_library.utils.youtube import (
    create_embed_url,
    extract_video_id_from_url,
    get_youtube_videos_information_list,
)
from tinymce import models as tinymce_models
import datetime as dt


class Category(models.Model):
    name = models.SlugField(
        verbose_name="Name",
        max_length=50,
        unique=True,
        db_index=True,
        help_text="This is the indentifier of the category",
    )
    full_name = models.CharField(
        verbose_name="Full Name",
        max_length=50,
        help_text="The full name as displayed on the site",
    )
    description = models.TextField(
        verbose_name="Description", max_length=500, blank=True, null=True
    )
    keywords = models.CharField(
        verbose_name="Keywords", max_length=255, blank=True, null=True
    )

    # NOTE: Deprecated in favor of ordered_videos
    video_entries = models.ManyToManyField(
        "question_library.VideoEntry", verbose_name="Video entries"
    )

    ordered_videos = models.ManyToManyField(
        "question_library.VideoEntry",
        verbose_name="Ordered videos",
        through="VideoEntryWithPosition",
        related_name="+",
    )

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return f"/category/{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class PostWithPosition(models.Model):
    post = models.ForeignKey("question_library.Post", on_delete=models.CASCADE)
    home_page = models.ForeignKey("question_library.HomePage", on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["position"]


class HomePage(models.Model):
    active = models.BooleanField(verbose_name="Is active ?", default=False)
    identifier = models.CharField(verbose_name="Identifier", max_length=80)

    modified_at = models.DateTimeField(verbose_name="Modified at", auto_now=True)
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)

    month_category = models.ForeignKey(
        "question_library.Category",
        on_delete=models.DO_NOTHING,
        verbose_name="Category of the month",
    )
    month_questions = models.TextField(
        verbose_name="Questions of the month", max_length=500, blank=True, null=True
    )
    day_question = models.CharField(
        verbose_name="Question of the day", max_length=180, blank=True, null=True
    )
    highlighted_video = models.ForeignKey(
        "question_library.VideoEntry",
        on_delete=models.DO_NOTHING,
        verbose_name="Highlighted video",
    )

    posts = models.ManyToManyField("question_library.Post", through="PostWithPosition")

    def __str__(self) -> str:
        return f"HomePage : {self.identifier}"

    class Meta:
        verbose_name = "HomePage"
        verbose_name_plural = "HomePages"


class VideoType(models.Model):
    name = models.CharField(verbose_name="Name", max_length=20, blank=True)
    full_name = models.CharField(verbose_name="Full name", max_length=20)

    def save(self, **kwargs):
        if not self.name and self.full_name:
            self.name = to_snake_case(self.full_name)
        super().save(**kwargs)

    def __str__(self):
        return self.full_name


class VideoEntryWithPosition(models.Model):
    category = models.ForeignKey(
        to="question_library.Category", on_delete=models.CASCADE
    )
    video_entry = models.ForeignKey(
        to="question_library.VideoEntry", on_delete=models.CASCADE
    )
    position = models.PositiveSmallIntegerField(default=0, db_index=True)

    def __str__(self) -> str:
        return f"Video: {self.video_entry.title[:20]}... (id={self.video_entry.id})"

    class Meta:
        ordering = ["position"]


class VideoEntry(models.Model):
    visible = models.BooleanField(verbose_name="Is visible ?", default=True)
    title = models.CharField(
        verbose_name="Title", max_length=200, blank=True, default=""
    )
    questions = tinymce_models.HTMLField(
        verbose_name="Questions", max_length=2000, blank=True
    )
    author = models.CharField(
        verbose_name="Author", max_length=100, default="", blank=True
    )
    views = models.IntegerField(verbose_name="Views", default=0)
    language = models.CharField(
        verbose_name="Language", max_length=3, default="", blank=True
    )

    video_url = models.URLField(verbose_name="Video url", max_length=200, blank=False)
    video_embed_url = models.URLField(
        verbose_name="Embed url", max_length=200, default="", blank=True
    )
    thumbnail_url = models.URLField(
        verbose_name="Video thumblail url", default="", blank=True
    )

    youtube_id = models.CharField(
        max_length=16, verbose_name="Youtube video id", default="", blank=True
    )
    yt_channel_id = models.CharField(
        max_length=50, verbose_name="Youtube - Channel id", blank=True, null=True
    )
    yt_channel_title = models.CharField(
        max_length=100, verbose_name="Youtube - Channel title", blank=True
    )
    yt_publish_time = models.DateTimeField(
        verbose_name="Youtube - Video publication date", blank=True, null=True
    )
    duration = models.CharField(
        max_length=8, verbose_name="Youtube - Duration", blank=True
    )

    video_types = models.ManyToManyField(
        "question_library.VideoType", verbose_name="Video Type", blank=True
    )

    def __str__(self):
        return f"{self.title} (id={self.pk})"

    def save(self, **kwargs):
        if not self.youtube_id:
            try:
                youtube_id = extract_video_id_from_url(self.video_url)
                if not youtube_id:
                    return super().save(**kwargs)
                self.youtube_id = youtube_id
            except Exception:
                return super().save(**kwargs)

        if not self.title:
            info_list = get_youtube_videos_information_list([self.youtube_id])
            if info_list and len(info_list) > 0:
                snippet = info_list[0]["snippet"]
                details = info_list[0]["contentDetails"]
                self.title = snippet["title"]
                self.yt_channel_title = snippet["channelTitle"]
                self.yt_publish_time = dt.datetime.fromisoformat(snippet["publishedAt"])
                self.yt_embed_url = create_embed_url(self.youtube_id)
                self.thumbnail_url = snippet["thumbnails"]["high"]["url"]
                self.author = self.yt_channel_title
                self.duration = iso8601_to_duration(details["duration"])

        super().save(**kwargs)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"


class BasePost(models.Model):
    is_active = models.BooleanField(verbose_name="Is active ?", default=False)

    header_title = models.CharField(
        "Header - Title", max_length=100, blank=True, null=True
    )
    header_supplementary_information = models.CharField(
        "Header - Supplementary information", max_length=50, blank=True, null=True
    )

    footer_left_name = models.CharField(
        "Footer - Left name", max_length=50, blank=True, null=True
    )
    footer_left_value = models.CharField(
        "Footer - Left value", max_length=50, blank=True, null=True
    )

    footer_right_name = models.CharField(
        "Footer - Right name", max_length=50, blank=True, null=True
    )
    footer_right_value = models.CharField(
        "Footer - Right value", max_length=50, blank=True, null=True
    )

    modified_at = models.DateTimeField("Modified at", auto_now=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    def __str__(self):
        return f"{self.pk}: {self.header_title} ({self.created_at.strftime('%d/%m/%y %H:%M:%S')})"

    class Meta:
        abstract = True


class Post(BasePost):
    video = models.ForeignKey(
        to="question_library.VideoEntry",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    content = tinymce_models.HTMLField(verbose_name="Content", blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Comment(models.Model):
    category = models.ForeignKey(
        "question_library.Category", verbose_name="category", on_delete=models.CASCADE
    )
    author = models.CharField("author", max_length=50, default="unknown")
    text_content = models.TextField("text content", max_length=1000)
    creation_date = models.DateTimeField("creation date")

    def __str__(self):
        return f"Comment {self.pk} by {self.author}"


class MenuPage(models.Model):
    is_active = models.BooleanField(verbose_name="Is active", default=False)
    slug = models.SlugField(verbose_name="Slug", unique=True, db_index=True)
    title = models.CharField(verbose_name="Full name", max_length=100)
    content = tinymce_models.HTMLField(verbose_name="Content")
