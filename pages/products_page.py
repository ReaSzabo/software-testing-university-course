from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    ITEM_ADD_BTN = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _get_items(self):
        self.wait.until(EC.visibility_of_element_located(self.INVENTORY_ITEMS))
        return self.driver.find_elements(*self.INVENTORY_ITEMS)

    def get_inventory_count(self):
        return len(self._get_items())

    def add_first_n_items(self, count):
        total = self.get_inventory_count()
        assert count <= total, f"Requested {count} items, but only {total} are available"
        items = self._get_items()
        for i in range(count):
            button = items[i].find_element(*self.ITEM_ADD_BTN)
            if button.text.strip().lower() == "add to cart":
                button.click()

    def get_cart_badge_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        if not badges:
            return 0
        return int(badges[0].text.strip())

    def all_items_added(self):
        items = self._get_items()
        for item in items:
            button = item.find_element(*self.ITEM_ADD_BTN)
            if button.text.strip().lower() != "remove":
                return False
        return True

    def apply_sort(self, sort_value):
        select = self.wait.until(EC.element_to_be_clickable(self.SORT_SELECT))
        select.click()
        for option in select.find_elements(By.TAG_NAME, "option"):
            if option.get_attribute("value") == sort_value:
                option.click()
                break

    def get_item_names(self):
        items = self._get_items()
        return [item.find_element(*self.ITEM_NAME).text.strip() for item in items]

    def get_item_prices(self):
        items = self._get_items()
        prices = []
        for item in items:
            text = item.find_element(*self.ITEM_PRICE).text.strip().replace("$", "")
            prices.append(float(text))
        return prices
