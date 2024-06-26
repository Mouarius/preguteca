# Generated by Django 4.1.7 on 2023-07-31 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question_library", "0024_alter_videoentry_thumbnail_url_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="videoentry",
            name="author",
            field=models.CharField(
                blank=True, default="", max_length=100, verbose_name="author"
            ),
        ),
        migrations.AlterField(
            model_name="videoentry",
            name="yt_publish_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2023, 7, 31, 13, 22, 14, 673951),
                verbose_name="Youtube - Video publication date",
            ),
        ),
    ]
