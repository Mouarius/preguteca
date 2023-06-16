export interface TVideoEntry {
    id: number,
    title: string,
    questions: string,
    videoUrl: string,
    views: number,
    language: string,
    youtubeId: string,
    ytChannelTitle: string,
    ytPublishTime: string,
    duration: string,

}

export interface TCategory {
    id: number,
    name: string,
    fullName: string,
    videoEntries: TVideoEntry[]
}

