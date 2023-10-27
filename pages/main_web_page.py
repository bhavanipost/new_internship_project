from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from support.logger import logger
from time import sleep



class MainWebPage(Page):

    FREE_SUBSCRIPTION = (By.CSS_SELECTOR, ".get-free-period.menu")
    MENU_BUTTON = (By.XPATH, '//div[text()="Menu"][@class="mobile-top-menu"]')
    CONNECT_THE_COMPANY_BUT = (By.XPATH, '/html/body/div[3]/div[2]/a[1]/div')
    def open_main(self):
        self.driver.get('https://soft.reelly.io/')
        sleep(3)
        self.driver.refresh()


    def free_subscription_click(self):
        self.wait_for_element_clickable_click(*self.FREE_SUBSCRIPTION)
        #self.click(*self.FREE_SUBSCRIPTION)
        sleep(3)


    def click_setting_menu(self):
        self.wait_for_element_clickable_click(*self.MENU_BUTTON)
    def click_connect_the_company(self):
        self.wait_for_element_clickable_click(*self.CONNECT_THE_COMPANY_BUT)


    def store_original_window(self):
        return self.get_current_window()

