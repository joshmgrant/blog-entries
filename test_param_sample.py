import pytest
¡
 # first draft
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

# with params

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

# we could do this, but it takes DRY a bit too far

cases = [
    "outOfStockItem",
    "itemNotSoldOnSite",
    "&^$!"
    "instockItem"
]

@pytest.parametrize("search_term", cases)
def test_search_item_not_found(search_term):
    search_page.visit()
    search_page.search_for(search_term)
    if search_term == "instockItem":
        assert not search_page.item_not_found_message.is_displayed()
        helpers.remote_item_from_stock("instockItem") #using a test hook
        search_page.search_for("instockInstock")
    assert search_page.item_not_found_message.is_displayed()