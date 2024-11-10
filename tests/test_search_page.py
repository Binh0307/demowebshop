import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.search_page import SearchPage
import configparser
import os

config_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "config.ini")
config = configparser.ConfigParser()
config.read(config_file_path)
BaseUrl = config['Settings']['base_url']

@pytest.mark.search
def test_search_results_contain_keyword(driver):
    driver.get(BaseUrl)

    search_page = SearchPage(driver)
    keyword = "computer"
    
    search_page.enter_search_keyword(keyword)

    # Verify all products contain the keyword
    product_titles = search_page.get_all_product_titles()
    for title in product_titles:
        assert keyword.lower() in title, f"Keyword '{keyword}' not found in product title: '{title}'"

    driver.quit()
