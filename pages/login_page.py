from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    INVENTORY = (By.ID, "inventory_container")
    ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).clear()
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).clear()
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()
        # wait for either success (inventory) or error to appear
        self.wait_for_result()

    def wait_for_result(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(lambda d: d.find_elements(*self.INVENTORY) or d.find_elements(*self.ERROR))
            return True
        except TimeoutException:
            return False

    def is_logged_in(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.INVENTORY))
            return True
        except TimeoutException:
            return False

    def is_on_login_page(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(self.URL))
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.USERNAME))
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.LOGIN_BTN))
            return True
        except TimeoutException:
            return False

    def has_error(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.ERROR))
            return True
        except TimeoutException:
            return False
