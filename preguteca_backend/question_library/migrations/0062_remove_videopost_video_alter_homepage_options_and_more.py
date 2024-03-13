# Generated by Django 4.2.10 on 2024-03-13 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_library', '0061_auto_20240313_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videopost',
            name='video',
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'HomePage', 'verbose_name_plural': 'HomePages'},
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='text_posts',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='video_posts',
        ),
        migrations.DeleteModel(
            name='TextPost',
        ),
        migrations.DeleteModel(
            name='VideoPost',
        ),
    ]
