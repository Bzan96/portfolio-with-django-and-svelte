<script lang="ts">
    import { browser } from "$app/env";
    import { onMount } from "svelte";

    export let currentPath: string[] = [];

    onMount(() => {
        // heh, no one can ever see this
        currentPath = location.pathname === '/' ? [''] : location.pathname.split("/");
    })

    const preparePath = (path: string) => {
        switch(path) {
            case '':
                return 'home';
            default:
                return path;
        }
    }
</script>

<style lang="scss">
    div {
        font-family: 'IM Fell English SC', 'Courier New', Courier, monospace;

        a {
            color: var(--text);
            font-size: 16px;
            position: relative;

            &::after {
                content: "";
                position: absolute;
                bottom: 0;
                left: 0;
                width: 0%;
                height: 2px;
                background-color: var(--card-line);
                transition: width .3s ease-in-out;
            }

            &:hover::after {
                width: 100%;
            }
        }

        span {
            margin: 0 2px;
        }
    }
</style>

{#if browser && currentPath.length}
    <div>
        {#each currentPath as path, index}
            {#if index > 0}
                <span>&#707;</span>
                <a href="/{path}">{preparePath(path)}</a>
            {:else}
                <a href="/{path}">{preparePath(path)}</a>
            {/if}
        {/each}
    </div>
{:else}
    <div />
{/if}