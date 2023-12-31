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
  ytChannelId: string;
  thumbnailUrl: string;
  duration: string;
  videoTypes: TVideoType[];
}

export interface HomepagePost {
  id: number;
  isActive: boolean;
  headerTitle: string;
  headerSupplementaryInformation: string | null;
  footerLeftName: string | null;
  footerLeftValue: string | null;
  footerRightName: string | null;
  footerRightValue: string | null;
  modifiedAt: string;
  createdAt: string;
}

export interface HomepageTextPost extends HomepagePost {
  content: string
}

export interface HomepageVideoPost extends HomepagePost {
  video: TVideoEntry
  content: string
}

export interface HomePage {
  id: number;
  active: boolean;
  monthQuestions: string;
  dayQuestion: string;
  monthCategory: TCategory;
  highlightedVideo: TVideoEntry;
  posts: HomepagePost[];
  textPosts: HomepageTextPost[];
  videoPosts: HomepageVideoPost[];

}

export interface MenuPage {
  id: number;
  isActive: boolean;
  slug: string;
  title: string;
  content: string;
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

export type ActivePanel = "home" | "category" | "custom"
