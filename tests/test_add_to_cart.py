import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.add_to_cart_page import AddToCartPage
from pages.login_page import LoginPage
import configparser
import os
import json


@pytest.mark.add_to_cart
class Test_AddToCart:

    @pytest.mark.add_to_cart_anonymous
    def test_add_to_cart_anonymous_user(self, driver, base_url):
        quantity = 1
        add_to_cart_page = AddToCartPage(driver)
        
        driver.get(base_url)

        initial_quantity = add_to_cart_page.get_cart_quantity()

        add_to_cart_page.search_product("computer")
        add_to_cart_page.select_first_product()
        add_to_cart_page.add_to_cart(quantity=quantity)

        expected_product_name = add_to_cart_page.get_product_name()
        expected_product_price = add_to_cart_page.calculate_total_price()

        add_to_cart_page.scroll_to_top()
        add_to_cart_page.go_to_cart()
        expected_quantity = initial_quantity + quantity
        assert add_to_cart_page.get_cart_quantity() == expected_quantity 
        add_to_cart_page.verify_cart_product(expected_product_name, expected_product_price) 

    @pytest.mark.add_to_cart_as_logged_in
    def test_add_to_cart_logged_in_user(self, driver, load_user_data, base_url):
        quantity = 1
        add_to_cart_page = AddToCartPage(driver)
        user_data = load_user_data('user_data.json')
        
        driver.get(base_url + "login")

        login_page = LoginPage(driver)
        user = user_data['login_user']
        login_page.login_user(email=user['email'], password=user['password'])

        initial_quantity = add_to_cart_page.get_cart_quantity()

        add_to_cart_page.search_product("computer")
        add_to_cart_page.select_first_product()
        add_to_cart_page.add_to_cart(quantity=quantity)

  
        expected_product_name = add_to_cart_page.get_product_name()
        expected_product_price = add_to_cart_page.calculate_total_price()

        
        add_to_cart_page.go_to_cart()
        expected_quantity = initial_quantity + quantity
        assert add_to_cart_page.get_cart_quantity() == expected_quantity  
        add_to_cart_page.verify_cart_product(expected_product_name, expected_product_price)  
