# Generated by Django 4.2.10 on 2024-03-06 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('question_library', '0052_videoentrywithposition_category_ordered_videos'), ('question_library', '0053_alter_videoentrywithposition_options'), ('question_library', '0054_alter_videoentrywithposition_position')]

    dependencies = [
        ('question_library', '0051_auto_20240302_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoEntryWithPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField(db_index=True, default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_library.category')),
                ('video_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_library.videoentry')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='ordered_videos',
            field=models.ManyToManyField(related_name='+', through='question_library.VideoEntryWithPosition', to='question_library.videoentry', verbose_name='Ordered videos'),
        ),
    ]
