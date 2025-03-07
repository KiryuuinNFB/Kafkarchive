<script>
	import Heading from "../../head.svelte"
	
	let sitetitle = "Login | Kafkarchive";
	let email = "";
	let password = "";

	const login = () => {
		alert(email + password)
	}



</script>

<Heading bind:SiteHead={sitetitle}/>

<body>
	<div class="centeradiv">
		<div class="loginbox">
				<p class="logintopic">Login</p>
				<div class="loginformlists">
					<input bind:value={email} placeholder="Email" class="loginform">
					<input bind:value={password} placeholder="Password" type="password" class="loginform">
				</div>
				<button on:click={login} class="loginsubmit">Login</button>
				<a href="/signup" class="register">Create an account</a>
				
		</div>
	</div>
</body>
