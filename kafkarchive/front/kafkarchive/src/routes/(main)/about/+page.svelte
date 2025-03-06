<script>
	import Heading from "../../head.svelte"

	let sitetitle = "About | Kafkarchive";
</script>

<Heading bind:SiteHead={sitetitle}/>

<body>
	<div class="content">
		<h1 class="topic">About</h1>
		<h2 class="subtopic">About Kafkarchive</h2>
		<div class=walloftext>
			<p>
				Kafkarchive is a Honkai: Star Rail database website where players can upload their character builds with tags that best describe them.
				So that other players can look up builds that might fit their playstyles. It is also a site for calculating hypothetical builds. You can import your builds by putting in your UID, 
				Or you can create your build manually.
				This site was originally created for a school project, So don't expect super accurate information or optimized system. 
			</p>
			<p>
				This site is written in <a href="https://kit.svelte.dev/" class="walloftextlink" target="_blank">SvelteKit</a> and <a href="https://fastapi.tiangolo.com/" class="walloftextlink" target="_blank">FastAPI</a>.
				And uses <a href="https://enka.network/?hsr" class="walloftextlink">Enka.Network</a> for importing builds. Game datas are from <a href="https://github.com/FortOfFans/HSRMaps" class="walloftextlinkstrikethrough">FortOfFans's HSRMaps</a>
				and <a href="https://yatta.top/en" class="walloftextlink">Project Yatta's API</a>.
			</p>
		</div>
		<h2 class="subtopic">About the developers</h2>
    <div class="walloftext">
        <p><a href="https://github.com/KiryuuinNFB" class="walloftextlink">Kiryuuin</a> | The only active developer. Did frontend and backend. And is the guy writing all of this.<br>
			</p>
			
		<p>Beta testers <br>
			Phot007, Zkung, Hydragear.K, BaNinena</p>
		
		<h2 class="subtopic">Special thanks to</h2>

		<p>
		<a href="https://github.com/Ranviee0" class="walloftextlink">Ranvie</a> | Programming tech support. Without him, I wouldn't be able to do programming at all. <br>

		<a href="https://github.com/ModelZ" class="walloftextlink">ModelZ</a> | Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sapiente, velit! <br>
		
		<a href="https://github.com/Algoinde" class="walloftextlink">Algoinde</a> | For making Enka.Network and helping me sometimes <br>
		
		<a href="https://github.com/seriaati" class="walloftextlink">seriaati</a> | For making the Enka API Python Wrapper</p>
	</div>
	<h2 class="subtopic">FAQ</h2>
	<div class="walloftext">
		<h3>Q | Why Kafka?</h3>
		<p class="walloftext">A | I just really like mommy Kafka.</p>
		<h3>Q | There are already a lot of websites like this. Why even make Kafkarchive?</h3>
		<p class="walloftext">A | It's for me to practice programming as a hobby. This is my first ever website, It's a passion project and if it works, I am happy. 
			And if I ever go to college I will put this website in my portfolio<br>
			And if anyone says that there is no point in making this website. Then I'll be quoting <a href="https://www.youtube.com/watch?v=Qp3b-RXtz4w&t=50s&cc_load_policy=1" class="walloftextlink" target="_blank">one of my favorite song</a>. 
		</p>

		<div class="centerdiv">
			<p class="quote">"Shut up, shut up, shut the fuck up. I&#39m healthier than you think. You are too mediocre to understand me, perhaps"</p>
		</div>		

		<p class="walloftext">What I meant by that was. I know it's pointless but shut up. This is my website and I get to do anything I want on my website. 
			Also I don't hate you guys, I just really like that song lol.</p>

		<h3>Q | How can I support the development of this website?</h3>
		<p class="walloftext">A | You can support me by visiting my <a class="walloftextlink" target="_blank" href="https://www.youtube.com/@KiryuuinNFB/featured">Youtube channel</a>
			where I did music there. But I have already lost lots of motivation in music production. I might not be able to make quality remixes like I used to before.</p>
		<p class="walloftext">You can also support the website just by giving me a hug. No, Seriously i need it so bad. 
            My mental health isn't very good at all. Halfway into designing this website i realized just how little i know about the game mechanics. 
            And the fact that a lot of players have already made much better and more practical websites just demotivates me. When I first started designing this website
            I didn't even know any JavaScript or anything about web frameworks. I have realized just how complicated web developing actually is and it is too late for me to stop now.</p>

		
	</div>

	</div>
	<div class="emptyspace"></div>
</body>
