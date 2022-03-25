# #option 1
# import pickle

# def save_cookie(driver, path):
#     with open(path, 'wb') as filehandler:
#         pickle.dump(driver.get_cookies(), filehandler)

# def load_cookie(driver, path):
#     with open(path, 'rb') as cookiesfile:
#         cookies = pickle.load(cookiesfile)
#         for cookie in cookies:
#             driver.add_cookie(cookie)


#option 2
import pickle
import selenium.webdriver

driver = selenium.webdriver.Chrome('./chromedriver.exe')
driver.get("https://tigre.service-now.com")
foo = input()
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))


# #Load cookie -> paste in code
# import pickle
# import selenium.webdriver

# driver = selenium.webdriver.Firefox()
# driver.get("http://www.google.com")
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)