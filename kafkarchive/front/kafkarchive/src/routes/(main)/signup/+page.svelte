<script>
	import Heading from "../../head.svelte"
	
	let sitetitle = "Login or sign up | Kafkarchive";
	let username = "";
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
            <p class="logintopic">Sign up</p>
            <div class="loginformlists">
                <input bind:value={username} placeholder="Username" class="loginform">
                <input bind:value={email} placeholder="Email" class="loginform">
                <input bind:value={password} placeholder="Password" class="loginform">
            </div>
            <button on:click={login} class="loginsubmit">Sign up</button>
            <a href="/login" class="register">I already have an account</a>
				
		</div>
	</div>
</body>

