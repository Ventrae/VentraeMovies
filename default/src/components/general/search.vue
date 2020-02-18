<template>
    <form class="form-inline mr-2 p-0" @submit.prevent="search">
        <div class="md-form m-0 p-0">
            <input class="form-control p-0 m-0 mr-sm-2" type="text" placeholder="Wyszukaj film..." aria-label="Wyszukaj film" v-model="query">
            <button type="submit" class="bg-transparent border-0">
                <i class="fas fa-search text-white ml-1" aria-hidden="true"></i>
            </button>
        </div>
    </form>
</template>

<script>
    export default {
        name: "search",
        data(){
            return {
                query: ''
            }
        },
        methods: {
            search(){
                if(this.query){
                    this.$router.push({
                        name: 'search',
                        query: {
                            query: this.query
                        }
                    })
                }
                else {
                    this.$router.push({name: 'browse'})
                }

            }
        }
    }
</script>

<style scoped>

</style>