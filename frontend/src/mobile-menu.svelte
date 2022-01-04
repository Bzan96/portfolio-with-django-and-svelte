<script lang="ts">
    import Divider from "./design-elements/divider.svelte";
    import { menuItems } from "./menu-items";

    export let menuIsOpen: boolean;
</script>

<style lang="scss">
    nav {
        position: absolute;
        top: 56px;
        right: 0;
        left: 0;
        bottom: 0;
        z-index: 100;
        background-color: var(--background);
        height: var(--nav-height);
        overflow-y: hidden;
        transition: height .3s;
        
        ul {
            list-style: none;
            padding: 16px;
            text-align: left;
            font-size: 40px;
            font-weight: bold;
            line-height: 1.5;

            a {
                li {
                    color: var(--text)
                }

                span {
                    width: 0;
                    height: 2px;
                    color: var(--yellow);
                    transition: width .3s cubic-bezier(0.39, 0.575, 0.565, 1);
                }

                &:hover {
                    li {
                        color: var(--yellow);
                    }

                    span {
                        width: 100%;
                    }
                }
            }
        }

        @media screen and (min-width: 1024px) {
            display: none;
        }
    }
</style>

<nav style="--nav-height: {menuIsOpen ? '100vh' : '0vh'}">
    <svelte:component this={Divider} />
    <ul>
        {#each menuItems as menuItem}
            <a href={menuItem.route}>
                <li>{menuItem.title}</li>
                <span />
            </a>
        {/each}
    </ul>
    <svelte:component this={Divider} />
</nav>