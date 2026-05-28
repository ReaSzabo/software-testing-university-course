from behave import given, when, then
from pages.login_page import LoginPage

@given('I open the login page')
def open_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('I login with username "{username}" and password "{password}"')
def login(context, username, password):
    context.login_page.login(username, password)

@then('I should see the products page')
def should_see_products(context):
    # ensure the page had time to resolve to either products or error
    context.login_page.wait_for_result()
    assert context.login_page.is_logged_in(), "Expected to be on products page"

@then('the login should be "{result}"')
def login_result(context, result):
    # wait for either outcome, then verify appropriately
    context.login_page.wait_for_result()
    if result == 'success':
        assert context.login_page.is_logged_in(), "Expected login to succeed"
    else:
        assert context.login_page.has_error(), "Expected login to fail and show an error"
