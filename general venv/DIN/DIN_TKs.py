from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import re

# import pickle

# read csv and convert it to a list
with open('DIN_input.csv', newline=r'') as input_file:
    reader = csv.reader(input_file)
    tk_list_of_lists = list(reader)
    tk_list = []
    for sublist in tk_list_of_lists:
        for item in sublist:
            tk_list.append(item)

# p = input('p: ')


browser = webdriver.Chrome('./chromedriver.exe')

browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
browser.get('https://tigre.service-now.com')

assert 'Sign in to your account' in browser.title
assert 'i0116' in browser.page_source
assert 'Microsoft' in browser.page_source

time.sleep(1)


# cookies = pickle.load(open("./cookies.pkl", "rb"))
# for cookie in cookies:
#     browser.add_cookie(cookie)


username_input = browser.find_element_by_id('i0116')
username_input.clear()
username_input.send_keys(' ') #enter email between ''

next_button = browser.find_element_by_id('idSIButton9')
next_button.click()

assert 'Sign in to your account' in browser.title
assert 'Enter password' in browser.page_source

time.sleep(40)

#enter p manually


assert 'ServiceNow' in browser.title
assert 'Service Management' in browser.page_source
assert 'CSC Chile' in browser.page_source

search_button = browser.find_element_by_class_name('sysparm-search-icon')
search_button.click()

search_bar = browser.find_element_by_id('sysparm_search')
search_bar.clear()

# TESTED OK UNTIL THIS POINT. for loop needed now.

for line in tk_list:
    try:
        search_bar.send_keys(line)
        search_bar.send_keys(Keys.ENTER)

        time.sleep(20)

        search_bar.clear()

        # assert line in browser.title

        # si hay un +2, etc en los docs
        plus_sign = browser.find_element_by_xpath('//*[@id="header_attachment"]/span/a/span[@class="badge"]')
        print(plus_sign)
        plus_sign.click()
        time.sleep(2)
        planilla = browser.find_elements_by_xpath("//*[contains(text(), 'esglose')]")
        planilla.click()
        time.sleep(0.5)
        din = browser.find_elements_by_xpath("//*[@class='content_editable'][contains(text(), 'Tigre')]")
        din.click()
        time.sleep(0.5)

    except: 
        pass


