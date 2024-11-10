# tests/conftest.py
import pytest
import configparser
import os
import json
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


config_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "config.ini")
config = configparser.ConfigParser()
config.read(config_file_path)

@pytest.fixture(scope="session")
def base_url():
    if 'Settings' not in config or 'base_url' not in config['Settings']:
        raise KeyError("The 'Settings' section or 'base_url' key is missing in the config.ini file.")
    return config['Settings']['base_url']

@pytest.fixture
def load_user_data():
    def _load_user_data(filename):
        file_path = os.path.join(os.path.dirname(__file__), "..", "data", filename)
        with open(file_path, 'r') as file:
            return json.load(file)
    return _load_user_data

@pytest.fixture
def load_checkout_data():
    def _load_checkout_data(filename):
        file_path = os.path.join(os.path.dirname(__file__), "..", "data", filename)
        with open(file_path, 'r') as file:
            return json.load(file)
    return _load_checkout_data
