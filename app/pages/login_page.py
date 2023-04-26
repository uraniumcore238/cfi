import allure
from selenium.webdriver.common.by import By
from app.pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.CSS_SELECTOR, '#email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')
    LOGIN_BTN = (By.CSS_SELECTOR, '#submit-btn')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '#alert-msg')
    WARNING_MESSAGE = (By.CSS_SELECTOR, '#mat-error-0')
    OPEN_AN_ACCOUNT = (By.CSS_SELECTOR, "[href*='registration']")

    def fill_the_email(self, email):
        with allure.step(f'Fill the email input field with "{email}"'):
            self.get_element(self.EMAIL_INPUT).send_keys(email)

    def fill_the_password(self, password):
        with allure.step(f'Fill the password input field with "{password}"'):
            self.get_element(self.PASSWORD_INPUT).send_keys(password)

    @allure.step('Click on login button')
    def click_on_login_btn(self):
        self.click_on(self.LOGIN_BTN)

    @allure.step('Assert error message')
    def assert_error_message(self, expected_message):
        error_message = self.get_element(self.ERROR_MESSAGE).text
        assert error_message == expected_message, f'Expected message "{expected_message}" does not match with "{error_message}"'

    @allure.step('Assert the login page visibility')
    def assert_login_page_visibility(self):
        self.get_element(self.LOGIN_BTN)

    @allure.step('Click on "Open an account"')
    def click_on_open_an_account(self):
        self.click_on(self.OPEN_AN_ACCOUNT)

    @allure.step('Assert warning message')
    def assert_warning_message(self, expected_message):
        error_message = self.get_element(self.WARNING_MESSAGE).text
        assert error_message == expected_message, f'Expected message "{expected_message}" does not match with "{error_message}"'
