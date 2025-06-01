<script lang="ts">
	import type { LifepadStatus } from '$lib/types';
	import { cn } from '$lib/utils';
	import { Minus, Plus } from '@lucide/svelte';

	type Props = {
		status: LifepadStatus;
		class?: string;
		sendCommand?: (cmd: string, payload: string | number) => void;
	};

	let { status, class: className, sendCommand }: Props = $props();

	let lastLife = $state<number | undefined>();
	let lastLifeTimeout: NodeJS.Timeout;
	// if (!lastLife) {
	// 	lastLife = status.life;
	// }

	// clearTimeout(lastLifeTimeout);
	// lastLifeTimeout = setTimeout(() => {
	// 	lastLife = undefined;
	// }, 4000);
</script>

<div
	class={cn('relative flex size-80 items-center justify-center rounded-lg border', className)}
	style:background-color={status.background}
	style:background-image="url({status.image})"
	style:background-size="cover"
	style:color={status.foreground}
>
	<span class="text-8xl font-bold">{status.life}</span>

	{#if lastLife !== undefined}
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
</div>
