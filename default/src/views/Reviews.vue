<template>
    <div>
        <mdb-container class="mt-5 p-5 pt-2 pt-md-5 white" id="page-recommendations">

            <h2>Twoje oceny:</h2>
            <hr/>
            <mdb-list-group>
                <mdb-list-group-item
                        class="p-0 pr-3 d-flex align-items-center"
                        v-for="review of reviews"
                        tag="a"
                        :action="true"
                        :href="'/#/movie/'+review.id"
                >

                    <div class="d-flex align-items-center">
                        <img
                                width="80"
                                :alt="review.title"
                                :src="review.poster"
                                class="mr-3"
                        />
                        <div class="lead">{{ review.title }}</div>
                    </div>

                    <div class="h3">
                        {{ review.rating }} / 10
                        <i class="fas fa-star text-warning"></i>
                    </div>

                </mdb-list-group-item>
            </mdb-list-group>
            <hr/>

        </mdb-container>
    </div>
</template>

<script>
    export default {
        name: "Reviews",
        data(){
            return {
                reviews: []
            }
        },
        mounted(){
            let url = 'https://projektarc.appspot.com/api/ratings?user='+this.$store.state.user.id;
            this.$http.get(url)
                .then(response => {
                    for(let review of response.body){
                        this.reviews.push({
                            id: review.id,
                            title: review.title,
                            rating: review.rating,
                            poster: review.poster
                        })
                    }
                })
        },
        beforeCreate() {
            document.body.className = 'page-reviews';
        }
    }
</script>

<style scoped>

</style>