from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SigninPage(BasePage):
    SIGN_IN_TXT = (By.CSS_SELECTOR, "div h1")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "div [data-test='accountNav-signIn']")

    def click_signin_btn(self):
        self.wait_and_click(*self.SIGN_IN_BTN)
        print("signin button clicked")

    def verify_user_can_sign_in(self):
        self.verify_text('Sign into your Target account', *self.SIGN_IN_TXT)
        print('signin text verified on side navigation page')