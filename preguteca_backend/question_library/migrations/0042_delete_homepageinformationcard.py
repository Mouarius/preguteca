# Generated by Django 4.1.7 on 2023-11-12 16:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("question_library", "0041_remove_homepage_information_cards_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="HomePageInformationCard",
        ),
    ]
