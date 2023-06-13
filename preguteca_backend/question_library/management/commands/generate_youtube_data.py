from django.core.exceptions import FieldDoesNotExist
from django.core.management import BaseCommand, CommandError

from question_library.models import VideoEntry
from question_library.utils.common import iso8601_to_duration
from question_library.utils.youtube import get_youtube_videos_information_list


class Command(BaseCommand):
    def handle(self, *args, **options):
        yt_id_list = []
        try:
            for tuple_id in VideoEntry.objects.all().values_list("youtube_id"):
                yt_id_list.append(tuple_id[0])
        except FieldDoesNotExist as e:
            raise CommandError("The youtube_id field does not exist on this model, try to create it first.")

        self.stdout.write(self.style.SUCCESS("Successfully retrieved ids from video entries."))

        self.stdout.write("Retrieving data from Youtube API...")
        information_list = get_youtube_videos_information_list(id_list=yt_id_list)
        self.stdout.write(self.style.SUCCESS("Successfully retrieved snippet and contentDetails from Youtube API."))

        for information in information_list:
            video = VideoEntry.objects.filter(youtube_id=information["id"])[0]
            snippet = information["snippet"]
            details = information["contentDetails"]
            if not video or not details or not snippet:
                continue
            yt_publish_time = snippet["publishedAt"]
            title = snippet["title"]
            yt_channel_title = snippet["channelTitle"]
            duration_iso = details["duration"]
            duration = iso8601_to_duration(duration_iso)
            video.yt_channel_title = yt_channel_title
            video.duration = duration
            video.title = title
            video.yt_publish_time = yt_publish_time
            video.save()
        self.stdout.write(self.style.SUCCESS("Successfully updated the video entries data from the database."))
