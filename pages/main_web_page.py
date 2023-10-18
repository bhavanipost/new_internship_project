from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from support.logger import logger
from time import sleep



class MainWebPage(Page):

    FREE_SUBSCRIPTION = (By.CSS_SELECTOR, ".get-free-period.menu")



    def open_main(self):
        self.driver.get('https://soft.reelly.io/')
        sleep(3)
        self.driver.refresh()


    def free_subscription_click(self):
        self.wait_for_element_clickable_click(*self.FREE_SUBSCRIPTION)
        #self.click(*self.FREE_SUBSCRIPTION)
        sleep(3)


    def store_original_window(self):
        return self.get_current_window()

