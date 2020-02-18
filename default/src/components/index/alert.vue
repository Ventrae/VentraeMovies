<template>
    <div class="mx-auto alert font-small" :class="positive ? 'alert-success' : 'alert-danger'">
        {{ error }}
    </div>
</template>

<script>
    export default {
        name: "alert",
        props: {
            error: {
                type: String
            },
            positive: {
                type: Boolean,
                default: false
            }
        }
    }
</script>

<style scoped>

</style>