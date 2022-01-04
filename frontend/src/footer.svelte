<script lang="ts">
	import { browser } from '$app/env';

	import Divider from './design-elements/divider.svelte';
	import FooterPolygon from './design-elements/footer-polygon.svelte';
	import GitHub from './social-media/github.svelte';
	import Gmail from './social-media/gmail.svelte';
	import LinkedIn from './social-media/linkedin.svelte';
	import Twitter from './social-media/twitter.svelte';
	import Youtube from './social-media/youtube.svelte';

	const currentYear = new Date().getFullYear();

	const isSmallPhone = browser
		? window.matchMedia('(max-width: 350px)').matches
		: false;
	const logoSize = isSmallPhone ? '64px' : '80px';

	const socialMedia = [
		{
			title: 'Twitter',
			image: {
				src: Twitter,
				alt: 'Twitter logo',
			},
			url: 'https://twitter.com/Bzan96',
		},
		{
			title: 'Youtube',
			image: {
				src: Youtube,
				alt: 'Youtube logo',
			},
			url: 'https://www.youtube.com/channel/UCZZUtDs782SOpKrN51F78kw?view_as=subscriber',
		},
		{
			title: 'GitHub',
			image: {
				src: GitHub,
				alt: 'GitHub logo',
			},
			url: 'https://github.com/Bzan96',
		},
		{
			title: 'LinkedIn',
			image: {
				src: LinkedIn,
				alt: 'LinkedIn logo',
			},
			url: 'https://www.linkedin.com/in/christopher-einarsson-0055009b/',
		},
		{
			title: 'Gmail',
			image: {
				src: Gmail,
				alt: 'Image of a letter',
			},
			url: 'mailto:bzan96@gmail.com',
		},
	];
</script>

<Divider />

<footer>
	<div>
		<a href="/">
			<img
				src="/kris-150x150.png"
				alt="Site logo"
				height={logoSize}
				width={logoSize}
			/>
		</a>
		{#each socialMedia as media}
			<a href={media.url}><svelte:component this={media.image.src} /></a>
		{/each}
	</div>
	<FooterPolygon />
	<small>© Christopher Einarsson {currentYear}</small>
</footer>

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
			--polygon-width: 265.5px;
			position: absolute;
			width: var(--polygon-width);
			left: calc(50vw - var(--polygon-width) / 2);
			height: 205px;
			margin: 8px auto;
			display: grid;
			grid-template-rows: repeat(4, 1fr);
			grid-template-columns: repeat(5, 1fr);
			align-items: center;
			text-align: center;
			overflow-y: hidden;

			@media screen and (max-width: 350px) {
				--polygon-width: 250px;
				height: 175px;
				margin: 24px auto;
			}

			@media screen and (min-width: 614px) {
				--polygon-width: 550px;
			}

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
					transition: transform 0.3s cubic-bezier(0.39, 0.575, 0.565, 1);

					@media screen and (max-width: 350px) {
						height: 32px;
						width: 32px;
					}

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

		small {
			position: absolute;
			left: 8px;
			bottom: 8px;
		}
	}
</style>
