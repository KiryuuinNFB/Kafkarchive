<script>
    
    import sitelogo from '$lib/assets/logo2.png';
    
    export let searchcontent = "";
    

    
</script>


<header class="top">
    <a href="/"><img class="logo" src={sitelogo} alt="kafkarchive" height="60"></a>
    <form class="searches">
        <input bind:value={searchcontent} type = "text" placeholder="Search on Kafkarchive" class="searchbar">
        <input type = "submit" value="🔎︎" class="searchsubmit">
    </form>
    
    <div class="buttons">
        <a class="top-button" href="/builds">Builds</a>
        <a class="top-button" href="/calculator">Calculator</a>
        <a class="top-button" href="/about">About</a>
        <a class="top-button" href="https://www.youtube.com/watch?v=GtL1huin9EE">Post</a>
        <a class="top-button" href="/login">Login</a>
    </div>
</header>

<slot />

<footer class="bottom">
    <div class="bottominfo">
        <h2 class="bottomkafka">Kafkarchive</h2>
        <p class="bottomtext">Copyright © 2025 Kafkarchive | <a href="https://www.youtube.com/@KiryuuinNFB/featured" target="_blank" class="bottomtextlink">NFB Production</a></p>
        <a class="bottomtextlink" href="/privacy">Privacy Policy</a>
        <p class="bottomtext">Powered by <a href="https://enka.network/?hsr" target="_blank" class="bottomtextlink">Enka.Network</a></p>
        <a class="bottomtextlink" href="/settings">Settings</a>
        <p class="bottomtext">kafka please hug me</p>
    </div>
    <div class="bottominfo1">
        <a class="bottomtext2" target="_blank" href="https://github.com/KiryuuinNFB/Kafkarchive">Github</a>
        <a class="bottomtext2" target="_blank" href="https://www.youtube.com/@KiryuuinNFB/featured">Youtube</a>
        <a class="bottomtext2" target="_blank" href="https://discord.com/invite/BDShp6P">Discord</a>

    </div>
</footer>
