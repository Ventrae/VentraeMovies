<template>
    <form @submit.prevent="login">

        <h1 class="flex-center my-0">VentraeMovies</h1>
        <hr/>

            <div class="mx-auto alert alert-danger font-small" v-if="error !== ''">
                {{ error }}
            </div>

            <mdb-input type="email" label="Adres e-mail" outline v-model="email"/>

            <mdb-input type="password" label="Hasło" outline v-model="password"/>

        <div class="text-center mt-3">
            <mdb-btn type="submit" gradient="blue">Zaloguj</mdb-btn>
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
        data(){
            return {
                email: '',
                password: '',
                error: ''
            }
        },
        methods: {
            validate(){
                let valid = true;
                let error = '';

                if(this.email === ''){
                    valid = false;
                    error = 'Podaj adres e-mail!';
                }

                if(this.password === ''){
                    valid = false;
                    error = 'Podaj hasło!';
                }

                return {valid, error};
            },
            login(){
                let url = 'https://projektarc.appspot.com/api/login';
                let validation = this.validate();

                if(validation.valid){
                    let user = {
                        email: this.email,
                        password: this.password
                    };
                    this.$http.post(url, user)
                        .then(
                            response => {
                                if(response.status === 200){
                                    this.$store.state.user.id = response.body.id;
                                    this.$store.state.user.token = response.body.token;
                                    this.$store.state.user.email = response.body.email;
                                    this.$router.push('/browse');
                                }
                                else {
                                    this.error = response.body;
                                }
                            },
                            error => {
                                this.error = error.body;
                            }
                        );
                }
                else {
                    this.error = validation.error;
                }
            },
            switchCard(){
                this.$emit('switched', 'register');
            }
        }
    }
</script>

<style scoped>

</style>