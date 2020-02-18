<template>
    <div>
        <mdb-container class="mt-5 p-5 pt-2 pt-md-5 white" id="page-search">

            <h2>Wyniki wyszukiwania dla "{{ $route.query.query }}":</h2>
            <hr/>

            <div class="row">

                <poster
                        v-if="movies.length > 0"
                        v-for="movie in movies"
                        :movie="movie">
                </poster>

                <p class="px-5 my-2 text-muted" v-if="movies.length === 0">
                    Nie znaleziono żadynch filmów pasujących do wyszukiwania
                </p>

                <div class="d-flex justify-content-center mx-auto">
                    <div class="spinner-border text-primary m-4" style="width: 5rem; height: 5rem;" role="status"
                         v-if="loading">
                        <span class="sr-only">Loading...</span>
                    </div>
                </div>

            </div>

            <hr/>

        </mdb-container>
    </div>
</template>

<script>
    import Poster from '@/components/browse/poster.vue';
    import Movie from "@/models/Movie";

    export default {
        name: "SearchResutls",
        components: { Poster },
        data(){
            return {
                query: '',
                movies: [],
                loading: false
            }
        },
        computed: {
            queryC(){
                return this.$route.query.query;
            }
        },
        methods: {
            search(arg){
                let url = "https://api.themoviedb.org/3/search/movie?api_key=ae3d804c4aed5b48745ca5d2de0c0294&language=pl-PL&query="+arg+"&page=1&include_adult=false";
                this.$http.get(url).then(
                    response => {
                        for(let m of response.data.results){
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
                    });
            }
        },
        watch: {
            '$route'(to, from){
                this.movies = [];
                this.query = to.query.query;
                this.search(this.$route.query.query);
            }
        },
        mounted() {
            this.query = this.$route.query.query;
            this.search(this.$route.query.query);
        }
    }
</script>

<style scoped>
</style>