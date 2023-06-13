import json
import os.path

from django.core.management import BaseCommand, CommandError

from preguteca_backend import settings
from question_library.models import Category, VideoType, VideoEntry


def get_or_create_category(category_name, category_fullname):
    if not category_name:
        raise ValueError(f'Category name is {type(category_name)}')
    category_qs = Category.objects.filter(name=category_name).first()
    if not category_qs:
        category_qs = Category.objects.create(name=category_name, full_name=category_fullname)
    return category_qs


def get_or_create_video_type(full_name):
    if not full_name:
        return None
    video_type_qs = VideoType.objects.filter(full_name=full_name).first()
    if not video_type_qs:
        video_type_qs = VideoType.objects.create(full_name=full_name)
    return video_type_qs


class Command(BaseCommand):
    help = "Load video entries from a json file"

    video_data_json_path = os.path.join(settings.BASE_DIR, "question_library/data/video_data__parsed.json")

    def handle(self, *args, **options):
        with open(self.video_data_json_path) as file:
            try:
                video_entries = json.load(file)
            except json.JSONDecodeError:
                raise CommandError("Unable to load JSON data.")

            for video in video_entries:
                category = get_or_create_category(video["category_name"], video["category_fullname"])
                if not category:
                    raise CommandError(
                        f"Trying to create a category with name={video['category_name']} of type {type(video['category_name'])}")
                video_type = get_or_create_video_type(video["video_type"])
                new_video = VideoEntry(video_url=video["video_url"], questions=video["questions"],
                                       language=video["language"])
                new_video.save()
                new_video.video_types.add(video_type)
                category.video_entries.add(new_video)
