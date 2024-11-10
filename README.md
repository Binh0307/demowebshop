# Demo Web Shop Test Automation

This repository contains end-to-end test cases for the Demo Web Shop, using Python, Selenium, and Pytest. It covers user registration, login scenarios, search, ordering, and adding items to the cart.

## Table of Contents

- [Overview](#overview)
- [Test Scenarios](#test-scenarios)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running Tests](#running-tests)
- [Usage](#usage)
- [Customization](#customization)

---

## Overview

This project is an automated testing suite for the Demo Web Shop. It includes a range of tests for verifying core functionalities like registration, login, search, add to cart, and order placement. Tests are written in Python and use Selenium WebDriver for browser automation and Pytest for test execution and organization.

## Test Scenarios

### 1. User Registration (Valid)
   - Tests that a new user can successfully register with valid information.

### 2. Login Scenarios
   - **Invalid Login**: Tests that an error message appears when logging in with invalid credentials.
   - **Valid Login**: Tests that a user can log in with valid credentials.

### 3. Search Functionality
   - Verifies that a user can search for products and relevant results appear.

### 4. Add to Cart
   - **Anonymous User**: Tests that an anonymous user can add items to the cart.
   - **Logged-In User**: Tests that a logged-in user can add items to the cart.

### 5. Place an Order
   - Tests that a logged-in user can successfully place an order.

## Project Structure

```plaintext
demowebshop/
├── pages/
│   ├── base_page.py             # Base class for page objects
│   ├── add_to_cart_page.py      # Page class for add to cart functionality
│   ├── registration_page.py     # Page class for registration functionality
│   ├── login_page.py            # Page class for login functionality
│   └── ...                      # Additional page classes
├── tests/
│   ├── test_add_to_cart.py      # Test cases for adding items to the cart
│   ├── test_register.py         # Test cases for user registration
│   ├── test_login.py            # Test cases for login scenarios
│   ├── test_order.py            # Test cases for placing orders
│   ├── test_search.py           # Test cases for search functionality
│   └── ...                      # Additional test cases
├── helper/
│   └── selenium_helper.py       # Helper functions for Selenium actions
├── pytest.ini                   # Pytest configuration with custom markers
└── requirements.txt             # Dependencies for the project
