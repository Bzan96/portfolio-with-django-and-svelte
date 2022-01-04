<script lang="ts">
    import Breadcrumbs from "./breadcrumbs.svelte";
    import Footer from "./footer.svelte";
    import Header from "./header.svelte";
    import ThemeContext from "./theme-context.svelte";
    import ThemeToggle from "./theme-toggle.svelte";

    export let pageTitle: string;
</script>

<style lang="scss">
    .misc {
        display: grid;
        grid-auto-flow: column;
        align-items: center;
        margin: 8px;

        @media screen and (max-width: 500px) {
            margin-top: 63px;
        }
    }

    main {
        min-height: calc(100vh - 56px - 245px);
        width: 90%;
        max-width: 650px;
        margin: 40px auto;
    }
</style>

<svelte:head>
    <title>{pageTitle}</title>
</svelte:head>

<ThemeContext>
    <Header />
    
    <div class="misc">
        <Breadcrumbs />
        <ThemeToggle />
    </div>
    
    <main>
        <slot />
    </main>
    
    <Footer />
</ThemeContext>