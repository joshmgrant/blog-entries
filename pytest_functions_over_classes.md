Big hat tip to [Lindsay Walker](https://www.linkedin.com/in/lindsayjowalker/) for inspiring this topic!

A good practice in Pytest is to [use fixtures](https://simplythetest.tumblr.com/post/189372692920/pytest-the-awesome-parts-fixtures), which are a first-class feature within Pytest. This allows specific fixture functionality to be applied to functions as well as classes and modules. Using fixtures at the function level is the default, but it turns out this is actually a good practice as well. 

In contrast most test framework libraries or tools encourage (or require) tests to use classes in a heavily object-oriented approach. In fact, Python's own unittest framework [encourages this approach](https://docs.python.org/3/library/unittest.html#unittest.TestCase). So why did Pytest decide on using (functional) fixtures instead of (class object-oriented) setup/teardown methods? 

Partially, I think this preference or design is an extension of the ["prefer composition over inheritance"](https://en.wikipedia.org/wiki/Composition_over_inheritance) approach. While inheritance does work fairly well in test code contexts (in my opinion), there are still some pitfalls. Two main pitfalls are
 
- explicitly mixing tests and setup/teardown logic, and 
- accidental tight coupling of individual tests and setup/teardown logic. 

Let's look at both of these drawbacks of using classes to represent tests and see how Pytest fixtures provide better approaches to avoid these pitfalls. In this post, I'll look at mixing tests and setup/teardown, how this can be problematic, and how Pytest fixtures alleviate this problem.

Let's start with an example. I'm going to consider a browser based test using the Selenium WebDriver, since browser tests have nontrivial setup (at least opening a browser) and teardown (at least closing the browser) steps. Here's a test class using `unittest.TestCase`:

```python
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("www.myapp.com/login")

    def tearDown(self):
        self.driver.quit()

    def test_valid(self):
        # test valid case

    def test_invalid(self):
        # test invalid case

    def test_blank(self):
        # test blank credentials cases

```

Pretty standard approach using a class to represent a test case. This looks fine right? It is fine, we could even move the `setUp` and `tearDown` methods to a parent class to use with additional test cases, which might look like the following:

```python
# parent test class - base.py
class BaseCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("www.myapp.com/login")

    def tearDown(self):
        self.driver.quit()


# subclass that makes use of the setup/teardown - test_login.py
class TestLogin(BaseCase):

    def test_valid(self):
        # test valid case

    def test_invalid(self):
        # test invalid case

    def test_blank(self):
        # test blank credentials cases

```

So far so good. We've applied a pretty straightforward inheritance approach for code reuse, so now `BaseCase` can be extended and reuse the `setUp` and `tearDown` methods.

However, something else that is allowed in this approach is adding one or more test methods to `BaseCase`. Consider reworking the above code slightly to look like this:

```python
# parent test class - base.py
class BaseCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("www.myapp.com/login")

    def tearDown(self):
        self.driver.quit()

    def test_valid(self):
        # test valid case

# subclass that makes use of the setup/teardown - test_login.py
class TestLogin(BaseCase):

    def test_invalid(self):
        # test invalid case

    def test_blank(self):
        # test blank credentials cases

```

The only difference here is that `test_valid` is now included in `BaseCase`, making it a valid test method that will execute if found by Pytest's test runner. This is totally legal, and might even be desired behaviour in some cases. It might seem like a good idea to _always_ run the `test_valid` test method, right? More testing is better, right? 

Not quite.

In the short-run, running a test "every time" might be desirable, but it won't take long for this design to cause problems. Debugging test runs become more complicated because it's not clear that the `BaseCase` has executable test methods. Looking at this pitfall more carefully, it's clear that there is not a clear [separation of concerns](https://medium.com/machine-words/separation-of-concerns-1d735b703a60) between tests and setup/teardown. The `BaseCase` class appears to only contain setup/teardown logic and functionality, but that isn't actually the case. Now test developers need to treat `BaseCase` as a test case class unnecessarily.

As well, as more test classes are added that extend `BaseCase`, the number of tests executed will grow somewhat unexpectedly. Since test classes are collected, instantiated and then the resulting test methods are executed, this could cause some confusion since there are "repeated" test methods. Again, allowing `BaseCase` to have test methods unnecessarily complicates debugging and mental models of how tests should execute.

Possibly most importantly, there's nothing really _stopping_ a test developer from implementing `BaseCase` like this. A short-sighted design choice up front could cause lots of maintenance and debugging headaches later on.

Now let's see the same thing with fixtures:

```python 
@pytest.fixture
def browser(request):
     # initialize a driver somehow, assume driver is initialized
     driver.get("www.myapp.com/login")
     yield driver
     driver.quit()

def test_valid(browser):
    # test valid case

def test_invalid(browser):
    # test invalid case

def test_blank(browser):
    # test blank credentials cases

```

The fixture approach avoids poor separation of concerns of the class approach by explicitly distinguishing between a test function and a fixture. Fixtures cannot be found and executed the same way that test functions are. Now, wherever fixtures are defined and used will not interfere or complicate how tests are being written. If we want to use the same fixture elsewhere, we can import it like any other Python function/module from this file (or other approaches that Pytest provides). Superficially, this structure is the same as the class approach, but makes this critical distinction. It works the same as the class approach, but without classes.

A nice corollary of this approach is that there's fewer lines of code and fewer constructs to keep track of when writing tests. I would say that's a benefit as well. 

This shows how Pytest uses fixtures to avoid the pitfall of mixing test logic with setup/teardown logic. In the next post, we'll see how Pytest fixtures can help avoid accidental tight coupling of individual tests and setup/teardown logic.