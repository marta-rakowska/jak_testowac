import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from helpers.base_test_class import BaseTestClass
from helpers.wrappers import screenshot_decorator

class LostHatProductDetailsTests(BaseTestClass):
    @screenshot_decorator
    def test_check_product_default_size(self):
        expected_product_default_size = 'M'
        size_select_xpath = '//*[@id="group_1"]'

        driver = self.ef_driver
        driver.get(self.man_t_shirt_url)

        product_size_select_element = driver.find_element(By.XPATH, size_select_xpath)
        product_size_select = Select(product_size_select_element)
        observed_product_default_size_text = product_size_select.first_selected_option.text

        self.assertEqual(expected_product_default_size, observed_product_default_size_text,
                         f'Expected size differs from actual on page: {driver.current_url}')

    # @screenshot_decorator
    # def test_check_product_size_change(self):
    #     expected_product_changed_size = 'L'
    #     size_select_xpath = '//*[@id="group_1"]'
    #     default_select_option_xpath = '//*[@id="group_1"]/*[@selected="selected"]'
    #     size_l_select_xpath = '//*[@id="group_1"]/*[text()="L"]'
    #
    #     driver = self.ef_driver
    #
    #     driver.get('https://autodemo.testoneo.com/en/men/1-4-hummingbird-printed-t-shirt.html')
    #     selected_size_element = driver.find_element(By.XPATH, default_select_option_xpath)
    #     observed_product_default_size_text = selected_size_element.text
    #
    #     product_size_select_element = driver.find_element(By.XPATH, size_select_xpath)
    #     product_size_select_element.click()
    #
    #     option_l_element = driver.find_element(By.XPATH, size_l_select_xpath)
    #     option_l_element.click()
    #
    #     observed_product_size_changed_value = product_size_select_element.get_attribute('value')
    #     observed_product_size_changed_value_element = driver.find_element(By.XPATH,
    #                                                                       f'//*[@id="group_1"]/*[@value="{observed_product_size_changed_value}"]')
    #     observed_product_size_changed_text = observed_product_size_changed_value_element.text
    #
    #     self.assertNotEqual(expected_product_changed_size, observed_product_default_size_text,
    #                         f'Expected size is the same as actual on page: {driver.current_url}')
    #     self.assertEqual(expected_product_changed_size, observed_product_size_changed_text,
    #                      f'Expected size differs from actual on page: {driver.current_url}')

    @screenshot_decorator
    def test_check_product_size_change(self):
        expected_product_changed_size = 'L'
        size_select_xpath = '//*[@id="group_1"]'

        driver = self.ef_driver
        driver.get('https://autodemo.testoneo.com/en/men/1-4-hummingbird-printed-t-shirt.html')

        product_size_select_element = driver.find_element(By.XPATH, size_select_xpath)
        product_size_select = Select(product_size_select_element)

        observed_product_default_size_text = product_size_select.first_selected_option.text

        product_size_select.select_by_visible_text(expected_product_changed_size)
        observed_product_size_changed_text = product_size_select.first_selected_option.text

        self.assertNotEqual(expected_product_changed_size, observed_product_default_size_text,
                            f'Expected size is the same as actual on page: {driver.current_url}')
        self.assertEqual(expected_product_changed_size, observed_product_size_changed_text,
                         f'Expected size differs from actual on page: {driver.current_url}')
