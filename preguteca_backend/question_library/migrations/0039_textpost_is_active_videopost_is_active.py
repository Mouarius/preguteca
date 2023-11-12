# Generated by Django 4.1.7 on 2023-11-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question_library", "0038_textpost_videopost"),
    ]

    operations = [
        migrations.AddField(
            model_name="textpost",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="Is active ?"),
        ),
        migrations.AddField(
            model_name="videopost",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="Is active ?"),
        ),
    ]