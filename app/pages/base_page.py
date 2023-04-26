import re
import time
import allure

from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver, timeout=5):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def open(self, url):
        with allure.step(f'Open url {url}'):
            self.driver.get(url)

    @allure.step('Wait for element visibility')
    def get_element(self, locator: tuple, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        el = wait.until(EC.visibility_of_element_located(locator))
        self.go_to_element(el)
        return el

    def get_element_without_wait(self, locator: tuple):
        return self.driver.find_element(*locator)

    def get_elements_without_wait(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def get_elements(self, locator: tuple, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_any_elements_located(locator))

    def get_present_elements(self, locator: tuple, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def go_to_page_bottom(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")

    def elements_are_visible(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_all_elements_located(locator))

    def get_clickable_element(self, locator: tuple, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def is_element_present(self, locator: tuple):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def get_element_by_text(self, text):
        return self.driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")

    def click_on(self, locator):
        el = self.get_element(locator)
        for _ in range(10):
            try:
                if self.get_clickable_element(locator).click():
                    break
            except ElementClickInterceptedException:
                time.sleep(0.5)
                self.go_to_element(el)

    def refresh_page(self, timeout: int = 5):
        time.sleep(timeout)
        self.driver.refresh()

    @allure.step('Hover cursor over element')
    def hover_cursor_over_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step('Wait for element invisibility')
    def wait_for_invisibility_of_element(self, locator):
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element(locator))

    def assert_text_in_element(self, locator, text):
        with allure.step(f'Wait for text - {text} in element'):
            WebDriverWait(self.driver, timeout=10, poll_frequency=0.1).until(
                EC.text_to_be_present_in_element(locator, text))

    def assert_text_in_url(self, url):
        with allure.step(f'Check if url contains - {url}'):
            try:
                WebDriverWait(self.driver, 10, poll_frequency=0.1).until(EC.url_contains(url))
                return 'passed'
            except TimeoutException:
                return 'failed'

    @allure.step('Wait for text in element')
    def wait_for_text_in_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step('Get hex color of element')
    def get_hex_color_of_element(self, locator):
        color_rgba = self.get_element(locator).value_of_css_property('color')
        color = re.findall(r'-[0-9]+|[0-9]+', color_rgba)
        color_int = tuple([int(i) for i in color])
        return '%02x%02x%02x%02x' % color_int

    @allure.step('Get hex color of background of element')
    def get_hex_background_color_of_element(self, locator):
        color_rgba = self.get_element(locator).value_of_css_property('background-color')
        color = re.findall(r'-[0-9]+|[0-9]+', color_rgba)
        color_int = tuple([int(i) for i in color])
        return '%02x%02x%02x%02x' % color_int
