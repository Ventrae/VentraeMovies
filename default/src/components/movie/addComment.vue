<template>
    <div class="bg-white col-12 col-md-6 mx-auto row border-secondary">
        <div class="col-11 col-md-8">
            <mdb-input type="textarea" label="Dodaj komentarz" outline :rows="2"/>
        </div>
        <div class="col-4 col-md-4 d-flex align-items-center">
            <mdb-btn color="primary" class="mx-auto d-flex align-items-center">Dodaj <i class="ml-2 fas fa-chevron-right"></i></mdb-btn>
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