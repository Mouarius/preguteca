# Generated by Django 4.2 on 2023-12-31 17:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('question_library', '0046_menupage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpost',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]
