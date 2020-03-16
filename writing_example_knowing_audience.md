In the first post of a series on [writing example code](https://simplythetest.tumblr.com/post/612302779439087616/writing-example-code-a-series), I'm going to explore a common pitfall when writing example code: Not Knowing Your Audience. 

In some ways, writing production code for a library or package is easy. A developer sits down, figures out what they want to code, writes the code and publishes it somehow for others to use. The developer writes what they write, and software is born. What happens next is left to the universe to decide, but the developer may accept some feedback in the forms of feature requests or bug reports. 

Writing example code has the additional requirement that it is code that is _meant_ to be read and shared with folks. Library code doesn't necessarily need to be seen by end users (see: any proprietary, closed source piece of software) but example code does, by definition. Example code has the expectation not just to be used but to be read and understood. Often, developers writing example code forget that it is used wider contexts than library/production code.

I'm a Python developer, so here's a scenario that illustrates what I mean. Suppose I've created a new Python packaged called _joshlabs_ that contains a helpful Python API for working with an (imaginary) service called Josh Labs. Also suppose the package was written using Python 3 on a MacOS environment. Lastly imagine this is an excellent Python package, and along with it I include some example code of how the package works and that the example code is high quality and shows pertinent parts of how this package works.

Now imagine what happens if someone wants to use _joshlabs_ with Python 2.7, currently included by default on many MacOS instances. When they try running the example code, it doesn't work due to breaking change between Python 2 and Python 3 versions. Is there a problem here?

If the _joshlabs_ developer makes it clear through documentation or comments that it is only compatible with Python 3, then this might be acceptable. If the developer does not, then this could lead to a confusing situation, and produce a bad developer experience for those interested in the _joshlabs_ package. This might get even more complicated if the example code actually _does_ work with Python 2.7 but the general functionality in the package does not.

Let's take this scenario further: imagine that this interested developer not only is using Python 2.7 but is also a member of the original developer's organization. This developer might want to use _joshlabs_ within her team, but her team is using Python 2.7. This might be a scenario that the original developer didn't think of at all. In some large organizations, the original developer might not have even considered other teams using her _joshlabs_ package. 

These are hypothetical scenarios but they do point to the problem of not knowing your audience when writing example code. Code is a form of communication, and good communication does require thinking about *who* will see your work and *how* will they interpret it.

In general, when thinking about who the audience example code is for, consider questions such as

- *Who* could use your code? If it's someone within your team or organization, does that change how the example code should look? What if someone is outside your team or organization? What if it's some rando on the Internet?
- *What* is the code trying to show? Does it illustrate something specific? How much understanding is needed by a developer looking at this sample code?
- *Where* is the example code? Where a piece of code is influences who can see it. Is it on a password-protected wiki page? A public GitHub repo?
- *Why* would a developer use this example code? 
- *How* could someone use your code? Would you be ok seeing someone use it in a production setting? Or as a piece of a larger block of code? And does it stand alone or are there particular requirements needed for the example code to work as intended?

These considerations might look familiar to you if you've studied [composition or writing](https://www.dailywritingtips.com/the-writers-5-ws/). This is somewhat intentional, since code is a form of communication. 

Remember your audience - even your potential audience - when writing example code. It could help save you a lot of headaches and rewrites.