import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener

class LostHatSmokeTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.clothes_product_url = self.base_url + '3-clothes'
        self.accessories_product_url = self.base_url + '6-accessories'
        self.art_product_url = self.base_url + '9-art'
        # self.service = Service('/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        # self.service.start()
        # self.driver = webdriver.Remote(self.service.service_url)
        service = webdriver.ChromeService(
            '/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        service.start()
        driver = webdriver.Chrome(service=service)
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    @classmethod
    def tearDown(self):
        self.ef_driver.quit()

    def test_base_page_title(self):
        expected_title = 'Lost Hat'
        self.assert_title(self.base_url, expected_title)

    def test_product_art_page_title(self):
        expected_title = 'Art'
        self.assert_title(self.art_product_url, expected_title)

    def test_product_clothes_page_title(self):
        expected_title = 'Clothes'
        self.assert_title(self.clothes_product_url, expected_title)

    def test_product_accessories_page_title(self):
        expected_title = 'Accessories'
        self.assert_title(self.accessories_product_url, expected_title)

    def test_login_page_title(self):
        expected_title = 'Login'
        self.assert_title(self.login_url, expected_title)

    def get_page_title(self, url):
        self.ef_driver.get(url)
        return self.ef_driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title, f'Expected title {expected_title} differs from actual title '
                                                       f'{actual_title} on page: {url}')

    def test_smoke_search_on_main_page(self):
        search_phrase = 'mug'
        search_input_xpath = '//*[@name="s"]'
        result_element_xpath = '//*[@class="product-miniature js-product-miniature"]'
        minimum_expected_elements = 5

        self.ef_driver.get(self.base_url)
        search_input_element = self.ef_driver.find_element(By.XPATH, search_input_xpath)
        search_input_element.send_keys(search_phrase)
        search_input_element.send_keys(Keys.ENTER)

        result_elements = self.ef_driver.find_elements(By.XPATH, result_element_xpath)
        self.assertLessEqual(minimum_expected_elements, len(result_elements),
                             f"Expected number {minimum_expected_elements} isn't lower or equal than actual number of elements found: {len(result_elements)}")
