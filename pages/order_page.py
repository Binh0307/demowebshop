import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from helper.selenium_helper import Selenium_Helper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


class OrderPage(Selenium_Helper):
    search_box = (By.ID, "small-searchterms")
    search_button = (By.CLASS_NAME, "search-box-button")
    product_link = (By.CSS_SELECTOR, "h2.product-title a")
    quantity_box = (By.CLASS_NAME, "qty-input")
    add_to_cart_button = (By.CLASS_NAME, "add-to-cart-button")
    cart_button = (By.CLASS_NAME, "cart-label")
    agree_checkbox = (By.ID, "termsofservice")
    checkout_button = (By.ID, "checkout")
    country_dropdown = (By.ID, "BillingNewAddress_CountryId")
    city = (By.ID, "BillingNewAddress_City")
    address1 = (By.ID, "BillingNewAddress_Address1")
    postal_code = (By.ID, "BillingNewAddress_ZipPostalCode")
    phone_number = (By.ID, "BillingNewAddress_PhoneNumber")
    continue_btn = (By.CLASS_NAME,"new-address-next-step-button")
    billing_dropdown_element = (By.ID, "billing-address-select")
    

    def __init__(self, driver):
        super().__init__(driver)

    def search_product(self, product_name):
        self.enter_text(self.search_box, product_name)
        self.click(self.search_button)

    def select_first_product(self):
        self.click(self.product_link)

    def add_to_cart(self, quantity=2):
        self.clear_text(self.quantity_box)
        self.enter_text(self.quantity_box, str(quantity))
        self.click(self.add_to_cart_button)

    def go_to_cart(self):
        self.click(self.cart_button)

    def proceed_to_checkout(self):
        self.click(self.agree_checkbox)
        self.click(self.checkout_button)

    def select_country(self, country_name):
        country_dropdown_element = self.find_element(self.country_dropdown)
        select = Select(country_dropdown_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", country_dropdown_element)
        select.select_by_visible_text(country_name)

    def complete_checkout(self, country_name, city, address1, postal_code, phone_number):

        try:
            billing_dropdown_element = self.find_element(self.billing_dropdown_element)
            select = Select(billing_dropdown_element)

            if select.options:
                select.select_by_visible_text("New Address")
            else:
                print("No 'New Address' option found. Skipping.")

        except NoSuchElementException:
            print("Billing address dropdown not found. Proceeding with other fields.")

        country_dropdown_element = self.find_element(self.country_dropdown)
        select = Select(country_dropdown_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", country_dropdown_element)
        select.select_by_visible_text(country_name)

        self.enter_text(self.city, city)
        self.enter_text(self.address1, address1)
        self.enter_text(self.postal_code, postal_code)
        self.enter_text(self.phone_number, phone_number)

        self.click(self.continue_btn)




