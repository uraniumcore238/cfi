import random
import time

import allure
from selenium.common import ElementClickInterceptedException

from selenium.webdriver.common.by import By

from app.pages.base_page import BasePage


class RegistrationPage(BasePage):

    HEADER_TEXT = (By.CSS_SELECTOR, "#screen-notice")
    RISK_DISCLOSURE_LINK = (By.CSS_SELECTOR, "[href*='Disclaimer']")
    ORDER_EXECUTION_POLICY_LINK = (By.CSS_SELECTOR, "[href*='Order']")
    CONFLICT_POLICY_LINK = (By.CSS_SELECTOR, "[href*='Conflict']")
    TERMS_AND_CONDITIONS_LINK = (By.CSS_SELECTOR, "[href*='Terms']")
    SHARES_TRADING_LINK = (By.CSS_SELECTOR, "[href*='Shares']")
    CFI_CY_LINK = (By.CSS_SELECTOR, "[href*='regulatory']")

    FIRST_NAME_TITLE = (By.CSS_SELECTOR, '#firstname-container .form-label')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#firstname')
    FIRST_NAME_ERROR = (By.CSS_SELECTOR, '#firstname-field .mat-error')
    FIRST_NAME_PLACEHOLDER = (By.CSS_SELECTOR, '[for="firstname"]')
    LAST_NAME_TITLE = (By.CSS_SELECTOR, '#lastname-container .form-label')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#lastname')
    LAST_NAME_ERROR = (By.CSS_SELECTOR, '#lastname-container .mat-error')
    LAST_NAME_PLACEHOLDER = (By.CSS_SELECTOR, '[for="lastname"]')
    MOBILE_NUMBER_TITLE = (By.CSS_SELECTOR, '#phone-number-container .form-label')
    MOBILE_NUMBER_PLACEHOLDER = (By.CSS_SELECTOR, '#phone-number-input')
    PHONE_CODE = (By.CSS_SELECTOR, '[formcontrolname="phone_code"] .flex')
    PHONE_INPUT = (By.CSS_SELECTOR, '#phone-number-input')
    PHONE_ERROR = (By.CSS_SELECTOR, '#error-msg')
    PHONE_CODE_NEXT_TO_SELECTED = (By.CSS_SELECTOR, '#phone-code-panel .mat-selected+.mat-option')
    EMAIL_ADDRESS_TITLE = (By.CSS_SELECTOR, '#email-container .form-label')

    PHONE_CODE_NEXT_TO_SELECTED = (By.CSS_SELECTOR, '#phone-code-panel .mat-selected+.mat-option')

    EMAIL_INPUT = (By.CSS_SELECTOR, '#email')
    EMAIL_ERROR = (By.CSS_SELECTOR, '#email-container .mat-error')
    EMAIL_ADDRESS_PLACEHOLDER = (By.CSS_SELECTOR, '[for="email"]')
    PASSWORD_TITLE = (By.CSS_SELECTOR, '#password-container .form-label')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password-input')
    PASSWORD_INVISIBLE = (By.CSS_SELECTOR, '#password-input[type="password"]')
    PASSWORD_VISIBLE = (By.CSS_SELECTOR, '#password-input[type="text"]')
    PASSWORD_EYE_ICON = (By.CSS_SELECTOR, '#password-input~.icon')
    PASSWORD_LENGTH_ICON = (By.XPATH, "//*[contains(text(), 'Password must be')]/preceding-sibling::*")
    PASSWORD_UPPERCASE_ICON = (By.XPATH, "//*[contains(text(), 'Uppercase')]/preceding-sibling::*")
    PASSWORD_LOWERCASE_ICON = (By.XPATH, "//*[contains(text(), 'Lowercase')]/preceding-sibling::*")
    PASSWORD_NUMERIC_ICON = (By.XPATH, "//*[contains(text(), 'Numeric')]/preceding-sibling::*")
    CREATE_PASSWORD_PLACEHOLDER = (By.CSS_SELECTOR, '[for="password-input"]')

    NEXT_BTN = (By.CSS_SELECTOR, '#submit-btn')
    CHECKBOX = (By.CSS_SELECTOR, ".tnc-container .mat-checkbox")
    CHECKBOX_LABEL = (By.CSS_SELECTOR, ".tnc-container .mat-checkbox-label")
    PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, "[href*='Privacy']")
    COOKIES_POLICY_LINK = (By.CSS_SELECTOR, "[href*='Cookies']")

    @allure.step('Assert header text')
    def assert_header_text(self, expected_text):
        self.wait_for_text_in_element(self.HEADER_TEXT, expected_text)

    @allure.step('Assert Risk Disclosure link')
    def assert_risk_disclosure_link(self, expected_text):
        text = self.get_element(self.RISK_DISCLOSURE_LINK).get_attribute('href')
        assert expected_text == text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Assert Order execution link')
    def assert_order_execution_policy_link(self, expected_text):
        text = self.get_element(self.ORDER_EXECUTION_POLICY_LINK).get_attribute('href')
        assert expected_text == text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Assert Conflicts policy link')
    def assert_conflicts_policy_link(self, expected_text):
        text = self.get_element(self.CONFLICT_POLICY_LINK).get_attribute('href')
        assert expected_text == text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Assert Terms and Condition link')
    def assert_terms_and_condition_link(self, expected_text):
        text = self.get_element(self.TERMS_AND_CONDITIONS_LINK).get_attribute('href')
        assert expected_text == text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Assert Shares and Trading Terms and Condition link')
    def assert_shares_trading_terms_and_condition_link(self, expected_text):
        text = self.get_element(self.SHARES_TRADING_LINK).get_attribute('href')
        assert expected_text == text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Assert CFI CY link')
    def assert_cy_website_link(self, expected_text):
        text = self.get_element(self.CFI_CY_LINK).get_attribute('href')
        assert expected_text == text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Check the First Name title')
    def assert_the_first_name_title(self, expected_text):
        self.wait_for_text_in_element(self.FIRST_NAME_TITLE, expected_text)

    @allure.step('Check the First Name placeholder')
    def assert_the_first_name_placeholder(self, expected_text):
        text = self.get_element(self.FIRST_NAME_PLACEHOLDER).text
        assert text == expected_text, f'The placeholder "{text}" do not match with expected "{expected_text}"'

    @allure.step('Check the Last Name title')
    def assert_the_last_name_title(self, expected_text):
        self.wait_for_text_in_element(self.LAST_NAME_TITLE, expected_text)

    @allure.step('Check the Last Name placeholder')
    def assert_the_last_name_placeholder(self, expected_text):
        text = self.get_element(self.LAST_NAME_PLACEHOLDER).text
        assert text == expected_text, f'The placeholder "{text}" do not match with expected "{expected_text}"'

    @allure.step('Check the Mobile Number title')
    def assert_the_mobile_number_title(self, expected_text):
        self.wait_for_text_in_element(self.MOBILE_NUMBER_TITLE, expected_text)

    @allure.step('Check the Mobile Number placeholder')
    def assert_the_mobile_number_placeholder(self):
        text = self.get_element(self.MOBILE_NUMBER_PLACEHOLDER).text
        assert text == "", f'Getting attribute "{text}" is not empty'

    @allure.step('Check the Email Address title')
    def assert_the_email_address_title(self, expected_text):
        self.wait_for_text_in_element(self.EMAIL_ADDRESS_TITLE, expected_text)

    @allure.step('Check the Email Address placeholder')
    def assert_the_email_address_placeholder(self, expected_text):
        text = self.get_element(self.EMAIL_ADDRESS_PLACEHOLDER).text
        assert text == expected_text, f'The placeholder "{text}" do not match with expected "{expected_text}"'

    @allure.step('Check the Create Password title')
    def assert_the_password_title(self, expected_text):
        self.wait_for_text_in_element(self.PASSWORD_TITLE, expected_text)

    @allure.step('Check the Create Password placeholder')
    def assert_the_create_password_placeholder(self, expected_text):
        self.wait_for_text_in_element(self.CREATE_PASSWORD_PLACEHOLDER, expected_text)

    @allure.step('Fill the first name')
    def fill_the_first_name(self, first_name):
        self.get_element(self.FIRST_NAME_INPUT).send_keys(first_name)

    @allure.step('Fill the last name')
    def fill_the_last_name(self, last_name):
        self.get_element(self.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step('Fill the phone')
    def fill_the_phone(self, phone):
        self.get_element(self.PHONE_INPUT).send_keys(phone)

    @allure.step('Fill the email')
    def fill_the_email(self, email):
        self.get_element(self.EMAIL_INPUT).send_keys(email)

    @allure.step('Fill the password')
    def fill_the_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    @allure.step('Assert password invisibility')
    def assert_password_invisibility(self):
        self.go_to_element(self.get_element(self.PASSWORD_INVISIBLE))

    @allure.step('Assert password visibility')
    def assert_password_visibility(self):
        self.go_to_element(self.get_element(self.PASSWORD_VISIBLE))

    @allure.step('Click on password eye icon')
    def click_on_eye_icon(self):
        for _ in range(20):
            self.go_to_page_bottom()
            try:
                self.get_element(self.PASSWORD_EYE_ICON).click()
                if self.get_element(self.PASSWORD_EYE_ICON):
                    break
            except ElementClickInterceptedException:
                time.sleep(0.1)

    @allure.step('Click on checkbox')
    def click_on_checkbox(self):
        for _ in range(10):
            self.go_to_page_bottom()
            try:
                self.get_element(self.CHECKBOX).click()
                if self.get_element(self.CHECKBOX):
                    break
            except ElementClickInterceptedException:
                time.sleep(0.5)

    @allure.step('Click on next button')
    def click_on_next_btn(self):
        self.get_clickable_element(self.NEXT_BTN, timeout=20).click()

    @allure.step('Assert the first name error')
    def assert_first_name_error(self, expected_text):
        error_text = self.get_element(self.FIRST_NAME_ERROR).text
        assert error_text == expected_text, f'The error text "{error_text}" do not match with expected "{expected_text}"'

    @allure.step('Assert the last name error')
    def assert_last_name_error(self, expected_text):
        error_text = self.get_element(self.LAST_NAME_ERROR).text
        assert error_text == expected_text, f'The error text "{error_text}" do not match with expected "{expected_text}"'

    @allure.step('Assert mobile phone error')
    def assert_mobile_phone_error(self, expected_text):
        error_text = self.get_element(self.PHONE_ERROR).text
        assert error_text == expected_text, f'The error text "{error_text}" do not match with expected "{expected_text}"'

    @allure.step('Assert email error')
    def assert_email_error(self, expected_text):
        error_text = self.get_element(self.EMAIL_ERROR).text
        assert error_text == expected_text, f'The error text "{error_text}" do not match with expected "{expected_text}"'

    @allure.step('Assert password length icon')
    def assert_password_length_icon(self, expected_text):
        text = self.get_element(self.PASSWORD_LENGTH_ICON).get_attribute('src')
        assert expected_text in text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Assert password upper case icon')
    def assert_password_upper_case_icon(self, expected_text):
        text = self.get_element(self.PASSWORD_UPPERCASE_ICON).get_attribute('src')
        assert expected_text in text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Assert password lower case icon')
    def assert_password_lower_case_icon(self, expected_text):
        text = self.get_element(self.PASSWORD_LOWERCASE_ICON).get_attribute('src')
        assert expected_text in text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Assert password numeric icon')
    def assert_password_numeric_icon(self, expected_text):
        text = self.get_element(self.PASSWORD_NUMERIC_ICON).get_attribute('src')
        assert expected_text in text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Assert color of checkbox label')
    def assert_color_of_checkbox_label(self, expected_color):
        color_hex = self.get_hex_color_of_element(self.CHECKBOX_LABEL)
        assert expected_color in color_hex, f"Color {color_hex} doesn't match to the expected {expected_color}"

    @allure.step('Assert checkbox text')
    def assert_checkbox_text(self, expected_text):
        self.wait_for_text_in_element(self.CHECKBOX_LABEL, expected_text)

    @allure.step('Assert Privacy policy link')
    def assert_privacy_policy_link(self, expected_text):
        text = self.get_element(self.PRIVACY_POLICY_LINK).get_attribute('href')
        assert expected_text == text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Assert Cookie policy link')
    def assert_cookies_policy_link(self, expected_text):
        text = self.get_element(self.COOKIES_POLICY_LINK).get_attribute('href')
        assert expected_text == text, f'Getting attribute "{text}" do not match with expected "{expected_text}"'

    @allure.step('Assert Next button title')
    def assert_next_button_title(self, expected_text):
        self.wait_for_text_in_element(self.NEXT_BTN, expected_text)

    @allure.step('Assert that the phone code is not empty')
    def assert_not_empty_phone_code(self):
        text = self.get_element(self.PHONE_CODE).text
        assert text != '', f'Getting attribute "{text}" is empty'

    @allure.step('Choose the phone code')
    def choose_the_phone_code(self):
        with allure.step('Scroll page to the phone code element'):
            self.go_to_page_bottom()
            self.get_element(self.PHONE_INPUT)
        with allure.step('Get text of the phone code'):
            initial_code = self.get_element(self.PHONE_CODE).text
        with allure.step('Click on the phone code selector'):
            self.click_on(self.PHONE_CODE)
        with allure.step('Click on the code in the selector'):
            self.get_clickable_element(self.PHONE_CODE_NEXT_TO_SELECTED).click()
        with allure.step('Wait for phone codes list invisibility'):
            self.wait_for_invisibility_of_element(self.PHONE_CODE_NEXT_TO_SELECTED)
        with allure.step('Get text of changed phone code'):
            changed_code = self.get_element(self.PHONE_CODE).text
        with allure.step('Assert that the code before and after changes is not the same'):
            assert changed_code != initial_code, f'The code "{initial_code}" is still the same {changed_code}'

    @allure.step('Assert test result')
    def assert_test_result(self, expected_text, text):
        assert text == expected_text, f"The expected result {expected_text} doesn't match with {text}"
