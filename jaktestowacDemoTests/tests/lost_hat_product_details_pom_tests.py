from jaktestowacDemoTests.helpers.base_test_class import BaseTestClass
from jaktestowacDemoTests.helpers.wrappers import screenshot_decorator
from jaktestowacDemoTests.pages.shirt_product_page import ShirtProductPage


class LostHatProductDetailsPomTests(BaseTestClass):

    @screenshot_decorator
    def test_check_product_default_size(self):
        expected_product_default_size = 'M'

        shirt_product_page = ShirtProductPage(self.conf_driver)
        shirt_product_page.visit()
        observed_product_default_size_text = shirt_product_page.get_product_default_size()
        self.assertEqual(expected_product_default_size, observed_product_default_size_text,
                         f'Expected product name differ from actual on page: {self.conf_driver.current_url}')

    @screenshot_decorator
    def test_check_product_size_change(self):
        expected_product_changed_size = 'L'

        shirt_product_page = ShirtProductPage(self.conf_driver)
        shirt_product_page.visit()
        observed_product_default_size_text = shirt_product_page.get_product_default_size()
        shirt_product_page.change_product_size(expected_product_changed_size)
        observed_product_size_changed_text = shirt_product_page.get_product_default_size()

        self.assertNotEqual(expected_product_changed_size, observed_product_default_size_text,
                            f'Expected size is the same as actual on page: {self.conf_driver.current_url}')
        self.assertEqual(expected_product_changed_size, observed_product_size_changed_text,
                         f'Expected size differ from actual on page: {self.conf_driver.current_url}')