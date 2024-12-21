from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_empty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_product_name(self, expected_text):
        self.verify_partial_text(expected_text, *self.PRODUCT_NAME)