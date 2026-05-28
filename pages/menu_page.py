from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MenuPage:
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    ABOUT_LINK = (By.ID, "about_sidebar_link")
    SAUCELABS_URL_FRAGMENT = "saucelabs.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.MENU_BTN)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()

    def open_about(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable(self.MENU_BTN)).click()
        wait.until(EC.element_to_be_clickable(self.ABOUT_LINK)).click()
        return self.is_on_saucelabs(timeout=timeout)

    def is_on_saucelabs(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(self.SAUCELABS_URL_FRAGMENT)
            )
            return True
        except TimeoutException:
            return False
