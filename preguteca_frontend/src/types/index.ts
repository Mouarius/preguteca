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
  ytChannelId: string | null;
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
  video: TVideoEntry;
  content: string;
}

export interface HomePage {
  id: number;
  identifier: string;
  active: boolean;
  monthQuestions: string;
  dayQuestion: string;
  modifiedAt: string;
  createdAt: string;
  monthCategory: TCategory;
  highlightedVideo: TVideoEntry;
  posts: HomepagePost[];
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

export interface BaseCategory {
  id: number;
  name: string;
  fullName: string;
}

export interface TCategory extends BaseCategory {
  keywords: string | null;
  description: string;
  videoEntries: TVideoEntry[];
}

export type ActivePanel = "home" | "category" | "menu";
