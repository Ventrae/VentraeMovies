<template>
    <div>

        <mdb-container class="mt-5 p-5 pt-2 pt-md-5 white" id="page-recommendations">

            <h2>Zarządzanie kontem:</h2>
            <hr/>
            <mdb-row>
                <mdb-col md="4" class="d-flex flex-column px-5">
                    <mdb-btn class="my-2 py-4" @click="changeScreenVisibility('change-email')" outline="primary">Zmień
                        e-mail
                    </mdb-btn>
                    <mdb-btn class="my-2 py-4" @click="changeScreenVisibility('change-password')" outline="primary">
                        Zmień hasło
                    </mdb-btn>
                    <mdb-btn class="my-2 py-4" @click="changeScreenVisibility('newsletter')" outline="primary">
                        Newsletter
                    </mdb-btn>
                    <mdb-btn class="my-2 py-4" @click="changeScreenVisibility('delete-account')" outline="danger">Usuń
                        konto
                    </mdb-btn>
                </mdb-col>
                <mdb-col md="8">
                    <component :is="visible"></component>
                </mdb-col>
            </mdb-row>

        </mdb-container>

    </div>
</template>

<script>
    import ChangeEmail from "@/components/account/changeEmail";
    import ChangePassword from "@/components/account/changePassword";
    import Newsletter from "@/components/account/newsletter";
    import DeleteAccount from "@/components/account/deleteAccount";

    export default {
        name: "Account",
        components: {DeleteAccount, Newsletter, ChangePassword, ChangeEmail},
        data() {
            return {
                visible: ''
            }
        },
        methods: {
            changeScreenVisibility(screen) {
                this.visible = screen;
            }
        },
        beforeCreate() {
            document.body.className = 'page-account';
        }
    }
</script>

<style scoped>

</style>