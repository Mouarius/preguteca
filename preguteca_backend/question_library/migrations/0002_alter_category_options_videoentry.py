# Generated by Django 4.1.7 on 2023-03-08 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question_library", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.CreateModel(
            name="VideoEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="title")),
                (
                    "questions",
                    models.TextField(max_length=500, verbose_name="questions"),
                ),
                ("link", models.CharField(max_length=80, verbose_name="video link")),
                ("views", models.IntegerField(default=0, verbose_name="views")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="question_library.category",
                        verbose_name="category",
                    ),
                ),
            ],
        ),
    ]
