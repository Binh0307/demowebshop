from selenium.webdriver.common.by import By
import random
from helper.selenium_helper import Selenium_Helper

class AddToCartPage(Selenium_Helper):
    search_box = (By.ID, "small-searchterms")
    search_button = (By.CLASS_NAME, "search-box-button")
    product_link = (By.CSS_SELECTOR, "h2.product-title a")
    quantity_box = (By.CLASS_NAME, "qty-input")
    add_to_cart_button = (By.CLASS_NAME, "add-to-cart-button")
    cart_button = (By.CLASS_NAME, "cart-label")
    cart_quantity = (By.CSS_SELECTOR, "a[href='/cart'] .cart-qty")
    product_name_element = (By.CLASS_NAME, "product-name")  
    price_element = (By.CLASS_NAME, "product-price")
    option_checkboxes = (By.CSS_SELECTOR, "ul.option-list input[type='checkbox']")
    option_radios = (By.CSS_SELECTOR, "ul.option-list input[type='radio']")
    
    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_quantity(self):
        quantity_text = self.get_text(self.cart_quantity)
        return int(quantity_text.strip("()"))

    def search_product(self, product_name):
        self.enter_text(self.search_box, product_name)
        self.click(self.search_button)

    def select_first_product(self):
        self.click(self.product_link)

    def add_to_cart(self, quantity=1):
        
        self.clear_text(self.quantity_box)
        self.enter_text(self.quantity_box, str(quantity))


        checkbox_options = self.find_elements(self.option_checkboxes)
        for checkbox in checkbox_options:
            if random.choice([True, False]):
                checkbox.click()


        radio_options = self.find_elements(self.option_radios)
        if radio_options:
            random.choice(radio_options).click()

        self.click(self.add_to_cart_button)

    def go_to_cart(self):
        self.scroll_to_top()
        self.click(self.cart_button)

    def get_product_name(self):
        return self.get_text(self.product_name_element)

    def get_base_price(self):
        price_text = self.get_text(self.price_element).strip()
        return float(price_text.replace(",", "").replace("€", "").strip())  
    def calculate_total_price(self):
        base_price = self.get_base_price()
        total_price = base_price


        for checkbox in self.find_elements(self.option_checkboxes):
            if checkbox.is_selected():
                label = checkbox.find_element(By.XPATH, f"following-sibling::label[@for='{checkbox.get_attribute('id')}']")
                price_text = label.text
                if "[+" in price_text:
                    additional_price = float(price_text.split("[+")[1].replace("]", "").strip())
                    total_price += additional_price


        for radio in self.find_elements(self.option_radios):
            if radio.is_selected():
                label = radio.find_element(By.XPATH, f"following-sibling::label[@for='{radio.get_attribute('id')}']")
                price_text = label.text
                if "[+" in price_text:
                    additional_price = float(price_text.split("[+")[1].replace("]", "").strip())
                    total_price += additional_price

        return total_price

    def get_cart_products(self):
        
        product_elements = self.find_elements((By.CLASS_NAME, "cart-item-row"))  
        products = []

        for product_element in product_elements:
            name_element = product_element.find_element(By.CLASS_NAME, "product-name")
            price_element = product_element.find_element(By.CLASS_NAME, "product-unit-price")
            
            product_name = name_element.text.strip()
            product_price = float(price_element.text.strip().replace(",", "").replace("€", "").strip()) 
            products.append({
                'name': product_name,
                'price': product_price
            })

        return products

    def verify_cart_product(self, expected_product_name, expected_product_price):
        cart_products = self.get_cart_products()
        found = any(p['name'] == expected_product_name and p['price'] == expected_product_price for p in cart_products)
    
        assert found, f"Product '{expected_product_name}' with price '{expected_product_price}' not found in the cart."
