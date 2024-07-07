import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from helpers import operational_helpers as oh

class LostHatShoppingCartTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.subpage_art_url = 'https://autodemo.testoneo.com/en/9-art'
        # self.service = Service(
        #     '/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        # self.service.start()
        # self.driver = webdriver.Remote(self.service.service_url)
        self.service = webdriver.ChromeService(
            '/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        self.service.start()
        self.driver = webdriver.Chrome(service=self.service)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_adding_item_to_shopping_cart(self):
        expected_confirmation_modal_text = '\ue876Product successfully added to your shopping cart'
        item_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
        shopping_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'

        driver = self.driver
        driver.get(self.subpage_art_url)

        item_element = driver.find_element(By.XPATH, item_xpath)
        item_element.click()
        shopping_cart_button_element = driver.find_element(By.XPATH, shopping_cart_button_xpath)
        shopping_cart_button_element.click()

        confirmation_modal_element = oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)
        self.assertEqual(expected_confirmation_modal_text, confirmation_modal_element.text)



