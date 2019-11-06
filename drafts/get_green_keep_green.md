I often think about process and workflows. It just sort of happens that way. 

One thing I've been thinking of lately is the usage of [red, green, refactor](https://www.jamesshore.com/Blog/Red-Green-Refactor.html). This is a common approach used in TDD and elsewhere. The basic premise to start with one or more failing tests then write code to make the tests pass. Once you have tests passing, you can effectively refactor you code.

Obviously this approach a lot of merit. But for me _personally_, I've struggled to make this approach work for me. Writing failing tests upfront seems to lead to simplistic or low-value tests. In statically typed languages (like Java) I find writing good failing tests is tricky since I already need to write compilable code. This is likely my tastes more than anything. 

Based on my love of the [Continuous Delivery mindset](https://simplythetest.tumblr.com/post/131950707000/short-post-on-continuous-deployment), I've been trying a "get green, stay green" approach. The idea is to start with passing tests then keep those tests passing.

Some advantages are: 
