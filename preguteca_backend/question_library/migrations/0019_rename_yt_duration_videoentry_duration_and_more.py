# Generated by Django 4.1.7 on 2023-06-13 07:00

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('question_library', '0018_videoentry_yt_duration_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videoentry',
            old_name='yt_duration',
            new_name='duration',
        ),
        migrations.AlterField(
            model_name='videoentry',
            name='yt_publish_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 13, 9, 0, 43, 819461),
                                       verbose_name='Youtube - Video publication date'),
        ),
    ]
