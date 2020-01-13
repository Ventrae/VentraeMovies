<template>
    <div class="row">

        <poster
                v-if="movies.length > 0"
                v-for="movie in movies"
                :movie="movie"
        />

        <div class="d-flex justify-content-center mx-auto">
            <div class="spinner-border text-primary m-4" style="width: 5rem; height: 5rem;" role="status"
                 v-if="loading">
                <span class="sr-only">Loading...</span>
            </div>
        </div>

    </div>
</template>

<script>
    import Movie from "@/models/Movie";
    import poster from "@/components/browse/poster";

    export default {
        name: "discover",
        components: {
            poster
        },
        data() {
            return {
                movies: [],
                loading: false,
                pages: 0
            }
        },
        methods: {
            handleScroll(){
                window.onscroll = () => {
                    let bottomOfWindow = Math.max(window.pageYOffset, document.documentElement.scrollTop, document.body.scrollTop) + window.innerHeight === document.documentElement.offsetHeight;
                    if (bottomOfWindow) {
                        this.getMovies(this.pages+1);
                    }
                }
            },
            getMovies(page) {
                this.loading = true;
                let url = 'https://api.themoviedb.org/3/discover/movie?api_key=ae3d804c4aed5b48745ca5d2de0c0294&language=pl-PL&sort_by=popularity.desc&include_adult=false&include_video=false&page=' + page;
                this.$http.get(url)
                    .then(
                        response => {
                            let res = response.body;
                            for (let m of res.results) {
                                let x = {
                                    id: m.id,
                                    title: m.title,
                                    description: m.overview,
                                    rating: m.vote_average,
                                    poster: 'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + m.poster_path
                                };
                                let y = new Movie(x);
                                this.movies.push(y);
                            }
                            this.pages++;
                            this.loading = false;
                        },
                        error => {
                            console.log(error);
                        }
                    )
            }
        },
        mounted() {
            this.getMovies(1);
        },
        created () {
            window.addEventListener('scroll', this.handleScroll);
        },
        destroyed () {
            window.removeEventListener('scroll', this.handleScroll);
        }
    };
</script>

<style scoped>

</style>