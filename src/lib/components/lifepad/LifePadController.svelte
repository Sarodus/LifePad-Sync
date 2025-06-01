<script lang="ts">
	import { PUBLIC_WS_URL } from '$env/static/public';
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
	let reconnectTimeout: NodeJS.Timeout;

	$effect(() => {
		status.id && connectToWs(status.id);
		return () => {
			clearTimeout(reconnectTimeout);
			ws?.close();
		};
	});

	function connectToWs(id: string) {
		try {
			clearTimeout(reconnectTimeout);
			ws?.close();
			ws = new WebSocket(`${PUBLIC_WS_URL}/lifepad/${id}`);

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
				// Reconnect after 5 seconds
				reconnectTimeout = setTimeout(() => connectToWs(id), 5000);
			};

			ws.onerror = (error) => {
				console.error('WebSocket error:', error);
				connected = false;
				// Reconnect after 5 seconds on error
				reconnectTimeout = setTimeout(() => connectToWs(id), 5000);
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

			case 'image':
				status.image = payload as string;
				break;

			case 'background':
				status.image = '';
				status.background = payload as string;
				break;

			case 'foreground':
				status.foreground = payload as string;
				break;
		}
	}

	function sendCommand(cmd: string, payload: any) {
		try {
			ws.send(JSON.stringify({ command: cmd, payload }));
		} catch (error) {
			console.error('Failed to send WebSocket message:', error);
		}
	}

	function manageCommand(cmd: string, payload: any) {
		if (connected) {
			sendCommand(cmd, payload);
		}
		processCommand(cmd, payload);
	}
</script>

<div class="h-dvh w-full">
	<LifePad {status} sendCommand={manageCommand} class={className} />
</div>
