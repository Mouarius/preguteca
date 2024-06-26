# Generated by Django 4.1.7 on 2023-03-08 23:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question_library", "0005_alter_comment_text_content_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="full_name",
            field=models.CharField(
                default="default_name", max_length=50, verbose_name="name"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=50, unique=True, verbose_name="name"),
        ),
    ]
