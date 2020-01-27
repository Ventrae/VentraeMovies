<template>
    <mdb-col col="10" class="mx-auto my-3">
        <mdb-card :style="positivityBorder">
            <mdb-card-body>
                <mdb-card-title tag="p" class="text-justify mb-0">{{ text }}</mdb-card-title>
                <hr class="my-1"/>
                <div class="d-flex justify-content-between font-small">
                    <p class="text-muted mb-0">{{ author }} | {{ time }}</p>
                    <span
                        :class="positivityPill"
                        class="badge badge-pill d-flex align-items-center"
                    >
                        {{ pillValue }}
                    </span>
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
            positivityPill(){
                if (this.positivity > 0) return 'badge-success'
                else if(this.positivity < 0) return 'badge-danger'
                else return 'badge-light'
            },
            positivityBorder() {
                if (this.positivity > 0) return {
                    borderLeft: '7px solid green'
                };
                else if(this.positivity < 0) return {
                    borderLeft: '7px solid red'
                }
                else return {
                    borderLeft: '7px solid gray'
                }
            },
            pillValue(){
                if (this.positivity > 0) return "Pozytywny w "+this.positivity+"%";
                else if(this.positivity < 0) return "Negatywny w "+Math.abs(this.positivity)+"%";
                else return "Neutralny (0%)";
            }
        }
    }
</script>

<style scoped>

</style>