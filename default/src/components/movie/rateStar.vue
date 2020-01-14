<template>
    <button type="button" @mouseover="setRate">
        <i class="fa-star" :class="{'fas': state, 'far': !state}"></i>
    </button>
</template>

<script>
    export default {
        name: "rateStar",
        props: {
            state: {
                type: Boolean,
                default: false
            }
        },
        methods: {
            setRate(){
                this.$emit('cddd', this.state);
            }
        }
    }
</script>

<style scoped>
    button {
        background: transparent;
        border: 0;
        color: gold;
        outline: 0;
        font-size: 42px;
    }
</style>