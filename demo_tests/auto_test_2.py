import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class MainTests(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(self):
        self.service = Service('/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)

    def test_demo_login(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
        title = driver.title
        print(title)
        assert title == 'Demobank - Bankowość Internetowa - Logowanie'

    def test_demo_accounts(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/konta.html')
        title = driver.title
        print(title)
        assert title == 'Demobank - Bankowość Internetowa - Konta'

    def test_demo_pulpit(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/pulpit.html')
        title = driver.title
        print(title)
        assert title == 'Demobank - Bankowość Internetowa - Pulpit'

    def test_demo_transfer(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/przelew_nowy_zew.html')
        title = driver.title
        print(title)
        assert title == 'Demobank - Bankowość Internetowa - Przelew'

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

