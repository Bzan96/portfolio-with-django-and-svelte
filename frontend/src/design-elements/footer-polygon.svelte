<script lang="ts">
    import { onMount } from "svelte";

    let isPhone: boolean = true;
    let isSmallPhone: boolean = false;

    const choosePolygon = () => {
        isPhone = window.matchMedia('(max-width: 613px)').matches;
        isSmallPhone = window.matchMedia('(max-width: 350px)').matches;
    }

    onMount(() => {
        choosePolygon();
    })
</script>

<style lang="scss">
    svg {
        display: block;
        margin: 0 auto;
    }
</style>

<svelte:window on:resize={choosePolygon} />

{#if isPhone}
    <svg width={isPhone && !isSmallPhone ? "355" : "300"} height="205" viewBox="0 0 355 205" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M177.7 201.186C177.572 201.241 177.428 201.241 177.3 201.186L3.17096 125.278C2.90244 125.161 2.7916 124.839 2.93109 124.582L0.732758 123.391L2.93112 124.582L68.6377 3.2475C68.725 3.08614 68.8938 2.9856 69.0773 2.9856L285.923 2.9856C286.106 2.9856 286.275 3.08612 286.362 3.2475L352.069 124.582C352.208 124.839 352.098 125.161 351.829 125.278L177.7 201.186Z" fill="#1C00C5" stroke="#FFA800" stroke-width="5"/>
    </svg>
{:else}
    <svg width="614" height="204" viewBox="0 0 614 204" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M306.878 201.448L3.46252 125.14C3.09277 125.047 2.95898 124.591 3.21991 124.313L116.904 3.19955C116.998 3.09886 117.13 3.04175 117.268 3.04175L496.732 3.04175C496.87 3.04175 497.002 3.09886 497.096 3.19955L610.78 124.313C611.041 124.591 610.907 125.047 610.537 125.14L307.122 201.448C307.042 201.468 306.958 201.468 306.878 201.448Z" fill="#1C00C5" stroke="#FFA800" stroke-width="5"/>
    </svg>     
{/if}
