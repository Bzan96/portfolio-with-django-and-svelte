<script lang="ts">
	export let space: number | undefined = 1;
</script>

<div style="--space: {8 * (space ?? 1)}px">
	<slot />
</div>

<style lang="scss">
	:global(div > *) {
		margin-bottom: var(--space);
	}
</style>
