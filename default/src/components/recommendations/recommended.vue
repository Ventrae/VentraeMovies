<template>
    <div class="row">

        <poster
                v-if="recommendations.length > 0"
                v-for="movie in recommendations"
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
    import Poster from "@/components/browse/poster";
    import Movie from "@/models/Movie";

    export default {
        name: "recommended",
        components: {Poster},
        data() {
            return {
                loading: false,
                recommendations: [
                    {
                        movie: '',
                        poster: '',
                        title: ''
                    }
                ]
            }
        },
        methods: {
            getRecommendations() {
                let url = 'https://projektarc.appspot.com/api/recommendations?user='+this.$store.state.user.id;
                this.$http.get(url)
                    .then(response => {
                        let arr = [];
                        let x;
                        for(let movie of response.body){
                            x = new Movie(movie);
                            x.id = movie.movie;
                            arr.push(x);
                        }
                        this.recommendations = arr;
                        this.loading=false;
                    });
            }
        },
        mounted() {
            this.loading = true;
            this.getRecommendations();
        }
    }
</script>

<style scoped>

</style>