__author__ = 'bocian'
from selenium import webdriver
from selenium.webdriver.support.ui  import WebDriverWait

import unittest

class wp_login_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://poczta.wp.pl')

    def test_wp_login(self):
        driver = self.driver
        wp_username = 'diegos17'
        wp_password = 'PASSWORD'

        # pobiera kazdy element ze strony za pomoca xpath - odpowiednio: pole email, password, przycisk zaloguj i
        # przycisk odbierz - bedziemy sprawdzac, czy wieswietla sie po zalogowaniu

        emailFieldXpath = "//input[@name='login_username']"
        passFieldXpath =  "//input[@name='login_password']"
        loginButtonXpath = "//input[@value='zaloguj']"
        odbierzButtonXpath = ".//*[@id='bxPanelTopBody']/div/div[1]/a[1]"

        # po wlaczeniu strony oczekuje sie wyswietlenia sie elementow, jesli nie wyswietla sie w 10 sekund - TimeOutExc.

        emailFieldElement   = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(emailFieldXpath))
        passFieldElement    = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(passFieldXpath))
        loginButtonElement  = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        # czyszczenie pola email, wpisanie do niego danych
        emailFieldElement.clear()
        emailFieldElement.send_keys(wp_username)

        # czyszczenie pola password, wpisanie do niego danych
        passFieldElement.clear()
        passFieldElement.send_keys(wp_password)

        # klikniecie przycisku zaloguj
        loginButtonElement.click()

        #oczekiwanie na wyswietlenie sie danego elementu w celu sprawdzenia poprawnosci zalogowania
        WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(odbierzButtonXpath))


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()