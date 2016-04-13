__author__ = 'bocian'
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

import unittest
import time



class SelectOptionTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com")

    def test_SelectOption(self):
        driver = self.driver

        # obiekt listy rozwijanej z miesiacami
        monthDropDownID = "month"

        # oczekiwanie na poprawne wyswietlenie obiektu
        monthDropDownElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(monthDropDownID))

        # wybranie elementu cze - czerwiec

        # Select(monthDropDownElement).select_by_visible_text("cze")
        # Select(monthDropDownElement).select_by_index(2)
        # Select(monthDropDownElement).select_by_value(10)


        # przesówa o jeden w dół
        # monthDropDownElement.send_keys(Keys.ARROW_DOWN)

        # time sleep w celu zauwazenie roznicy - wybranego elementu
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()