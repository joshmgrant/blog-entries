In my previous post, I introduced the lovely [Nerodia](http://simplythetest.tumblr.com/post/177455969240/introducing-nerodia-part-1-what-is-nerodia), a port of Watir for Python. Here I'd like to show a sample script and how Nerodia works. I'll assume effectively no familarity with Watir, just to keep things light and easy. 

Here is a Python script using Nerodia to verify there are some text values located on the Watir project homepage:

> from nerodia.browser import Browser
> 
> br = Browser(browser="firefox")
> 
> br.goto("https://watir.com")
> 
> \# Check that "Titus" is somewhere in the page text
> assert "Watir" in br.text
> 
> \# Check "open source" is in the intro
> intro = br.div(class_name='intro')
> intro_text = intro.text
> assert "open source" in intro_text
> 
> \# Check that the page is correct via the URL
> br.link(text='Guides').click()
> assert 'watir.com/guides/' in br.url
> 
> br.close()

As of the posting of this article, this script should run and exit without errors providing Nerodia is installed. 

There's a few interesting aspects to this script I'd like to point out: 

*Similar feel to using the Selenium WebDriver*: If you substituted *br = webdriver.Firefox()* for *br = Browser(browser="firefox")*, this script would look and feel just like a WebDriver script (even if it wouldn't execute properly). This suggests that the learning curve for those proficient with the WebDriver for writing scripts would not too steep for writing script with Nerodia.

*Logical reuse of elements*: One aspect of Nerodia that distinguishes it from the WebDriver is the ability to define elements individually and use them effectively later in a script. As an example, consider the line

> intro = br.div(class_name='intro')

in the above script. This gets a div element from the DOM with class name *intro* and creates an object that represents it for use in the script. This object can be reused in ways that are logical, such as in the next line

> intro_text = intro.text

which gets text from this element for verification. We could even add a line later in the script to check if the element is visible by writing

> assert intro.visible

without needing to reassign the variable. This is allows elements to be defined and use in a logical manner without having to call *findElement*-style methods over and over again.

*Synchronization is standard*: Notice this script does not contain any sleep statements, explicit waits, or global implicit waits. In fact, this script should work on a variety of differently powered machines - some low-powered - without adding any of these things. This is because Nerodia contains built-in synchronization functionality to smartly wait for browser and DOM events to occur before interacting with the DOM. This means test developer don't have to have as much overhead to get scripts running in a stable way against apps that are slow due to architecture or networking.

*It's Pythonic*: While I'm not exactly hardcore when it comes to language idioms, I do appreciate how Pythonic Nerodia is as a browser automation tool. Assertion statements are easy to understand, [snake casing](https://en.wikipedia.org/wiki/Snake_case) is used and overall the script feels like a Python script and not some hacky holdover from Ruby.

These are some strengths that Nerodia brings over conventional WebDriver scripting. In the next post I'll take a look at what this might mean for some page object implementations using Nerodia.