<template>
    <mdb-col col="10" class="mx-auto my-3">
        <mdb-card :style="positiveStyle">
            <mdb-card-body>
                <mdb-card-title tag="p" class="h5 mb-0">{{ text }}</mdb-card-title>
                <hr class="my-1"/>
                <p class="font-small text-muted mb-0">{{ author }} | {{ time }}</p>
            </mdb-card-body>
        </mdb-card>
    </mdb-col>
</template>

<script>
    export default {
        name: "comment",
        props: {
            text: {
                type: String,
                required: true
            },
            author: {
                type: String,
                required: true
            },
            time: {
                type: String,
                required: true
            },
            ifPositive: {
                type: Boolean,
                default: true
            }
        },
        computed: {
            positiveStyle(){
                return {
                    borderLeft: '7px solid darkgray'
                }
                /*
                    if(this.ifPositive) return {
                        borderLeft: '7px solid green'
                    };
                    else return {
                        borderLeft: '7px solid red'
                    }
                */
            }
        }
    }
</script>

<style scoped>

</style>