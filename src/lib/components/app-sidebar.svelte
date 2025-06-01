<script lang="ts" module>
	// This is sample data.
	const data = {
		user: {
			name: 'shadcn',
			email: 'm@example.com',
			avatar: '/avatars/shadcn.jpg'
		},
		projects: [
			{
				name: 'Playground',
				url: '/',
				icon: Activity
			},
			{
				name: 'Gallery',
				url: '/gallery',
				icon: Image
			}
		]
	};
</script>

<script lang="ts">
	import * as Sidebar from '$lib/components/ui/sidebar/index.js';
	import { Activity, Image } from '@lucide/svelte';
	import type { ComponentProps } from 'svelte';
	import NavProjects from './nav-projects.svelte';
	import NavTitle from './nav-title.svelte';
	import NavUser from './nav-user.svelte';

	let {
		ref = $bindable(null),
		collapsible = 'icon',
		...restProps
	}: ComponentProps<typeof Sidebar.Root> = $props();
</script>

<Sidebar.Root {collapsible} {...restProps}>
	<Sidebar.Header>
		<NavTitle />
	</Sidebar.Header>
	<Sidebar.Content>
		<NavProjects projects={data.projects} />
	</Sidebar.Content>
	<Sidebar.Footer>
		<NavUser user={data.user} />
	</Sidebar.Footer>
	<Sidebar.Rail />
</Sidebar.Root>
