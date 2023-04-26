import allure

from selenium.webdriver.common.by import By
from app.pages.base_page import BasePage


class AgreementPage(BasePage):

    MAT_CHECKBOX = (By.CSS_SELECTOR, '[for*=mat-checkbox]')
    NEXT_BTN = (By.CSS_SELECTOR, '#submit-btn')
    LOGO_RECAPTCHA = (By.CSS_SELECTOR, '.rc-anchor-logo-large')

    @allure.step('Assert agreement page')
    def assert_page(self):
        self.get_element(self.MAT_CHECKBOX)

    @allure.step('Click on mat checkbox')
    def click_on_mat_checkbox(self):
        self.get_element(self.LOGO_RECAPTCHA, timeout=20)
        self.go_to_page_bottom()
        self.click_on(self.MAT_CHECKBOX)

    @allure.step('Click on next button')
    def click_on_submit_btn(self):
        self.click_on(self.NEXT_BTN)
