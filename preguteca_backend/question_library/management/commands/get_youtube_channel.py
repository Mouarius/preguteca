from django.core.exceptions import FieldDoesNotExist
from django.core.management import BaseCommand, CommandError

import json

from question_library.models import VideoEntry
from question_library.utils.youtube import get_youtube_video_channel_id_list, get_youtube_channel_information_list


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        video_id_list = []
        try:
            for tuple_id in VideoEntry.objects.exclude(youtube_id="").values_list("youtube_id"):
                video_id_list.append(tuple_id[0])
        except FieldDoesNotExist as e:
            raise CommandError(
                "The youtube_id field does not exist on this model, try to create it first."
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully retrieved ids from video entries.")
        )
        video_channel_id_list = get_youtube_video_channel_id_list(video_id_list)
        channel_id_list = [channel_id for youtube_id, channel_id in video_channel_id_list]
        channel_info_list = get_youtube_channel_information_list(channel_id_list)
        self.stdout.write(
            self.style.SUCCESS("Successfully written channel information from ids.")
        )
        with open("./channel_info_list.json", "w") as f:
            f.write(json.dumps(channel_info_list))
            f.close()
        

            
    
    