from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    SIGN_IN_ICON = (By.CSS_SELECTOR, "a[data-test='@web/AccountLink'][href='/account?prehydrateClick=true']")
    SIGN_IN_USER = (By.CSS_SELECTOR, "[data-test='modal-drawer-heading']")


    def click_signin_icon(self):
        self.wait_and_click(*self.SIGN_IN_ICON)


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart(self):
        self.wait_and_click(*self.CART_ICON)


