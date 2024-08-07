import jaktestowacDemoTests.config_reader
from jaktestowacDemoTests.pages.category_page import CategoryPage


class ArtCategoryPage(CategoryPage):
    def __init__(self, driver):
        super().__init__(driver)
        config = jaktestowacDemoTests.config_reader.load()
        self.url = config['base_url'] + '9-art'