import jaktestowacDemoTests.config_reader
from jaktestowacDemoTests.pages.product_page import ProductPage


class ShirtProductPage(ProductPage):
    def __init__(self, driver):
        super().__init__(driver)
        config = jaktestowacDemoTests.config_reader.load()
        self.url = config['base_url'] + 'men/1-4-hummingbird-printed-t-shirt.html'