<script>
	let sitetitle = "Settings | Kafkarchive";
	import Heading from "../../head.svelte"
	import { onDestroy } from "svelte";
	import { sitetheme } from "$lib/theme.svelte"

	const allSiteThemes = [
		{ key: ["dark"], display: "Developer's Kafka"},
		{ key: ["light"], display: "light blue thing"},
	];
	
	let crnttheme

	const unsubscribe = sitetheme.subscribe(value => {
		crnttheme = value;
	})

	function settheme() {
		sitetheme.set(crnttheme)
	}
	
	onDestroy(unsubscribe);
</script>

<Heading bind:SiteHead={sitetitle}/>

<body>
	<div class="centeradiv">
	<div class="loginbox">
		<h1 class="topic">Settings</h1>

		<h3>Site theme</h3>
		<select bind:value={crnttheme} class="loginform" onchange={settheme}>
			{#each allSiteThemes as theme, i}
			<option value={i}>{theme.display}</option>
			{/each}
		</select>

	</div>
	</div>
	
</body>