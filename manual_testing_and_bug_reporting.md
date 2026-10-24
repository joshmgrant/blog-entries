In a past article, I wrote that software quality [is going to have a revolution](https://simplythetest.tumblr.com/post/809999894733619200/software-quality-is-heading-toward-a-revolution). I still believe this, and I see some forms of what this revolution might take. One form: more manual testing.

I recently [posted](https://bsky.app/profile/joshgrant.online/post/3mycwplwu5k2r) that I feel two lessons the software world is going to re-learn in the age of LLMs is the importance of manual testing and that all software (even that one) has bugs. I'd like to go a bit further on the first point.

As LLM usage goes up, more and more code is going to be "written" by developers. I have seen first hand that this leads to a bottleneck of new change sets and higher pressure to review code. This isn't unique to me, this is a talking point which has been around for at least a few months now. As well, various people are experimenting with vibe-coding. In both professional and hobbyist circles, people are "writing" code without ever looking at it, focusing on an end goal instead of the code created along the way. These trends are causing a lot more code to be written and put in production than ever before. In some cases, this code isn't even been looked at by a human.

Of course a modern solution to this modern problem is test automation. Write automated tests alongside the code you create and the tests will validate whether or not the code works. But LLMs can also be used to read existing code and create automated tests for them. In some cases these tests will simply just run and pass, or do trivial verifications that effectively verify nothing. And if you're under pressure, any passing test is a good test. So the original problem kind of gets kicked down the road.

This is where the unmitigated power of Looking At The Software comes into play. If you try actually using the software you've built, you often will find bugs. Some may be trivial, some may be obvious, and some may be extremely important to fix. Discovering which is which is up to a human in the loop, namely a tester. A human in the loop is very helpful for validating LLM output. Fortunately, this topic of manually testing software is something that's been fully developed by many software professionals over several decades. So there's hope.

A human could also read the code and look for issues directly. Another thing that's been so well developed there's tools to accomplish this.

Actually looking at the software you create might be an excellent approach to the oncoming avalanche of code being created. It might even have benefits beyond this.

