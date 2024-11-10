# tests/test_register.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.registration_page import RegistrationPage
import configparser
import os
import json



@pytest.mark.register
def test_user_registration(driver, load_user_data, base_url):
    registration_page = RegistrationPage(driver)

    user_data = load_user_data('user_data.json')

    driver.get(base_url+"register")

    user = user_data['user2']
    registration_page.register_user(
        first_name=user['first_name'],
        last_name=user['last_name'],
        email=user['email'],
        password=user['password'],
        gender=user['gender']
    )

    driver.quit()