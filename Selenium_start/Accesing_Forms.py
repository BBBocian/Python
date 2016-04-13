__author__ = 'bocian'
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("http://www.nngroup.com/articles/checkboxes-vs-radio-buttons/")

# CHECKBOXES

checkboxPermissionName = 'permission'

checkboxPermissionElement = driver.find_element_by_name(checkboxPermissionName)

for i in range(0,5):

    checkboxPermissionElement.click()
    print(checkboxPermissionElement.is_selected())

# LINKS

# by partial link
driver.find_element_by_partial_link_text("Supporting").click()

# by link - ??? does not work
#driver.find_element_by_link_text("Supporting Mobile Navigation in Spite of a Hamburger Menu")

# DROPDOWNS - it was in another file!


#Selecting Items in a Multiple SELECT element

driver.get("http://jsbin.com/osebed/2")

fruitsId = "fruits"

select = Select(driver.find_element_by_id(fruitsId))

dropoptions = driver.find_elements_by_tag_name("option")

for values in dropoptions:
    print(values.get_attribute("value"))