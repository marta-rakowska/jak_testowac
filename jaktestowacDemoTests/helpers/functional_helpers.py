from selenium.webdriver.common.by import By


def user_login(driver, user_email, user_pass):
    """Login user to website using given email and password

    :param driver: webdriver instance
    :param user_email: user email
    :param user_pass: user password
    :return: None
    """
    login_input_element = driver.find_element(By.XPATH, '//*[@type="email"]')
    login_input_element.send_keys(user_email)

    password_input_element = driver.find_element(By.XPATH, '//*[@type="password"]')
    password_input_element.send_keys(user_pass)

    button_next_element = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
    button_next_element.click()