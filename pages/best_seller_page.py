from selenium.webdriver.common.by import By
from pages.base_page import Page

class BestSellerPage(Page):
    TOP_MENU = (By.CSS_SELECTOR, 'div.celwidget.c-f ul a')
    TEXT_TOP_MENU = (By.ID, 'zg_banner_text')

    def best_seller_menu_links(self):
        self.find_elements(*self.TOP_MENU)

    def get_text_top_menu(self):
        self.get_text(*self.TEXT_TOP_MENU)

    def verify_top_menu_count(self, number):
        self.verify_number_elements(number, *self.TOP_MENU)

    # def verify_top_menu_page_opens(self):
    #     top_links = self.find_elements(*self.TOP_MENU)
    #
    #     for i in range(len(top_links)):  # 8, 1, 2, 3,
    #         link_to_click = self.find_elements(*self.TOP_MENU[i])
    #         link_text = link_to_click.text
    #         link_to_click.click()
    #         self.verify_text(link_text, *self.TEXT_TOP_MENU)
