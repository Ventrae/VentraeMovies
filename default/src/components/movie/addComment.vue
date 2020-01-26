<template>
    <div class="bg-white col-12 col-md-6 mx-auto row">
        <div class="col-11 col-md-8">
            <mdb-input type="textarea" label="Dodaj komentarz" outline :rows="2" v-model="comment"/>
        </div>
        <div class="col-4 col-md-4 d-flex align-items-center">
            <mdb-btn 
                color="primary" 
                class="mx-auto d-flex align-items-center"
                @click="addComment()"
            >
            Dodaj <i class="ml-2 fas fa-chevron-right"></i></mdb-btn>
        </div>
    </div>
</template>

<script>
    export default {
        name: "addComment",
        data(){
            return {
                comment: ""
            }
        },
        methods: {
            addComment(){
                let url = "https://projektarc.appspot.com/api/comment";
                let body = {
                    author: this.$store.state.user.email,
                    content: this.comment,
                    movie: this.$route.params.id
                }
                this.$http.post(url, body)
                    .then(response => {
                        
                    },
                    error => {
                        console.error(error);
                    })
            }
        }
    }
</script>

<style scoped>

</style>