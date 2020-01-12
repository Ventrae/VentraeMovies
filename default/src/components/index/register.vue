<template>
    <form @submit.prevent="register">

        <h1 class="flex-center">VentraeMovies</h1>

        <hr/>

        <label for="register_email" class="grey-text mb-1">Adres e-mail:</label>
        <input type="email" id="register_email" class="form-control mb-2" v-model="email"/>

        <label for="register_password_a" class="grey-text mb-1">Hasło:</label>
        <input type="password" id="register_password_a" class="form-control mb-2" v-model="password_a"/>

        <label for="register_password_b" class="grey-text mb-1">Powtórz hasło:</label>
        <input type="password" id="register_password_b" class="form-control" v-model="password_b"/>

        <div class="text-center mt-3">
            <mdb-btn type="submit" gradient="blue">Zarejestruj</mdb-btn>
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
        data(){
            return {
                email: '',
                password_a: '',
                password_b: ''
            }
        },
        methods: {
            validate(){
                let valid = true;
                let error = '';
                if(this.password_a.length <= 4){
                    error = 'Hasło musi mieć co najmniej 5 znaków!';
                    valid = false;
                }

                if(this.password_a !== this.password_b){
                    error = 'Hasła muszą się zgadzać!';
                    valid = false;
                }

                if(!/^[a-z\d]+[\w\d.-]*@(?:[a-z\d]+[a-z\d-]+\.){1,5}[a-z]{2,6}$/i.test(this.email)){
                    error = 'Podaj poprawny adres e-mail!';
                    valid = false;
                }
                return {valid, error};
            },
            register(){

                let url = 'https://projektarc.appspot.com/api/register';

                let validation = this.validate();

                if(validation.valid){
                    let user = {
                        email: this.email,
                        password: this.password_a
                    };
                    this.$http.post(url, user)
                        .then(
                            response => {
                                alert('Rejestracja udana!');
                                this.switchCard();
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
            switchCard() {
                this.$emit('switched', 'login');
            }
        }
    }
</script>

<style scoped>

</style>