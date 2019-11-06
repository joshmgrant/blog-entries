Starting a series of posts based on [awesome stuff in Pytest](https://simplythetest.tumblr.com/post/188858906385/pytest-the-awesome-parts), I thought I'd start with a well-known plugin for working with browser-based tests. This plugin is called, helpfully, [pytest-selenium](https://pytest-selenium.readthedocs.io/en/latest/). 

Mainly, I think there are two cool aspects to pytest-selenium:

1. It provides a clean, straightforward command line interface for executing browser-based tests, and
2. It provides fixtures for a browser instance in a minimal, easy way. 

Let's look at these two points in order. 

In my experience, one underappreciated aspects of test automation is the interface for _how_ tests get executed. I've more than once committed changes to a configuration file that I was using for debugging to have a test execution blow up when executed on Jenkins. I've also wrestled - mostly unsuccessfully - with setting up command line arguments in the correct way to execute test. Pytest and pytest-selenium work pretty well together to help avoid these problematic situations. 

With pytest-selenium, you can start tests by browser neatly. Suppose I have some tests I'd like to run against a local version of Firefox. With pytest-selenium, this can be done using 

```bash
pytest --driver Firefox
```

and if I decide to change to Chrome, I can change this line to

```bash
pytest --driver Chrome
```

which is nice and easy. And if I'd like to set up tests to run against a Selenium Grid instance I can [specify capabilities](https://pytest-selenium.readthedocs.io/en/latest/user_guide.html#specifying-capabilities) either from command line arguments directly or using a [capabilities.json file](https://pytest-selenium.readthedocs.io/en/latest/user_guide.html#capabilities-files). This is helpful for local test execution or debugging since no configuration files need to be updated or changed and Continuous Integration execution is unaffected. 

Now let's look at how those `driver` values are used in test code. As mentioned previously, pytest-selenium provides fixtures to produce a driver object. Let's see what a minimal test looks likes with the basic `selenium` fixture:

```python
def test_example(selenium):
    selenium.get('http://www.example.com')
```

That's it! Out of the box the `selenium` fixture can be passed into tests to provide a Selenium-based driver object. Light and easy.

Where this really starts to get interesting is when you use a page object pattern. If page objects take a `selenium` object as a constructor, then generating page objects by fixtures can be lightweight as well:

```python
@pytest.fixture
def HomePage(selenium):
    return HomePageObject(selenium)
```

That's it! No awkward driver instantiation code in page objects, only clean reusable fixtures.

Pytest has some other interesting features but to me these are the killer ones. Pytest-selenium is definitely a good choice for working with Selenium-based tests in Pytest.