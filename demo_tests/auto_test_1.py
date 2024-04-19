from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/Users/martarakowska/Desktop/podstawy_testow_automatycznych_w_selenium_i_python/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
# driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
driver.get('https://demobank.jaktestowac.pl/logowanie_prod.html')

title = driver.title
print(title)
# assert title == 'Demobank - Bankowość Internetowa - Logowanie'
assert title == 'Demobank - Strona główna - Logowanie'
driver.quit()


