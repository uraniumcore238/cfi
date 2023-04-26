import allure

from selenium.webdriver.common.by import By
from app.pages.base_page import BasePage


class VerificationPage(BasePage):

    VERIFY_LATER = (By.ID, 'verify-later-btn')

    @allure.step('Assert verification page')
    def assert_page(self):
        self.get_element(self.VERIFY_LATER)

    @allure.step('Click on verify later btn')
    def click_on_verify_later(self):
        self.click_on(self.VERIFY_LATER)
