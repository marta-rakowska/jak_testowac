import time
from selenium.webdriver.common.by import By


def wait_for_elements(driver, xpath, max_seconds_to_wait=5):
    """Checking every second if list of elements under specified xpath is greater than 0

        :param driver: webdriver instance
        :param xpath: xpath of web element
        :param max_seconds_to_wait: maximum time in seconds to wait for element (default: 5)
        :return: list of found elements
        """

    for seconds in range(max_seconds_to_wait):
        elements = driver.find_elements(By.XPATH, xpath)
        print(f'Total waiting: {seconds}s')
        if len(elements) > 0:
            print('Element found')
            # return elements
        if seconds == (max_seconds_to_wait - 1):
            print('End of wait')
            assert len(elements) > 0, f'Element for xpath {xpath} not found in time of {seconds}s'
        time.sleep(1)
