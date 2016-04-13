from selenium import webdriver
#import Kyes provides keys in the keyboard like RETURN,F1,ALT etc.
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()                                # instance of Firefox WebDriver
driver.get("http://www.python.org")                         # driver.get method will navigate to the page given by URL
                                                            # WebDriver will wait until the page has fully loaded
assert "Python" in driver.title                             # assertion to confirm that title has "python" word in it

elem = driver.find_element_by_name('q')                     # method to find element by argument: name="q"

elem.send_keys("pycon")                                   # sending keys to elem element ( founded above )

elem.send_keys(Keys.RETURN)                                 # next send RETURN


assert "No results found." not in driver.page_source        # assertion to ensure that some results are found


driver.close()                                              # close one tab, quit() - exit from browser


