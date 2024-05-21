import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from jaktestowacDemoTests.helpers import functional_helpers as fh


class LostHatTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.service = Service('/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

        :param driver: webdriver instance
        :param xpath: xpath to element with text to be observed
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

    def test_check_product_name(self):
        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        name_xpath = '//*[@class="col-md-6"]//*[@itemprop="name"]'
        driver = self.driver

        driver.get(self.sample_product_url)
        self.assert_element_text(driver, name_xpath, expected_product_name)

    def test_check_product_price(self):
        expected_product_price = 'PLN23.52'
        price_xpath = '//*[@class="current-price"]//*[@itemprop="price"]'
        driver = self.driver

        driver.get(self.sample_product_url)
        self.assert_element_text(driver, price_xpath, expected_product_price)


class LostHatFrontPageTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.service = Service(
            '/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_slider_presence(self):
        slider_xpath = '//*[@id="carousel"]'
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH, slider_xpath)

    def test_slider_minimum_size(self):
        expected_min_height = 300
        expected_min_width = 600
        slider_xpath = '//*[@id="carousel"]'
        driver = self.driver

        driver.get(self.base_url)
        slider_element = driver.find_element(By.XPATH, slider_xpath)
        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']
        with self.subTest('Element height'):
            self.assertLess(expected_min_height, actual_slider_height, f'Element height found by xpath {slider_xpath} on page {driver.current_url} is smaller than expected {expected_min_height}px')
        with self.subTest('Element width'):
            self.assertLess(expected_min_width, actual_slider_width, f'Element width found by xpath {slider_xpath} on page {driver.current_url} is smaller than expected {expected_min_width}px')

    def test_slider_contain_exact_number_of_slides(self):
        expected_number_of_slides = 3
        slides_xpath = '//*[@id="carousel"]/ul/li'
        driver = self.driver

        driver.get(self.base_url)
        slider_elements = driver.find_elements(By.XPATH, slides_xpath)
        actual_number_of_slides = len(slider_elements)

        self.assertEqual(expected_number_of_slides, actual_number_of_slides, f'Slides number differs for page {self.base_url}')

    def test_slides_required_title_text(self):
        expected_text_included_in_slide = 'sample'
        slides_titles_xpath = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'
        driver = self.driver

        driver.get(self.base_url)
        title_elements = driver.find_elements(By.XPATH, slides_titles_xpath)

        for title_element in title_elements:
            title_element_text = title_element.get_attribute("textContent")
            title_element_text_lower = title_element_text.lower()
            with self.subTest(title_element_text_lower):
                self.assertIn(expected_text_included_in_slide, title_element_text_lower,
                          f"Slides do not contain expected text for page {self.base_url}")

    def test_number_of_featured_products(self):
        expected_number_of_products = 8
        product_xpath = '//*[@class="product-miniature js-product-miniature"]'
        driver = self.driver

        driver.get(self.base_url)
        product_elements = driver.find_elements(By.XPATH, product_xpath)
        actual_number_of_products = len(product_elements)

        self.assertEqual(expected_number_of_products, actual_number_of_products,
                         f'Slides number differs for page {self.base_url}')

