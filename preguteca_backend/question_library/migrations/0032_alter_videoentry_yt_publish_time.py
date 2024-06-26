# Generated by Django 4.1.7 on 2023-10-15 22:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "question_library",
            "0031_category_keywords_alter_category_description_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="videoentry",
            name="yt_publish_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2023, 10, 16, 0, 26, 23, 29931),
                verbose_name="Youtube - Video publication date",
            ),
        ),
    ]
