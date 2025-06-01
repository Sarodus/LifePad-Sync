<script lang="ts">
	import * as Sidebar from '$lib/components/ui/sidebar/index.js';
	import { Activity } from '@lucide/svelte';
</script>

<Sidebar.MenuButton
	size="lg"
	class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
>
	<div
		class="bg-sidebar-primary text-sidebar-primary-foreground flex aspect-square size-8 items-center justify-center rounded-lg"
	>
		<Activity class="size-4" />
	</div>
	<div class="grid flex-1 text-left text-sm leading-tight">
		<span class="truncate font-medium"> LifePad Sync </span>
	</div>
</Sidebar.MenuButton>
