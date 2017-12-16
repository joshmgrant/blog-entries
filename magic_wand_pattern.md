Sometimes, all we need is a little magic. This goes double for automated browser testing.

Often times a specific testing tool or framework will provide almost all the capabilities and features needed to test a particular application. There are rare cases where our test or test harness needs to do something non-standard or "against the grain". In these cases, we can often solve our problem by accessing a lower-level component of a tool with some more general (but also potentially more dangerous) capabilities. Test tools that are built with this in mind follow the _magic wand pattern_, which is a helpful design pattern in testing tools. 

I think this idea may be better illustrated with some examples. 

**The Selenium WebDriver and its JavascriptExecutor**

The Selenium WebDriver is a low-level API for driving a browser with actions that are similar to that of a human end-user. The WebDriver has standard capabilities for opening a browser instance, navigating to sites and interacting with elements on a site in its DOM. Such interactions include clicking, sending keystrokes or reading element attributes. In most cases of browser tests, elements are interacted with and the WebDriver handles cases in an expected way. As an example, consider an HTML input element. If the WebDriver tries to send keys to an input that exists and is visible, the keys is are sent to the input and the application executes any program logic that may follow. If the WebDriver tries to send keys to an element that does not exist or is not visible, an exception is raised. When interacting with inputs, often these outcomes are entirely acceptable and work as intended. 

But what if you wanted to send keys to an input that purposely invisible and have it work as if it were visible? Typically users (and tests) wouldn't want do this but there are cases where this may be useful. One common use case is interacting with a [file input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file) when downloading a file. Often these kinds of elements are invisible from view and are nested in more complicated elements. How could we do this with the WebDriver? 

The magic wand in this case is the [JavascriptExecutor](https://seleniumhq.github.io/selenium/docs/api/java/org/openqa/selenium/JavascriptExecutor.html). The JavascriptExecutor allows the WebDriver to execute arbitrary JavaScript into the browser. Typically an end user would not do this; any JavaScript executed is based on the logic of the underlying web app and not user provided. In our case we may need to work around this technical limitation for our test context. The JavascriptExectuor could execute a script to make the file input visible and set a download file path. 

