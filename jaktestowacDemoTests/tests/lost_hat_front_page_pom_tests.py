from jaktestowacDemoTests.helpers.wrappers import screenshot_decorator
from jaktestowacDemoTests.helpers.base_test_class import BaseTestClass
from jaktestowacDemoTests.pages.front_page import FrontPage


class LostHatFrontPagePomTests(BaseTestClass):
    @screenshot_decorator
    def test_slider_presence(self):
        driver = self.conf_driver

        front_page = FrontPage(driver)
        front_page.visit()
        front_page.get_slider_size()

    @screenshot_decorator
    def test_slider_minimum_size(self):
        expected_min_height = 300
        expected_min_width = 600
        driver = self.conf_driver

        front_page = FrontPage(driver)
        front_page.visit()
        slider_size = front_page.get_slider_size()

        actual_slider_height = slider_size['height']
        actual_slider_width = slider_size['width']
        with self.subTest('Element height'):
            self.assertLess(expected_min_height, actual_slider_height,
                            f'Slider height found on page {driver.current_url} is smaller than expected {expected_min_height}px')
        with self.subTest('Element width'):
            self.assertLess(expected_min_width, actual_slider_width,
                            f'Slider width found on page {driver.current_url} is smaller than expected {expected_min_width}px')

    @screenshot_decorator
    def test_slider_contain_exact_number_of_slides(self):
        expected_number_of_slides = 3
        driver = self.conf_driver

        front_page = FrontPage(driver)
        front_page.visit()
        actual_number_of_slides = front_page.get_slider_elements_count()

        self.assertEqual(expected_number_of_slides, actual_number_of_slides,
                         f'Slides number differs for page {self.base_url}')

    @screenshot_decorator
    def test_slides_required_title_text(self):
        expected_text_included_in_slide = 'sample'
        driver = self.conf_driver

        front_page = FrontPage(driver)
        front_page.visit()
        title_elements = front_page.get_slider_titles()

        for title_element in title_elements:
            title_element_text = title_element.get_attribute("textContent")
            title_element_text_lower = title_element_text.lower()
            with self.subTest(title_element_text_lower):
                self.assertIn(expected_text_included_in_slide, title_element_text_lower,
                              f"Slides do not contain expected text for page {self.base_url}")

    @screenshot_decorator
    def test_number_of_featured_products(self):
        expected_number_of_products = 8
        driver = self.conf_driver

        front_page = FrontPage(driver)
        front_page.visit()
        actual_number_of_products = front_page.get_featured_products_count()

        self.assertEqual(expected_number_of_products, actual_number_of_products,
                         f'Products number differs for page {self.base_url}')

    @screenshot_decorator
    def test_featured_products_price_in_pln(self):
        expected_product_price_currency = 'PLN'
        driver = self.conf_driver

        front_page = FrontPage(driver)
        front_page.visit()
        product_price_elements = front_page.get_product_prices()

        for product_price_element in product_price_elements:
            price_element_text = product_price_element.get_attribute("textContent")
            with self.subTest(price_element_text):
                self.assertIn(expected_product_price_currency, price_element_text,
                               f"Expected text not found in product description for page {self.base_url}")