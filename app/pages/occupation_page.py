import allure

from selenium.webdriver.common.by import By

from app.pages.base_page import BasePage


class OccupationPage(BasePage):

    OCCUPATION_STATUS = (By.CSS_SELECTOR, '#occupation-status')
    INDUSTRY = (By.ID, 'industry')
    DETAILED_PROFESSION = (By.ID, "profession")
    ARE_YOU_PEP = (By.CSS_SELECTOR, '#pep-status')

    INDUSTRY_LIST = (By.CSS_SELECTOR, '#industry-panel')
    OCCUPATION_STATUS_EMPLOYED = (By.CSS_SELECTOR, '#occupation-status-Employed')
    INDUSTRY_EDUCATION = (By.CSS_SELECTOR, '#industry-Education .mat-option-text')
    ADDRESS_COUNTRY = (By.CSS_SELECTOR, '#address-country')
    ADDRESS_COUNTRY_LIST = (By.CSS_SELECTOR, '#address-country-panel')
    #address
    CITY_FIELD = (By.CSS_SELECTOR, '#address-city')
    STREET_FIELD = (By.CSS_SELECTOR, '#street')
    BUILDING_NUMBER_FIELD = (By.CSS_SELECTOR, '#address-street-building')
    COMPANY_NAME_FIELD = (By.CSS_SELECTOR, '#address-company')
    NEXT_BTN = (By.CSS_SELECTOR, '#submit-btn')

    @allure.step('Assert occupation page')
    def assert_page(self):
        self.get_element(self.OCCUPATION_STATUS)

    @allure.step('Fill occupation status')
    def fill_occupation_status(self, occupation_status):
        self.get_element(self.OCCUPATION_STATUS).send_keys(occupation_status)

    @allure.step('Select industry')
    def select_industry(self, industry):
        self.get_element(self.INDUSTRY).send_keys(industry)
        self.wait_for_invisibility_of_element(self.INDUSTRY_LIST)

    @allure.step('Fill detailed profession')
    def fill_detailed_profession(self, profession):
        self.get_element(self.DETAILED_PROFESSION).click()
        self.get_element(self.DETAILED_PROFESSION).send_keys(profession)
        # self.get_element(self.DETAILED_PROFESSION).send_keys(profession)

    @allure.step('Select country in work address')
    def select_country(self, country):
        self.get_element(self.ADDRESS_COUNTRY).send_keys(country)
        # self.get_element(self.ADDRESS_COUNTRY).click()
        # self.get_element(self.ADDRESS_COUNTRY_LIST)
        # self.get_element(By.CSS_SELECTOR, f'#country-{country}').click()

    @allure.step('Fill full address. City, street, building')
    def fill_full_working_address(self, customer):
        self.get_element(self.CITY_FIELD).send_keys(customer.address_city)
        self.get_element(self.COMPANY_NAME_FIELD).send_keys(customer.address_street)
        self.get_element(self.BUILDING_NUMBER_FIELD).send_keys(customer.address_building_number)

    @allure.step('Click on next button')
    def click_on_next_btn(self):
        self.click_on(self.NEXT_BTN)
