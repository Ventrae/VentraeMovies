export default class Actor {
    id: number;
    character: string;
    name: string;
    image: string;

    constructor(id: number, character: string, name: string, image: string) {
        this.id = id;
        this.character = character;
        this.name = name;
        this.image = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + image;
    }

}