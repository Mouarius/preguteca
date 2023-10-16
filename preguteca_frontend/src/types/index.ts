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

export interface HomePage {
  id: number;
  active: boolean;
  monthQuestions: string;
  dayQuestion: string;
  monthCategory: TCategory;
  highlightedVideo: TVideoEntry;
  informationCards: HomePageInformationCard[];
}

export interface HomePageInformationCard {
  id: number;
  title: string;
  content: string;
  modifiedAt: string;
  createdAt: string;
}

export interface TCategory {
  id: number;
  name: string;
  keywords: string;
  fullName: string;
  videoEntries: TVideoEntry[];
  description: string;
}
