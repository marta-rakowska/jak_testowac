from jaktestowacDemoTests.helpers.base_test_class import BaseTestClass
from jaktestowacDemoTests.helpers.wrappers import screenshot_decorator
from jaktestowacDemoTests.pages.shirt_product_page import ShirtProductPage


class LostHatProductPagePomTests(BaseTestClass):
    @screenshot_decorator
    def test_check_product_name(self):
        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'

        shirt_product_page = ShirtProductPage(self.conf_driver)
        shirt_product_page.visit()
        product_name = shirt_product_page.get_product_name()
        self.assertEqual(expected_product_name, product_name,
                         f'Expected product name differ from actual on page: {self.conf_driver.current_url}')

    @screenshot_decorator
    def test_check_product_price(self):
        expected_product_price = 'PLN23.52'

        shirt_product_page = ShirtProductPage(self.conf_driver)
        shirt_product_page.visit()
        product_price = shirt_product_page.get_product_price()
        self.assertEqual(expected_product_price, product_price,
                         f'Expected product name differ from actual on page: {self.conf_driver.current_url}')