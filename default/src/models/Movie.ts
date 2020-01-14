import IMovie from "@/models/IMovie";
import Actor from "@/models/Actor";
import Review from "@/models/Review";

export default class Movie {

    // required fields
    id: number;
    title: string;
    description: string;
    poster: string;
    rating: number;

    // loaded-on-details subpage
    release: string;
    minutes: number;
    language: string;
    budget: number;
    genres: Array<string>;
    companies: Array<string>;
    cast: Array<Actor>;
    reviews: Array<Review>;

    constructor(data: IMovie) {

        this.id = data.id;
        this.title = data.title;
        this.description = data.description;
        this.poster = data.poster;
        this.rating = data.rating;

        this.release = '';
        this.minutes = 0;
        this.language = '';
        this.budget = 0;

        this.genres = [];
        this.companies = [];
        this.cast = [];
        this.reviews = [];

    }

}