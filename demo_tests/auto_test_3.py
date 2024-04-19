import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class MainTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.service = Service('/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)

    def test_demo_login(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Logowanie', title,
                         f'Expected title differs from actual for page url: {url}')

    def test_demo_accounts(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/konta.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Konta', title,
                         f'Expected title differs from actual for page url: {url}')

    def test_demo_pulpit(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/pulpit.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Pulpit', title,
                         f'Expected title differs from actual for page url: {url}')

    def test_demo_transfer(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/przelew_nowy_zew.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Przelew', title,
                         f'Expected title differs from actual for page url: {url}')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

class LoginPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.service = Service(
            '/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)

    def test_exact_text_for_login_form_header(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        login_form_header_element = driver.find_element(By.XPATH, '//*[@id="login_form"]/h1')
        login_form_header_text = login_form_header_element.text
        self.assertEqual('Wersja demonstracyjna serwisu demobank', login_form_header_text,
                         f'Expected title differs from actual title for page url: {url}')

    def test_button_dalej_is_disabled_when_login_input_is_empty(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        login_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_input_element.clear()

        login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        login_next_button_element_disabled = login_next_button_element.get_property('disabled')
        self.assertEqual(True, login_next_button_element_disabled,
                         f'Expected state of "dalej" button: True, differs from actual {login_next_button_element_disabled}, for page url: {url}')

    def test_display_error_message_when_user_submit_less_than_8_signs(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        login_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_input_element.clear()

        login_input_element.send_keys('1234567')

        hint_button_element = driver.find_element(By.XPATH, '//*[@id="login_id_container"]//*[@class="i-hint-white tooltip widget-info"]')
        hint_button_element.click()

        warning_message_element = driver.find_element(By.XPATH, '//*[@class="error"]')
        warning_message_text = warning_message_element.text
        self.assertEqual('identyfikator ma min. 8 znaków', warning_message_text,
                         f'Expected warning message differ from actual one for url: {url}')

    def test_button_dalej_respond_when_enter_8_signs_id(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        login_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_input_element.clear()
        login_text = '12345678'
        login_input_element.send_keys(login_text)

        login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        login_next_button_element.click()

        time.sleep(3)

        login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        new_login_button_text = login_next_button_element.text

        self.assertEqual('zaloguj się', new_login_button_text,
                         f'Expected login button text "zaloguj się", differ from actual {new_login_button_text}')

    def test_correct_popup_text(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        login_reminder_element = driver.find_element(By.XPATH, '//*[@id="ident_rem"]')
        login_reminder_element.click()

        time.sleep(3)

        popup_text_element = driver.find_element(By.XPATH, '//*[@class="shadowbox-content contact-popup"]/div/h2')
        popup_text_element_text = popup_text_element.text

        popup_text_element_close_button = driver.find_element(By.XPATH, '//*[@id="shadowbox"]/div/i')
        popup_text_element_close_button.click()
        self.assertEqual('ta funkcja jest niedostępna', popup_text_element_text,
                         f'Expected login button text differ from actual {popup_text_element_text}')

    def test_correct_login_from_login_etap2(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_2.html'
        driver.get(url)

        login_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_input_element.send_keys('kocur131')

        password_input_element = driver.find_element(By.XPATH, '//*[@id="login_password"]')
        password_input_element.send_keys('12345678')

        button_next_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        button_next_element.click()

        time.sleep(3)

        messages_element = driver.find_element(By.XPATH, '//*[@id="show_messages"]')
        messages_element_text = messages_element.text
        self.assertEqual('Brak wiadomości', messages_element_text,
                         f'Expected login button text differ from actual: {messages_element_text}')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()