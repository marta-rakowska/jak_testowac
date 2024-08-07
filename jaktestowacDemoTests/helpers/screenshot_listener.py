import time
import allure
import os
from allure_commons.types import AttachmentType
from selenium.webdriver.support.events import AbstractEventListener

class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        pycharm_debugger_exceptions = [
            "'WebElement' object has no attribute '__len__'",
            "'WebDriver' object has no attribute '__len__'",
            "'WebDriver' object has no attribute 'shape'",
            "'WebElement' object has no attribute 'shape'"
        ]
        if str(exception) not in pycharm_debugger_exceptions:
            make_screenshot(driver, 'driver')


def make_screenshot(driver, producer):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    screenshot_path = rf"{dir_path}/../testResults/{producer}_exception_{time.time()}.png"
    driver.get_screenshot_as_file(screenshot_path)
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    print(f"Screenshot saved as {screenshot_path}")

