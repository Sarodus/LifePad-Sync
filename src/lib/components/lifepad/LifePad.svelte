<script lang="ts">
	import LifePadSettings from '$lib/components/lifepad/LifePadSettings.svelte';
	import type { LifepadStatus } from '$lib/types';
	import { cn } from '$lib/utils';
	import { Minus, Plus, Settings, X } from '@lucide/svelte';
	import { debounceState } from '../../../utils.svelte';
	import Button from '../ui/button/button.svelte';

	type Props = {
		status: LifepadStatus;
		class?: string;
		sendCommand?: (cmd: string, payload: string | number) => void;
	};

	let { status, class: className, sendCommand }: Props = $props();

	let lastLife = $derived.by(debounceState(() => status.life, 4000));

	let settingsOpen = $state(false);
</script>

<div
	class={cn('relative flex size-80 items-center justify-center rounded-lg border', className)}
	style:background-color={status.background}
	style:background-image="url({status.image})"
	style:background-size="cover"
	style:color={status.foreground}
>
	<span class="text-8xl font-bold">{status.life}</span>

	{#if lastLife !== status.life}
		<span
			class="absolute top-1/2 right-1/5 flex -translate-y-1/2 items-center justify-center text-2xl font-bold"
		>
			{#if status.life > lastLife}+{/if}{status.life - lastLife}
		</span>
	{/if}

	<button
		class="absolute top-0 flex size-10 h-1/2 w-full cursor-pointer items-center justify-center"
		onclick={() => sendCommand?.('life', status.life + 1)}
	>
		<Plus class="size-6" />
	</button>
	<button
		class="absolute bottom-0 flex size-10 h-1/2 w-full cursor-pointer items-center justify-center"
		onclick={() => sendCommand?.('life', status.life - 1)}
	>
		<Minus class="size-6" />
	</button>

	{#if settingsOpen}
		<LifePadSettings {sendCommand} {status} />
	{/if}

	<Button
		class="text-muted-foreground absolute top-2 right-2"
		variant="ghost"
		onclick={() => (settingsOpen = !settingsOpen)}
	>
		{#if settingsOpen}
			<X />
		{:else}
			<Settings />
		{/if}
	</Button>
</div>
