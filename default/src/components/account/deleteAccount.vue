<template>
    <div class="px-5">
        <h3 class="lead">Usunięcie konta:</h3>
        <hr/>
        <h4
            class="alert alert-danger font-small text-bold mx-auto text-danger"
        >
            <div>Usunięcie konta to operacja nieodwracalna, czy na pewno chcesz to zrobić?</div>
        </h4>
        <mdb-input type="password" label="Hasło" class="mb-1" outline v-model="password"></mdb-input>
        <mdb-btn class="my-2" color="danger" @click="deleteAccount()">Usuń konto</mdb-btn>
    </div>
</template>

<script>
    export default {
        name: "deleteAccount",
        data(){
            return {
                password: ""
            }
        },
        methods: {
            deleteAccount() {
                alert("Funkcja niezaimplementowana!");
                // if(this.password !== ''){
                //     let url = "https://projektarc.appspot.com/api/delete-account";
                //     let body = {
                //         user: this.$store.state.user.id,
                //         password: this.password
                //     };
                //     this.$http.post(url, body)
                //         .then(response => {
                //                 url = 'https://projektarc.appspot.com/api/logout';
                //                 this.$http.post(url)
                //                     .then(
                //                         res => {
                //                             this.$store.state.user.token = '';
                //                             this.$router.push({name: 'index'});
                //                         },
                //                         error => {
                //                             console.error(error);
                //                         }
                //                     );
                //             },
                //             error => {
                //                 console.error(error);
                //             });
                // }
                // else {
                //     alert("Podaj hasło!");
                // }
            }
        }
    }
</script>

<style scoped>
    .text-bold {
        font-weight: bold;
    }
</style>