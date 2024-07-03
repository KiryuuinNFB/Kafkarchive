<script>
	let sitelogo = "img/logo2.png";
	let sitetitle = "Kafkarchive";
	let searchcontent = '';
</script>

<svelte:head>
	<title>{sitetitle}</title>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="icon" href="img/KF.png"type="image/x-icon">
	<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sarabun:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800&display=swap" rel="stylesheet">
</svelte:head>

<body>
	<header class="top">
		<a href="https://github.com/KiryuuinNFB/Kafkarchive" target="_blank"><img class="logo" src={sitelogo} alt="kafkarchive" height="60"></a>
		<form class="searches">
			<input bind:value={searchcontent} type = "text" placeholder="Search on Kafkarchive" class="searchbar">
			<input type = "submit" value="🔎︎" class="searchsubmit">
		</form>
		
		<div class="buttons">
            <a class="top-button" target="_blank" href="https://www.lipsum.com/feed/html">Builds</a>
            <a class="top-button" target="_blank" href="https://www.youtube.com/watch?v=GtL1huin9EE">Calculator</a>
            <a class="top-button" target="_blank" href="https://www.youtube.com/@KiryuuinNFB/featured">About</a>
            <a class="top-button" target="_blank" href="https://www.lipsum.com/feed/html">Post</a>
            <a class="top-button" target="_blank" href="https://www.lipsum.com/feed/html">Login</a>
        </div>
	</header>
	<div class="content">
		<h1>Kafkarchive is under maintenance</h1>
	</div>
</body>

<style>
	:global(body) {
		margin: 0;
		padding: 0;
	}
	body {
		background-color: #170a10;
    	margin: 0px;
    	padding: 0px;
	}

	:root::-webkit-scrollbar {
    	width: 6px;

    	-webkit-transition: 0.5s;
    	transition: 0.5s;
  	}

	:root::-webkit-scrollbar-track {
    	background: #170a10;
  	}

  	:root::-webkit-scrollbar-thumb {
	    background: #260f1a;
	    border-radius: 2px;
    
  	}

  	:root::-webkit-scrollbar-thumb:hover {
    	background: #d4a028;
  	}

	::selection {
    	background: #d4a028;
    	color: #1f0e16;
  	}

	.logo {
		margin-left: 10px;
	}

	.top {
		background-color: #672e49;
		display: flex;
    	flex-direction: row;
    	justify-content: space-between;
    	align-items: center;
    	background-color: #672e49;
    	padding: 5px;
	}

	.top-button {
    	-webkit-transition: 0.3s;
    	transition: 0.3s;
    	font-family: Sarabun, Arial;
    	font-size: 22px;
    	color: white;
    	padding: 20px;
    	display: inline-block;
    	text-decoration: none;
	}

	.top-button:hover {
    	color: #d4a028;
    	background-color: #2e1d20;
    	border-radius: 10px;
	}

	.searches {
    	display: flex;
    	
    	align-items: left;
    	flex-direction: row;

	}

	.searchbar {
		-webkit-transition: 0.3s;
		transition: 0.3s;
		background-color: #2e1a23;
		border-radius: 10px 0px 0px 10px;
    	font-family: Sarabun, Arial;
    	outline: none;
    	width: 500px;
    	padding: 5px 5px;
    	border: 4px solid #1f0e16;
		color: white;
	}

	.searchbar:focus {
		border: 4px solid #d4a028;
	}

	.searchsubmit {
		-webkit-transition: 0.3s;
		transition: 0.3s;
		background-color: #1f0e16;
		border-radius: 0px 10px 10px 0px;
    	font-family: Sarabun, Arial;
    	outline: none;
    	width: 80px;
    	padding: 5px 5px;
    	border: 4px solid #1f0e16;
		color: white;
	}

	.content {
		font-family: Sarabun, Arial;
		font-size: 70px;
    	font-weight: 700;
		color: #ffffff;
    	margin-top: 30px;
    	margin-left: 200px;
    	margin-right: 200px;
	}

</style>