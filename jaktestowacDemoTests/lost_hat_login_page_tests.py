import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from helpers import functional_helpers as fh


class LostHatLoginPageTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        # self.service = Service('/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        # self.service.start()
        # self.driver = webdriver.Remote(self.service.service_url)
        self.service = webdriver.ChromeService(
            '/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        self.service.start()
        self.driver = webdriver.Chrome(service=self.service)

    @classmethod
    def tearDown(self):
        self.driver.quit()

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
    def test_login_text_header(self):
        expected_text = 'Log in to your account'
        xpath = '//header[@class="page-header"]'
        driver = self.driver

        driver.get(self.login_url)
        self.assert_element_text(driver, xpath, expected_text)

    def test_correct_login(self):
        expected_text = 'Marta Testerka'
        user_name_xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'
        user_email = 'marta.testerka@test.com'
        user_pass = '0123456789'
        driver = self.driver

        driver.get(self.login_url)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, user_name_xpath, expected_text)

    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        alert_xpath = '//*[@class="alert alert-danger"]'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'
        driver = self.driver

        driver.get(self.login_url)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, alert_xpath, expected_text)