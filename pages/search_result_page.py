from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')
    ADD_CART_BUTTON = (By.CSS_SELECTOR, "#add-to-cart-button")
    NO_PROTECTIONPLAN_BUTTON = (By.CSS_SELECTOR, '.a-button-input[aria-labelledby="attachSiNoCoverage-announce')
    G0_TO_CART_BUTTON = (By.CSS_SELECTOR, "a[href='/cart?ref_=sw_gtc']")
    SUB_TOTAL_BUTTON = (By.CSS_SELECTOR, "#sc-subtotal-label-buybox")

    #def verify_search_result(self, expected_text):
        #actual_text = self.find_element(*self.SEARCH_RESULT).text
        #assert actual_text == expected_text,  \
            #f'Error, expected {expected_text} did not match actual {actual_text}'

    def verify_search_result(self, result):  # "tea"
        self.verify_text(result, *self.SEARCH_RESULT)


    def verify_cart_is_empty(self,expected_text):
        self.verify_text(expected_text, *self.EMPTY_CART_TEXT)


    def verify_cart_item(self,text):
        self.verify_text(text, *self.SUB_TOTAL_BUTTON)


    def add_cart_click(self):
        self.click(*self.ADD_CART_BUTTON)
        self.click(*self.NO_PROTECTIONPLAN_BUTTON)
        self.click(*self.G0_TO_CART_BUTTON)
