# Don't Build a Pseudo-Number Generator

Often, developers need to write code that has some element of randomness. In game development actions may depend on a dice roll or coin flip. In scientific programming and simulation generating random fractional values within a range (between 0 and 1, for example) is a common task. From a design perspective, perhaps a developer needs to randomly select an image from a set of images to present in a front-end. In any case, a developer may think "I know, I'll write some code myself to generate some random values". 

This is -- with some narrow exceptions -- not a good idea and a developer should _not_ do this and instead use a pre-built pseudo-random number generator library. There are libraries for this task in most programming languages. Failing that, there are CLI utilities that can be called from the OS level. 

Let's take a look at why this is the case.

## The Theory is Hard

First, what's the difference between random and pseudo-random anyway? Isn't this just a technicality? 

The short answer is: no, it is not just a technicality.

Randomness is a [difficult topic](https://www.psychologytoday.com/us/blog/dear-life-please-improve/202106/why-we-get-randomness-so-wrong) for human beings to understand. Truly random events have zero relationship with one another, meaning that one event has zero impact or influence on the next one. If I roll a six-sided die and it turns up a four, then rolling again has no impact on the next roll the next time if the rolling event is truly random. 

Now consider about a computer program or script. It needs to run from the beginning to the end. Code runs in a predictable and _deterministic_ way. By definition running a program from beginning to end cannot have any randomness. Computers can't stop and roll a die.  

Luckily, there's a workaround: create a function for generating numbers that _appear_ random, statistically. Such a function returns the same output for a given input. However, each generated number is "random-enough" to simulate a random event such as dice roll. Mathematicians have worked on creating algorithms and functions that output random-seeming values called [pseudo-random numbers](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) that have good properties for being close enough to random. These include algorithms such as [linear congruential generators](https://demonstrations.wolfram.com/LinearCongruentialGenerators/) and the widely implemented [Mersenne Twister algorithm](https://en.wikipedia.org/wiki/Mersenne_Twister). 

(As a side note, if true randomness is a hard requirement in an application such actual lotteries using dice rolling, there are approaches that use physical phenomena to generate true random values. See [RANDOM.org](https://www.random.org/) for more information.)

Given the theoretical issues, the creation of pseudo-random number generator (PRNG) algorithms provide a path forward. Sadly, PRNGs do not end the problems developers face.

## The Practice is Hard

Implementing a PRNG seems straightforward. Find an algorithm, pick some values for various aspects of the implementation, and execute away. Many PRNG algorithms are effectively difference equations that start with a given value and iterate through a provided number of times. Easy right? 

Well, no.

The first issue that arises is computation time. Generating a single value from a PRNG is fast, but what about generating 100 values, or 1000? In practice, applications require a random value on every command or execution which could mean that many, many random values need to be generated. If each generation requires many, many iterations of a particular algorithm this could lead to non-trivial execution times. In game development, this could be a deal breaker, since performance is crucial. Often PRNGs need to be _fast_ at runtime. 

Computer hardware has gotten fast thanks to Moore's Law so even executing a large number of iterations within a function is pretty fast. However, speed isn't the only consideration for PRNGs. There's also the aspect of being "statistically random" which means choosing a "good" PRNG with good configuration. 

An infamous example of choosing a "bad" PRNG algorithm was [RANDU](https://www.johndcook.com/blog/2019/04/14/randu/). RANDU was based on a linear congruence generator as mentioned above. While RANDU generated approximately random values, it had some [obvious flaws](https://www.reddit.com/r/math/comments/um9q2/randu_a_random_number_generator_used_widely_in/?utm_source=share&utm_medium=web2x&context=3). For example, RANDU only generated odd numbers. As well, after a while generated values would repeat, meaning there was a pattern that did not appear random at all. Worst of all, RANDU was taken an implemented in a variety of settings. Note that this was a vetted algorithm by smart folks.

While it is definitely possible to [test a random-number generator](https://www.johndcook.com/blog/2009/10/27/how-to-test-a-random-number-generator/) for correctness and performance, PRNGs are sensitive to configuration and there are many pitfalls that a developer may encounter if they are not familiar with the problem space of numerical analysis and computational mathematics. Which in my experience is not a lot of developers.

However, smart folks have learned from their mistakes and now there are off-the-shelf PRNGs using vetted algorithms in most mainstream programming languages. 

It's all good, right?

## Don't Forget About Security

The last and possibly biggest issue with using PRNGs in code is security. If an attacker can determine the PRNG values being generated by a program, that attacker can exploit this knowledge. A helpful example is an [online poker site](https://www.adda52.com/blog/your-online-poker-site-is-as-safe-as-its-random-number-generator/). If each card that turns up is chosen using PRNG algorithm, then a player who knows what value the PRNG will output next can use that information to determine every single card dealt to every player. This knowledge can easily be exploited to manipulate each hand.

One of the reasons that RANDU was such a disaster was that it was not secure _and_ it was widely used. Once an attacker know a piece of software is using RANDU they can exploit that information for other malicious purposes. Using a PRNG in a local toy piece of code may be completely fine but using an insecure PRNG in production could lead to major security holes.

Again this is not a scenario that many developers consider when deciding to use a bit of randomness in their code.

Mercifully, there are well-tested [cryptographically secure PRNGs](https://stackoverflow.com/questions/2449594/how-does-a-cryptographically-secure-random-number-generator-work#2450098) available in [many](https://www.baeldung.com/java-secure-random) [programming](https://docs.python.org/3/library/secrets.html#random-numbers) [languages](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues).

In summation, choosing a PRNG built and maintained by experts is a better bet than rolling your own.


