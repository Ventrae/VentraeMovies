<template>
    <div class="px-5">
        <h3 class="lead">Zmień hasło:</h3>
        <hr/>
        <mdb-input type="password" label="Stare hasło" class="mb-1" outline v-model="password_old"></mdb-input>
        <mdb-input type="password" label="Nowe hasło" class="mb-1" outline v-model="password_new_a"</mdb-input>
        <mdb-input type="password" label="Powtórz nowe hasło" class="mb-1" outline v-model="password_new_b"></mdb-input>
        <mdb-btn class="my-2" color="primary" @click="changePassword()">Zmień hasło</mdb-btn>
    </div>
</template>

<script>
    export default {
        name: "changePassword",
        data(){
            return {
                password_old: "",
                password_new_a: "",
                password_new_b: ""
            }
        },
        methods: {
            changePassword(){
                alert("Funkcja niezaimplementowana!");
            }
        }
    }
</script>

<style scoped>

</style>