from pages.base_page import Page
#from support.logger import logger
from time import sleep

class MainPage(Page):



    def open_main(self):
        #logger.info('Opening https://soft.reelly.io/ ')
        self.driver.get('https://amazon.com/')
        sleep(3)
        self.driver.refresh()


