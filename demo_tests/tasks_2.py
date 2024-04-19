import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.service = Service('/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)

    def test_home(self):
        driver = self.driver
        driver.get('https://sweetsoundtrack.com')
        title = driver.title
        print(title)
        assert title == 'Songs from movies'

    def test_movie_directory(self):
        driver = self.driver
        driver.get('https://sweetsoundtrack.com/MovieDirectory')
        title = driver.title
        print(title)
        assert title == 'Movie Directory'

    def test_artist_directory(self):
        driver = self.driver
        driver.get('https://sweetsoundtrack.com/ArtistDirectory')
        title = driver.title
        print(title)
        assert title == 'Artist Directory'

    @classmethod
    def tearDownClass(self):
        self.driver.quit()