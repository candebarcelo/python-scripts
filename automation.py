import time
from selenium import webdriver


chrome_browser = webdriver.Chrome('./chromedriver.exe')


chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')


time.sleep(3) # waits for 3 seconds
popup_close_button = chrome_browser.find_element_by_class_name('at4-close')
popup_close_button.click() # close the pop-up

time.sleep(1)
assert 'Selenium Easy Demo' in chrome_browser.title # check if we're on the right website.
show_message_button = chrome_browser.find_element_by_class_name('btn-default') # find this button by class.
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source # check if this text exists in the WHOLE PAGE (p_source).

# this part can be done with either of these: u can find the button by its id or by its css selector.
# (its design properties. it's usually in the class. this time it's btn).
user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn') # the # means it's an id.
                                                       # this checks for btn items inside the get-input id.

user_message.clear() # clear() clears the input box, in case there's a saved value.
user_message.send_keys('I\'M THE BEST. KOFAL ROCKS.') # send_keys writes this.

show_message_button.click() # click() clicks on something (the button).
output_message = chrome_browser.find_element_by_id('display') # find your output.

assert 'I\'M THE BEST. KOFAL ROCKS.' in output_message.text # check the output is correct, else error out.

#chrome_browser.close() # this is kinda buggy, so u should call it twice. closes the window.
#chrome_browser.quit() # closes the entire driver, closes all instances opened by it.
