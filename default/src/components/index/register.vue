<template>
    <form @submit.prevent="register">

        <h1 class="flex-center">VentraeMovies</h1>

        <hr/>

        <div class="mx-auto alert alert-danger font-small" v-if="error !== ''">
            {{ error }}
        </div>

        <mdb-input type="email" label="Adres e-mail" class="mb-1" outline v-model="email"></mdb-input>

        <mdb-input type="password" label="Hasło" class="mb-1" outline v-model="password_a"></mdb-input>

        <mdb-input type="password" label="Powtórz hasło" class="mb-1" outline v-model="password_b"></mdb-input>

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
                password_b: '',
                error: ''
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
                                this.error = error.body;
                            }
                        );
                }
                else {
                    this.error = validation.error;
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