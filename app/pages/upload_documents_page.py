import pathlib

import allure

from selenium.webdriver.common.by import By

from app import tests
from app.pages.base_page import BasePage


class UploadDocumentsPage(BasePage):

    UPLOAD_IDENTITY_BUTTON = (By.CSS_SELECTOR, '#poi-box .desktop #upload-btn')
    IDENTITY_UPLOADED = (By.CSS_SELECTOR, '#poi-box .desktop .document-file')

    UPLOAD_ADDRESS_BUTTON = (By.CSS_SELECTOR, '#poa-box .desktop #upload-btn')
    ADDRESS_UPLOADED = (By.CSS_SELECTOR, '#poa-box .desktop .document-file')

    UPLOAD_RESIDENCY_BUTTON = (By.CSS_SELECTOR, '#por-box .desktop #upload-btn')
    RESIDENCY_UPLOADED = (By.CSS_SELECTOR, '#por-box .desktop .document-file')
    HINT_BOX = (By.CSS_SELECTOR, '#por-box .desktop .frontback-hint')

    NEXT_BTN = (By.CSS_SELECTOR, '#submit-btn')
    CONFIRMATION_POPUP_TITLE = (By.CSS_SELECTOR, '#mat-dialog-0 h1')

    @allure.step('Assert upload-documents page')
    def assert_page(self):
        self.get_element(self.UPLOAD_IDENTITY_BUTTON)

    @allure.step('Upload proof of identity')
    def upload_proof_of_identity(self, filename):
        path_to_file = pathlib.Path(tests.__file__).parent.parent.joinpath(f'files_to_upload/{filename}')
        self.get_element(self.UPLOAD_IDENTITY_BUTTON).send_keys(path_to_file)
        self.get_element(self.IDENTITY_UPLOADED)

    @allure.step('Upload proof of address')
    def upload_proof_of_address(self, filename):
        path_to_file = pathlib.Path(tests.__file__).parent.parent.joinpath(f'files_to_upload/{filename}')
        self.get_element(self.UPLOAD_ADDRESS_BUTTON).send_keys(path_to_file)
        self.get_element(self.ADDRESS_UPLOADED)

    @allure.step('Upload proof of residency')
    def upload_proof_of_residency(self, filename):
        path_to_file = pathlib.Path(tests.__file__).parent.parent.joinpath(f'files_to_upload/{filename}')
        self.get_element(self.UPLOAD_RESIDENCY_BUTTON).send_keys(path_to_file)
        self.wait_for_text_in_element(self.HINT_BOX, 'Back')
        self.get_element(self.UPLOAD_RESIDENCY_BUTTON).send_keys(path_to_file)
        self.get_element(self.RESIDENCY_UPLOADED)

    @allure.step('Click on proceed button')
    def click_on_proceed_btn(self):
        self.click_on(self.NEXT_BTN)

    @allure.step('Assert confirmation message')
    def assert_confirmation_message(self, expected_confirmation_msg):
        success_msg = self.get_element(self.CONFIRMATION_POPUP_TITLE).text
        assert expected_confirmation_msg == success_msg, f"The expected message {expected_confirmation_msg} doesn't " \
                                                         f"match to actual {success_msg}"
