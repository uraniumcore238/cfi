import pathlib

import allure

from selenium.webdriver.common.by import By

from app import tests
from app.pages.base_page import BasePage


class IdVerificationPage(BasePage):

    UPLOAD_BUTTON = (By.CSS_SELECTOR, '#upload-btn')
    SELFIE_UPLOADED_IMG = (By.CSS_SELECTOR, '.requirement-image')
    NEXT_BTN = (By.CSS_SELECTOR, '#submit-btn')

    @allure.step('Assert id-verification page')
    def assert_page(self):
        self.get_element(self.UPLOAD_BUTTON)

    @allure.step('Upload selfie')
    def upload_selfie(self, filename):
        path_to_selfie = pathlib.Path(tests.__file__).parent.parent.parent.joinpath(f'files_to_upload/{filename}')
        print(path_to_selfie)
        self.get_element(self.UPLOAD_BUTTON).send_keys(path_to_selfie)
        self.get_element(self.SELFIE_UPLOADED_IMG)

    @allure.step('Click on next button')
    def click_on_next_btn(self):
        self.click_on(self.NEXT_BTN)
