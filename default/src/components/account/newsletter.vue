<template>
    <div class="px-5">
        <h3 class="lead">Ustawienia newslettera:</h3>
        <hr/>
        <div class="d-flex justify-content-between align-items-center px-md-4">
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="ifNewsletter" v-model="newsletter">
                <label class="custom-control-label" for="ifNewsletter">Wysyłaj rekomendacje co tydzień</label>
            </div>
            <div>
                <mdb-btn class="my-2" color="primary" @click="sendMail">Wyślij rekomendacje teraz</mdb-btn>
            </div>
        </div>
        <hr/>
        <div class="d-flex justify-content-between align-items-center px-md-4">
            <div>
                <p>
                    Newsletter wysyłany jest raz w tygodniu i zawiera rekomendacje na temat 5 ocenionych filmów.
                    Subskrypcja do newslettera jest stuprocentowo opcjonalna.
                </p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "newsletter",
        data(){
          return {
              newsletter: this.$store.state.user.newsletter
          }
        },
        watch: {
            newsletter(){
                alert('Funkcja niezaimplementowana!');
            }
        },
        methods: {
            sendMail(){
                let url = "https://projektarc.appspot.com/api/mail?user="+this.$store.state.user.id;
                this.$http.get(url)
                    .then(response => {
                        alert(response.body);
                    })
            }
        }
    }
</script>

<style scoped>

</style>