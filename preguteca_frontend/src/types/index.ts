export interface TVideoEntry {
    id: number,
    title: string,
    questions: string,
    video_url: string,
    views: number,
    youtube_id: string,
    language: string
}

export interface TCategory {
    id: number,
    name: string,
    full_name: string,
    video_entries: TVideoEntry[]
}

