from selenium.webdriver.common.by import By
from helper.selenium_helper import Selenium_Helper

class SearchPage(Selenium_Helper):
    search_box = (By.ID, "small-searchterms")
    search_button = (By.CLASS_NAME, "search-box-button")
    product_titles = (By.CSS_SELECTOR, "h2.product-title a")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_search_keyword(self, keyword):
        self.enter_text(self.search_box, keyword)
        self.click(self.search_button)

    def get_all_product_titles(self):
        elements = self.find_elements(self.product_titles)
        return [element.text.lower() for element in elements]
