# pages/registration_page.py
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from helper.selenium_helper import Selenium_Helper
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage(Selenium_Helper):

    password = (By.ID, "Password")
    email = (By.ID, "Email")
    login_btn = (By.XPATH, '//input[@value="Log in"]')
    register_btn = (By.XPATH, '//input[@class="button-1 register-button"]')
    error = (By.XPATH, '//div[@class="validation-summary-errors"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_error_message(self):
        error = self.find_element(self.error)
        return error.text


    def login_user(self, email, password):
        self.enter_text(self.email, email)
        self.enter_text(self.password, password)
        self.click(self.login_btn)

    def login_invalid_user(self, email, password):
        self.enter_text(self.email, email)
        self.enter_text(self.password, password)
        self.click(self.login_btn)
        self.clear_text(self.email)
        self.clear_text(self.password)


