from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class GetFreeSubscriptionPage(Page):


    FREE_SUBSCRIPTION_TEXT = (By.XPATH, "//div[text()='Get a month of free subscription!']")
    #SUBSCRIPTION_PLAN = (By.CSS_SELECTOR, "a.step-button.margin-bottom-8.w-button")



    def open_new_reelly_page(self):
        self.driver.get('https://soft.reelly.io/book-presentation')
        sleep(3)
        self.refresh()

    def open_new_window(self, window_id):
        self.switch_to_window(window_id)

    def verify_subscription_text(self, text):
        self.verify_text(text, *self.FREE_SUBSCRIPTION_TEXT)
