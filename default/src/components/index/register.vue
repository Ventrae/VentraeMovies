<template>
    <form>

            <h1 class="flex-center">VentraeMovies</h1>

        <hr/>

            <label for="defaultFormLoginEmailEx" class="grey-text mb-1">Adres e-mail:</label>
            <input type="email" id="defaultFormLoginEmailEx" class="form-control mb-2"/>

            <label for="defaultFormLoginPasswordEx" class="grey-text mb-1">Hasło:</label>
            <input type="password" id="defaultFormLoginPasswordEx" class="form-control mb-2"/>

            <label for="defaultFormLoginPasswordEx" class="grey-text mb-1">Powtórz hasło:</label>
            <input type="password" id="defaultFormLoginPasswordEx2" class="form-control"/>

            <div class="text-center mt-3">
                <mdb-btn type="button" gradient="blue">Zarejestruj</mdb-btn>
            </div>

        <hr/>

            <div class="d-flex justify-content-end">
                <a href="#" class="text-decoration-none" @click="switchCard">
                    Zaloguj się
                </a>
            </div>

    </form>
</template>

<script>
    export default {
        name: "register",
        methods: {
            switchCard(){
                this.$emit('switched', 'login');
            }
        }
    }
</script>

<style scoped>

</style>