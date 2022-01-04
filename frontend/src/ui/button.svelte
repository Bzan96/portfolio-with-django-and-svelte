<script lang="ts">
	export let buttonText: string;
</script>

<button>{buttonText}</button>

<style lang="scss">
	button {
		display: block;
		background-color: var(--blue);
		color: var(--primary);
		font-size: 20px;
		border-radius: 50px;
		border: none;
		min-width: 170px;
		height: 40px;
		cursor: pointer;
	}
</style>
