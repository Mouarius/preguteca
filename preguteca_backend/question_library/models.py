from __future__ import annotations

import re

from django.db import models
from unidecode import unidecode


def to_snake_case(string: str) -> str:
    string = unidecode(string)
    string = (
        re.sub(r"(?<=[a-z])(?=[A-Z])|[^a-zA-Z]", " ", string).strip().replace(" ", "_")
    )
    return "".join(string.lower())


class Category(models.Model):
    name = models.CharField("name", max_length=50, unique=True)
    full_name = models.CharField("full name", max_length=50)
    video_entries = models.ManyToManyField(
        "question_library.VideoEntry", verbose_name="Video entries"
    )
    description = models.TextField("Description", max_length=500, blank=True, null=True)
    keywords = models.CharField("Keywords", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return f"/category/{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class HomePage(models.Model):
    active = models.BooleanField("Is active ?", default=False)
    month_category = models.ForeignKey(
        "question_library.Category",
        on_delete=models.CASCADE,
        verbose_name="Category of the month",
    )
    month_questions = models.TextField(
        "Questions of the month", max_length=500, blank=True, null=True
    )
    day_question = models.CharField(
        "Question of the day", max_length=180, blank=True, null=True
    )
    highlighted_video = models.ForeignKey(
        "question_library.VideoEntry",
        on_delete=models.CASCADE,
        verbose_name="Highlighted video",
    )
    information_cards = models.ManyToManyField(
        "question_library.HomePageInformationCard"
    )
    modified_at = models.DateTimeField("Modified at", auto_now=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class HomePageInformationCard(models.Model):
    title = models.CharField("Title", max_length=180, blank=True, null=True)
    content = models.TextField("Content", max_length=1000, blank=True, null=True)
    modified_at = models.DateTimeField("Modified at", auto_now=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        verbose_name = "Information Card"
        verbose_name_plural = "Information Cards"

    def __str__(self) -> str:
        return f"{ self.title } ({self.modified_at.strftime('%d/%m/%y %H:%M:%S')})"


class VideoType(models.Model):
    name = models.CharField(max_length=20, blank=True)
    full_name = models.CharField(max_length=20)

    def save(self, **kwargs):
        if not self.name and self.full_name:
            self.name = to_snake_case(self.full_name)
        super().save(**kwargs)

    def __str__(self):
        return self.full_name


class VideoEntry(models.Model):
    visible = models.BooleanField(verbose_name="Est Visible ?", default=True)
    title = models.CharField("title", max_length=200, blank=True, default="")
    questions = models.TextField("questions", max_length=2000, blank=True)
    video_url = models.CharField("video url", max_length=200, blank=True)
    video_embed_url = models.CharField(
        "video embed url", max_length=200, default="", blank=True
    )
    author = models.CharField("author", max_length=100, default="", blank=True)
    views = models.IntegerField("views", default=0)
    language = models.CharField(max_length=3, default="", blank=True)
    video_types = models.ManyToManyField(
        "question_library.VideoType", verbose_name="Video Type", blank=True
    )
    youtube_id = models.CharField(
        max_length=16, verbose_name="Youtube video id", default="", blank=True
    )
    yt_channel_title = models.CharField(
        max_length=100, verbose_name="Youtube - Channel title", blank=True
    )
    yt_publish_time = models.DateTimeField(
        verbose_name="Youtube - Video publication date",
        blank=True,
    )
    duration = models.CharField(
        max_length=8, verbose_name="Youtube - Duration", blank=True
    )
    thumbnail_url = models.URLField(
        verbose_name="Video thumblail url", default="", blank=True
    )

    def __str__(self):
        return f"{self.title} (id={self.id})"

    def save(self, **kwargs):
        # if not self.youtube_id:
        #     self.youtube_id = extract_video_id_from_url(self.video_url)
        # if not self.title:
        #     data = get_youtube_videos_snippet_list([self.youtube_id])
        #     if data:
        #         snippet = data[0]["snippet"]
        #         self.title = snippet["title"]
        #         self.yt_channel_title = snippet["channelTitle"]
        super().save(**kwargs)

    class Meta:
        verbose_name_plural = "Video entries"


class Comment(models.Model):
    category = models.ForeignKey(
        "question_library.Category", verbose_name="category", on_delete=models.CASCADE
    )
    author = models.CharField("author", max_length=50, default="unknown")
    text_content = models.TextField("text content", max_length=1000)
    creation_date = models.DateTimeField("creation date")

    def __str__(self):
        return f"Comment {self.pk} by {self.author}"
