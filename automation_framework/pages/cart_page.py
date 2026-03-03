from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.cart_item = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_product_name(self):
        return self.driver.find_element(*self.cart_item).text