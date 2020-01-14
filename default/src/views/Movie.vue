<template>
    <div class="container-fluid px-0 py-5 mt-5 white" id="page-movie">

        <mdb-container>
            <mdb-jumbotron class="mb-0 d-flex p-4 justify-content-between align-items-center bg-dark">
                <h3 class="h4 text-light m-0">
                    {{ movie.title }}
                    <span class="h6 text-muted">
                        | {{ movie.id }}
                    </span>
                </h3>

                <div class="h4 text-light m-0">
                    {{ movie.rating }} / 10
                    <i class="fas fa-star text-warning"></i>
                </div>
            </mdb-jumbotron>

            <mdb-jumbotron class="mb-0 d-flex pl-0 pr-4 py-0 align-items-center" fluid>

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

                    <p>
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

                    <rate-movie/>

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
                                :alt="movie.title"
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
                    :text="i%2 ? 'Chujowy film nie polecam strata czasu' : 'Arcydzieło współczesnej kinematografii'"
                    :author="'ventrae@gmail.com'"
                    :time="'12 października 2019r.'"
                    :if-positive="!(i%2)"
                    v-for="i in [1,2,3,4,5,6,7,8,9]"
            />

        </mdb-container>

        <mdb-btn class="mt-4 mx-0" gradient="blue" size="lg" @click="$router.go(-1)">
            <i class="fa fa-chevron-left mr-2"></i> Wróć
        </mdb-btn>

    </div>
</template>

<script>
    import Movie from "@/models/Movie";
    import RateMovie from "@/components/movie/rateMovie";
    import Actor from "@/models/Actor";
    import Comment from "@/components/movie/comment";
    import Review from "@/models/Review";

    export default {
        name: "movie",
        components: {Comment, RateMovie},
        data() {
            return {
                id: this.$route.params.id,
                movie: null
            }
        },
        methods: {
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
                console.log('dupa');
                this.$http.get(url)
                    .then(response => {
                        let x = [];
                        let cast = response.body.cast;
                        let i = 0;
                        for (let actor of cast) {
                            if (i === 10) {
                                break;
                            } else {
                                x.push(
                                    new Actor(actor.id, actor.character, actor.name, actor.profile_path)
                                );
                                i++;
                            }
                        }
                        return x;
                    });
            },
            async getReviews(id) {
                let url = 'https://api.themoviedb.org/3/movie/' + id + '/reviews?api_key=ae3d804c4aed5b48745ca5d2de0c0294&language=en-US&page=1';
                this.$http.get(url)
                    .then(async response => {
                        let x = [];
                        let reviews = response.body.results;
                        for (let review of reviews) {
                            x.push(
                                new Review(review.id, review.author, review.content)
                            );
                        }
                    });
                return x;
            },
            requestData(id) {
                let url = 'https://api.themoviedb.org/3/movie/' + id + '?api_key=ae3d804c4aed5b48745ca5d2de0c0294&language=pl-PL';
                this.$http.get(url)
                    .then(
                        response => {
                            console.log('requestuje dane filmu ' + id);
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
                            const cast = this.getCast(this.id).then(cast => {
                                return cast;
                            });
                            const reviews = this.getReviews(this.id).then(reviews => {
                                return reviews;
                            });
                            this.movie.cast = cast;
                            this.movie.reviews = reviews;
                            console.log(this.movie);
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