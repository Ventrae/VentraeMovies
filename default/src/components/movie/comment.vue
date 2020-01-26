<template>
    <mdb-col col="10" class="mx-auto my-3">
        <mdb-card :style="positiveStyle">
            <mdb-card-body>
                <mdb-card-title tag="p" class="text-justify mb-0">{{ text }}</mdb-card-title>
                <hr class="my-1"/>
                <div class="d-flex justify-content-between font-small">
                    <p class="text-muted mb-0">{{ author }} | {{ time }}</p>
                    <mdb-badge pill
                               :color="positivity > 0 ? 'success' : 'danger'"
                               class="d-flex align-items-center"
                    >
                        {{ pillValue }}
                    </mdb-badge>
                </div>
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
            positivity: {
                type: Number
            }
        },
        computed: {
            positiveStyle() {
                if (this.positivity > 0) return {
                    borderLeft: '7px solid green'
                };
                else return {
                    borderLeft: '7px solid red'
                }
            },
            pillValue(){
                if (this.positivity > 0) return "Pozytywny w "+this.positivity+"%";
                else return "Negatywny w "+Math.abs(this.positivity)+"%";
            }
        }
    }
</script>

<style scoped>

</style>