<script>
	let sitetitle = "Login | Kafkarchive";
	let username = "";
	let email = "";
	let password = "";
	let hasacc = true;

	const login = () => {
		alert(email + password)
	}

	const noacc = () => {
		hasacc = !hasacc;
	}
</script>

<svelte:head>
	<title>{sitetitle}</title>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sarabun:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800&display=swap" rel="stylesheet">
</svelte:head>

<body>
	<div class="centeradiv">
		<div class="loginbox">
			{#if hasacc == true}
				<p class="logintopic">Login</p>
				<div class="loginformlists">
					<input bind:value={email} placeholder="Email" class="loginform">
					<input bind:value={password} placeholder="Password" class="loginform">
				</div>
				<button on:click={login} class="loginsubmit">Login</button>
				<button on:click={noacc} class="register">Create an account</button>
			{:else if hasacc == false}
				<p class="logintopic">Sign up</p>
				<div class="loginformlists">
					<input bind:value={username} placeholder="Username" class="loginform">
					<input bind:value={email} placeholder="Email" class="loginform">
					<input bind:value={password} placeholder="Password" class="loginform">
				</div>
				<button on:click={login} class="loginsubmit">Sign up</button>
				<button on:click={noacc} class="register">Already have an account</button>
			{/if}
		</div>
	</div>
</body>

<style>

	.centeradiv {
		display: flex;
  		justify-content: center;
  		text-align: center;
  		min-height: 10vh;
		font-family: Sarabun, Arial;
    	color: #ffffff;

	}

	.loginbox {
		-webkit-transition: 0.3s;
        transition: 0.3s;
		background-color: #411c2d;
		width: 400px;
		margin-top: 5%;
		margin-bottom: 5%;
		margin-left: 10%;
		margin-right: 10%;
		padding: 20px;
		border-radius: 20px;
	}

	.logintopic {
		margin: 10%;
		font-size: 60px;
    	font-weight: 700;
		text-align: center;
	}

	.loginformlists {
		
		flex-direction: column;
		justify-content: space-between;
		display: flex;
		align-items: center;
	}

	.loginform {
		margin: 20px;
		width: 70%;
		-webkit-transition: 0.3s;
        transition: 0.3s;
        background-color: #2e1a23;
		font-family: Sarabun, Arial;
		border-radius: 10px;
		outline: none;
        padding: 15px;
        border: 4px solid #1f0e16;
        color: white;
	}

	.loginform:focus {
		border: 4px solid #d4a028;
	}

	.loginsubmit {
		-webkit-transition: 0.3s;
        transition: 0.3s;
        background-color: #1f0e16;
        border-radius: 10px;
        font-family: Sarabun, Arial;
        outline: none;
        width: 80px;
        padding: 5px 5px;
        border: 4px solid #1f0e16;
        color: white;
	}

	.loginsubmit:hover {
		background-color: #d4a028;
		border: 4px solid #d4a028;
		color: #1f0e16;
	}

	.register {
		-webkit-transition: 0.3s;
        transition: 0.3s;
		border: 4px solid #411c2d;
		background-color: #411c2d;
		color: white;
		text-decoration: none;
		padding: 5px 5px;
	}

	.register:hover {
		color: #d4a028;
	}

</style>