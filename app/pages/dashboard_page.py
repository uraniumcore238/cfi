import allure

from selenium.webdriver.common.by import By

from app.pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_CONTAINER = (By.CSS_SELECTOR, '.dashboard-container')

    @allure.step('Assert dashboard page visibility')
    def assert_dashboard_container_visibility(self):
        self.get_element(self.DASHBOARD_CONTAINER)
