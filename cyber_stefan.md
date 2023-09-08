If you're looking for a good time, check out the hot new tech subject, _Cybersecurity_.

(I'm channeling my best [Stefon](https://www.thewrap.com/snl-stefon-bill-hader-sketches-saturday-night-live-videos/) here.)

Seriously, this topic has _everything_. Two talks in this area from this year definitely have me thinking that when it comes to cybersecurity, the truth can be stranger than fiction.

Earlier this year, I attended a talk at [BSides Rochester](https://bsidesroc.com/assets/archive/2023/) entitled "TikTok Under Attack: Attacker Uses a Popular TikTok Challenge to Lure Users Into Installing Malicious Package". I was intrigued because I do [enjoy TikTok](https://www.tiktok.com/@joshin5colours), but was _not_ prepared for the roller coaster ride of this talk. 

The overall story goes like this: the speaker is a security researcher who was interested in starjacking, a potentially malicious process where a given GitHub repository is shown to have a much higher number of stars/stargazers than it actually does. This can be exploited by poor controls on package managers such as NPM or PyPI which don't necessarily validate a GitHub repo's metrics. Here's a [good intro](https://checkmarx.com/blog/starjacking-making-your-new-open-source-package-popular-in-a-snap/) to the topic. 

This researcher was finding ways to understand how starjacking works, and found that there were malicious PyPI packages that if installed, will enable starjacking on particular repos. Installing a PyPI module does require some Python knowledge - it's not quite as easy as clicking a link on a webpage - so the attackers had to find a way to get individuals to install this mysterious PyPI package.

This is where TikTok comes in.

The researcher found a challenge on TikTok called the Invisible Filter challenge. The idea was that TikTok created a filter that makes a person in a video "invisible" (you can only see a rough outline of a human while the shape blends into the background). The challenge was to create videos and have viewers guess who the invisible person is, what they're wearing, etc. A variation of this challenge was for the person in the video to be naked so to "appear naked" on TikTok without actually appearing, er, naked. The attackers exploited this by posting links to their malicious PyPI package saying this Python package could remove the invisible filter showing the person in the video. This caused a bunch of folks (referred to as "creeps" by the speaker) to download and install the malicious package, thus facilitating starjacking.

That talk was a wild ride. Where it started and where it ended up were two different places.

I thought for sure this was a one-off style of presentation (PyPI! Starjacking! TikTok! Nude people!). 

But wait, there's more!

During this year's BlackHat conference, a PhD student gave a talk called ["Houston, We Have a Problem: Analyzing the Security of Low Earth Orbit Satellites"]("https://www.blackhat.com/us-23/briefings/schedule/#houston-we-have-a-problem-analyzing-the-security-of-low-earth-orbit-satellites-32468"). Effectively, the researcher asked "How secure are in-orbit satellites?" and the answer is "not very". 

While I didn't see this talk myself, I can imagine this having the same flow as the TikTok talk. For example, the researcher found that many security features of satellites are non-existent, likely based on the thinking that attackers on Earth couldn't access them in any way. That turns out to be false, and even cloud services such as AWS offer [Ground Service to low-orbit satellites](https://aws.amazon.com/ground-station/pricing/). You can even get started for free. 

Again, this talk had everything: basic hacking techniques, cloud providers, satellites...in space!

When I think of cybersecurity, I typically don't think of talks that offer stranger than fiction style narrative, but it may be the best place to find some such tales.

