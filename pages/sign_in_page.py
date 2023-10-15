
from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):

    SIGN_IN_PAGE_CHECK = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_INPUT = (By.ID, 'ap_email')

    def verify_signin_opened(self):
        self.verify_text('Sign in', *self.SIGN_IN_PAGE_CHECK)
        # Verify email field present
        self.driver.find_element(*self.EMAIL_INPUT)
        self.verify_partial_url('ap/signin')
