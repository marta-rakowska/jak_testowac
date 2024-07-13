from selenium.webdriver.common.by import By

from helpers import functional_helpers as fh
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass

class LostHatLoginPageTests(BaseTestClass):
    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

        :param driver: webdriver instance
        :param xpath: x path to element with text to be observed
        :param expected_text: text that we expect to be found
        :return: None
        """
        element = driver.find_element(By.XPATH, xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Expected text differs from actual on page: {driver.current_url}')

    @screenshot_decorator
    def test_login_text_header(self):
        expected_text = 'Log in to your account'
        xpath = '//header[@class="page-header"]'
        driver = self.ef_driver

        driver.get(self.login_url)
        self.assert_element_text(driver, xpath, expected_text)

    @screenshot_decorator
    def test_correct_login(self):
        expected_text = 'Marta Testerka'
        user_name_xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'
        user_email = 'marta.testerka@test.com'
        user_pass = '0123456789'
        driver = self.ef_driver

        driver.get(self.login_url)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, user_name_xpath, expected_text)

    @screenshot_decorator
    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        alert_xpath = '//*[@class="alert alert-danger"]'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'
        driver = self.ef_driver

        driver.get(self.login_url)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, alert_xpath, expected_text)