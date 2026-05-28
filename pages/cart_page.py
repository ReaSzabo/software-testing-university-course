from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, ".cart_button")
    CART_LIST = (By.CLASS_NAME, "cart_list")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
        self.wait.until(EC.visibility_of_element_located(self.CART_LIST))

    def get_cart_item_count(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_LIST))
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_remove_button_count(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_LIST))
        return len(self.driver.find_elements(*self.REMOVE_BUTTONS))

    def remove_first_n_items(self, count):
        self.wait.until(EC.visibility_of_element_located(self.CART_LIST))
        for _ in range(count):
            buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
            if not buttons:
                break
            buttons[0].click()
