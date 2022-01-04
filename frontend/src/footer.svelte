<script lang="ts">
    import Divider from './design-elements/divider.svelte';
    import GitHub from './social-media/github.svelte';
    import Gmail from './social-media/gmail.svelte';
    import LinkedIn from './social-media/linkedin.svelte';
    import Twitter from './social-media/twitter.svelte';
    import Youtube from './social-media/youtube.svelte';

    const currentYear = new Date().getFullYear();

    const socialMedia = [
        {
            title: 'Twitter',
            image: {
                src: Twitter,
                alt: 'Twitter logo',
            },
            url: 'https://twitter.com/Bzan96'
        },
        {
            title: 'Youtube',
            image: {
                src: Youtube,
                alt: 'Youtube logo',
            },
            url: 'https://www.youtube.com/channel/UCZZUtDs782SOpKrN51F78kw?view_as=subscriber'
        },
        {
            title: 'GitHub',
            image: {
                src: GitHub,
                alt: 'GitHub logo',
            },
            url: 'https://github.com/Bzan96'
        },
        {
            title: 'LinkedIn',
            image: {
                src: LinkedIn,
                alt: 'LinkedIn logo',
            },
            url: 'https://www.linkedin.com/in/christopher-einarsson-0055009b/'
        },
        {
            title: 'Gmail',
            image: {
                src: Gmail,
                alt: 'Image of a letter',
            },
            url: 'mailto:bzan96@gmail.com'
        },
    ];
</script>

<style lang="scss">
    @keyframes -global-clockwork {
        from {
            transform: rotate(23deg);
        }

        to {
            transform: rotate(73deg);
        }
    }

    footer {
        margin-top: 40px;
        height: 245px;
        position: relative;

        div {
            position: absolute;
            width: 70%;
            left: 15%;
            height: 205px;
            margin: 8px auto;
            display: grid;
            grid-template-rows: repeat(4, 1fr);
            grid-template-columns: repeat(5, 1fr);
            align-items: center;
            text-align: center;
            overflow-y: hidden;

            a {
                fill: var(--yellow);
                margin: auto;

                &:first-of-type {
                    grid-area: 1 / 2 / 1 / span 3;

                    img {
                        transform: rotate(48deg);
                        animation-name: clockwork;
                        animation-iteration-count: infinite;
                        animation-duration: 2s;
                        animation-play-state: running;
                        animation-direction: alternate;
                        animation-timing-function: ease-in-out;
    
                        @media (prefers-reduced-motion) {
                            animation-play-state: paused;
                        }
                    }
                }

                &:not(:first-of-type) {
                    height: 40px;
                    width: 40px;
                    transition: transform .3s cubic-bezier(0.39, 0.575, 0.565, 1);

                    &:hover {
                        transform: translate3d(0, -10px, 0);
                    }
                }
    
                &:nth-of-type(2) {
                    grid-area: 2 / 1 / 3 / 1;
                }
    
                &:nth-of-type(3) {
                    grid-area: 2 / 2 / 4 / 2;
                }
    
                &:nth-of-type(4) {
                    grid-area: 3 / 3 / 3 / 3;
                }
    
                &:nth-of-type(5) {
                    grid-area: 2 / 4 / 4 / 4;
                }
    
                &:nth-of-type(6) {
                    grid-area: 2 / 5 / 3 / 5;
                }
            }
        }

        svg {
            display: block;
            margin: 0 auto;
        }
    
        small {
            position: absolute;
            left: 8px;
            bottom: 8px;
        }
    }
</style>

<svelte:component this={Divider} />

<footer>
    <div>
        <a href="/">
            <img src="/kris-150x150.png" alt="Site logo" height="80" width="80">
        </a>
        {#each socialMedia as media}
            <a href={media.url}><svelte:component this={media.image.src} /></a>
        {/each}
    </div>
    <svg width="355" height="205" viewBox="0 0 355 205" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M177.7 201.186C177.572 201.241 177.428 201.241 177.3 201.186L3.17096 125.278C2.90244 125.161 2.7916 124.839 2.93109 124.582L0.732758 123.391L2.93112 124.582L68.6377 3.2475C68.725 3.08614 68.8938 2.9856 69.0773 2.9856L285.923 2.9856C286.106 2.9856 286.275 3.08612 286.362 3.2475L352.069 124.582C352.208 124.839 352.098 125.161 351.829 125.278L177.7 201.186Z" fill="#1C00C5" stroke="#FFA800" stroke-width="5"/>
    </svg>
    <small>© Christopher Einarsson {currentYear}</small>
</footer>
    