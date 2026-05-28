from behave import when, then
from pages.cart_page import CartPage
from pages.products_page import ProductsPage


@when('I open the cart')
def open_cart(context):
    CartPage(context.driver).open()


@then('the cart should have "{count}" items')
def cart_should_have_items(context, count):
    expected = int(count)
    actual = CartPage(context.driver).get_cart_item_count()
    assert actual == expected, f"Expected {expected} cart items, got {actual}"


@then('the cart should show "{count}" remove buttons')
def cart_should_show_remove_buttons(context, count):
    expected = int(count)
    actual = CartPage(context.driver).get_remove_button_count()
    assert actual == expected, f"Expected {expected} remove buttons, got {actual}"


@then('all items should be in the cart when remove count is "{count}"')
def all_items_in_cart_when_count_matches(context, count):
    expected = int(count)
    total = getattr(context, 'inventory_total', None)
    if total is not None and expected == total:
        actual = CartPage(context.driver).get_cart_item_count()
        assert actual == total, "Expected all items to be in the cart"
