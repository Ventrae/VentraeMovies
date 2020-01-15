<template>
    <div class="container-fluid px-0 py-5 mt-5 white" id="page-movie">

        <mdb-container>
            <mdb-jumbotron class="mb-0 d-flex p-4 justify-content-between align-items-center bg-dark">
                <div class="d-flex align-items-center">
                    <a href="#" class="my-0 mr-3 text-white" @click="$router.go(-1)">
                        <i class="fa fa-chevron-left mr-1"></i>
                    </a>
                    <h3 class="h4 text-light m-0">
                        {{ movie === null ? '' : movie.title }}
                        <span class="h6 text-muted">
                            | {{ movie === null ? '' : movie.id }}
                        </span>
                    </h3>
                </div>

                <div class="h4 text-light m-0">
                    {{ movie === null ? '' : movie.rating }} / 10
                    <i class="fas fa-star text-warning"></i>
                </div>
            </mdb-jumbotron>

            <mdb-jumbotron class="mb-0 d-flex pl-0 pr-4 py-0 align-items-center" style="background-color: #f3f3f3" fluid>

                <div>
                    <img
                            width="360"
                            :alt="movie.title"
                            :src="movie.poster"
                            class="mr-5"
                    />
                </div>

                <div>

                    <p v-if="movie.genres.length" class="lead">
                        <mdb-badge class="ml-1" :color="genreColor(genre)" v-for="genre in movie.genres">
                            {{ genre }}
                        </mdb-badge>
                    </p>

                    <p v-if="movie.companies.length">
                        Producenci:
                        <template v-for="(company, index) in movie.companies">
                            {{ company }}
                            <template v-if="index !== movie.companies.length-1">,</template>
                        </template>
                    </p>

                    <hr class="my-4"/>

                    <p v-if="movie !== null">
                        Opis: {{ movie.description }}
                    </p>


                    <div class="d-flex">
                        <b v-if="movie.release !== null">
                            Premiera: {{ movie.release }}r.
                        </b>
                        <p class="mx-2">|</p>
                        <b v-if="movie.budget !== null">
                            Budżet: {{ movie.budget }}$
                        </b>
                    </div>

                    <star-rating
                            :increment="0.1"
                            :max-rating="10"
                            :round-start-rating="false"
                            v-model="userRating"
                            inactive-color="#abb8ed"
                            active-color="#5771db"
                            @rating-selected="rateMovie(userRating)"
                    />

                </div>

            </mdb-jumbotron>

            <hr/>

        </mdb-container>


        <mdb-jumbotron class="mb-0 d-flex p-4 flex-column align-items-center bg-dark px-0 container-fluid">

            <h4 class="h4 text-light mb-4 align-self-start container">
                Obsada
            </h4>

            <div class="row mx-auto container px-5">

                <div class="d-flex flex-column mx-auto mt-1"
                     v-for="actor of movie.cast">
                    <figure class="text-center">
                        <img
                                width="230"
                                :alt="actor.name"
                                :src="actor.image"
                                class="mx-auto mb-2"
                                v-if="actor.image"
                        />
                        <div class="spinner-border text-primary" role="status" v-if="!actor.image">
                            <span class="sr-only">Loading...</span>
                        </div>
                        <figcaption class="mt-1 text-light">
                            <div class="text-left">{{ actor.name }}</div>
                            <div class="text-left small">jako {{ actor.character }}</div>
                        </figcaption>
                    </figure>
                </div>

            </div>
        </mdb-jumbotron>

        <mdb-container>
            <hr/>
            <h4 class="my-3">
                Recenzje:
            </h4>

            <comment
                    :text="review.content"
                    :author="review.author"
                    :time="'12 października 2019r.'"
                    :if-positive="!(index%2)"
                    v-for="(review, index) of movie.reviews"
            />

        </mdb-container>

    </div>
</template>

<script>
    import Movie from "@/models/Movie";
    import Actor from "@/models/Actor";
    import Comment from "@/components/movie/comment";
    import Review from "@/models/Review";
    import StarRating from 'vue-star-rating'

    export default {
        name: "movie",
        components: {Comment, StarRating},
        data() {
            return {
                id: this.$route.params.id,
                movie: null,
                userRating: 0
            }
        },
        methods: {
            rateMovie(rating){
              alert('Oceniam film "'+this.movie.title+'" na '+rating+'/10');
            },
            genreColor(genre) {

                let red_genres = ['Kryminał', 'Akcja', 'Horror', 'Romans'];
                let blue_genres = ['Thriller', 'Sci-Fi', 'Historyczny'];
                let purple_genres = ['Dramat', 'Familijny', 'Wojenny'];
                let green_genres = ['Przygodowy', 'Fantasy', 'Animacja', 'Komedia'];

                if (red_genres.includes(genre)) return 'red';
                else if (blue_genres.includes(genre)) return 'primary';
                else if (purple_genres.includes(genre)) return 'secondary';
                else if (green_genres.includes(genre)) return 'success';
                else return 'warning';
            },
            async getCast(id) {
                let url = 'https://api.themoviedb.org/3/movie/' + id + '/credits?api_key=ae3d804c4aed5b48745ca5d2de0c0294';
                return await this.$http.get(url)
                    .then(response => {
                        let x = [];
                        let cast = response.body.cast;
                        let i = 0;
                        for (let actor of cast) {
                            if (i === 10) {
                                break;
                            }
                            else {
                                x.push(new Actor(actor.id, actor.character, actor.name, actor.profile_path));
                                i++;
                            }
                        }
                        return x;
                    });
            },
            async getReviews(id) {
                let url = 'https://api.themoviedb.org/3/movie/' + id + '/reviews?api_key=ae3d804c4aed5b48745ca5d2de0c0294&language=en-US&page=1';
                return await this.$http.get(url)
                    .then(response => {
                        let x = [];
                        let reviews = response.body.results;
                        for (let review of reviews) {
                            x.push(
                                new Review(review.id, review.author, review.content)
                            );
                        }
                        return x;
                    });
            },
            requestData(id) {
                let url = 'https://api.themoviedb.org/3/movie/' + id + '?api_key=ae3d804c4aed5b48745ca5d2de0c0294&language=pl-PL';
                this.$http.get(url)
                    .then(
                        response => {
                            let res = response.body;
                            let y = {
                                id: res.id,
                                title: res.title,
                                description: res.overview,
                                rating: res.vote_average,
                                poster: 'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + res.poster_path
                            };
                            let x = new Movie(y);

                            x.budget = res.budget;
                            for (let genre of res.genres) {
                                x.genres.push(genre.name);
                            }
                            for (let company of res.production_companies) {
                                x.companies.push(company.name);
                            }
                            x.release = res.release_date;
                            x.minutes = res.runtime;
                            x.language = res.original_language;
                            this.movie = x;
                            this.getCast(this.id).then(cast => { this.movie.cast = cast;});
                            this.getReviews(this.id).then(reviews => {this.movie.reviews = reviews;});
                        },
                        error => {
                            console.log(error);
                        }
                    )
            }
        },
        created() {
            this.requestData(this.id);
        },
        beforeCreate() {
            document.body.className = 'page-movie';
        }
    }
</script>

<style scoped>
    #page-movie {
        min-height: 95vh;
    }

    .comment header {
        font-weight: bold;
    }
</style>