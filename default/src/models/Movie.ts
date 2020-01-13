import IMovie from "@/models/IMovie";

export default class Movie {

    // required fields
    id: number;
    title: string;
    description: string;
    poster: string;
    rating: number;

    // loaded-on-details fields
    genres: Array<string> | null;
    release: string | null;
    minutes: number | null;
    language: string | null;
    companies: Array<string> | null;
    budget: number | null;

    constructor(data: IMovie) {
        this.id = data.id;
        this.title = data.title;
        this.description = data.description;
        this.poster = data.poster;
        this.rating = data.rating;
        this.genres = [];
        this.release = null;
        this.minutes = null;
        this.language = null;
        this.companies = [];
        this.budget = null;
    }

}