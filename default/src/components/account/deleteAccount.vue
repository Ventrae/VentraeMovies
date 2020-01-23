<template>
    <div class="px-5">
        <h3 class="lead">Usunięcie konta:</h3>
        <hr/>
        <h4 class="mx-auto text-danger">Usunięcie konta to operacja nieodwracalna, czy na pewno chcesz to zrobić?</h4>
        <mdb-input type="password" label="Hasło" class="mb-1" outline></mdb-input>
        <mdb-btn class="my-2" color="danger">Usun konto</mdb-btn>
    </div>
</template>

<script>
    export default {
        name: "deleteAccount"
    }
</script>

<style scoped>

</style>