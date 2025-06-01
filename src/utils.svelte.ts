/**
 *  Example:
 * let value = $state();
 * let debouncedValue = $derived.by(debounceState(() => value, 300));
 */
export function debounceState<T>(getter: () => T, delay: number) {
	let value = $state<T>(getter());
	let timer: NodeJS.Timeout;
	$effect(() => {
		const newValue = getter(); // read here to subscribe to it
		clearTimeout(timer);
		timer = setTimeout(() => (value = newValue), delay);
		return () => clearTimeout(timer);
	});
	return () => value;
}
