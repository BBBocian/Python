__author__ = 'bocian'

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://jsbin.com/usidix/1")

driver.maximize_window()

driver.find_element_by_xpath("html/body/input").click()   #button

text_message = driver.switch_to.alert.text                # saving data from alert to string

print(text_message)