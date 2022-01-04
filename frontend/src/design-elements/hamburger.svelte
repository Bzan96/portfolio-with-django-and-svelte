<script lang="ts">
    export let handleMenu: () => void;
</script>

<style lang="scss">
    button {
        background-color: transparent;
        border: none;
        cursor: pointer;
        
        span {
            display: block;
            height: 3px;
            width: 25px;
            background-color: var(--yellow);

            &:nth-of-type(2) {
                margin: 5px 0;
            }
        }
    }
</style>

<button on:click={handleMenu} class="hamburger">
    <span />
    <span />
    <span />
</button>