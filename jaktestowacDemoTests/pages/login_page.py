# from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from jaktestowacDemoTests.pages import front_page


class LoginPage:
    def __init__(self, driver):
        self.url = 'https://autodemo.testoneo.com/en/login'
        self.driver = driver
        self.header_xpath = '//header[@class="page-header"]'
        self.error_xpath = '//*[@class="alert alert-danger"]'
        self.email_xpath = '//*[@type="email"]'
        self.password_xpath = '//*[@type="password"]'
        self.login_button_xpath = '//*[@id="submit-login"]'

    def visit(self):
        self.driver.get(self.url)
        return self

    def get_header(self):
        element = self.driver.find_element(By.XPATH, self.header_xpath)
        return element.text

    def get_error(self):
        element = self.driver.find_element(By.XPATH, self.error_xpath)
        return element.text

    def enter_email(self, user_email):
        # finding login input box and sending value
        login_input_element = self.driver.find_element(By.XPATH, self.email_xpath)
        login_input_element.send_keys(user_email)
        return self

    def enter_password(self, user_pass):
        # finding password input box and sending value
        login_input_element = self.driver.find_element(By.XPATH, self.password_xpath)
        login_input_element.send_keys(user_pass)
        return self

    def click_login_button(self):
        # finding button 'SIGN IN'
        button_next_element = self.driver.find_element(By.XPATH, self.login_button_xpath)
        button_next_element.click()
        return self

    def log_in(self, user_email, user_pass):
        self.enter_email(user_email)
        self.enter_password(user_pass)
        self.click_login_button()
        return front_page.FrontPage(self.driver)

    def log_in_invalid(self, user_email, user_pass):
        self.enter_email(user_email)
        self.enter_password(user_pass)
        self.click_login_button()
        return self


