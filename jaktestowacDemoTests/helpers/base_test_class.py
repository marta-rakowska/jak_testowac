import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener
import config_reader


class BaseTestClass(unittest.TestCase):
    @classmethod
    def setUp(self):
        config = config_reader.load()
        self.base_url = config[0].strip('\n')
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.subpage_art_url = self.base_url + '9-art'
        self.man_t_shirt_url = self.base_url + 'men/1-4-hummingbird-printed-t-shirt.html'
        service = webdriver.ChromeService(
            '/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        service.start()
        driver = webdriver.Chrome(service=service)
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    @classmethod
    def tearDown(self):
        self.ef_driver.quit()