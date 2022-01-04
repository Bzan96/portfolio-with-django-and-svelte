<script lang="ts">
    import { browser } from "$app/env";

    const offset = 25;
    const maxWidth = browser ? Math.floor(document.documentElement.scrollWidth + offset) : 0;
    const midWayWidth = Math.floor(maxWidth / 3 + offset) ?? 0;
</script>

<style lang="scss" >
    svg {
        color: var(--card-line);
        margin-left: calc(-50vw + 50%);
    }
</style>

<svg height="125" width={maxWidth} class="divider">
    <path d="M-25 125 S50 25 {midWayWidth} 60 S355 50 {maxWidth} 25" stroke="currentColor" stroke-width="5" fill="none" />
</svg>

<!-- <svg height="100" width="400" class="divider">
    <path d="M-25 100 S50 25 150 60 S355 50 400 0" stroke="currentColor" stroke-width="5" fill="none" />
</svg> -->