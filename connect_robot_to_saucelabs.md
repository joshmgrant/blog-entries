I'm a major Python fan. One test tool that's gaining (has gained?) popularity in the Python world is [Robot Framework](https://robotframework.org/). Robot Framework - which I will call Robot from now on - is a keyword-based test framework with a wide range of keyword libraries and a clean keyword domain specific language (DSL) for writing test cases that is quite similar to Markdown. One of the reasons teams choose Robot is that it allows developers to write Python code when needed but also provides neat and tidy approaches to working with both Selenium Webdriver and Appium in projects. 

One question that comes up from time to time when using Robot with Sauce Labs is

```
How do I connect my existing tests to run on Sauce Labs?
```

In this post I'll cover two examples of how to connect Robot tests to Sauce Labs. First, I'll show how to connect Selenium-based web tests using the SeleniumLibrary library. Second, how to connect Appium-based native app tests using the AppiumLibrary library. In a later post, I'll show how you can use pure Python to create custom libraries, or at least the basics of how to do so.

For the rest of this post, I'm going to assume basic familiarity with Robot constructs such as [writing test cases](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-cases) and [working with libraries](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#using-test-libraries).

## Connecting Selenium-Based Web Tests to Sauce

The most common approach to writing Selenium-based web tests in Robot is to use the [SeleniumLibrary](https://github.com/robotframework/SeleniumLibrary) library. This library wraps up all needed Python dependencies such as the Webdriver and provides an extensive list of keywords to use for browser actions. 

The main keyword I want to point out is [Open Browser](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html#Open%20Browser). This keyword starts a new browser session, either local or remote. It has a set of named arguments to pass in, and if no arguments are passed in will default to trying to start a local Firefox browser instance.

To connect to Sauce, the following arguments are required:

- browser
- remote_url
- capabilities

which is usual for Selenium Webdriver sessions that connect to Sauce Labs. Here's an example of a test using the SeleniumLibrary keywords to start a Chrome session on Sauce Labs. Let's call is `selenium_example.robot`.

```markdown
*** Settings ***

Library  SeleniumLibrary

*** Variables ***

@{_tmp} 
    ...  browserName: Chrome,
    ...  platform: Windows 10,
    ...  version: latest,
    ...  username: %{SAUCE_USERNAME},
    ...  accessKey: %{SAUCE_ACCESS_KEY},
    ...  name: ${SUITE_NAME},
    ...  build: My-Selenium-Robot-Test

${browser}          Chrome
${capabilities}     ${EMPTY.join(${_tmp})} 
${remote_url}       https://ondemand.saucelabs.com/wd/hub

*** Keywords ***

Open Test App
    Open browser  https://www.saucedemo.com  browser=${browser}
    ...  remote_url=${remote_url}
    ...  desired_capabilities=${capabilities}


*** Test Cases ***

Verify Connection
	Open Test App

	Title Should Be  Swag Labs

	[Teardown]  Close Browser
```

This can be executed by running

```
robot selenium_example.robot
```

Let's unpack this. 

First, the SeleniumLibrary is imported. This provides all keywords in that library for use in this test case.

Next we define some variables. Since the needed arguments are `browser`, `remote_url`, and `capabilities`, each of these are defined. Both the `browser` and `remote_url` arguments are strings and so can defined in a pretty straightforward way. The `capabilities` argument is defined as a list of values, and so a list is created using the Robot test case syntax, providing all needed information for Sauce Labs.

One subtle but important thing to point out when defining values is that Robot provides some special constructs for defining values. 

To access Sauce username and access key credentials, the [environment variable](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#environment-variables) values are used (the `%` values). 

As well, inline values can be computed/called using the [scalar value](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#scalar-variable-syntax) construct (the `$` value for `name`). Values within a scalar can be either [`Built-In` values](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#built-in-variables) such as the `SUITE_NAME` above, or can be Python values either constant or computed.

Since we have the needed values to start a Sauce session, we can pass these values into the Open Browser keyword (_note_: there are _two_ spaces between a Robot keyword and its argument(s)). I've decided to create a custom keyword `Open Test App` to wrap up starting a session in a neat and tidy way. 

Finally, we have the test case. The test case is very basic, starting a session, checking a title then closing the session. Clearly this is a low value test but [sometimes good developers write bad tests](https://simplythetest.tumblr.com/post/623552640767361024/when-good-developers-write-bad-tests) for demonstration purposes. This test makes use of the `Title Should Be` and `Close Browser` keywords from the SeleniumLibrary. 

Voilà, we have a working test in Robot that connects to Sauce Labs. 

## Connecting Appium-Based Native Mobile App Tests to Sauce

A case that comes up even more often in my experience is using Robot to test mobile apps (web and native). This is likely because the AppiumLibrary makes getting started with testing native apps more intuitive than using Appium directly (but could also be because folks just love using Python!). 

Much like the SeleniumLibrary, the AppiumLibrary library packages up Python dependencies for working with Appium and provides an extensive list of keywords for working with mobile apps. Let's take a look at a similar Robot test for connecting to Sauce labs to test a native mobile application.

```markdown
*** Settings ***

Library  AppiumLibrary

*** Variables ***

${KEY}                  %{TESTOBJECT_SAMPLE_ANDROID}

*** Keywords ***

Open Mobile App
    Open application  http://us1.appium.testobject.com/wd/hub/
    ...  platformName=Android
    ...  platformVersion=9
    ...  deviceOrientation=portrait
    ...  browserName=''
    ...  testobject_api_key=${KEY}
    ...  privateDevicesOnly=true
    ...  name=${TEST_NAME}  


*** Test Cases ***

Valid Login with Standard User
	Open Mobile App

	Element should be visible  accessibility_id=test-LOGIN

	[Teardown]  Close All Applications
```

As you can see, this looks similar to the Selenium case. However, one important distinction is in the [`Open Application` keyword](https://serhatbolsu.github.io/robotframework-appiumlibrary/AppiumLibrary.html#Open%20Application) from the AppiumLibrary library. This keyword opens the target application, but instead of having all named parameters in its definition, `Open Application` also takes a `remote_url` named argument as well as a Python `**kwargs` argument, also known as [keyword arguments](https://treyhunner.com/2018/04/keyword-arguments-in-python/#What_are_keyword_arguments?). This is a variable-length dictionary of key/values that AppiumLibrary will pass along to the AppiumDriver instance that is instantiated.The `remote_url` argument is fairly straightforward to understand.

Likely, these kwargs will be a set of capabilities specifying the mobile environment that the driver will be created within. There's no set requirements or restrictions on the kwargs that are passed into the `Open Application` keyword but consider passing in only "needed" values.

Just for fun, instead of defining needed capabilities in a variable, they are hard-coded in the keyword itself. This is true for some definition of "fun". As well, the legacy TestObject API key credential is defined using an environment variable. 

The last thing to note is that both `Element should be visible` and `Close all applications` are keywords provided by AppiumLibrary. 

Voilà, we have another working test in Robot that connects to Sauce Labs.

That's it for now. Happy testing!