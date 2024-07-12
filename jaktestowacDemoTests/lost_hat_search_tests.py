import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener

class LostHatSearchTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        # self.service = Service(
        #     '/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
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

    def test_sanity_search_on_main_page(self):
        search_phrase = 'Hummingbird'
        expected_element_name = 'Hummingbird Printed T-Shirt'
        search_input_xpath = '//*[@name="s"]'
        result_element_xpath = '//*[@class="product-miniature js-product-miniature"]'

        self.ef_driver.get(self.base_url)
        search_input_element = self.ef_driver.find_element(By.XPATH, search_input_xpath)
        search_input_element.send_keys(search_phrase)
        search_input_element.send_keys(Keys.ENTER)

        result_elements = self.ef_driver.find_elements(By.XPATH, result_element_xpath)
        found_elements_number = 0
        for element in result_elements:
            if expected_element_name in element.text:
                found_elements_number = found_elements_number + 1

        self.assertEqual(1, found_elements_number,
                         f"We expect 1 and actual number of found items is {found_elements_number}")
