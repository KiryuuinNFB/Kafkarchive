<script>
	let sitetitle = "Settings | Kafkarchive";
	import Heading from "../../head.svelte"
	import { sitetheme } from "$lib/theme.svelte"

	const allSiteThemes = [
		{ key: ["dark"], display: "Developer's Kafka"},
		{ key: ["light"], display: "light blue thing"},
	];
	

</script>

<Heading bind:SiteHead={sitetitle}/>

<body>
	<div class="centeradiv">
	<div class="settingsbox">
		<h2 class="topic">Settings</h2>
		<div class="settingsmenu">
			<h3>Site theme</h3>
			<select bind:value={allSiteThemes.key} class="settingsselect">
			{#each allSiteThemes as theme, i}
			<option value={i}>{theme.display}</option>
			{/each}
		</select>
		</div>
	</div>
	</div>
	
</body>