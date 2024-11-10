import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.order_page import OrderPage
from pages.login_page import LoginPage
import configparser
import os
import json



@pytest.mark.order
def test_order_product(driver, load_user_data, load_checkout_data, base_url):
    order_page = OrderPage(driver)
    user_data = load_user_data('user_data.json')
    checkout_data = load_checkout_data('checkout_data.json')['checkout1'] 

    driver.get(base_url + "login")

    login_page = LoginPage(driver)
    user = user_data['login_user']
    login_page.login_user(email=user['email'], password=user['password'])

    order_page.search_product("computer")
    order_page.select_first_product()
    order_page.add_to_cart(quantity=2)
    order_page.go_to_cart()

    order_page.proceed_to_checkout()
    order_page.complete_checkout(
        country_name=checkout_data["country"],
        city=checkout_data["city"],
        address1=checkout_data["address1"],
        postal_code=checkout_data["postal_code"],
        phone_number=checkout_data["phone_number"]
    )

    driver.quit()

