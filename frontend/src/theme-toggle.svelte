<script lang="ts">
    import { getContext } from "svelte";
    import type { ThemeContext } from "./theme-context.svelte";

    const { toggleTheme } = getContext<ThemeContext>('theme');
</script>

<style lang="scss">
    :global(#svelte) {
        background-color: var(--background);
        color: var(--text);
    }

    fieldset {
        border: none;
        padding: 4px 0;
        white-space: nowrap;
        text-align: right;
        transform: translateX(50px);

        legend {
            font-size: 2px;
            opacity: 0;
            position: absolute;
        }

        input {
            opacity: 0;
            position: absolute;
            
            &:first-of-type:checked ~ label:first-of-type::after {
                background: linear-gradient(90deg, var(--primary) 50%, var(--secondary) 50%);
            }

            &:first-of-type:checked ~ label:first-of-type::before {
                transform: translate(-2.25em, 0.25em);
                background: var(--secondary);
            }

            &:last-of-type:checked ~ label:last-of-type {
                z-index: 1;
            }
        }

        label {
            display: inline-block;
            line-height: 2;
            position: relative;
            z-index: 2;

            &:first-of-type {
                padding-right: 5em;
            };

            &:last-of-type {
                margin-left: -4.25em;
                padding-left: 5em;
            };

            &:first-of-type::before,
            &:first-of-type::after {
                border: 1px solid var(--text);
                content: "";
                height: 2em;
                overflow: hidden;
                pointer-events: none;
                position: absolute;
                vertical-align: middle;
            }

            &:first-of-type::before {
                background: var(--primary);
                border: 1px solid var(--secondary);
                border-radius: 100%;
                position: absolute;
                right: -.075em;
                transform: translate(-0.4em, 0.25em);
                transition: transform .2s ease-in-out;
                width: 1.5em;
                height: 1.5em;
                z-index: 2;
            }

            &:first-of-type::after {
                background: linear-gradient(90deg, var(--primary) 50%, var(--secondary) 50%);
                border-radius: 1em;
                margin: 0 1em;
                transition: background .2s ease-in-out;
                width: 4em;
            }
        }

        &:focus-within label:first-of-type::after {
            box-shadow: 0 0 0 4px var(--yellow);
        }
    }
</style>

<fieldset>
    <legend>
      Theme
    </legend>
    <input type="radio" name="theme" id="light" checked on:click={() => toggleTheme('light')}>
    <label for="light">
      <span class="visually-hidden">Light</span>
    </label>
  
    <input type="radio" name="theme" id="dark" on:click={() => toggleTheme('dark')}>
    <label for="dark">
      <span class="visually-hidden">Dark</span>
    </label>
</fieldset>