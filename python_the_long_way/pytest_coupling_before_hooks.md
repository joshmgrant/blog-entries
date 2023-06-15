In a [previous post](https://simplythetest.tumblr.com/post/640676369255268352/fixtures-over-classes-why-using-pytest-fixtures) I discussed why Pytest's fixtures are preferable to using class-based object oriented programming approaches for before/after hooks in tests. The main point was that using classes and inheritance, it can be too easy to mix setup/teardown logic and test logic together. This violates the concept of staying in the [valley of success](https://titusfortner.com/2020/09/08/valley-of-success.html) and instead lingering into the valley of doom.

In this post, I'd like to discuss the second main pitfall of OOP test deign, namely the pitfall of

- accidental tight coupling of individual tests and setup/teardown logic

with some examples. 

Suppose we have a base test class that looks like this:

```python
class BaseCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("www.myapp.com/login")

    def tearDown(self):
        self.driver.quit()

```

and we use it to create a test case like this

```python
class TestLogin(BaseCase):

    def test_valid(self):
        # test valid case

    def test_invalid(self):
        # test invalid case

    def test_blank(self):
        # test blank credentials cases

```

Seems pretty clear cut so far. Now suppose we have a bunch of tests that depend on logging in. Thinking of code reuse through inheritance, we could create the following class:

```python
class LoggedInCase(BaseCase):

    def logInAsAlice(self):
        # use Alice's credentials

    def logOutAsAlice(self):
        # logout, purely for example

    def setUp(self):
        super().setUp()
        self.logInAsAlice()
        

    def tearDown(self):
        self.logOutAsAlice()
        super().tearDown()

```

and for completeness, here's a sample test using `LoggedInCase`:

```python
class TestCreateAccount(LoggedInCase):

    def test_alice_can_create_an_account(self):
        # basic test

    def test_alice_can_create_an_account_special_case(self):
        # maybe leave out a required value or something

```

This all looks fairly straightforward so far. What could [possibly go wrong?](https://www.youtube.com/watch?v=7trn91xkJ0w).

Let's say that over time, new test cases need to be added that use Bob's account. Bob may have different permissions than Alice, for example. How could we fit that into this test code structure?

There's a few approaches. Here's one that will totally work and is not at all a good idea: adding a conditional to check the user credentials. This approach might look like the following:

```python
class LoggedInCase(BaseCase):

    def logInAsAlice(self):
        # use Alice's credentials

    def logOutAsAlice(self):
        # logout, purely for example
    
    def logInAsBob(self):
        # use Bob's credentials

    def logOutAsBob(self):
        # logout, purely for example

    def setUp(self, isBob=False):
        super().setUp()
        if isBob:
            self.logInAsBob()
        else:
            self.logInAsAlice()
        

    def tearDown(self, isBob=False):
        if isBob:
            self.logOutAsBob()
        else:
            self.logOutAsAlice()
        
        super().tearDown()

```

This approach looks clunky, and it is. Each time a test case extends `LoggedInCase` the setup, a check is performed on the setup/teardown methods to verify if the user is Bob or not. This does have the benefit of not affecting previously written tests, which is good - at least in the short term. However maintenance becomes a major issue. For example, what if an additional user `Carla` is needed? Suddenly using a Boolean value to denote who is logged in becomes tricky. Should the default be Alice, or someone else? As well, if someone forgets to add the Boolean value, will this invalidate some test results? Questions questions, and not a lot of good answers. 

Using conditionals in tests isn't a great pattern to follow in general, and this example shows one such pitfall of doing so.

What else could we try? Let's create a new class that inherits from `BaseTest` instead, which might look like this:

```python
class LoggedInAsBobCase(BaseCase):

    def logInAsBob(self):
        # use Bob's credentials

    def logOutAsBob(self):
        # logout, purely for example

    def setUp(self):
        super().setUp()
        self.logInAsBob()
        

    def tearDown(self, isBob=False):
        self.logOutAsBob()
        super().tearDown()

```

This is a bit better, since now we could simply extend either `LoggedInCase` or `LoggedInAsBobCase` as needed. However, the naming of these classes is a bit underwhelming. What's so special about Bob? We could rename `LoggedInCase` to something else, but that would require some nontrivial refactoring of subclasses. And we still have the issue that we may need to add more classes if additional cases such as `LoginAsCarla` pop up. This approach is more "correct" than the conditional approach but still problematic.

Micheal Feathers has written long, long ago in 2013 about [the anti-pattern of superclassing in frameworks](https://michaelfeathers.typepad.com/michael_feathers_blog/2013/01/the-framework-superclass-anti-pattern.html). I feel like using super classes for setup/teardowns in test code is a flavour of this anti-pattern. Once you start using superclasses for setup/teardown behaviour, you're basically stuck with it and the pitfalls that come with it. Adding middle layers in the class hierarchy doesn't really help much and can create a lot of headaches as test projects grow. One not-so obvious workaround is to simply copy and paste a lot of code with small tweaks, which is fine but also not overly maintainable. 

Once again, Pytest's fixtures come to the rescue. 

Two ways fixtures can help are by allowing fixtures to use fixtures and allowing fixtures to be parameterized. 

Let's rework the first `BaseTest` and `LoggedInCase` using fixtures, which might look like the following:

```python

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.get("www.myapp.com/login")
    yield driver
    driver.quit()

@pytest.fixture
def loggedIn(browser):
    logInAsAlice(browser)

```

Each of these fixtures can be used independently, and we can see the direct relationship between them. The approach is decided for us, not requiring any clever hacking or lots of code creation. In our tests, we can also swap `browser` for `loggedIn` as needed.

Now let's discuss the Bob problem. How can we allow for the case where we need to login with Bob's credentials for tests? We can add another fixture:

```python
@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.get("www.myapp.com/login")
    yield driver
    driver.quit()

@pytest.fixture
def loggedIn(browser):
    logInAsAlice(browser)

@pytest.fixture
def loggedInAsBob(browser):
    logInAsBob(browser)

```

How do we address the `Carla` problem? Well we could add another fixture, but now we also have another trick up our sleeve: parametrized fixtures. Once we start adding more than two credentials, we can plan for the general case like this:

```python
@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.get("www.myapp.com/login")
    yield driver
    driver.quit()

@pytest.fixture(params=["Alice", "Bob", "Carla"])
def loggedIn(request, browser):
    loginAsUser(browser, request.param)
```

Here we can create a generic method `LoginAsUser` which accepts a `browser` value and a user string to login as that user. This is a big help with code reuse if test cases are similar to one another except for setup/teardown. This is an approach that isn't readily available in the classic OOP approach. Since fixtures are essential Python functions, we can consider functions calling other functions to handle test design, as opposed to trying to jiggle around classes and methods.

Pytest fixtures don't solve _all_ problems with designing and writing good tests but they do help quite a bit.