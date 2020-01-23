<template>
    <div class="px-5">
        <h3 class="lead">Ustawienia newslettera:</h3>
        <hr/>
        <div>
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="defaultUnchecked">
                <label class="custom-control-label" for="defaultUnchecked">Wysyłaj rekomendacje co tydzień</label>
            </div>
            <mdb-btn class="my-2" color="primary">Wyślij rekomendacje teraz</mdb-btn>
        </div>
    </div>
</template>

<script>
    export default {
        name: "newsletter"
    }
</script>

<style scoped>

</style>