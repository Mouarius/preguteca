from django.test import TestCase
from urllib3.exceptions import HTTPError
from .models import extract_video_id_from_url, VideoEntry, Category
from preguteca_backend.settings import YOUTUBE_API_KEY
from googleapiclient.discovery import build


class YoutubeApiTestCase(TestCase):
    def setUp(self) -> None:
        self.url1 = "https://www.youtube.com/watch?v=LFB9WJeBCdA&ab_channel=TEDxTalks"

    def test_extract_video_id_not_found(self):
        video_id = extract_video_id_from_url("ajfhhsfd")
        self.assertEqual(video_id, None)

    def test_extract_video_id(self):
        video_id = extract_video_id_from_url(self.url1)
        self.assertEqual(video_id, "LFB9WJeBCdA")

    def test_request_api_get_video_object(self):
        video_id = "LFB9WJeBCdA"
        youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
        videos = youtube.videos()
        request = videos.list(
            part="snippet,contentDetails,statistics",
            id=video_id,
            access_token=YOUTUBE_API_KEY,
            fields="items(id, snippet, statistics)",
        )
        try:
            response = request.execute()
        except HTTPError as e:
            print(
                "Error response status code : {0}, reason : {1}".format(
                    e.status_code, e.error_details
                )
            )
        youtube.close()
        video_item = response["items"][0]
        self.assertEqual(video_item["id"], video_id)


class VideoEntryTestCase(TestCase):
    def setUp(self) -> None:
        self.category1 = Category.objects.create(
            name="test_category", full_name="Test Category"
        )
        self.video1 = VideoEntry.objects.create(
            category=self.category1,
            title="Test Video Title",
            url="https://www.youtube.com/watch?v=7fERX0OXAIY",
            questions="Question 1? Question 2?",
        )

    def test_video_exists_in_category(self):
        videos_list = self.category1.videoentry_set.all()
        self.assertListEqual(list(videos_list), [self.video1])

    def test_video_embed_url(self):
        self.assertEqual(
            self.video1.embed_url, "https://www.youtube.com/embed/7fERX0OXAIY"
        )
