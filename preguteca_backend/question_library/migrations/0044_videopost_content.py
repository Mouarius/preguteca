# Generated by Django 4.1.7 on 2023-11-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "question_library",
            "0043_alter_homepage_text_posts_alter_homepage_video_posts",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="videopost",
            name="content",
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]