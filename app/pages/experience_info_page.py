import allure

from selenium.webdriver.common.by import By

from app.pages.base_page import BasePage


class ExperienceInfoPage(BasePage):

    STOCKS_EXPERIENCE = (By.CSS_SELECTOR, '#question_a')
    STOCKS_EXPERIENCE_LIST = (By.CSS_SELECTOR, '#question_a-panel')
    STOCKS_EXPERIENCE_NEVER = (By.CSS_SELECTOR, '#question_a-panel [id="1"]')

    FOREX_EXPERIENCE = (By.CSS_SELECTOR, '#question_b')
    FOREX_EXPERIENCE_LIST = (By.CSS_SELECTOR, '#question_b-panel')
    FOREX_EXPERIENCE_LESS_TEN = (By.CSS_SELECTOR, '#question_b-panel [id="2"]')

    CRYPTO_EXPERIENCE = (By.CSS_SELECTOR, '#question_c')
    CRYPTO_EXPERIENCE_LIST = (By.CSS_SELECTOR, '#question_c-panel')
    CRYPTO_EXPERIENCE_TEN_TWENTY = (By.CSS_SELECTOR, '#question_c-panel [id="3"]')

    TRADING_EMPLOYMENT_EXPERIENCE = (By.CSS_SELECTOR, '#question_d')
    TRADING_EMPLOYMENT_EXPERIENCE_LIST = (By.CSS_SELECTOR, '#question_d-panel')
    TRADING_EMPLOYMENT_EXPERIENCE_NO = (By.CSS_SELECTOR, '#question_d-panel [id="4"]')
    NEXT_BTN = (By.CSS_SELECTOR, '#submit-btn')
    FOURTH_ACTIVE_POINT = (By.XPATH, "//li[contains(@class, 'active')]//*[text()='4']")

    @allure.step('Wait for the experience info page')
    def wait_for_exp_page(self):
        self.get_element(self.FOURTH_ACTIVE_POINT)

    @allure.step('Select stocks experience')
    def select_stocks_experience_never(self):
        self.get_element(self.STOCKS_EXPERIENCE).click()
        self.get_element(self.STOCKS_EXPERIENCE_LIST)
        self.get_element(self.STOCKS_EXPERIENCE_NEVER).click()
        self.wait_for_invisibility_of_element(self.STOCKS_EXPERIENCE_LIST)

    @allure.step('Select Forex experience')
    def select_forex_experience_less_than_ten(self):
        self.get_element(self.FOREX_EXPERIENCE).click()
        self.get_element(self.FOREX_EXPERIENCE_LIST)
        self.get_element(self.FOREX_EXPERIENCE_LESS_TEN).click()
        self.wait_for_invisibility_of_element(self.FOREX_EXPERIENCE_LIST)

    @allure.step('Select crypto experience')
    def select_crypto_experience_ten_twenty(self):
        self.get_element(self.CRYPTO_EXPERIENCE).click()
        self.get_element(self.CRYPTO_EXPERIENCE_LIST)
        self.get_element(self.CRYPTO_EXPERIENCE_TEN_TWENTY).click()
        self.wait_for_invisibility_of_element(self.CRYPTO_EXPERIENCE_LIST)

    @allure.step('Select trading employment experience')
    def select_trading_employment_experience_no(self):
        self.get_element(self.TRADING_EMPLOYMENT_EXPERIENCE).click()
        self.get_element(self.TRADING_EMPLOYMENT_EXPERIENCE_LIST)
        self.get_element(self.TRADING_EMPLOYMENT_EXPERIENCE_NO).click()
        self.wait_for_invisibility_of_element(self.TRADING_EMPLOYMENT_EXPERIENCE_LIST)

    @allure.step('Click on next button')
    def click_on_next_btn(self):
        self.click_on(self.NEXT_BTN)

