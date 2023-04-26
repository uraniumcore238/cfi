import allure

from selenium.webdriver.common.by import By

from app.pages.base_page import BasePage


class BasicInfoPage(BasePage):

    DATE_OF_BIRTH = (By.CSS_SELECTOR, '#date-birth')
    RESIDENCE_FIELD = (By.CSS_SELECTOR, '#country-residence')
    CITY_FIELD = (By.CSS_SELECTOR, '#city')
    STREET_FIELD = (By.CSS_SELECTOR, '#street')
    POST_CODE_FIELD = (By.CSS_SELECTOR, '#postcode')
    BUILDING_NUMBER_FIELD = (By.CSS_SELECTOR, '#building')
    NEXT_BTN = (By.CSS_SELECTOR, '#submit-btn')

    @allure.step('Assert basic info page')
    def assert_page(self):
        self.get_element(self.DATE_OF_BIRTH)

    @allure.step('Fill date of birth')
    def fill_date_of_birth(self, date_of_birth):
        self.get_element(self.DATE_OF_BIRTH).send_keys(date_of_birth)

    @allure.step('Fill country of residence')
    def fill_residence(self, residence):
        self.get_element(self.RESIDENCE_FIELD).send_keys(residence)

    @allure.step('Fill full address. City, street, building')
    def fill_full_address(self, customer):
        self.get_element(self.CITY_FIELD).send_keys(customer.address_city)
        self.get_element(self.STREET_FIELD).send_keys(customer.address_street)
        self.get_element(self.BUILDING_NUMBER_FIELD).send_keys(customer.address_building_number)

    @allure.step('Click on next button')
    def click_on_next_btn(self):
        self.click_on(self.NEXT_BTN)
