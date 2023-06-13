from django.core.management import BaseCommand

from question_library.models import VideoEntry
from question_library.utils.youtube import extract_video_id_from_url


class Command(BaseCommand):
    def handle(self, *args, **options):
        videos = VideoEntry.objects.all()
        for video in videos:
            yt_id = extract_video_id_from_url(video.video_url)
            if yt_id:
                video.youtube_id = yt_id
            video.save()
