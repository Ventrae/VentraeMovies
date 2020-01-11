<template>
    <!-- Material form login -->
    <mdb-container class="my-5">

        <mdb-row>
            <mdb-col col="5" class="mx-auto">
                <mdb-card>
                    <mdb-card-body>
                        <transition name="fade" mode="out-in">
                            <component @switched="state = $event" :is="state"/>
                        </transition>
                    </mdb-card-body>
                </mdb-card>
            </mdb-col>
        </mdb-row>

    </mdb-container>
    <!-- Material form login -->
</template>

<script>
    import Login from "@/components/index/login";
    import Register from "@/components/index/register";
    export default {
        name: "Index",
        components: {Login, Register},
        data(){
            return {
                state: 'login'
            }
        }
    }
</script>

<style>
    body {
        background-size: cover !important;
        background: url('../assets/img/bg-index.jpg') no-repeat;
    }
    h1 {
        font-family: 'Raleway', sans-serif;
    }
    .fade-enter {
        opacity: 0;
    }
    .fade-enter-active {
        transition: opacity .3s ease-in-out;
    }
    .fade-leave {

    }
    .fade-leave-active {
        opacity: 0;
        transition: opacity .3s ease-in-out;
    }
</style>