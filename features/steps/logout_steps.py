from behave import when, then
from pages.menu_page import MenuPage
from pages.login_page import LoginPage


@when('I logout')
def logout(context):
    assert LoginPage(context.driver).is_logged_in(timeout=10), "Expected to be logged in before logout"
    MenuPage(context.driver).logout()


@then('I should see the login page')
def should_see_login_page(context):
    assert LoginPage(context.driver).is_on_login_page(timeout=10), "Expected to be on login page"
