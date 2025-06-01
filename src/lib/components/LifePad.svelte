<script lang="ts">
	import { cn } from '$lib/utils';
	import { Minus, Plus } from '@lucide/svelte';

	type Props = {
		id: string;
		class?: string;
	};

	let { id, class: className }: Props = $props();

	type Status = {
		id: string;
		connected: boolean;
		life: number;
		background: string;
		image: string;
		foreground: string;
	};

	let status = $state<Status>({
		id,
		connected: false,
		life: 20,
		background: '#000000',
		image: '',
		foreground: '#ffffff'
	});

	let temporalChange = $state<number | undefined>();
	let temporalChangeTimeout: NodeJS.Timeout;

	function command(cmd: string, payload: string | number) {
		switch (cmd) {
			case 'life':
				status.life += payload as number;

				clearTimeout(temporalChangeTimeout);
				if (!temporalChange) {
					temporalChange = 0;
				}
				temporalChange += payload as number;

				temporalChangeTimeout = setTimeout(() => {
					temporalChange = undefined;
				}, 4000);
				break;
		}
	}
</script>

<div
	class={cn('relative flex size-80 items-center justify-center rounded-lg border', className)}
	style:background-color={status.background}
	style:background-image="url({status.image})"
	style:color={status.foreground}
>
	<span class="text-8xl font-bold">{status.life}</span>

	{#if temporalChange !== undefined}
		<span
			class="absolute top-1/2 right-1/5 flex -translate-y-1/2 items-center justify-center text-2xl font-bold"
		>
			{#if temporalChange > 0}+{/if}{temporalChange}
		</span>
	{/if}

	<button
		class="absolute top-0 flex size-10 h-1/2 w-full cursor-pointer items-center justify-center rounded-full"
		onclick={() => command('life', 1)}
	>
		<Plus class="size-6" />
	</button>
	<button
		class="absolute bottom-0 flex size-10 h-1/2 w-full cursor-pointer items-center justify-center rounded-full"
		onclick={() => command('life', -1)}
	>
		<Minus class="size-6" />
	</button>
</div>
