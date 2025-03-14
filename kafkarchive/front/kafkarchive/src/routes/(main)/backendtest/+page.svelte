<script>
    import Heading from "../../head.svelte"
    

	let sitetitle = "Backend test | Kafkarchive";
    let numb1, numb2, res;

    $: mynums = {
        'num1': numb1,
        'num2': numb2
    }

    async function postnum() {
        const response = await fetch("http://127.0.0.1:8000/calc", {
            method: 'POST',
            body: JSON.stringify(mynums),
            headers: {"Content-Type":"application/json; charset=UTF-8"}
        });
        const result = await response.json();
        res = result.result
    }

</script>

<Heading bind:SiteHead={sitetitle}/>

<body>
	<div class="content">
        
		<h1 class="topic">{res}</h1>
        <p class="walloftext">{numb1}</p>
        <form class="content">
            <input class="calcselect" bind:value={numb1} placeholder="num1">
            <input class="calcselect" bind:value={numb2} placeholder="num2">
            <button on:click={postnum}>submit</button>
        </form>
	</div>
</body>
<div class="emptyspace">

</div>