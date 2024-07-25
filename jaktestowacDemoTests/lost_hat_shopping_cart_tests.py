from selenium.webdriver.common.by import By
from helpers.wrappers import screenshot_decorator

from helpers import operational_helpers as oh
from helpers.base_test_class import BaseTestClass

class LostHatShoppingCartTests(BaseTestClass):
    @screenshot_decorator
    def test_adding_item_to_shopping_cart(self):
        expected_confirmation_modal_text = '\ue876Product successfully added to your shopping cart'
        item_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
        shopping_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'

        driver = self.ef_driver
        driver.get(self.subpage_art_url)

        item_element = driver.find_element(By.XPATH, item_xpath)
        item_element.click()
        shopping_cart_button_element = driver.find_element(By.XPATH, shopping_cart_button_xpath)
        shopping_cart_button_element.click()

        confirmation_modal_element = driver.find_element(By.XPATH, confirmation_modal_title_xpath)
        self.assertEqual(expected_confirmation_modal_text, confirmation_modal_element.text)



