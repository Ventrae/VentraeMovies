export default class Review {
    id: string;
    author: string;
    content: string;
    positivity: number;
    time: string;

    constructor(id: string, author: string, content: string, positivity: number, time: string) {
        this.id = id;
        this.author = author;
        this.content = content;
        this.positivity = positivity;
        this.time = time;
    }
}