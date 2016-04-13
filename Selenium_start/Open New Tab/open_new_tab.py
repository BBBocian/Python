from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest

# Use send_keys(Keys.CONTROL + Keys.TAB) to switch tab in browser.

driver = webdriver.Firefox()
driver.get("http://www.allegrp.pl")
allegro = driver.current_window_handle

driver.maximize_window()

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get("http://www.google.pl")
google = driver.current_window_handle

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get("http://www.facebook.com")
facebook = driver.current_window_handle
driver.back()


'''
first_link = driver.find_element_by_xpath(".//*[@id='LinkArea:Breadcrumbs']/li[3]/a")
main_window = driver.current_window_handle

first_link.send_keys(Keys.CONTROL + Keys.RETURN)

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

driver.switch_to.window(main_window)
'''


#driver.quit()



