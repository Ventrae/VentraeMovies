<template>
    <div class="px-5">
        <h3 class="lead">Zmień e-mail:</h3>
        <hr/>
        <mdb-input type="email" label="Nowy adres e-mail" class="mb-1" outline></mdb-input>
        <mdb-input type="password" label="Hasło" class="mb-1" outline></mdb-input>
        <mdb-btn class="my-2" color="primary">Zmień e-mail</mdb-btn>
    </div>
</template>

<script>
    export default {
        name: "changeEmail"
    }
</script>

<style scoped>

</style>