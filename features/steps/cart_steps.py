from behave import when, then
from pages.products_page import ProductsPage


@when('I add the first "{count}" items to the cart')
def add_first_items(context, count):
    products_page = ProductsPage(context.driver)
    context.inventory_total = products_page.get_inventory_count()
    products_page.add_first_n_items(int(count))


@then('the cart badge should show "{count}"')
def cart_badge_should_show(context, count):
    products_page = ProductsPage(context.driver)
    expected = int(count)
    actual = products_page.get_cart_badge_count()
    assert actual == expected, f"Expected cart count {expected}, got {actual}"


@then('all items should be in the cart when count is "{count}"')
def all_items_in_cart_when_count_matches(context, count):
    products_page = ProductsPage(context.driver)
    expected = int(count)
    total = products_page.get_inventory_count()
    if expected == total:
        assert products_page.all_items_added(), "Expected all items to be in the cart"
