from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://sliding.toys/mystic-square/8-puzzle/daily/')

title = driver.title
print(title)
assert title == '8 puzzle | Sliding Toys'
driver.quit()

