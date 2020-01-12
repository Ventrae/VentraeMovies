<template>
    <footer class="page-footer font-small fixed-bottom">
        <div class="footer-copyright py-3 px-5">
            Powered by
            <a href="https://facebook.com/ventrae" target="_blank">
                Filip Dobrzyniewicz
            </a>
            &copy; {{ new Date().getFullYear() }}
        </div>
    </footer>
</template>

<script>
    export default {
        name: "indexFooter"
    }
</script>

<style lang="scss" scoped>
    footer.page-footer .footer-copyright{
        background-color: transparent !important;
        @media screen and (max-width:991px) {
            text-align: center;
        }
    }
</style>