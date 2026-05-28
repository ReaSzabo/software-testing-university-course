from behave import when, then
from pages.products_page import ProductsPage


@when('I sort products by "{sort_value}"')
def sort_products(context, sort_value):
    products_page = ProductsPage(context.driver)
    if sort_value in ("az", "za"):
        context.pre_sort = products_page.get_item_names()
    elif sort_value in ("lohi", "hilo"):
        context.pre_sort = products_page.get_item_prices()
    else:
        context.pre_sort = None
    products_page.apply_sort(sort_value)


@then('the products should be sorted "{sort_value}"')
def products_should_be_sorted(context, sort_value):
    products_page = ProductsPage(context.driver)
    if sort_value in ("az", "za"):
        names = products_page.get_item_names()
        expected = sorted(names)
        if sort_value == "za":
            expected = list(reversed(expected))
        assert names == expected, f"Name order not sorted: {sort_value}"
        if sort_value == "za" and context.pre_sort is not None:
            assert names != context.pre_sort, "Expected name order to change for za"
    elif sort_value in ("lohi", "hilo"):
        prices = products_page.get_item_prices()
        expected = sorted(prices)
        if sort_value == "hilo":
            expected = list(reversed(expected))
        assert prices == expected, f"Price order not sorted: {sort_value}"
        if sort_value in ("lohi", "hilo") and context.pre_sort is not None:
            assert prices != context.pre_sort, f"Expected price order to change for {sort_value}"
    else:
        raise AssertionError(f"Unknown sort value: {sort_value}")
