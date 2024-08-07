from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from jaktestowacDemoTests.helpers import operational_helpers as oh


class ProductPage():
    def __init__(self, driver):
        self.url = None # cause there is no empty ProductPage
        self.driver = driver
        self.product_name_xpath = '//*[@class="col-md-6"]//*[@itemprop="name"]'
        self.product_price_xpath = '//*[@class="current-price"]//*[@itemprop="price"]'
        self.product_size_select_xpath = '//*[@id="group_1"]'
        self.shopping_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        self.confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'
        self.continue_shopping_button_xpath = '//*[@class="btn btn-secondary"]'
        self.cart_products_count_xpath = './/*[@class="cart-products-count"]'

    def visit(self):
        self.driver.get(self.url)
        return self

    def get_product_name(self):
        element = self.driver.find_element(By.XPATH, self.product_name_xpath)
        return element.text

    def get_product_price(self):
        element = self.driver.find_element(By.XPATH, self.product_price_xpath)
        return element.text

    def get_product_default_size(self):
        product_size_select_element = self.driver.find_element(By.XPATH, self.product_size_select_xpath)
        product_size_select = Select(product_size_select_element)
        return product_size_select.first_selected_option.text

    def change_product_size(self, new_size):
        product_size_select_element = self.driver.find_element(By.XPATH, self.product_size_select_xpath)
        product_size_select = Select(product_size_select_element)
        product_size_select.select_by_visible_text(new_size)
        return self

    def add_item_and_get_confirmation_message(self):
        shopping_cart_button_element = self.driver.find_element(By.XPATH, self.shopping_cart_button_xpath)
        shopping_cart_button_element.click()

        confirmation_modal_element = oh.visibility_of_element_wait(self.driver, self.confirmation_modal_title_xpath)
        return confirmation_modal_element.text

    def add_item_to_cart(self):
        shopping_cart_button_element = self.driver.find_element(By.XPATH, self.shopping_cart_button_xpath)
        shopping_cart_button_element.click()
        oh.visibility_of_element_wait(self.driver, self.confirmation_modal_title_xpath)
        continue_shopping_button_element = self.driver.find_element(By.XPATH, self.continue_shopping_button_xpath)
        continue_shopping_button_element.click()
        return self

    def get_items_count(self):
        cart_products_count_element = oh.visibility_of_element_wait(self.driver, self.cart_products_count_xpath)
        return cart_products_count_element.text