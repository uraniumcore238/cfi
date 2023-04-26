import allure

from selenium.webdriver.common.by import By
from app.pages.base_page import BasePage


class HeaderPage(BasePage):

    LOGO = (By.CSS_SELECTOR, 'img[src*="logo_red_white.png"]')

    @allure.step('Check logo visibility')
    def assert_logo_visibility(self):
        self.get_element(self.LOGO)

    def assert_color_of_step_element(self, expected_color, step):
        with allure.step(f'Assert color of step bullet {step}'):
            step_bullet = (By.XPATH, f"//*[contains(@class, 'step-bullet full-step')][text()='{step}']")
            color_hex = self.get_hex_background_color_of_element(step_bullet)
            assert expected_color in color_hex, f"Color {color_hex} doesn't match to the expected {expected_color}"
