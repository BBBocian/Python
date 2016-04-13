__author__ = 'bocian'
from selenium import webdriver
from selenium.webdriver.support.ui  import WebDriverWait

import unittest

class wp_login_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.facebook.com')

    def test_get_attribute_from_web(self):
        driver = self.driver

        emailFieldID = 'email'
        emailFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailFieldID))

        # pobieranie atrybutu
        att = emailFieldElement.get_attribute('class')
        print(att)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()