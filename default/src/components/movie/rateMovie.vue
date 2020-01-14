<template>
    <form>
        <rate-star @cddd="rating = 1" :state="rating > 0" />
        <rate-star @cddd="rating = 2" :state="rating > 1" />
        <rate-star @cddd="rating = 3" :state="rating > 2" />
        <rate-star @cddd="rating = 4" :state="rating > 3" />
        <rate-star @cddd="rating = 5" :state="rating > 4" />
    </form>
</template>

<script>
    import RateStar from "./rateStar";
    export default {
        name: "rateMovie",
        components: {RateStar},
        data(){
            return {
                rating: 0
            }
        }
    }
</script>

<style scoped>

</style>