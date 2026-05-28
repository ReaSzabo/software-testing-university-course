from behave import when, then
from pages.menu_page import MenuPage
from pages.login_page import LoginPage


@when('I open the About page')
def open_about_page(context):
    assert LoginPage(context.driver).is_logged_in(timeout=10), "Expected to be logged in before opening About"
    MenuPage(context.driver).open_about()


@then('I should be on the Saucelabs website')
def should_be_on_saucelabs(context):
    assert MenuPage(context.driver).is_on_saucelabs(timeout=10), "Expected to be on Saucelabs website"
