__author__ = 'bocian'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui  import Select
from selenium.webdriver.common.keys import Keys
import time

baseUrl = "http://newtours.demoaut.com/"
driver = webdriver.Firefox()

underConsTitle = "Under Construction: Mercury Tours"

driver.implicitly_wait(5)

driver.get(baseUrl)
a = driver.current_window_handle
#linkElements = driver.find_elements_by_tag_name("a")

linkText = driver.find_elements_by_xpath("//a[@href]")

for value in linkText:
    a = value.text
    driver.find_element_by_link_text(a).click()
    if driver.title == underConsTitle:
        print(a + "is under construction")
    else:
        print(a + " is working")
    driver.switch_to.window(a)
#for value in linkText:
#   print(value.text)


