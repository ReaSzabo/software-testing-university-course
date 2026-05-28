from behave import when, then
from pages.cart_page import CartPage
from pages.products_page import ProductsPage


@when('I add all items to the cart')
def add_all_items(context):
    products_page = ProductsPage(context.driver)
    total = products_page.get_inventory_count()
    context.inventory_total = total
    products_page.add_first_n_items(total)


@when('I remove "{count}" items from the cart')
def remove_items_from_cart(context, count):
    CartPage(context.driver).remove_first_n_items(int(count))


@then('the cart should have "{count}" items remaining')
def cart_should_have_count(context, count):
    expected = int(count)
    actual = CartPage(context.driver).get_cart_item_count()
    assert actual == expected, f"Expected {expected} cart items, got {actual}"
