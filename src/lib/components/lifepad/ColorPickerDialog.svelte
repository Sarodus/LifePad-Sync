<script lang="ts">
	import { buttonVariants } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import Button from '../ui/button/button.svelte';

	type Props = {
		title: string;
		onColorPicked?: (color: string) => void;
	};

	let { title, onColorPicked }: Props = $props();

	let open = $state(false);

	const predefinedColors = [
		{ name: 'White', value: '#ffffff' },
		{ name: 'Black', value: '#000000' },
		{ name: 'Red', value: '#dc2626' },
		{ name: 'Blue', value: '#2563eb' },
		{ name: 'Green', value: '#16a34a' },
		{ name: 'Yellow', value: '#eab308' },
		{ name: 'Purple', value: '#9333ea' },
		{ name: 'Pink', value: '#ec4899' },
		{ name: 'Orange', value: '#ea580c' },
		{ name: 'Teal', value: '#0d9488' },
		{ name: 'Indigo', value: '#4f46e5' },
		{ name: 'Gray', value: '#6b7280' }
	];

	function onPickColor(color: string) {
		onColorPicked?.(color);
		open = false;
	}
</script>

<Dialog.Root bind:open>
	<Dialog.Trigger class={buttonVariants({ variant: 'outline' })}>{title}</Dialog.Trigger>
	<Dialog.Content class="flex h-dvh flex-col sm:max-w-[1000px]">
		<Dialog.Header>
			<Dialog.Title>{title}</Dialog.Title>
			<Dialog.Description>Select a color</Dialog.Description>
		</Dialog.Header>

		<div class="flex min-h-0 flex-1 flex-col gap-4">
			<div class="grid grid-cols-3 gap-3 sm:grid-cols-4">
				{#each predefinedColors as color}
					<Button
						class="flex h-20 flex-col items-center justify-center gap-2"
						variant="outline"
						onclick={() => onPickColor(color.value)}
					>
						<div
							class="h-8 w-8 rounded border-2 border-gray-300"
							style="background-color: {color.value}"
						></div>
						<span class="text-xs">{color.name}</span>
					</Button>
				{/each}
			</div>
		</div>
	</Dialog.Content>
</Dialog.Root>
