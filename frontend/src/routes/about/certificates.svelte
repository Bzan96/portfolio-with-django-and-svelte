<script lang="ts">
	import Divider from '../../design-elements/divider.svelte';
	import Card from '../../ui/card.svelte';
	import Layout from '../../__layout.svelte';
	import { certificates } from './certificates';

	const { images, links } = certificates;

	const pageTitle = 'About';
	const subPageTitle = 'Certificates';
</script>

<Layout pageTitle="{pageTitle} | {subPageTitle}">
	<h1>{subPageTitle}</h1>
	{#each images as { name, image: { src, alt }, excerpt }}
		<Divider />
		<section>
			<Card cardHeading={name} cardExcerpt={excerpt} />
			<a
				href={src}
				aria-label="See the certificate in full size in another tab"
				target="_blank"
			>
				<figure>
					<img {src} {alt} />
					<figcaption class="visually-hidden">{name}</figcaption>
				</figure>
			</a>
		</section>
	{/each}
	{#each links as { name, link, excerpt }}
		<Divider />
		<section>
			<Card cardHeading={name} cardExcerpt={excerpt} />
			<a href={link.src} aria-label={link['aria-label']} target="_blank"
				>{name}</a
			>
		</section>
	{/each}
</Layout>

<style lang="scss">
	section {
		--transform-amount: 25px;
		position: relative;
		z-index: 1;
		margin-bottom: calc(var(--transform-amount) * -1);

		a {
			cursor: pointer;
			position: relative;
			z-index: -1;
			display: inline-block;
			transform: translateY(-75px);
			transition: transform 0.3s ease-in, z-index 0s 0.3s;
			box-shadow: 5px 7px 5px 2px var(--box-shadow);

			figure {
				img {
					width: 100%;
					height: auto;
				}
			}
		}

		&:hover {
			a {
				transform: translateY(var(--transform-amount));
				outline: var(--yellow) ridge 5px;
				z-index: 1;
			}
		}
	}
</style>
