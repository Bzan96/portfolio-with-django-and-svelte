<script lang="ts">
	import { browser } from '$app/env';
	import { onMount } from 'svelte';
	import type { Nullable } from '../types';

	let path: Nullable<string> = undefined;
	let maxWidth = 0;

	const updatePath = () => {
		if (browser) {
			const offset = 25;
			maxWidth = Math.floor(document.documentElement.scrollWidth + offset);
			const midWayWidth = Math.floor(maxWidth / 3 + offset) ?? 0;

			if (window.matchMedia('(max-width: 500px)').matches) {
				path = `M-25 125 S50 25 ${midWayWidth} 60 S355 50 ${maxWidth} 25`;
			} else {
				path = `M-25 125 S50 25 ${midWayWidth} 80 S355 20 ${maxWidth} 55`;
			}
		}
	};

	onMount(() => {
		updatePath();
	});
</script>

<svelte:window on:resize={updatePath} />

<!-- d="M-25 100 S50 25 150 60 S355 50 400 0" -->
<svg height="125" width={maxWidth} class="divider">
	<path d={path} stroke="currentColor" stroke-width="5" fill="none" />
</svg>

<style lang="scss">
	svg {
		color: var(--card-line);
		margin-left: calc(-50vw + 50%);
	}
</style>
