from behave import when, then
from pages.social_links_page import SocialLinksPage


@when('I open the Twitter social link')
def open_twitter(context):
    page = SocialLinksPage(context.driver)
    original, _new = page.open_twitter()
    context.original_window = original


@when('I open the Facebook social link')
def open_facebook(context):
    page = SocialLinksPage(context.driver)
    original, _new = page.open_facebook()
    context.original_window = original


@when('I open the LinkedIn social link')
def open_linkedin(context):
    page = SocialLinksPage(context.driver)
    original, _new = page.open_linkedin()
    context.original_window = original


@then('I should be on the Twitter page')
def should_be_on_twitter(context):
    url = context.driver.current_url
    assert "twitter.com" in url or "x.com" in url, "Expected to navigate to Twitter"
    SocialLinksPage(context.driver).close_new_tab(context.original_window)


@then('I should be on the Facebook page')
def should_be_on_facebook(context):
    assert "facebook.com" in context.driver.current_url, "Expected to navigate to Facebook"
    SocialLinksPage(context.driver).close_new_tab(context.original_window)


@then('I should be on the LinkedIn page')
def should_be_on_linkedin(context):
    assert "linkedin.com" in context.driver.current_url, "Expected to navigate to LinkedIn"
    SocialLinksPage(context.driver).close_new_tab(context.original_window)
