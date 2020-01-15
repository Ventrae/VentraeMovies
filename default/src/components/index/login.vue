<template>
    <form @submit.prevent="login">

        <h1 class="flex-center my-0">VentraeMovies</h1>
        <hr/>
            <label for="login_email" class="grey-text mb-1">Adres e-mail:</label>
            <input type="email" id="login_email" class="form-control mb-2" v-model="email"/>

            <label for="login_password" class="grey-text mb-1">Hasło:</label>
            <input type="password" id="login_password" class="form-control" v-model="password"/>
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
                password: ''
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
                                    alert(response.body);
                                }
                            },
                            error => {
                                console.error(error);
                            }
                        );
                }
                else {
                    alert(validation.error);
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