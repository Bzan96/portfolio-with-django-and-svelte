<script lang="ts">
    import Button from "../ui/button.svelte";
    import Card from "../ui/card.svelte";
    import Stack from "../ui/stack.svelte";
    import Layout from "../__layout.svelte";
    import Divider from "../design-elements/divider.svelte";

    const card = {
        cardHeading: 'Lorem Ipsum',
        cardExcerpt: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad...'
    }
</script>

<style lang="scss">
    :global(button:not(.hamburger)) {
        margin: 40px auto 0;
    }
</style>

<svelte:component this={Layout} pageTitle="Home">
    <h1>WELCOME</h1>
    <section>
        <svelte:component this={Stack}>
            <p>My name is <strong>Christopher Einarsson</strong>. I am a <strong>Frontend Developer</strong> from <strong>Sweden</strong>, generally interested in creating great user experiences on the web.</p>
            <p>Have a look around, read about a subject I have covered and get inspired to create great user experiences you too!</p>
        </svelte:component>
    </section>

    <svelte:component this={Divider} />

    <section>
        <h2>Recent Posts</h2>
        <svelte:component this={Stack} space={4}>    
            {#each Array.from({ length: 5 }, () => card) as card}
                <svelte:component this={Card} cardHeading={card.cardHeading} cardExcerpt={card.cardExcerpt} />
            {/each}
        </svelte:component>
        <svelte:component this={Button} buttonText="Load More" />
    </section>
</svelte:component>
