<script>
	let sitetitle = "Calculator | Kafkarchive";
	import Heading from "../../head.svelte"
	
</script>

<Heading bind:SiteHead={sitetitle}/>

<body>
	<div class="content">
		<div class="resultbox">
				<img alt="kafka" src="http://127.0.0.1:8000/img/charbig/1005" class="charbig">
			<div class="resultblock">
				<p>HP | 3369.839</p>
				<p>ATK | 3208.931</p>
				<p>DEF | 1031.435</p>
				<p>SPD | 129.332</p>
				<p>Effect Hit Rate | 87.0%</p>
				<p>Outgoing Healing Boost | 0%</p>
				<p>CRIT Rate | 5.0%</p>
				<p>CRIT DMG | 101.8%</p>
			</div>
		</div>
		<div class="calculatorbox">
			<div class="centeradiv">
				<div class="calcblock">
					<div class="imagewindow">
						<img alt="kafka" src="http://127.0.0.1:8000/img/char/1005" class="charsmol">
					</div>
					<h2>Character</h2>
					<select class="calcselect">
						<option value="1005">Kafka</option>
					</select>
					<h2>Level</h2>
					<select class="calcselect">
						<option value="680">80</option>
					</select>
					<h2>Eidolon</h2>
					<select class="calcselect">
						<option value="0">E0</option>
					</select>
				</div>
				<div class="calcblock">
					<div class="imagewindow">
						<img alt="kafka" src="http://127.0.0.1:8000/img/lightcones/21008" class="charsmol">
					</div>
					
					<h2>Light Cone</h2>
					<select class="calcselect">
						<option value="21008">Eyes of the prey</option>
					</select>
					<h2>Level</h2>
					<select class="calcselect">
						<option value="680">80</option>
					</select>
					<h2>Superimposition</h2>
					<select class="calcselect">
						<option value="0">S2</option>
					</select>
				</div>
			</div>
		</div>
	</div>
</body>