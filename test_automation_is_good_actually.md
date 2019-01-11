Here's a somewhat radical opinion: mostly, test automation is good. And developers, testers and any other technical folks out there need to understand this.

I'm specifically talking about test automation here, not automation in general. Think unit testing, Selenium-based testing or fuzz tools or even linters. I agree automation in general is good in software development but that's not what I want to discuss today.

Recently, a tweet by Katrina Clokie about her frustrations of the software testing made an impact. She mentions how the testing profession seems to discuss the same ideas and themes over and over again, without really trying to progress past them. Based on my experience with testing and automation, I think this is mostly true.

One thing I've noticed recently is there's a sort of intellectual resistance to test automation. On top of the "testing vs checking" debate, which seems to be an argument that's used in bad faith to spread FUD about test automation generally, I've seen several discussions and posts around the topic of writing test automation and how many ways this can go badly. Ideas references are: writing bad UI automation can ruin projects, test automation takes a large amount of effort to catch bugs that humans can find easily, focusing too much on tools means not enough focus on value and results, and so on. Very often, these ideas are ones I've seen time and time again. As Katrina mentions, there isn't much progression past them. 

The resulting opinion? Be suspicious of test automation, because it might be badly done. 

This opinion is - to me - very short-sighted.

Mainly because there's a lot of *good* test automation out there. Focusing simply on the bad doesn't add much to the conversation. Focusing on what could *potentially* be bad might actually take away from the conversation. 

On a practical level, many software projects now have some form of test automation. Developers writing unit tests is now seen as the standard and mainstream, while not writing unit tests is old-fashioned and behind the times. There's been many common practices and approaches to writing good UI or functional test automation, in particular for web applications (with mobile apps following up close behind). There's also been many individuals in both the testing world and software development world who discuss test automation as part of strategies on software quality and approaches to producing and releasing software.

There's projects like Wikimedia who employ test automation at a fairly large scale and make that test automation code [freely available](https://www.mediawiki.org/wiki/Selenium/Node.js). There's projects like [Cucumber](https://docs.cucumber.io/) that promote good test automation practices. There's also projects such as [Selenium](https://docs.seleniumhq.org/) and [Watir](watir.com) that don't just produce tools but also have active communities to discuss test automation practices and ideas. 

There's simply too much good stuff going to be overly suspicious of test automation these days, as a software tester or otherwise.

And lastly to note, as the late Jerry Weinberg used to say, "However it looks at first, it's always a people problem". Many problems with test automation are really problems with team composition, mismatched expectations, and team management gone awry. Projects that are doomed to fail from the onset are sign of a bad system, not necessarily bad work.

Some things to think about whenever you see discussion of test automation, and how "bad" it can be. 