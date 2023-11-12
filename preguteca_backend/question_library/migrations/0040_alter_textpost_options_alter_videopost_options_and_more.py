# Generated by Django 4.1.7 on 2023-11-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question_library", "0039_textpost_is_active_videopost_is_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="textpost",
            options={
                "verbose_name": "Homepage - Text Post",
                "verbose_name_plural": "Homepage - Text Posts",
            },
        ),
        migrations.AlterModelOptions(
            name="videopost",
            options={
                "verbose_name": "Homepage - Video Post",
                "verbose_name_plural": "Homepage - Video Posts",
            },
        ),
        migrations.RemoveField(
            model_name="textpost",
            name="title",
        ),
        migrations.RemoveField(
            model_name="videopost",
            name="title",
        ),
        migrations.AddField(
            model_name="textpost",
            name="footer_left_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Footer - Left name"
            ),
        ),
        migrations.AddField(
            model_name="textpost",
            name="footer_left_value",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Footer - Left value"
            ),
        ),
        migrations.AddField(
            model_name="textpost",
            name="footer_right_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Footer - Right name"
            ),
        ),
        migrations.AddField(
            model_name="textpost",
            name="footer_right_value",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Footer - Right value",
            ),
        ),
        migrations.AddField(
            model_name="textpost",
            name="header_supplementary_information",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Header - Supplementary information",
            ),
        ),
        migrations.AddField(
            model_name="textpost",
            name="header_title",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Header - Title"
            ),
        ),
        migrations.AddField(
            model_name="videopost",
            name="footer_left_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Footer - Left name"
            ),
        ),
        migrations.AddField(
            model_name="videopost",
            name="footer_left_value",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Footer - Left value"
            ),
        ),
        migrations.AddField(
            model_name="videopost",
            name="footer_right_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Footer - Right name"
            ),
        ),
        migrations.AddField(
            model_name="videopost",
            name="footer_right_value",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Footer - Right value",
            ),
        ),
        migrations.AddField(
            model_name="videopost",
            name="header_supplementary_information",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Header - Supplementary information",
            ),
        ),
        migrations.AddField(
            model_name="videopost",
            name="header_title",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Header - Title"
            ),
        ),
    ]
