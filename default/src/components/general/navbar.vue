<template>
    <mdb-navbar expand="large" dark color="blue-gradient" class="fixed-top">
        <mdb-navbar-brand>
            <router-link to="/browse" class="navbar-brand py-0">
                VentraeMovies
            </router-link>
        </mdb-navbar-brand>
        <mdb-navbar-toggler>
            <mdb-navbar-nav right>
                <search />
                <mdb-nav-item>
                    <p class="nav-link d-none d-md-block p-0 my-0">|</p>
                </mdb-nav-item>
                <mdb-nav-item>
                    <router-link to="/browse" class="nav-link py-0">
                        Odkrywaj
                    </router-link>
                </mdb-nav-item>
                <mdb-nav-item>
                    <router-link to="/recommendations" class="nav-link py-0">
                        Rekomendacje
                    </router-link>
                </mdb-nav-item>
                <mdb-nav-item>
                    <router-link to="/reviewed" class="nav-link py-0">
                        Ocenione
                    </router-link>
                </mdb-nav-item>
                <mdb-nav-item>
                    <router-link to="/account" class="nav-link py-0">
                        Konto
                    </router-link>
                </mdb-nav-item>
                <mdb-nav-item>
                    <p class="nav-link p-0 my-0">|</p>
                </mdb-nav-item>
                <mdb-nav-item>
                    <a href="#" class="nav-link d-none d-md-block py-0 my-0" @click="logout">Wyloguj</a>
                </mdb-nav-item>
            </mdb-navbar-nav>
        </mdb-navbar-toggler>
    </mdb-navbar>
</template>

<script>
    import Search from "@/components/general/search";
    export default {
        name: "navbar",
        components: {Search},
        methods: {
            logout() {
                let url = 'https://projektarc.appspot.com/api/logout';
                this.$http.post(url)
                    .then(
                        response => {
                            this.$store.state.user.token = '';
                            this.$router.push({name: 'index'});
                        },
                        error => {
                            console.error(error);
                        }
                    );
            }
        }
    }
</script>

<style scoped>
    .navbar-brand {
        font-family: 'Raleway', sans-serif;
    }
</style>