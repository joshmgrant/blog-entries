Over the past two posts, I've [introduced Nerodia](http://simplythetest.tumblr.com/post/177455969240/introducing-nerodia-part-1-what-is-nerodia) and also [given a sample of what Nerodia can do](http://simplythetest.tumblr.com/post/177593273770/introducing-nerodia-part-2-a-simple-example). Now I'd like to show a sample of how a page object might look using Nerodia.

Page objects are a foundational design pattern in many browser test projects, and are often at the core of how such projects start and grow. If a team can nail down a good page object implementation, they are more likely to see success in their project long term.

Here is an implementation of a page object using Nerodia in Python 3: 

    class WatirPage(BasePage):
       
       def __init__(self, browser):
           super(WatirPage, self).__init__(browser)
           self.url = 'www.watir.com'
           self.intro = self.browser.div(class_name='intro')
           self.news = self.browser.link(href='/blog/')

and this class does depend on a base class, which looks like this:

    from nerodia import browser
    
    class BasePage(object):
    
    def __init__(self, br):
         if isinstance(br, browser.Browser):
             self.browser = br
           elif isinstance(br, str):
               self.browser = browser.Browser(br)
           else:
               raise TypeError("Incorrect object type passed to constructor")
    
       def close(self):
           self.browser.close()
    
       def goto(self, url=None):
           self.browser.goto(url) if url else self.browser.goto(self.url)

(Before I go on, I'd like to disclaim that these are prototypical examples that serve a particular purpose. Please keep the [bike shedding](https://personalexcellence.co/blog/bike-shed-effect/) to a minimum.)

Lastly, here's a small script showing how this page object might be used:

    w = WatirPage('chrome')
    w.goto()
    assert 'Watir' in w.intro.text
    w.news.click()
    assert 'Titus' in w.browser.text
    w.close()

Similar to the last post, I'd like point out a few interesting characteristics of these page objects:

*Minimal implementation*: Looking at *WatirPage* above, it's easy to see that it's as minimal a page object class as you get. It is initialized with a list of elements that can be interacted with, with nothing else. It also contains some utility methods from its parent class for going to the page URL and closing the browser. There's no getters/setters needed, no awkward utility methods for handling locators or performing actions. In the past, I've had to resort to adding helper methods to allow for interacting with elements on an as-needed basis since the WebDriver effectively requires *findElement* calls to be made in a just-in-time fashion. Using Nerodia in page objects means elements can be defined upfront and then used in a logical manner without the fuss. 

*Straightforward base class methods*: As mentioned, looking at *BasePage* it's clear that the methods *close()* and *goto()* are straightforward basic methods that apply to every page object. They're also short and concise. Further, many methods can be implemented neatly in the base method like this. Because Nerodia has built-in synchronization, writing methods to perform basic actions is simple and doesn't require a lot of additional logic. The same could go for methods like *click()* or *getText()* on elements, which are particularly useful if additional functionality  like special page handling or custom logging is needed for these actions.

Also note that all of the previous benefits discussed about Nerodia (similar feel as the WebDriver API, element reuse and synchronization) apply to the page object case.

Based on these benefits, I think Nerodia is an excellent tool for Python developers to consider using for browser testing in their projects. It bring with it the hard earned experience of the Watir project, and a better user experience for developers and SDETs. Take a look!