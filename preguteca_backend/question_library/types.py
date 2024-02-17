from typing import TypedDict


class YoutubeApiThumbnail(TypedDict):
    url: str
    width: int
    height: int


class YoutubeApiThumbnails(TypedDict):
    default: YoutubeApiThumbnail
    medium: YoutubeApiThumbnail
    high: YoutubeApiThumbnail
    standard: YoutubeApiThumbnail
    maxres: YoutubeApiThumbnail


class YoutubeApiLocalized(TypedDict):
    title: str
    description: str


class YoutubeApiSnippet(TypedDict):
    publishedAt: str  # isoformat datetime
    channelId: str
    title: str
    description: str
    thumbnails: YoutubeApiThumbnails
    channelTitle: str
    categoryId: str
    liveBroadcastContent: str
    localized: YoutubeApiLocalized
    defaultAudioLanguage: str


class YoutubeApiContentDetails(TypedDict):
    duration: str
    dimension: str
    definition: str
    caption: str
    licensedContent: bool
    contentRating: dict
    projection: str


class YoutubeApiResponseItem(TypedDict):
    kind: str
    etag: str
    id: str
    snippet: YoutubeApiSnippet
    contentDetails: YoutubeApiContentDetails


class YoutubeApiResponse(TypedDict):
    kind: str
    etag: str
    items: list[YoutubeApiResponseItem]
