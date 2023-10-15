from pages.base_page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    SIGN_IN_LINK = (By.CSS_SELECTOR, '.sing-in-text')
    SIGNIN_INPUT_EMAIL = (By.ID, "email-2")
    REELLY_PASSWORD = (By.ID, "field")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '.login-button.w-button')

    def login_pages(self):
        self.open_url('sign-up')

    def click_on_signin_link(self):
        self.click(*self.SIGN_IN_LINK)

    def input_email(self, text):
        self.input_text(text, *self.SIGNIN_INPUT_EMAIL)

    def password_input_field(self, text):
        self.input_text(text, *self.REELLY_PASSWORD)

    def click_continue(self):
        self.click(*self.CONTINUE_BUTTON)





