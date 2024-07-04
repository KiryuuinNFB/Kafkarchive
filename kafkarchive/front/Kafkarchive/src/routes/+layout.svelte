<script>
    import './global.css';
    import sitelogo from '$lib/assets/logo2.png'
    export let searchcontent;
</script>


<header class="top">
    <a href="/"><img class="logo" src={sitelogo} alt="kafkarchive" height="60"></a>
    <form class="searches">
        <input bind:value={searchcontent} type = "text" placeholder="Search on Kafkarchive" class="searchbar">
        <input type = "submit" value="🔎︎" class="searchsubmit">
    </form>
    
    <div class="buttons">
        <a class="top-button" href="https://www.lipsum.com/feed/html">Builds</a>
        <a class="top-button" href="https://www.youtube.com/watch?v=GtL1huin9EE">Calculator</a>
        <a class="top-button" href="/about">About</a>
        <a class="top-button" href="https://www.lipsum.com/feed/html">Post</a>
        <a class="top-button" href="/login">Login</a>
    </div>
</header>

<slot />

<footer class="bottom">
    <div class="bottominfo">
        <h2 class="bottomkafka">Kafkarchive</h2>
        <p class="bottomtext">Copyright © 2024 Kafkarchive | <a href="https://www.youtube.com/@KiryuuinNFB/featured" target="_blank" class="bottomtextlink">NFB Production</a></p>
        <a class="bottomtextlink" target="_blank" href="https://www.reddit.com/r/copypasta/comments/13725q0/10_reasons_javascript_is_homophobic/">Privacy Policy</a>
        <p class="bottomtext">Powered by <a href="https://enka.network/?hsr" target="_blank" class="bottomtextlink">Enka.Network</a></p>
        <p class="bottomtext">i want segg with kafka</p>
    </div>
    <div class="bottominfo1">
        <a class="bottomtext2" target="_blank" href="https://github.com/KiryuuinNFB/Kafkarchive">Github</a>
        <a class="bottomtext2" target="_blank" href="https://www.youtube.com/@KiryuuinNFB/featured">Youtube</a>
        <a class="bottomtext2" target="_blank" href="https://discord.com/invite/BDShp6P">Discord</a>

    </div>
</footer>

<style>
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
        border-radius: 12px;
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

    .searchsubmit:hover {
        border: 4px solid #d4a028;
        background-color: #d4a028;
        color: #1f0e16;

    }

    .bottom {
        display: flex;
        flex-direction: row;
        background-color: #411c2d;
        padding: 5px;
    }

    .bottominfo {
        font-family: Sarabun, Arial;
        color: #ffffff;
        padding: 5px;
        margin-left: 100px;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .bottominfo1{
        font-family: Sarabun, Arial;
        color: #ffffff;
        padding: 5px;
        margin-left: 100px;
        margin-top: 40px;
    }

    .bottomtext {
        font-family: Sarabun, Arial;
        color: #ffffff;
        text-decoration: none;
    }

    .bottomtextlink {
        -webkit-transition: 0.3s;
        transition: 0.3s;
        font-family: Sarabun, Arial;
        color: #ffffff;
        text-decoration: none;
    }

    .bottomtextlink:hover {
        font-family: Sarabun, Arial;
        color: #d4a028;
        text-decoration: none;
    }

    .bottomtext2 {
        -webkit-transition: 0.3s;
        transition: 0.3s;
        font-family: Sarabun, Arial;
        color: #ffffff;
        text-decoration: none;
        font-weight: 600;
        margin: 20px;
    }

    .bottomtext2:hover {
        font-family: Sarabun, Arial;
        color: #d4a028;
        text-decoration: none;
        font-weight: 600;
        margin: 20px;
    }

    .bottomkafka {
        font-family: Sarabun, Arial;
        font-weight: 700;
    }

</style>