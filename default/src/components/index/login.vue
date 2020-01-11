<template>
    <form>

        <h1 class="flex-center my-0">VentraeMovies</h1>
        <hr/>
            <label for="defaultFormLoginEmailEx" class="grey-text mb-1">Adres e-mail:</label>
            <input type="email" id="defaultFormLoginEmailEx" class="form-control mb-2"/>

            <label for="defaultFormLoginPasswordEx" class="grey-text mb-1">Hasło:</label>
            <input type="password" id="defaultFormLoginPasswordEx" class="form-control"/>
        <div class="text-center mt-3">
            <mdb-btn type="button" gradient="blue">Zaloguj</mdb-btn>
        </div>
        <hr/>

        <div class="d-flex justify-content-between">
            <a href="#" class="text-decoration-none">
                Nie pamiętasz hasła?
            </a>
            <a href="#" class="text-decoration-none" @click="switchCard">
                Zarejestruj się
            </a>
        </div>

    </form>
</template>

<script>
    export default {
        name: "login",
        methods: {
            switchCard(){
                this.$emit('switched', 'register');
            }
        }
    }
</script>

<style scoped>

</style>