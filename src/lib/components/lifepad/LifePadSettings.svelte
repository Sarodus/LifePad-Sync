<script lang="ts">
	import BackgroundDialog from './BackgroundDialog.svelte';
</script>

<div class="bg-background absolute inset-0 size-full p-4">
	<h1>Settings</h1>

	<div class="flex gap-2">
		<BackgroundDialog />

		<!-- <Button onclick={() => (chooseColorOpen = !chooseColorOpen)}>Colors</Button> -->
	</div>
</div>
