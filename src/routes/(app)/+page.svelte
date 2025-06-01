<script lang="ts">
	import LifePad from '$lib/components/LifePad.svelte';
	import { nanoid } from 'nanoid';
</script>

<div class="flex flex-wrap items-center gap-5">
	<LifePad id={nanoid()} />
	<LifePad id={nanoid()} />
	<LifePad id={nanoid()} />
	<LifePad id={nanoid()} />
	<LifePad id={nanoid()} />
	<LifePad id={nanoid()} />
</div>
