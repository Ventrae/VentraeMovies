<template>
    <div class="bg-white col-12 col-md-6 mx-auto fixed-bottom row">
        <div class="col-11 col-md-8">
            <mdb-input type="textarea" label="Dodaj komentarz" outline :rows="2"/>
        </div>
        <div class="col-4 col-md-2">
            <mdb-btn color="primary" class="d-flex">Dodaj <i class="fas fa-chevron-right"></i></mdb-btn>
        </div>
    </div>
</template>

<script>
    export default {
        name: "addComment"
    }
</script>

<style scoped>

</style>