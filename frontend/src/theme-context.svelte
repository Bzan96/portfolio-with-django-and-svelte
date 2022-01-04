<script lang="ts" context="module">
    type ThemeType = 'light' | 'dark';

    export type ThemeContext = {
        theme: ThemeType,
        toggleTheme: (theme: ThemeType) => void;
    }
</script>

<script lang="ts">
    import { onMount, setContext } from "svelte";
    import { writable } from "svelte/store";

    let chosenTheme: ThemeType | undefined;

    const Theme = writable(chosenTheme)

    const setCSSVariables = (theme: ThemeType) => {
        const svelteElementClassList = document.getElementById('svelte').classList;
        
        ['light', 'dark'].forEach((currentTheme) => {
            if(svelteElementClassList.contains(currentTheme)) {
                svelteElementClassList.remove(currentTheme)
            }
        })

        chosenTheme = theme;
        svelteElementClassList.add(theme)
    }

    setContext<ThemeContext>('theme', {
        theme: chosenTheme,
        toggleTheme: (theme: ThemeType) => {
            Theme.update(() => {
                setCSSVariables(theme)
                window.localStorage.setItem('theme', theme)
                return theme;
            })
        }
    })


    onMount(() => {
        const userPrefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

        const storedTheme = window.localStorage.getItem('theme');

        const shouldTriggerDark = storedTheme === 'dark' || userPrefersDark;

        if(shouldTriggerDark) {
            (document.getElementById('light') as HTMLInputElement).checked = false;
            (document.getElementById('dark') as HTMLInputElement).checked = true;
            
            setCSSVariables('dark')
        }

        if(!shouldTriggerDark) {
            (document.getElementById('light') as HTMLInputElement).checked = true;
            (document.getElementById('dark') as HTMLInputElement).checked = false;

            setCSSVariables('light')
        }

    })
</script>

<slot />