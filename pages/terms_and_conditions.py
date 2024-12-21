from pages.base_page import BasePage


class TermsAndConditionsPage(BasePage):

    def verify_TandC_opened(self):
        self.verify_partial_url('terms-conditions/')