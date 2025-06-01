<script lang="ts">
	import LifePad from '$lib/components/LifePad.svelte';
	import type { LifepadStatus } from '$lib/types';

	type Props = {
		id: string;
		class?: string;
	};
	let { id, class: className }: Props = $props();

	let status = $state<LifepadStatus>({
		id,
		life: 20,
		background: '#000000',
		image: '',
		foreground: '#ffffff'
	});
	let connected = $state(false);

	let ws: WebSocket;

	$effect(() => {
		status.id && connectToWs(status.id);
	});

	function connectToWs(id: string) {
		try {
			ws?.close();
			ws = new WebSocket(`ws://localhost:5000/lifepad/${id}`);

			ws.onopen = () => {
				console.log('WebSocket connected');
				sendCommand('status', status);
				connected = true;
			};

			ws.onmessage = (event) => {
				try {
					const data = JSON.parse(event.data);
					console.log(data);
					if (data.command) {
						processCommand(data.command, data.payload);
					}
				} catch (error) {
					console.error('Failed to parse WebSocket message:', error);
				}
			};

			ws.onclose = () => {
				console.log('WebSocket disconnected');
				connected = false;
				// Optionally reconnect after a delay
				setTimeout(() => connectToWs(id), 3000);
			};

			ws.onerror = (error) => {
				console.error('WebSocket error:', error);
				connected = false;
			};

			return ws;
		} catch (error) {
			console.error('Failed to connect to WebSocket:', error);
			connected = false;
		}
	}

	function processCommand(cmd: string, payload: any) {
		switch (cmd) {
			case 'life':
				status.life = payload as number;
				break;
		}
	}

	function sendCommand(cmd: string, payload: any) {
		ws.send(JSON.stringify({ command: cmd, payload }));
	}
</script>

<div class="h-dvh w-full">
	{#if connected}
		<LifePad {status} {sendCommand} class={className} />
	{/if}
</div>
