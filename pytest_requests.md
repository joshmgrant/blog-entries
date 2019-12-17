In my final post about how [awesome Pytest is](https://simplythetest.tumblr.com/post/188858906385/pytest-the-awesome-parts), I'd like to bend the rules a bit and talk about how awesome another excellent Python library is: [requests](https://pypi.org/project/requests/). Requests is hands down one of my favourite pieces of software. Just like it says at the top of its home page, requests is HTTP made for humans. 

Let's look for an example with the handy [Restful-Booker](https://restful-booker.herokuapp.com/apidoc/index.html) app by Mark Winteringham:

```python
import requests

r = requests.get('https://restful-booker.herokuapp.com/booking')

print(r.status_code) # should be 200
print(r.text) # response body, should look like [{"bookingid":3},{"bookingid":1},...
print(r.json()) # same as r.text but in valid JSON

```

Straightforward and easy. No malarkey here, just HTTP requests and responses. 

Requests is nice because of its syntax and because it is a full featured HTTP library. Whether you need a one time simple GET or a more complicated request requiring things like manipulating headers or authentication along with a custom request body, requests has you covered.

Tying this back into Pytest and test automation, two questions I've seen a lot of teams and developers have are

1. "How do I build an API test framework?", and
2. "How can I use APIs in my automated browser tests for more stability?"

One (good) answer to both is "build your own with Pytest and Requests". 

For an example of API tests, a typical case is to examine the status code of a response. With requests, this is pretty easy. Here is what some basic GET style tests look like:

```python

import pytest
import requests

def test_app_is_available():
    response = requests.get("https://restful-booker.herokuapp.com/booking")

    assert response.ok

def test_page_unavailable():
    response = requests.get("https://restful-booker.herokuapp.com/not_there.html")

    assert response.status_code == 404

```

These tests verify if web app under test is up, meaning returning a 200- or 300-level HTTP status, and if a particular page does not exist and returns the correct 404 status. (For a fun reference on HTTP statuses and what they mean, please see [http.cat](http://http.cat).) In each case the `.get()` method returns a `Response` that can be used in a variety of ways. The first test makes use of requests' [Response.ok](https://2.python-requests.org//en/master/api/#requests.Response.ok) property. The second test looks for the particular status code of 404. While these tests are fairly elementary, they do represent core kinds of API tests: making a request and analyzing the response. Requests and Pytest make a great combination to start simple and build up tests as needed.

Another really great feature of requests for automated testing is the [Requests Session](https://2.python-requests.org//en/master/api/#requests.Session) construct. This allows for handling of a series of HTTP requests, maintaining stateful aspects of a session such as authentication, cookies, and so on. 

Here requests can help with building API utilities for browser testing. Here's a possible test that uses an API request directly to login to a web app instead of using the app UI:

```python
import pytest
import requests
from selenium import webdriver

@pytest.fixture
def logged_in_browser(request):
    api_session = requests.session.post("https://my-web-app.net/login", auth=('myuser', 'mypass'))
    cookies = api_session.cookies
    cookie = cookies['needed_cookie_from_authentication']

    driver = webdriver.Firefox()
    driver.add_cookie(cookie)

    yield driver

    driver.quit()
    api.session.close()

def create_entry_test(logged_in_browser):
    driver.get("https://my-web-app.net/welcome_page.html") # fast forward to the desired page

    # continue with the test

```

Again, straightforward and clean. It is even possible to separate the API and browser sessions into different fixtures so that API- and browser-driven actions in a set of automated tests. 

I've had success using the requests session in exactly these ways. For an example of an API test framework based on requests, take a look at [svp](https://github.com/joshmgrant/svp).

In conclusion, Python's requests is incredible. Requests is almost a good enough reason to learn Python for testers and SDETs. 
