<script lang="ts">
	import { buttonVariants } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import { debounceState } from '../../../utils.svelte';
	import Button from '../ui/button/button.svelte';
	import Input from '../ui/input/input.svelte';

	type Props = {
		setBackground?: (image: string) => void;
	};

	let { setBackground }: Props = $props();

	let value = $state('');
	let open = $state(false);

	let debouncedValue = $derived.by(debounceState(() => value, 500));

	$effect(() => {
		search(debouncedValue);
	});

	type CardType = {
		id: string;
		name: string;
		image_uris: {
			art_crop: string;
		};
	};

	let cards = $state<CardType[]>([]);

	async function search(value: string) {
		if (!value) return;

		const params = new URLSearchParams();
		params.set('order', 'cmc');
		params.set('q', value);
		params.set('unique', 'art');

		const response = await fetch(`https://api.scryfall.com/cards/search?${params.toString()}`);
		const data = await response.json();
		cards = data?.data?.filter((card: CardType) => card?.image_uris?.art_crop) ?? [];
	}

	function onSelectCard(card: CardType) {
		setBackground?.(card.image_uris.art_crop);
		open = false;
	}
</script>

<Dialog.Root bind:open>
	<Dialog.Trigger class={buttonVariants({ variant: 'outline' })}>Background image</Dialog.Trigger>
	<Dialog.Content class="flex h-dvh flex-col sm:max-w-[1000px]">
		<Dialog.Header>
			<Dialog.Title>Backgrounds</Dialog.Title>
			<Dialog.Description>Select a background for your life pad.</Dialog.Description>
		</Dialog.Header>

		<div class="flex min-h-0 flex-1 flex-col gap-2">
			<Input bind:value />

			<div class="-mx-2 flex min-h-0 flex-1 flex-col gap-4 overflow-y-auto px-2">
				{#each cards as card (card.id)}
					<Button class="relative h-fit w-full" variant="ghost" onclick={() => onSelectCard(card)}>
						<img alt={card.name} src={card.image_uris.art_crop} />
						<div class="absolute right-0 bottom-0 left-0 bg-black/50 p-2 text-white">
							{card.name}
						</div>
					</Button>
				{/each}
			</div>
		</div>
	</Dialog.Content>
</Dialog.Root>
