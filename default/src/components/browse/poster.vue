<template>
    <article class="mx-auto d-flex flex-column mx-1 my-2 movie-poster" @click="openDetails">
        <img
                width="260"
                :alt="movie.title"
                :src="movie.poster"
        />
        <div class="overlay">{{ movie.title }}</div>
    </article>
</template>

<script>
    import Movie from "@/models/Movie";

    export default {
        name: "poster",
        props: {
            movie: {
                required: true
            }
        },
        methods: {
            openDetails(){
                this.$router.push('/movie/'+this.movie.id);
            }
        }
    }
</script>

<style scoped>

</style>