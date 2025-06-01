<script lang="ts">
	import LifePadController from '$lib/components/lifepad/LifePadController.svelte';
	import { nanoid } from 'nanoid';
	import { onMount } from 'svelte';

	let id = $state<string | undefined>();

	onMount(() => {
		id = nanoid();
	});
</script>

<div class="h-dvh w-full">
	{#if id}
		<LifePadController {id} class="size-full" />
	{/if}
</div>
