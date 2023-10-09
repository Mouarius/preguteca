export interface TVideoType {
  id: number;
  name: string;
  fullName: string;
}
export interface TVideoEntry {
  id: number;
  title: string;
  author: string;
  questions: string;
  videoUrl: string;
  videoEmbedUrl: string;
  views: number;
  language: string;
  youtubeId: string;
  ytChannelTitle: string;
  ytPublishTime: string;
  thumbnailUrl: string;
  duration: string;
  videoTypes: TVideoType[];
}

export interface TCategory {
  id: number;
  name: string;
  fullName: string;
  videoEntries: TVideoEntry[];
}
