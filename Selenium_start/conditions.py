__author__ = 'bocian'

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.python.org")


# isEnabled() is used when you want to verify whether a certain element is enabled or not before executing a command.
searchFieldId = "id-search-field"
searchFieldElement = driver.find_element_by_id(searchFieldId)

if(searchFieldElement.is_enabled()):
    searchFieldElement.send_keys("pycon")

# isDisplayed() is used when you want to verify whether a certain element is displayed or not before executing a command.

if(searchFieldElement.is_displayed()):
    searchFieldElement.send_keys("a")

# isSelected() is used when you want to verify whether a certain check box, radio button, or option in a drop-down
# box is selected. It does not work on other elements.