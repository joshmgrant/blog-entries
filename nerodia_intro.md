One of the most underrated browser testing tools out is Watir, as I've [blogged about before](http://simplythetest.tumblr.com/post/166573913200/the-third-way). The beauty of Watir is that it bundles features on top of a Selenium WebDriver that are often (always?) helpful in the context of browser test automation in a way that still has good user experience for test developers.

This nice utility has been primarily based in the Ruby language and community, which has taken test automation as a [first class feature of the ecosystem](https://twitter.com/chris_mcmahon/status/1032676531947024384). What about other languages and communities? 

If you're a Pythonista, there is now a Python port of Watir called [Nerodia](https://github.com/watir/nerodia). It has been under development for a while now but has had parity with recent Watir versions in terms of features. Nerodia maintains the same user experience as Watir does in Ruby but is not just available for Python but also has a more native "Pythonic" feel. Better testing tools for everyone (using Python)!

Why Python for a port of Watir? Some reasons are:
- Python and Ruby are both dynamically typed languages, so some of the ideas of the Ruby implementation of Watir more naturally carry over into Python
- The Selenium community officially supports Python APIs of the WebDriver, so there's already some interest in using Python as a browser testing tool language
- Python also has good testing related tooling such as PyTest, so there's opportunity for synergies in the ecosystem
- Porting Watir to several other languages would be beneficial to the testing community overall.

If you're interested in Nerodia, check out [these docs](https://nerodia.readthedocs.io/en/latest/) that contain more information for how to install and use Nerodia.

In the next post I'll show an example script using Nerodia.