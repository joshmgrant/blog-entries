As I continue my series on [writing good example code](https://simplythetest.tumblr.com/post/612302779439087616/writing-example-code-a-series), I'm going to delve into nefariously beloved aspect of writing code: copying and pasting code snippets. I have copy/pasted code, most of those reading this post have done it, and copy/pasting will be done in the future. 

In my last post, I discussed [knowing your audience](https://simplythetest.tumblr.com/post/612751899042742272/writing-example-code-knowing-your-audience-or) when writing samples of code. One place this becomes clear is when considering who might use your code sample, and how. The classic use case is a reader copying and pasting code into their local environment and trying to execute the code somehow. Sometimes the example code will "just work", but often this is not the case. As well, sometimes copy/pasted code can end up creating some [pretty bad situations](https://twitter.com/Foone/status/1229641258370355200) if developers aren't careful.

The key problem is this following conundrum: 

> Should example code _encourage_ copy/pasting, or not? And if example code is copy/pasted into some local context, how can developers writing that example code help the situation?

I call this the _copy/paste conundrum_ (runner-up description: the _duplication dilemma_). 

This isn't as trivial as it might seem. Many developers will write a small snippet of code without much thought showing how a particular feature works. Many documentation pages have long and short pieces of code illustrating many aspects of a library or package that are shown as example code, but still miss some key aspects that could help them out significantly. I'm going to return to my previous hypothetical Josh Labs API library that can be used to interface with the (totally imaginary) Josh Labs service to provide some examples of how to improve copy/paste code samples.

## Completeness

Suppose a feature of the Josh Labs service is that it provides full URLs used to connect to the Josh Labs API. Let's consider this code example for getting the API status via an endpoint:

```
base_url = jl_instance.JOSH_LABS_BASE_URL
status = requests.get(baseurl + "/status")
```

This snippet looks like it it could be a good example. It shows the basic feature (how to access the base url for the Josh Labs API) in a fairly straightforward way. However, this snippet has some serious deficiencies when it comes to being complete. It is missing a number of things. 

_How the library is instantiated_ is not clear. There's the `js_instance` object, but where did it come from? Even if folks are acquainted with object oriented programming there's a few ways this instance could've been created. This could be confusing if this example was copy/pasted, since it likely would fail right off the start. Putting in a constructor, previous steps for creating an instance or just some extra setup code would clarify how this is supposed to be created. Let's do that:

```
jl_instance = JoshLabsAPI()

base_url = jl_instance.JOSH_LABS_BASE_URL
status = requests.get(baseurl + "/status")
```

This adds some clarity, but also means that `jl_instance` will work as expected. Or will it? 

_Where is the library defined_ is also not included. The `JoshLabsAPI()` class definition needs to come from somewhere. It is possible this class definition is included in some local or global context after installation, but that's not too likely. If the [principle of least surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment) - which is a good principle to follow - is followed, we would expect this definition to be included somewhere as part of an import statement or reference to some other external file or library. This would help since it would reduce the surprise that the Josh Labs library is some magical, exceptional package that doesn't need to follow the rules. Since I like Python, let's use a Python-style of import to make this clear:

```
from joshlabs import JoshLabsAPI

jl_instance = JoshLabsAPI()

base_url = jl_instance.JOSH_LABS_BASE_URL
status = requests.get(baseurl + "/status")
```

If `requests` isn't included in the default namespace or standard Python library, it should also be added as an explicit import:
```
from joshlabs import JoshLabsAPI
import requests

jl_instance = JoshLabsAPI()

base_url = jl_instance.JOSH_LABS_BASE_URL
status = requests.get(baseurl + "/status")
```

Now this is looking better! Each step of using the Josh Labs library - importing it, creating an object instance by constructor and using the feature of interest - is clear. This example code has a much better chance of working properly when copy/pasted into some local environment.

**Obviousness**

Suppose my previous code snippet was this:

```
base_url = jl_instance.JOSH_LABS_BASE_URL
```

It it obvious what this code snippet does? Even if all the additional code is provided to make this complete and copy/pastable, one question I'd have when looking at this code snippet is _what is this code for?_ It's definitely not obvious. It may be clear that this code produces a URL in the form of a string but that's about it. Why a string and not some other object? And how exactly does this help a user start using the Josh Labs library? 

Looking at piece of example code and understanding (at least at a high level) what it is accomplishing should be as obvious as possible. Whether something is obvious or not [can be a tricky to determine](https://en.wikipedia.org/wiki/I_know_it_when_I_see_it) but some questions to consider would be:

- If I saw this example code appear, would I understand what it is meant for?
- If I put this in a different context or language, would I understand it?
- Would a novice programmer understand this? What about an expert programmer?

The reason obviousness helps the copy/paste conundrum is it helps folks decide what to copy/paste and where, without strange unintended consequences. 

**Platform**

Even a well formed piece of example code can fail if platform considerations aren't taken into account. For me, the classic case is the poor Windows user: a piece of code written on a Linux operating system might work beautifully on other Unix-based systems but fall over immediately on Windows. Here, copy/pasting might lead to weeping and gnashing of teeth. 

There are other similar but more subtle situations where this can be a problem such as

- implicit system dependencies: example code might inadvertently rely on system packages or libraries that installed on the development environment. There might be OS-level dependencies that aren't obvious until the example is executed on a different operating system.
- (not) future proofing: dependencies might change in the future, wildly unexpectedly sometimes. Code that works as expected today might not work at all tomorrow even with the same configuration. Example code needs a longer shelf life to accommodate this.
- (not) backwards compatible code: in addition to dependencies, programming languages change as well (particularly JavaScript but that's another blog series). Syntactic changes can occur over time even in mature programming languages. This might lead to a poor copy/paste experience.

To prevent these situations from occurring, remember to think about which language the example code is in, trying executing copy/paste snippets in different environments and recognizing platform considerations up front. If a piece of code was never meant to run on Windows 7, add comments saying so!

**Safety**:

This last aspect is often overlooked but highly important. One of the most dangerous aspects of copy/pasting code is unexpected side effects. Here's a clear example:

```
from joshlabs import JoshLabsAPI
import requests

jl_instance = JoshLabsAPI(password='mySuperSecretPassword1')

base_url = jl_instance.JOSH_LABS_BASE_URL
status = requests.get(baseurl + "/status")
```

This code looks fine, except that there's a secret password exposed. Exposing this password could lead to all kinds of malicious behaviour from bad actors. This is bad practice and could be quite dangerous. 

Other examples might be including other sensitive information such as server names, project names, IP ranges, and so on in plain text in example code. As well, including malicious code can cause problems when executed, such as the infamous [fork bomb](https://en.wikipedia.org/wiki/Fork_bomb#Bash) that can crash processes or operating systems. Such code might look unfamiliar and be copy/pasted without much thought, leading to dire consequences. Be mindful of side effects, security and overall safety when imagining example code being copy/pasted.


## I Copy, You Copy, We All Paste

Copy/paste considerations are, at the least, complex. What could be a nice clean piece of example code might end up being a headache for well-meaning users who copy and paste it into their context. It is a crucial consideration if example code accomplishes its goal of being helpful, and copy/paste is here to stay.