<template>
    <div class="container p-5 my-5" id="page-movie">

        <mdb-jumbotron class="mb-0 d-flex p-4 align-items-center">
            <div>
                <img
                        width="260"
                        :alt="movie.title"
                        :src="movie.poster"
                        class="mr-5"
                />
            </div>
            <div>
                <h3 class="display-4">{{ movie.title }}</h3>
                <p v-if="movie.companies.length > 0" class="lead">
                    <template v-for="(company, index) in movie.companies">
                        {{ company }}
                        <template v-if="index !== movie.companies.length-1">,</template>
                    </template>
                </p>
                <hr class="my-4" />

                <div class="d-flex">
                    <p v-if="movie.genres.length > 0">
                        <mdb-badge class="ml-1" :color="randomColor(genre)" v-for="genre in movie.genres">
                            {{ genre }}
                        </mdb-badge>
                    </p>
                    <p class="mx-2">|</p>
                    <p v-if="movie.release !== null">
                        Premiera: {{ movie.release }}r.
                    </p>
                    <p class="mx-2">|</p>
                    <p v-if="movie.budget !== null">
                        Budżet: {{ movie.budget }}$
                    </p>
                    <p class="mx-2">|</p>
                    <p>
                        Id: {{ movie.id }}
                    </p>
                </div>

                <p>
                    {{ movie.description }}
                </p>

                <mdb-btn gradient="blue" size="lg">Oceń</mdb-btn>
            </div>


        </mdb-jumbotron>

        <hr/>

        <router-link to="/browse" class="btn btn-primary">
            <i class="fa fa-chevron-left mr-2"></i> Wróć
        </router-link>

    </div>
</template>

<script>
    import Movie from "@/models/Movie";

    export default {
        name: "movie",
        data(){
            return {
                id: this.$route.params.id,
                movie : null
            }
        },
        methods: {
            randomColor(genre){

                let red_genres = ['Kryminał', 'Akcja'];
                let blue_genres = ['Thriller', 'Sci-Fi'];
                let purple_genres = ['Dramat', 'Familijny'];
                let green_genres = ['Przygodowy', 'Fantasy'];

                if(red_genres.includes(genre)) return 'red';
                else if(blue_genres.includes(genre)) return 'primary';
                else if(purple_genres.includes(genre)) return 'secondary';
                else if(green_genres.includes(genre)) return 'success';
                else return 'warning';
            },
            requestData(id) {
                this.$http.get('https://api.themoviedb.org/3/movie/' + id + '?api_key=ae3d804c4aed5b48745ca5d2de0c0294&language=pl-PL')
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
                        },
                        error => {
                            console.log(error);
                        }
                    )
            }
        },
        mounted() {
            this.requestData(this.id);
        },
        beforeCreate() {
            document.body.className = 'page-movie';
        }
    }
</script>

<style scoped>
    #page-movie {
        min-height: 94vh;
    }
</style>