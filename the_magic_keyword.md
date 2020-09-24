In the past while, I've been looking at some specific uses of Robot Framework. I've seen a few teams work with Robot to build test frameworks based in Selenium and/or Appium, and I've dabbled in writing custom keyword libraries. Overall I think Robot is pretty good, even if I heartily still prefer [Pytest](https://simplythetest.tumblr.com/post/188858906385/pytest-the-awesome-parts). Robot does provide solid reporting via HTML/XML pages off the shelf and is straightforward to get started with.

However, I can see pitfalls ahead with using keyword-driven frameworks, and Robot is no different. Here are two tips to keep in mind if you decide to use Robot in Python:

**Stay Away from Excel-Driven Development**: I think the biggest red flag for a keyword-based test framework is when the first thing a tester/developer does as part of their workflow is open a spreadsheet in Excel. Before even seeing how the rest of the framework is structured, running tests from an Excel-like interface means there's big problems. 

The reason using Excel is such a bad sign is that the tests almost certainly are not _autonomous_, meaning tests cannot be run without major human intervention or assistance. Not being autonomous means there are several major issues in this case.

Tests require a tester or developer to be present to setup and run tests - meaning running tests as part of an autonomous continuous integration job or pipeline is almost certainly not possible. This might be fine at first, maybe even desirable, but not being pipeline or CI friendly is a major shortcoming over time.
  
As well, tests based on an Excel sheet tend to have specific, bespoke configurations. A tester/developer needs to know which values go in which cell and in what format. This is overloading the spreadsheet with too much implicit data. 
  
A side effect of this setup tends to be tests that do too much and try to account for too many possible execution paths. Since it is possible to arrange, add and remove test cases based on what is in each row, test setup and teardown need to be overly flexible. The supposed benefit here is that the tester/developer can use the test framework to test the application in novel, exploratory ways but this is often an unrealized promise. Using an Excel-based approach for designing your tests and test data can lead to all sorts of [premature optimization](https://www.goodreads.com/quotes/1194913-premature-optimization-is-the-root-of-all-evil).
In my opinion, this is the single worst part aspect of using an Excel sheet to drive automated tests since it affects the overall architecture of such test frameworks in deep ways. 

**Write Your Own Keywords**: A more Robot-specific observation is to write you own keywords instead of directly writing tests with keywords from third-party libraries. Robot does allow this but it is not emphasized enough. The main reason for composing your own set of keywords is for test framework maintenance; successful test automation efforts tend to fall into a [valley of success](https://titusfortner.com/2020/09/08/valley-of-success.html) and this is done by building your test framework for maintainability from the start. 

Two ways that Robot tests can become unmaintainable are when third-party libraries change unexpectedly and when trying to make use of multiple libraries in a single test case. 

For example, consider this Robot test using AppiumLibrary:

```
Library  AppiumLibrary

# snip

Verify Keyboard is Visible

    Open Application  http://my-appium-server:4321/wd/hub 
       ... platformName=Android 
       ... platformVersion=10.0 
       ... deviceName="Google Pixel 3"
       ... app=myAppAndroid
    ${keyboardShown}=  Is Keyboard Shown
    Should Be True  ${keyboardShown}
```

In this test, the app is expected to invoke the keyboard when opened. This can be verified using an Android device without issue. 

Now suppose that the _Is Keyboard Shown_ keyword becomes deprecated. This could be due to not working with iOS apps or due to how Appium works with keyboards on devices. Now this test needs to be updated, along with any other test where _Is Keyboard Shown_ is used, leading to a find-and-replace headache.

One way to curb this problem is to write a custom keyword capturing this test functionality. Here's an example implementation:

```
Verify Keyboard Appears
    ${keyboardShown}=  Is Keyboard Shown
    Should Be True  ${keyboardShown}
```

Now using this custom keyword means that the test functionality can be updated in one place throughout the whole test framework, and can updated as needed in AppiumLibrary changes.

Another place where custom keywords becomes handy is when multiple libraries are used. Consider this example:

```
Library  SeleniumLibrary

# snip

Mobile Web Case
    Open Browser  browser=Chrome # more options
    Click Element  id=enter-site
    # more possible steps
```

This looks fine. Suppose now due to how devices are set up on your grid you need to specify a landscape orientation first on the device. Assuming that Selenium and Appium work well in conjunction with each other, if you tried this:

```
Library  SeleniumLibrary
Library  AppiumLibrary

# snip

Mobile Web Case
    Open Browser  browser=Chrome # more options
    Landscape
    Click Element  id=enter-site
    # more possible steps
```

you would see some runtime errors stating that the Landscape keyword is not defined. This is completely true since it is not clear which library defines each keyword now. This can be solved by something like this

```
# snip

Mobile Web Case
    SeleniumLibrary.Open Browser  browser=Chrome # more options
    AppiumLibrary.Landscape
    SeleniumLibrary.Click Element  id=enter-site
    # more possible steps
```

but this creates a lot of extra work since now each library needs to be specified for each keyword. This does not seem maintainable. 

Again one way around this is to create a middle layer for custom keywords so that the Robot test cases do not need to be updated for syntactic changes when adding additional libraries. 

## Can I Have a Word?

Overall, maintainability is crucial for any successful test automation approach. Managing keywords in Robot keeps test frameworks maintainable, and thinking about autonomous test execution will drive test frameworks towards success.
