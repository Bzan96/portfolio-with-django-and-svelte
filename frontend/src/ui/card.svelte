<script lang="ts">
	import CardLeftLine from '../design-elements/card-left-line.svelte';
	import CardTopLine from '../design-elements/card-top-line.svelte';

	export let cardHeading: string;
	export let cardExcerpt: string;
</script>

<article>
	<CardTopLine />
	<CardLeftLine />
	<section>
		<h3>{cardHeading}</h3>
		<p>{cardExcerpt}</p>
	</section>
</article>

<style lang="scss">
	article {
		position: relative;
		box-shadow: 7px 7px 5px 2px var(--box-shadow);
		height: 150px;
		width: 300px;
		margin-left: auto;
		margin-right: auto;

		:global(.card-top-line),
		:global(.card-left-line) {
			display: block;
			position: absolute;
			top: 0;
			left: 0;
			color: var(--card-line);
		}

		section {
			background-color: var(--card);
			color: var(--text);
			padding: 8px 16px;
			height: 100%;
			width: 100%;

			h3 {
				margin-bottom: 8px;
			}

			p {
				line-height: 1.3;
			}
		}
	}
</style>
