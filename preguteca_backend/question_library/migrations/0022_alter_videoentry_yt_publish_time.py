# Generated by Django 4.1.7 on 2023-07-31 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "question_library",
            "0021_videoentry_visible_alter_videoentry_yt_publish_time",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="videoentry",
            name="yt_publish_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2023, 7, 31, 13, 4, 11, 671441),
                verbose_name="Youtube - Video publication date",
            ),
        ),
    ]
