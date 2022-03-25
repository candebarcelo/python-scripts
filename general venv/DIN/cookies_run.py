from selenium import webdriver
from cookies import save_cookie

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://tigre.service-now.com')

foo = input()

save_cookie(driver, './tmp/cookie')

