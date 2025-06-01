<script lang="ts">
	import LifePad from '$lib/components/LifePad.svelte';
	import type { LifepadStatus } from '$lib/types';
	import { onMount } from 'svelte';

	onMount(() => {
		connectToWs();
	});

	let lifepads = $state<LifepadStatus[]>([]);
	let ws: WebSocket;
	let reconnectTimeout: NodeJS.Timeout;

	function connectToWs() {
		clearTimeout(reconnectTimeout);
		ws?.close();
		ws = new WebSocket('ws://localhost:5000/lifepad');

		ws.onmessage = (event) => {
			const data = JSON.parse(event.data);
			console.log(data.payload);
			if (data.command === 'status') {
				lifepads = data.payload;
			}
		};

		ws.onerror = (event) => {
			console.error('WebSocket error:', event);
			clearTimeout(reconnectTimeout);
			reconnectTimeout = setTimeout(() => connectToWs(), 5000);
		};

		ws.onclose = (event) => {
			console.error('WebSocket closed:', event);
			clearTimeout(reconnectTimeout);
			reconnectTimeout = setTimeout(() => connectToWs(), 5000);
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
