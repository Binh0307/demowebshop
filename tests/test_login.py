import pytest
from pages.login_page import LoginPage

@pytest.mark.login
class Test_Login:
    
    @pytest.mark.invalidlogin
    def test_invalid_login(self, driver, load_user_data, base_url):
        login_page = LoginPage(driver)
        user_data = load_user_data('user_data.json')
        user = user_data['not_registed_user']
        
        driver.get(base_url + "login")
        
        login_page.login_invalid_user(
            email=user['email'],
            password=user['password'],
        )
        
        error_text = login_page.get_error_message()
        expected_errors = [
            "Login was unsuccessful. Please correct the errors and try again.",
            "No customer account found"
        ]
        
        assert any(
            expected_error in error_text for expected_error in expected_errors
        ), "Expected error message was not displayed"

    @pytest.mark.validlogin
    def test_login(self, driver, load_user_data, base_url):
        login_page = LoginPage(driver)
        user_data = load_user_data('user_data.json')
        user = user_data['user2']
        
        driver.get(base_url + "login")
        
        login_page.login_user(
            email=user['email'],
            password=user['password'],
        )
