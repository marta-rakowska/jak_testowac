from jaktestowacDemoTests.helpers.wrappers import screenshot_decorator
from jaktestowacDemoTests.helpers.base_test_class import BaseTestClass
import jaktestowacDemoTests.config_reader

from jaktestowacDemoTests.pages.login_page import LoginPage


class LostHatLoginPagePomTests(BaseTestClass):
    @screenshot_decorator
    def test_login_text_header(self):
        expected_text = 'Log in to your account'

        login_page = LoginPage(self.conf_driver)
        login_page.visit()
        header_text = login_page.get_header()
        self.assertEqual(expected_text, header_text,
                         f'Expected text differ from actual on page: {self.conf_driver.current_url}')

    @screenshot_decorator
    def test_correct_login(self):
        config = jaktestowacDemoTests.config_reader.load()
        expected_text = config['correct_user_fullname']
        user_email = config['correct_user_email']
        user_pass = config['correct_user_pass']

        login_page = LoginPage(self.conf_driver)
        login_page.visit()
        front_page = login_page.log_in(user_email, user_pass)
        self.assertEqual(expected_text, front_page.get_username(),
                         f'Expected text differs from actual on page: {self.conf_driver.current_url}')

    @screenshot_decorator
    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'

        login_page = LoginPage(self.conf_driver)
        login_page.visit()
        login_page = login_page.log_in_invalid(user_email, user_pass)
        self.assertEqual(expected_text, login_page.get_error(),
                         f'Expected text differs from actual on page: {self.conf_driver.current_url}')
