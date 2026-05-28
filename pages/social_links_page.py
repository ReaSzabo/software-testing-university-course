from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SocialLinksPage:
    FOOTER = (By.CLASS_NAME, "footer")
    TWITTER = (By.CSS_SELECTOR, "a[href*='twitter.com']")
    FACEBOOK = (By.CSS_SELECTOR, "a[href*='facebook.com']")
    LINKEDIN = (By.CSS_SELECTOR, "a[href*='linkedin.com']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _open_link(self, locator):
        original = self.driver.current_window_handle
        existing = set(self.driver.window_handles)
        self.wait.until(EC.visibility_of_element_located(self.FOOTER))
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        self.wait.until(lambda d: len(d.window_handles) > len(existing))
        new_handles = [h for h in self.driver.window_handles if h not in existing]
        new_handle = new_handles[0]
        self.driver.switch_to.window(new_handle)
        return original, new_handle

    def open_twitter(self):
        return self._open_link(self.TWITTER)

    def open_facebook(self):
        return self._open_link(self.FACEBOOK)

    def open_linkedin(self):
        return self._open_link(self.LINKEDIN)

    def close_new_tab(self, original_handle):
        self.driver.close()
        self.driver.switch_to.window(original_handle)
