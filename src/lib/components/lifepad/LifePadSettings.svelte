<script lang="ts">
	import type { LifepadStatus } from '$lib/types';
	import BackgroundImageDialog from './BackgroundImageDialog.svelte';
	import ColorPickerDialog from './ColorPickerDialog.svelte';

	type Props = {
		status: LifepadStatus;
		sendCommand?: (cmd: string, payload: string | number) => void;
	};

	let { status, sendCommand }: Props = $props();

	function setBackground(image: string) {
		sendCommand?.('image', image);
	}

	function setBackgroundColor(color: string) {
		sendCommand?.('background', color);
	}

	function setForeground(color: string) {
		sendCommand?.('foreground', color);
	}
</script>

<div class="bg-background absolute inset-0 size-full p-4">
	<h1>Settings</h1>

	<div class="flex flex-wrap gap-2">
		<BackgroundImageDialog {setBackground} />
		<ColorPickerDialog onColorPicked={setBackgroundColor} title="Background color" />
		<ColorPickerDialog onColorPicked={setForeground} title="Text color" />
	</div>
</div>
