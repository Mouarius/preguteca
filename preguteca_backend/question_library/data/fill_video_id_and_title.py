from question_library.models import VideoEntry
from question_library.utils.youtube import extract_video_id_from_url, get_youtube_videos_snippet_list


def main():
    videos = VideoEntry.objects.all()
    video_id_batch = []
    for video in videos:
        video_id = extract_video_id_from_url(video.url)
        video_id_batch.append(video_id)

    items = get_youtube_videos_snippet_list(video_id_batch)
    for item in items:
        snippet = item["snippet"]
        if not snippet["title"]:
            print(f"Error with video with id {video_id}")
        video = VideoEntry.objects.filter(youtube_id=item["id"]).first()
        if not video:
            print(f"Video not found (id = {item['id']})")
        video.title = snippet['title']
        video.save()


if __name__ == "__main__":
    main()