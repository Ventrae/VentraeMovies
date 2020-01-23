<template>
    <div class="px-5">
        <h3 class="lead">Zmień hasło:</h3>
        <hr/>
        <mdb-input type="password" label="Stare hasło" class="mb-1" outline></mdb-input>
        <mdb-input type="password" label="Nowe hasło" class="mb-1" outline></mdb-input>
        <mdb-input type="password" label="Powtórz nowe hasło" class="mb-1" outline></mdb-input>
        <mdb-btn class="my-2" color="primary">Zmień hasło</mdb-btn>
    </div>
</template>

<script>
    export default {
        name: "changePassword"
    }
</script>

<style scoped>

</style>