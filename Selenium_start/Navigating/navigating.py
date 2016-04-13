from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
import time

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_navigation_elements(self):
        driver = self.driver
        self.driver.get("https://www.facebook.com")


        # Filling in forms : choosing element from drag down, by index, value, visible text

        dayDropDownXpath = "//*[@id='day']"
        monthDropDownID = "month"
        yearDropDownID = "year"

        selectDayElement = Select(driver.find_element_by_xpath(dayDropDownXpath))
        selectMonthElement = Select(driver.find_element_by_id(monthDropDownID))
        selectYearElement = Select(driver.find_element_by_id(yearDropDownID))

        selectDayElement.select_by_visible_text("6")
        selectMonthElement.select_by_index(6)
        selectYearElement.select_by_value("1990")

        # clicking a button - Register button

        registerButtonXpath = "//*[@id='u_0_i']"
        registerButtonElement = driver.find_element_by_xpath(registerButtonXpath)
        registerButtonElement.click()

        # Drag and drop
        '''
        element = driver.find_element_by_name("source")
        target = driver.find_element_by_name("target")

        from selenium.webdriver import ActionChains
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(element, target).perform()
        '''

        print(driver.current_window_handle)



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()