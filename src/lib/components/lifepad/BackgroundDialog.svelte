<script lang="ts">
	import { buttonVariants } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
</script>

<Dialog.Root>
	<Dialog.Trigger class={buttonVariants({ variant: 'outline' })}>Backgrounds</Dialog.Trigger>
	<Dialog.Content class="sm:max-w-[425px]">
		<Dialog.Header>
			<Dialog.Title>Backgrounds</Dialog.Title>
			<Dialog.Description>Select a background for your life pad.</Dialog.Description>
		</Dialog.Header>

		zzzzzzzzzzzzzzzzzzzzzzz
	</Dialog.Content>
</Dialog.Root>
