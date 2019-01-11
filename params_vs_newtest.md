Lately I've seen some chatter on Twitter and elsewhere about the benefits and drawbacks of keeping test code [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (or even [DAMP](https://codeshelter.wordpress.com/2011/04/07/dry-and-damp-principles-when-developing-and-unit-testing/)). This is a topic I've come back to a few times in my career. In particular, one thing I've thought about is when and why to parametrize tests. There are cases where parametrization is a massive win, reducing a adding a new test case to adding a single entry in a list. There are other cases where this makes test maintenance problematic and makes even maintaining existing test cases cumbersome.

Based on my experience, I think this issue can be solved cleanly. The idea comes down how a test is structured and what needs to change for a new case. The simple rule is this:

If a value needs to be changed to add a new case, parametrize.
If logic needs to be changed to add a new case, create a new test.

This might be illustrated with some examples.

Imagine testing an e-commerce site where a user can search for a potential items to purchase. There some cases for when the search returns a "Sorry not found" message and this functionality should be verified. Three such cases are

- search for an item that is not sold on the site
- searching for an item that is sold on the site but is not in stock 
- and inputting a search term with invalid characters. 

Here's how these cases may be written in Python using Pytest: 

```
import pytest


def test_search_item_not_in_stock():
    search_page.visit()
    search_page.search_for("outOfStockItem")
    assert search_page.item_not_found_message.is_displayed()

def test_search_item_not_sold():
    search_page.visit()
    search_page.search_for("itemNotSoldOnSite")
    assert search_page.item_not_found_message.is_displayed()

def test_search_invalid_item_value()
    search_page.visit()
    search_page.search_for("&^$!")
    assert search_page.item_not_found_message.is_displayed()
```

These are pretty well written, with good names for each test function. Notice that the logic of each case only really differs by a single _value_. Using DRY and the fact Pytest supports parametrized tests, these tests could be re-written like this:

```
cases = [
    "outOfStockItem",
    "itemNotSoldOnSite",
    "&^$!"
]

@pytest.mark.parametrize("search_term", cases)
def test_search_item_not_found(search_term):
    search_page.visit()
    search_page.search_for(search_term)
    assert search_page.item_not_found_message.is_displayed()
```

This cuts down the number of test functions to manage, and allows new cases to be added in a straightforward manner. Easy peasy.

Now consider adding a new case where an item is initially in stock, but a helper test hook is applied and takes the item out of stock. The test may want to validate that the item appears in stock then is not found. 

Making use of the parametrized test above, this could be done like this:

```
cases = [
    "outOfStockItem",
    "itemNotSoldOnSite",
    "&^$!"
    "instockItem"
]

@pytest.mark.parametrize("search_term", cases)
def test_search_item_not_found(search_term):
    search_page.visit()
    search_page.search_for(search_term)
    if search_term == "instockItem":
        assert not search_page.item_not_found_message.is_displayed()
        helpers.remove_item_from_stock("instockItem") #using a test hook
        search_page.search_for("instockItem")
    assert search_page.item_not_found_message.is_displayed()
```

At first, this looks somewhat DRY since the initial test case is being re-used. However, this is a bit suboptimal in other ways. First, the test case now has an `if` statement that creates multiple branches. These branches have to be maintained; if the `instockItem` item is removed from the `cases` list, the `if` block is now deadweight in the code as it shouldn't be executed. As well, the test case is now less readable since the `instockItem` case deviates from the other cases. In the worst case, more and more logic is added and this single test function becomes a hot mess to deal with.

Here, I'd say that parametrizing and DRY has made the test code less and not more understandable and maintainable. This is because the `instockItem` requires a change in _logic_ in addition to changing a _value_.

Instead of shoehorning in this case to the parametrized test, a new test should be added. The tests would then look like this:

```
cases = [
    "outOfStockItem",
    "itemNotSoldOnSite",
    "&^$!"
]

# these tests only change by a value
@pytest.mark.parametrize("search_term", cases)
def test_search_item_not_found(search_term):
    search_page.visit()
    search_page.search_for(search_term)
    assert search_page.item_not_found_message.is_displayed()

# new test added because of new logic
def test_search_item_in_stock_then_out_of_stock():
    search_page.visit()
    search_page.search_for("instockItem")
    assert not search_page.item_not_found_message.is_displayed()
    helpers.remote_item_from_stock("instockItem")
    search_page.search_for("instockInstock")
    assert search_page.item_not_found_message.is_displayed()
```

While not quite DRY in that there's now two separate test functions to maintain instead of one, this code is DAMP enough that maintenance is easier and the code is easier to reason about. 