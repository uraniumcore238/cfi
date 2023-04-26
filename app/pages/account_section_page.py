import allure

from selenium.webdriver.common.by import By

from app.pages.base_page import BasePage


class AccountSectionPage(BasePage):

    LEVERAGE_CHECKBOX = (By.ID, 'leverage-agree')
    NEXT_BTN = (By.ID, 'submit-btn')
    ACCOUNT_CONTAINER = (By.ID, 'account-selection-container')

    @allure.step('Wait for account section page')
    def wait_for_the_page(self):
        self.get_element(self.ACCOUNT_CONTAINER)

    @allure.step('Click on leverage checkbox')
    def click_on_leverage_checkbox(self):
        el = self.get_element_without_wait(self.LEVERAGE_CHECKBOX)
        self.go_to_element(el)
        el.click()

    @allure.step('Click on next button')
    def click_on_next_btn(self):
        self.click_on(self.NEXT_BTN)
