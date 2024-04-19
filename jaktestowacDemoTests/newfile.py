import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LostHatTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.service = Service('/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def user_login(self, driver, user_email, user_pass):
        login_input_element = driver.find_element(By.XPATH, '//*[@type="email"]')
        login_input_element.send_keys(user_email)

        password_input_element = driver.find_element(By.XPATH, '//*[@type="password"]')
        password_input_element.send_keys(user_pass)

        button_next_element = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
        button_next_element.click()

    def test_login_text_header(self):
        expected_text = 'Your account'
        driver = self.driver
        driver.get(self.login_url)
        header_element = driver.find_element(By.XPATH, '//*[@class="page-header"]')
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected title differs from actual for page url: {self.login_url}')

    def test_correct_login(self):
        expected_text = 'Marta Testerka'
        user_email = 'marta.testerka@test.com'
        user_pass = '0123456789'
        driver = self.driver
        driver.get(self.login_url)

        self.user_login(driver, user_email, user_pass)
        header_element = driver.find_element(By.XPATH, '//a[@class="account"]/*[@class="hidden-sm-down"]')
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected title differs from actual title for page url: {self.login_url}')

    def test_check_product_name_and_price(self):
        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        driver = self.driver
        driver.get(self.sample_product_url)

        name_element = driver.find_element(By.XPATH, '//*[@class="col-md-6"]//*[@itemprop="name"]')
        name_element_text = name_element.text
        self.assertEqual(expected_product_name, name_element_text,
                         f'Expected text differs from actual for page url: {self.sample_product_url}')

    def test_check_product_price(self):
        expected_product_price = 'PLN23.52'
        driver = self.driver
        driver.get(self.sample_product_url)
        price_element = driver.find_element(By.XPATH, '//*[@class="current-price"]//*[@itemprop="price"]')
        price_element_text = price_element.text
        self.assertEqual(expected_product_price, price_element_text,
                         f'Expected text differs from actual for page url: {self.sample_product_url}')

    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'
        driver = self.driver
        driver.get(self.login_url)

        self.user_login(driver, user_email, user_pass)
        alert_element = driver.find_element(By.XPATH, '//*[@class="alert alert-danger"]')
        alert_element_text = alert_element.text
        self.assertEqual(expected_text, alert_element_text,
                         f'Expected title differs from actual title for page url: {self.login_url}')

