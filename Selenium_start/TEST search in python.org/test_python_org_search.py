__author__ = 'bocian'
from selenium import webdriver
#import Kyes provides keys in the keyboard like RETURN,F1,ALT etc.
from selenium.webdriver.common.keys import Keys
import unittest

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):                                        # setUp is part of initialization, this method will get
                                                            # called before every test function
        self.driver = webdriver.Firefox()                   # instance of Firefox WebDriver


    def test_search_in_python_org(self):
        driver = self.driver                                # local reference to the driver object created in setUp meth
        driver.get("http://www.python.org")                 # driver.get method will navigate to the page given by URL
                                                            # WebDriver will wait until the page has fully loaded

        self.assertIn("Python",driver.title)                # assertion to confirm that title has "python" word in it


        elem = driver.find_element_by_name('q')             # method to find element by argument: name="q"

        elem.send_keys("pycon")                             # sending keys to elem element ( founded above )

        elem.send_keys(Keys.RETURN)                         # next send RETURN


        self.assertNotIn("No results found.", driver.page_source)  # assertion to ensure that some results are found

    def tearDown(self):                                     # tearDown is pleace to do all cleanup actions,
                                                            # will get called after test method
        self.driver.quit()                                  # close one tab, quit() - exit from browser


if __name__ == '__main__':
    unittest.main()



