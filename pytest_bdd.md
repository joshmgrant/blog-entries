In continuing my [exploration]() of Pytest and its wonderful features, I want to cover a pytest plugin that's really more a full fledged test automation tool - [pytest-bdd]().

Pytest-bdd is really a variant on more widely used frameworks like [Cucumber](https://cucumber.io) or [Behave](https://behave.readthedocs.io/en/latest/), which itself is essentially Python Cucumber. BDD is a popular approach for many teams either working with automated testing for the first time, or teams that experienced with automation and looking for a mature methodology to use. They key feature to BDD is writing _feature files_ in a particular common language syntax called [Gherkin](https://cucumber.io/docs/gherkin/reference/). This allows features to first be written in a form such as this

```
Feature: Adding Items to Shopping Cart
  Scenario: Add Item to Empty Cart
    Given: I am on the items list page
    When: I add one item to my cart
    Then: I should see one item in my cart
```

which can then be translated into computer-code and executed. These feature files can the created by any team members, including through collaboration. This allows new features to be documented by executing test code and facilitates team communication.

Let's see an example of how pytest-bdd manages this. Start with a feature file using Gherkin. Keeping with the theme of an online store, the feature is called `store_login.feature` which describes how two particular login flows work, one valid and one invalid. It looks like this:

```
Feature: Login to My Store
    Basic login flows to my-store.ca

Scenario: Valid Login
    Given I visit the login page
    When I login with valid credentials
    Then I should be on the inventory page

Scenario: Invalid Login
    Given I visit the login page
    When I login with invalid credentials
    Then I should see an error message
```

Notice how these scenarios are descriptive. The idea is that these features may not be written directly by test developers but in collaboration with product owners, user experience designers and other stakeholders.

Now let's see how these steps are implemented. The test developer now can write a file called `test_store_login.py` which might look like this:

```python
import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver


@pytest.fixture
def browser(request):
    br = webdriver.Firefox()

    yield br

    br.quit()


@scenario("store_login.feature", "Valid Login")
def test_valid_login():
    pass

@scenario("store_login.feature", "Valid Login")
def test_invalid_login():
    pass

@given("I visit the login page")
def visit_page(browser):
    browser.get("https://my-store.ca")

@when("I login with valid credentials")
def login_valid(browser):
    browser.find_element_by_id("user-name").send_keys('valid_user')
    browser.find_element_by_id("password").send_keys('good_password')
    browser.find_element_by_class_name("btn_action").click()

@when("I login with invalid credentials")
def login_valid(browser):
    browser.find_element_by_id("user-name").send_keys('nope')
    browser.find_element_by_id("password").send_keys('still_nope')
    browser.find_element_by_class_name("btn_action").click()

@then("I should be on the inventory page")
def on_inventory_page(browser):
    assert 'inventory' in browser.current_url

@then("I should see an error message")
def on_inventory_page(browser):
    assert browser.find_element_by_class_name('error-button').present

```

This shows how we can still use Pytest constructs we know - fixtures, appending `test_` to files to execute - and make use of the BDD tooling around Gherkin steps. Also there might be additional work that could be done here like using a page object pattern or combining steps, but I want to focus on the BDD aspect of this example.

To execute this test, we can call

```bash
pytest test_store_login.py
```

and see the result. Pytest-bdd will also generate some helpful Cucumber-style reporting in addition to the standard Pytest reporting. Also available are [substitutions and regular expressions]() in Gherkin steps.

At last, BDD and Pytest together!

While this is all fine and good, some teams may want to experiment with BDD-style tooling without committing to a full-on BDD tool such as Cucumber. Even if teams do want to commit to using BDD tools, eventually some teams find that test developers end up writing and managing all the test automation code directly, including writing and managing feature files. This can be cumbersome, particularly since test developers don't need to have feature files as an extra layer to manage.

This is where pytest-bdd starts to really shine. Since pytest-bdd uses pytest, it is possible to

- write test frameworks that mix both BDD and conventional Pytest style tests, and
- remove BDD usage while refactoring into plain Pytest tests.

In the above situation, suppose we want to remove the BDD tooling and use plain pytest functionality. We can rewrite the valid login test to do this, while keeping the invalid login test using pytest-bdd. After some copy-pasting, the resulting `test_store_login.py` might look like this: 

```python
import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver


@pytest.fixture
def browser(request):
    br = webdriver.Firefox()

    yield br

    br.quit()


def test_valid_login(browser):
    browser.get("https://my-store.ca")

    browser.find_element_by_id("user-name").send_keys('valid_user')
    browser.find_element_by_id("password").send_keys('good_password')
    browser.find_element_by_class_name("btn_action").click()

    assert 'inventory' in browser.current_url

@scenario("store_login.feature", "Valid Login")
def test_invalid_login():
    pass

@given("I visit the login page")
def visit_page(browser):
    browser.get("https://my-store.ca")


@when("I login with invalid credentials")
def login_valid(browser):
    browser.find_element_by_id("user-name").send_keys('nope')
    browser.find_element_by_id("password").send_keys('still_nope')
    browser.find_element_by_class_name("btn_action").click()

@then("I should see an error message")
def on_inventory_page(browser):
    assert browser.find_element_by_class_name('error-button').present

```

Using the same command as before,

```bash
pytest test_store_login.py
```

both tests execute, the Pytest reporting is the same as before and the additional pytest-bdd reporting is available for the invalid login scenario. If this is deemed successful, the same process could be applied to the invalid login case. Notice we did not need to manipulate the feature file in anyway, so that can be kept or removed as needed without affecting test execution.

While pytest-bdd is a useful plugin on its own for getting started with BDD and Python, it also has the additional goodness of not locking teams into BDD approaches to test automation. This is a surprisingly killer feature that many BDD frameworks do not have, which is another excellent reason to use Pytest, with or without pytest-bdd.