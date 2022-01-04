<script lang="ts">
    import { browser } from "$app/env";

    import Button from "../ui/button.svelte";
    import Card from "../ui/card.svelte";
    import Stack from "../ui/stack.svelte";
    import Layout from "../__layout.svelte";
    import Divider from "../design-elements/divider.svelte";

    const recentPostsCount = browser && window.matchMedia('max-width: 500px').matches ? 5 : 10;

    const card = {
        cardHeading: 'Lorem Ipsum',
        cardExcerpt: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad...'
    }
</script>

<style lang="scss">
    :global(button:not(.hamburger)) {
        margin: 40px auto 0;
    }

    @media screen and (min-width: 501px) {
        .recent-posts > :global(div) {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-gap: 16px;
        }
    }
</style>

<Layout pageTitle="Home">
    <h1>WELCOME</h1>
    <section>
        <Stack>
            <p>My name is <strong>Christopher Einarsson</strong>. I am a <strong>Frontend Developer</strong> from <strong>Sweden</strong>, generally interested in creating great user experiences on the web.</p>
            <p>Have a look around, read about a subject I have covered and get inspired to create great user experiences you too!</p>
        </Stack>
    </section>

    <Divider />

    <section class="recent-posts">
        <h2>Recent Posts</h2>
        <Stack space={4}>    
            {#each Array.from({ length: recentPostsCount }, () => card) as card}
                <Card cardHeading={card.cardHeading} cardExcerpt={card.cardExcerpt} />
            {/each}
        </Stack>
        <Button buttonText="Load More" />
    </section>
</Layout>
