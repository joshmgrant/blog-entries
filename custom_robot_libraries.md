In a [previous post](https://simplythetest.tumblr.com/post/623812587615813633/using-robot-framework-with-sauce-labs-a-primer) I showed some examples of how to connect to Sauce Labs in Robot Framework using both the SeleniumLibrary and AppiumLibrary. I also alluded to showing how to write custom libraries with Robot, which I will show in this post. 

In my humble opinion, one of the killer features of Robot Framework in Python is the ability to write custom libraries using pure Python and the Robot API. This can be done in addition to using pre-written keyword libraries or instead of using such libraries. Writing custom keywords in Python that can be used in `.robot` files is also a neat separation of concerns for test writing and test maintenance. A team's Pythonistas can handle test logic and page object layers in a conventional way while non-Pythonistas (BA-istas or PO-istas perhaps?) can write test cases using a Markdown-like format.

Here is a a scenario where using a custom library instead of SeleniumLibrary may arise. As well, I'm going to use features in the Robot Framework API as of [version 3.2](https://github.com/robotframework/robotframework/releases/tag/v3.2).

## How To Do It

Suppose a web app needs to be tested against a latest version of Safari - 12.0 or later. These later versions all communicate with the Selenium WebDriver using the W3C wire protocol, which drops desired capabilities and changes the capabilities/options syntax. There are also changes to how cloud services such as Sauce Labs receive capabilities with this new protocol. This scenario is (currently) a bit tricky to handle with SeleniumLibrary, but relatively easy to handle with the Python WebDriver bindings. 

There are two parts to this test scenario:

- the Robot test case, and
- the Python custom library. 

Let's examine the Robot test case first, which looks like this

```markdown
*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This case was created to validate the app against Safari.
Library   SafariCase.py

*** Test Cases ***
Verification Workflow
	Open Safari

	Login As User

	Verify Page

	[Teardown]  Close Safari

```

Let's say this file is called `verify_safari_case.robot`. So far this looks like a conventional `.robot` file test case. The only interesting part is that the library that is imported is a Python file. Let's take a look at the Python file `SafariCase.py`:

```python
from robot.api.deco import keyword, library
from selenium import webdriver
import os


BASE_URL = 'https://www.saucedemo.com'

@library
class SafariCase(object):
    def __init__(self):
        self.browser = None

    @keyword
    def open_safari(self, url=BASE_URL):
        caps = {
            'browserName': 'safari',
            'browserVersion': '13.1',
            'platformName': 'macOS 10.15',
            'sauce:options': {
                'seleniumVersion': '3.14.0'
            }
        }

        username = os.environ['SAUCE_USERNAME']
        access_key = os.environ['SAUCE_ACCESS_KEY']
        sauce_endpoint = 'ondemand.saucelabs.com/wd/hub/'

        remote_url = 'https://{}:{}@{}'.format(username, access_key, sauce_endpoint)

        self.browser = webdriver.Remote(command_executor=remote_url desired_capabilities=caps)
        self.browser.get(BASE_URL)

    @keyword
    def login_as_user(self):
        self.browser.find_element_by_id("user-name").send_keys("standard_user")
        self.browser.find_element_by_id("password").send_keys("secret_sauce")
        self.browser.find_element_by_id("login-button").click()

    @keyword
    def verify_page(self):
        assert "inventory" in self.browser.current_url


    @keyword
    def close_safari(self):
        self.browser.close()
```

Definitely looking like a conventional Python file with a single class `SafariCase` defined. To execute this test case, we can use the Robot runner as follows:

```bash
robot verify_safari_case.robot
```

if we require that `verify_safari_case.robot` and `SafariCase.py` are located in the same directory.

All good at this point. Writing the test logic for keywords can be done using Python while test cases themselves can be written in Robot. Time to [celebrate!](https://www.youtube.com/watch?v=3GwjfUFyY6M)

Now let's unpack `SafariCase.py` a bit further. 

First we can note that we're making use of Robot's API for writing keywords and libraries via 

```python
from robot.api.deco import keyword, library
```

We only need to import the `keyword` and `library` decorators for our case but there are other tools in the [`robot.api`](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-libraries) module for other use cases. These decorators allow a standard class with methods to become a Robot library with keywords. Each method decorated with `@keyword` creates a Robot keyword that can be used. Robot in Python is smart enough to handle casing changes, so a `snake_cased_keyword` can be interpreted as a `Sentence Cased Keyword` without much trouble. This is helpful for keeping Python code looking like Python while Robot file look like, well, Robot. 

The [`@library`](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#library-decorator) and [`@keyword`](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#keyword-decorator) decorators work mostly as one would expect but both take additional optional arguments for things like scoping. Also note that `@keyword` functions do not need to be in a class but we do so here because we need to maintain an internal state for the `browser` field. Object-oriented programming is not a requirement for writing custom libraries but tends to be helpful.

One last important point is that the name of the library class `SafariCase` matches the name of the Python file `SafariCase.py`. This is a convention and simplification in the Robot library API. Please follow this convention. 

### Warning: Mind the Gap

There is one important pitfall I will point out to writing custom Python libraries for use with Selenium- and Appium-based tests, something that astute readers may have noticed already. What happens if the `SafariCase` library is used in conjunction with test cases that also make use of SeleniumLibrary keywords?

One problem that comes to mind is collision of keywords. What if `SafariCase` implements a keyword called `Open Browser`, which is also in SeleniumLibrary? How would a test know which one to execute? More importantly, how would a test developer know? 

A deeper problem is encapsulated WebDriver state. Remember that the `SafariCase` library uses an object-oriented approach by creating a class with a `browser` field. Would SeleniumLibrary have access to this field? If so, how? Managing WebDriver instances may get pernicious when multiple libraries are creating and handling their own instance.

These are both problems that can be solved by [extending the SeleniumLibrary](https://github.com/robotframework/SeleniumLibrary/blob/master/docs/extending/extending.rst#id3) instead of writing custom libraries from scratch. This allows for custom functionality that can be added to SeleniumLibrary for a given project. I may or may not dig into this topic in a future post, depending on [_gestures wildly_] all of this stuff that happening.

For now, relax knowing that it is possible and even desireable to write custom libraries in Python for Robot Framework.
