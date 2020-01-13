<template>
    <mdb-container class="my-5">

        <mdb-row>
            <mdb-col col="col-11 col-lg-4" class="mx-auto">
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
        },
        beforeCreate() {
            document.body.className = 'page-index';
        }
    }
</script>

<style scoped>

</style>