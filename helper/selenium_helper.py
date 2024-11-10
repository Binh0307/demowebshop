# helper/selenium_helper.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Selenium_Helper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        #element.click()
        self.driver.execute_script('arguments[0].click()', element)

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()  
        element.send_keys(text)

    def clear_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1) 

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(-1, -1);")
        
