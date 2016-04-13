__author__ = 'bocian'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time

class test_web_title(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.guru99.com")

    def test_title(self):
        self.assertEqual(self.driver.title,"Meet Guru99")



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()