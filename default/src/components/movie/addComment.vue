<template>
    <div class="bg-white col-12 col-md-6 mx-auto row">
        <div class="col-11 col-md-8">
            <mdb-input type="textarea" label="Dodaj komentarz" outline :rows="2" v-model="comment"/>
        </div>
        <div class="col-4 col-md-4 d-flex align-items-center">
            <button
                type="button"
                :class="{disabled: cooldown > 0}"
                class="btn btn-primary mx-auto d-flex align-items-center"
                @click="cooldown === 0 ? addComment() : ''"
            >
                <div class="d-flex align-items-center" v-if="cooldown === 0">
                    Dodaj <i class="ml-2 fas fa-chevron-right"></i>
                </div>
                <div class="d-flex align-items-center" v-else>
                    Czekaj ({{ cooldown }}s)
                </div>
            </button>

        </div>
    </div>
</template>

<script>
    export default {
        name: "addComment",
        data(){
            return {
                comment: "",
                cooldown: 0
            }
        },
        methods: {
            addComment(){
                if(this.comment !== '' && this.cooldown === 0){
                    let url = "https://projektarc.appspot.com/api/comment";
                    let body = {
                        author: this.$store.state.user.email,
                        content: this.comment,
                        movie: this.$route.params.id
                    };
                    this.cooldown = 3;
                    this.$http.post(url, body)
                        .then(response => {
                                this.$emit('added');
                                setTimeout(()=>{
                                    this.cooldown--;
                                    setTimeout(()=>{
                                        this.cooldown--;
                                        setTimeout(()=>{
                                            this.cooldown--;
                                        },1000);
                                    },1000);
                                },1000);
                            },
                            error => {
                                console.error(error);
                            })
                }
            }
        }
    }
</script>

<style scoped>

</style>