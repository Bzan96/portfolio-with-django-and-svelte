<script lang="ts">
    import HeaderLine from './design-elements/header-line.svelte'
    import Hamburger from './design-elements/hamburger.svelte';
    import MobileMenu from './mobile-menu.svelte';

    export let menuIsOpen = false;
    
    let scrollPosition: number;
    let headerIsHidden = false;
    let previousScrollPosition: number;

    const handleMenu = () => {
        if(!menuIsOpen) {
            document.documentElement.classList.add('prevent-scrolling')
            return menuIsOpen = !menuIsOpen;
        }

        if(menuIsOpen) {
            document.documentElement.classList.remove('prevent-scrolling')
            return menuIsOpen = !menuIsOpen;
        }
    };

    const handleScroll = () => {
        if(scrollPosition > previousScrollPosition && !headerIsHidden) {
            headerIsHidden = true;
            document.getElementsByTagName('header')[0].classList.add('hide-header');
        }
        
        if(scrollPosition <= previousScrollPosition && headerIsHidden) {
            headerIsHidden = false;
            document.getElementsByTagName('header')[0].classList.remove('hide-header');
        }

        previousScrollPosition = scrollPosition;
    }
</script>

<style lang="scss">
    header {
        height: 56px;
        transition: transform .3s ease-in-out;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        padding-right: 16px;
        background-color: var(--blue);
        
        @media screen and (max-width: 500px) {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 99;
        }
    }

    :global(.hide-header) {
        transform: translateY(-56px);
    }
</style>

<svelte:window on:scroll|passive={handleScroll} bind:scrollY={scrollPosition} />

<header>
    <a href="/">
        <img src="/kris-150x150.png" alt="Site logo" height="48" width="48">
    </a>
    <HeaderLine />
    <Hamburger {handleMenu} />
    <MobileMenu {menuIsOpen} />
</header>