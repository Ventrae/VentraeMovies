<template>
    <div>
        <mdb-container class="mt-5 p-5 pt-2 pt-md-5 white" id="page-browse">

            <h2>Odkrywaj filmy!</h2>
            <hr/>

            <discover/>
            <hr/>

        </mdb-container>
    </div>
</template>

<script>
    import Recomendations from "@/components/browse/recomendations";
    import Discover from "@/components/browse/discover";

    export default {
        name: "Browse",
        components: {Discover, Recomendations},
        data() {
            return {

            }
        },
        beforeCreate() {
            document.body.className = 'page-browse';
        }
    }
</script>

<style scoped>
    #page-browse {
        min-height: 94vh;
    }
    h2 {
        font-family: 'Raleway', sans-serif;
    }
</style>