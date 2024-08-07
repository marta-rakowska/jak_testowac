import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from jaktestowacDemoTests.helpers.screenshot_listener import ScreenshotListener
import jaktestowacDemoTests.config_reader


class BaseTestClass(unittest.TestCase):
    @classmethod
    def setUp(self):
        config = jaktestowacDemoTests.config_reader.load()
        # self.base_url = config[0].strip('\n')
        self.base_url = config['base_url']
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.subpage_art_url = self.base_url + '9-art'
        self.man_t_shirt_url = self.base_url + 'men/1-4-hummingbird-printed-t-shirt.html'
        service = webdriver.ChromeService(config['chromedriver_path'])
        service.start()
        driver = webdriver.Chrome(service=service)
        if config['event_firing_driver']:
            self.conf_driver = EventFiringWebDriver(driver, ScreenshotListener())
        else:
            self.conf_driver = driver

    @classmethod
    def tearDown(self):
        self.conf_driver.quit()