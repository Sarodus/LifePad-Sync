<script lang="ts">
	import LifePad from '$lib/components/LifePad.svelte';
	import type { LifepadStatus } from '$lib/types';
	import { onMount } from 'svelte';

	onMount(() => {
		connectToWs();
	});

	let lifepads = $state<LifepadStatus[]>([]);
	let ws: WebSocket;

	function connectToWs() {
		ws = new WebSocket('ws://localhost:5000/lifepad');

		ws.onmessage = (event) => {
			const data = JSON.parse(event.data);
			console.log(data.payload);
			if (data.command === 'status') {
				lifepads = data.payload;
			}
		};
	}

	function sendCommand(id: string, cmd: string, payload: string | number) {
		ws.send(JSON.stringify({ id, command: cmd, payload }));
	}
</script>

<div class="flex flex-wrap items-center gap-5">
	{#each lifepads as status}
		<LifePad {status} sendCommand={(cmd, payload) => sendCommand(status.id, cmd, payload)} />
	{/each}
</div>
