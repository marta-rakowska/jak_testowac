from selenium.webdriver.common.by import By
from helpers.base_test_class import BaseTestClass


class LostHatProductPageTests(BaseTestClass):
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

    def test_check_product_name(self):
        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        name_xpath = '//*[@class="col-md-6"]//*[@itemprop="name"]'
        driver = self.conf_driver

        driver.get(self.sample_product_url)
        self.assert_element_text(driver, name_xpath, expected_product_name)

    def test_check_product_price(self):
        expected_product_price = 'PLN23.52'
        price_xpath = '//*[@class="current-price"]//*[@itemprop="price"]'
        driver = self.conf_driver

        driver.get(self.sample_product_url)
        self.assert_element_text(driver, price_xpath, expected_product_price)




