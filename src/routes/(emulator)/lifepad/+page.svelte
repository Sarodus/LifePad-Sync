<script lang="ts">
	import LifePad from '$lib/components/LifePad.svelte';
	import { nanoid } from 'nanoid';
	import { onMount } from 'svelte';

	onMount(() => {
		id = nanoid();
	});

	let id = $state<string>();
</script>

<div class="h-dvh w-full">
	{#if id}
		<LifePad {id} class="size-full" />
	{/if}
</div>
