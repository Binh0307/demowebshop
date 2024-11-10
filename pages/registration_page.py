# pages/registration_page.py
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from helper.selenium_helper import Selenium_Helper
from selenium.webdriver.support.ui import WebDriverWait


class RegistrationPage(Selenium_Helper):

    gender_male = (By.ID, "gender-male")
    gender_female = (By.ID, "gender-female")
    first_name = (By.ID, "FirstName")
    last_name = (By.ID, "LastName")
    password = (By.ID, "Password")
    email = (By.ID, "Email")
    confirm_password = (By.ID, "ConfirmPassword")
    register_btn = (By.ID, "register-button")
    continue_btn= (By.XPATH, '//input[@class="button-1 register-continue-button"]')

    def __init__(self, driver):
        super().__init__(driver)

    def select_gender(self, gender="M"):
        if gender == "M":
            self.click(self.gender_male)
        elif gender == "F":
            self.click(self.gender_female)


    def open_registration_page(self):
        self.click(self.REGISTER_LINK)

    def register_user(self, first_name, last_name, email, password, gender="M"):
        self.select_gender(gender)
        self.enter_text(self.first_name, first_name)
        self.enter_text(self.last_name, last_name)
        self.enter_text(self.email, email)
        self.enter_text(self.password, password)
        self.enter_text(self.confirm_password, password)
        self.click(self.register_btn)

        #self.wait.until(lambda driver: driver.find_element(*self.continue_btn))
        self.click(self.continue_btn)


