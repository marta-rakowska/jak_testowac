import time
from selenium.webdriver.support.events import AbstractEventListener

class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        screenshot_path = rf"testResults/noSuchElementException_{time.time()}.png"
        driver.get_screenshot_as_file(screenshot_path)
        print(f"Screenshot saved as {screenshot_path}")