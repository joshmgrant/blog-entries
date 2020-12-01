As mentioned by my excellent colleague [Nikolay Advolodkin](https://twitter.com/Nikolay_A00/), the Sauce Bindings 1.0.0 [have been released for Java](https://twitter.com/Nikolay_A00/status/1331300392571953155).

This is an exciting milestone for the [Sauce Bindings](https://github.com/saucelabs/sauce_bindings) project I've been working on with Nikolay, [Titus Fortner](https://twitter.com/titusfortner) and other lovely folks, so I'd like to take a look at what this project is, what is included in this release, and what's coming up next. 

# The Sauce Bindings Project - What Is It? 

Sauce Labs was designed and built on top of Selenium, right from the start. Building good automated tests and tooling on top of Selenium is [a pretty good idea overall](https://simplythetest.tumblr.com/post/177212136130/selenium-as-the-next-xml) since Selenium is designed to be a low-level component in a test automation framework. This is part of why Sauce Labs has been so beloved in the test automation community. 

As browser testing has become more complex, using Selenium has followed suit, particularly with the evolution of the [W3C wire protocol](https://sfconservancy.org/news/2018/may/31/seleniumW3C/) that the Selenium project has championed and implemented and the rise - and fall - of the share of browser usage by different browser vendors. This complexity has trickled down to Sauce Labs and Sauce users, who need to somehow manage this complexity in their tests. 

To help with this problem, the Sauce Bindings project was created. The goal is to create libraries or "bindings" for starting and managing Selenium and Appium sessions in a user-friendly way that also provides helpful functionality and a good user experience. These bindings are supported in Java, .NET, Python and Ruby - all of which are supported by the Selenium project and, in turn, Sauce Labs. And in the spirit of open source, these bindings are free and open sourced, so issues and pull requests are always welcome.

In this post I'll focus on the Java bindings.

# What's In Version 1.0.0?

There are three main aspects that I think are particularly great about the Sauce Bindings: implementation of the W3C wire protocol, being able to start a Sauce session neatly, and using Sauce features in an easy to use way.

## W3C By Default

Beginning in Selenium 3, the Selenium bindings supported a new protocol for connecting the Selenium client with the Selenium server. Based on the World Wide Web Consortium standard that was put forward to make the WebDriver a web standard, this protocol is know as the W3C wire protocol. This protocol replaces the original protocol based on JSON wire calls between the server and client. While later versions of Selenium 3 supported both the JSON and W3C protocol, Selenium 4 will drop support for the JSON wire protocol and only support the new W3C protocol. 

"Uh, sure thing", you're thinking. "So what does that mean for my tests?"

This means that as of Selenium 4, the _DesiredCapabilities_ class will be removed from the Selenium client bindings, replaced by browser-specific _Options_ classes. 

That's right: no more _DesiredCapabilities_ class.

Your reliable old Java-based Selenium tests will probably break hard with this change, whether you're using Sauce Labs, a Selenium Grid or even just local executions. Yikes, right? 

The Sauce Bindings have you covered. Converting _DesiredCapabilities_ to browser-options classes to start Selenium sessions isn't overly difficult but it does require some work and some code changes. In some cases it may also mean revising logic around how to select between different browser/operations combinations. Using Sauce Labs with the Sauce Bindings means all of this is handled for you by the bindings themselves. No fuss, no muss.

This is one of the goals of the Sauce Bindings: let the Bindings manage any potentially breaking changes or complexity that arises with using Sauce with Selenium. Test authors can write tests, Sauce Labs acts as the platform to run tests against, and the Sauce Bindings is the [critical plumbing layer](https://www.johndcook.com/blog/2011/11/15/plumber-programmers/) that connect the two.

Let the experts do their thing, as it were.

## Start a Sauce Session in a Simple Way

Even without the W3C vs JSON protocol distinction, managing capabilities to execute WebDriver tests in different environments is often non-trivial. Switching from an internal grid to Sauce Labs means reworking several capabilities and disentangling internal-only capabilities and Sauce-only capabilities. Switching from local executions to Sauce Labs means introducing capabilities from scratch, which can be even more confusing for novice users. 

To encapsulate this complexity, the Sauce Bindings was built with a friendly developer experience in mind. This means providing sensible defaults where possible and separating setting capabilities and starting a session. This allows for one or multiple configurations to be set up cleanly while providing a clear way to start (and stop) sessions on Sauce Labs.

One nice thing that falls out from this design: starting a new browser session on Sauce Labs is possible _in a single line of Java_.  When's the last time you were able to do _anything_ cool in one line of Java? 

## Using Sauce Features in An Easy Way

The last thing I want to highlight is that the Sauce Bindings provide a neat and tidy way to see what features are available on Sauce Labs. As developers, we often like to write code and ask questions later, so providing as much functionality "off the shelf" is a nice feature to have for many tools. While Selenium is battle hardened as a browser driver tool, Sauce Labs also provides several features to help with  test automation. Since many of these Sauce features intermingle with Selenium, it can be slightly unclear how to use these features.

Once again, the Sauce Bindings can help out. In statically typed languages like Java and C#, IDEs can provide insight into what methods are available for objects. With the Sauce Bindings, we're trying to expose as much Sauce functionality as possible in a neat and tidy way. Whether a feature needs a Sauce API endpoint, an in-browser JavaScript execution or some other utility, the Bindings will take care of those elements for you.

# What's Coming Up Next? 

While automatic W3C protocol support and exposing Sauce features for browsers are a good start, the next big area of focus is support for mobile devices. 

In this post, the terms "Selenium" and "browser" appear often, whilst "Appium", "iOS" and "Android" do not. Obviously, the Sauce Bindings need to handle mobile devices as well, so that work is being done even as we speak (as we type?). Having an easy breezy "defaults with minimal configuration" is a bit more challenging in the mobile case, but there's some good things coming. 

We're also looking at how the Sauce Bindings will allow users to use newer Sauce Labs features such as Sauce Visual (for visual testing) and Sauce Performance, while keeping the overall developer experience great. 

## Just One More Thing...

In my next post, I'll show some code-based examples of each of these aspects of the Sauce (Java) Bindings. Code examples are often clearer than paragraphs of text, so I'm excited to show what the Sauce Bindings can do. 

I'm also no Steve Jobs, clearly.