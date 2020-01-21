<template>
    <div>

        <mdb-container class="mt-5 p-5 pt-2 pt-md-5 white" id="page-recommendations">

            <h2>Polecane dla Ciebie:</h2>
            <hr/>

            <recommended />
            <hr/>

        </mdb-container>

    </div>
</template>

<script>
    import Recommended from "@/components/reviewed/recommended";
    export default {
        name: "Recommendations",
        components: {Recommended},
        beforeCreate() {
            document.body.className = 'page-recommendations';
        }
    }
</script>

<style scoped>

</style>