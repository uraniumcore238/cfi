import allure
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

from app.pages.base_page import BasePage


class FinancialInfoPage(BasePage):

    GROSS_ANNUAL_INCOME = (By.CSS_SELECTOR, '#annual-income')
    GROSS_ANNUAL_INCOME_LIST = (By.CSS_SELECTOR, '#annual-income-panel')
    NET_ASSETS_IN_USD = (By.CSS_SELECTOR, '#net-assets')
    NET_ASSETS_IN_USD_LIST = (By.CSS_SELECTOR, '#net-assets-panel')
    SOURCE_OF_FUNDS = (By.CSS_SELECTOR, '#source-fund')
    SOURCE_OF_FUNDS_LIST = (By.CSS_SELECTOR, '#source-fund-panel')
    EXPECTED_INITIAL_DEPOSIT = (By.CSS_SELECTOR, '#initial-deposit')
    EXPECTED_INITIAL_DEPOSIT_LIST = (By.CSS_SELECTOR, '#initial-deposit-panel')
    EXPECTED_ANNUAL_DEPOSIT = (By.CSS_SELECTOR, '#annual-deposit')
    EXPECTED_ANNUAL_DEPOSIT_LIST = (By.CSS_SELECTOR, '#annual-deposit-panel')
    NEXT_BTN = (By.CSS_SELECTOR, '#submit-btn')
    THIRD_ACTIVE_POINT = (By.XPATH, "//li[contains(@class, 'active')]//*[text()='3']")

    @allure.step('Wait for the financial info page')
    def wait_for_fin_page(self):
        self.get_element(self.THIRD_ACTIVE_POINT)

    @allure.step('Select gross annual income')
    def select_gross_annual_income(self, income):
        self.get_element(self.GROSS_ANNUAL_INCOME).click()
        # self.get_element(self.GROSS_ANNUAL_INCOME).click()
        self.get_element(self.GROSS_ANNUAL_INCOME_LIST)
        self.get_clickable_element((By.CSS_SELECTOR, f'[id="{income}"]')).click()
        self.wait_for_invisibility_of_element(self.GROSS_ANNUAL_INCOME_LIST)

    @allure.step('Select net assets in USD')
    def select_net_assert_in_usd(self, assets):
        self.get_element(self.NET_ASSETS_IN_USD).click()
        self.get_element(self.NET_ASSETS_IN_USD_LIST)
        self.get_element((By.CSS_SELECTOR, f'[id="{assets}"]')).click()
        self.wait_for_invisibility_of_element(self.NET_ASSETS_IN_USD_LIST)

    @allure.step('Select one source of funds')
    def select_one_source_of_funds(self, souce):
        self.get_element(self.SOURCE_OF_FUNDS).click()
        self.get_element(self.SOURCE_OF_FUNDS_LIST)
        self.get_element((By.CSS_SELECTOR, f'[id="{souce}"]')).click()
        self.get_element(self.SOURCE_OF_FUNDS_LIST).send_keys(Keys.TAB)
        self.wait_for_invisibility_of_element(self.SOURCE_OF_FUNDS_LIST)

    @allure.step('Select expected initial deposit')
    def select_expected_initial_deposit(self, deposit):
        self.get_element(self.EXPECTED_INITIAL_DEPOSIT).click()
        self.get_element(self.EXPECTED_INITIAL_DEPOSIT_LIST)
        self.get_element((By.CSS_SELECTOR, f'[id="{deposit}"]')).click()
        self.wait_for_invisibility_of_element(self.EXPECTED_INITIAL_DEPOSIT_LIST)

    @allure.step('Select expected annual deposit')
    def select_expected_annual_deposit(self, deposit):
        self.get_element(self.EXPECTED_ANNUAL_DEPOSIT).click()
        self.get_element(self.EXPECTED_ANNUAL_DEPOSIT_LIST)
        self.get_element((By.CSS_SELECTOR, f'[id="{deposit}"]')).click()
        self.wait_for_invisibility_of_element(self.EXPECTED_ANNUAL_DEPOSIT_LIST)

    @allure.step('Click on next button')
    def click_on_next_btn(self):
        self.click_on(self.NEXT_BTN)
