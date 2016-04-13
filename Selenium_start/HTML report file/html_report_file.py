# -*- coding: utf-8 -*-
'''
Test zaczerpniety z facebook_login.py

Dokonane zmiany: mozliwosc wygenerowania wynikow przebiegu testu za pomoca HTML Test Runner
pobranego ze strony http://tungwaiyip.info/software/HTMLTestRunner.html. Aby wygenerowac plik HTML nalezy
umiescic plik html_report_file.py do filderu z projekem, nastepnie import HTMLTestRunner, zmienic wywolanie
if name = main --> unittest.main() na HTMLTestRunner. Wywolanie z command line: python nazwa_pliku.py > ReportHtml.html

'''
__author__ = 'bocian'

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

import HTMLTestRunner

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com")

    def test_login(self):

        driver = self.driver
        facebookUsername = "szymciunio@gmail.com"
        facebookPassword = "PASSWORD"

        emailFieldID =      "email"
        passFieldID =       "pass"
        loginButtonXpath =  "//input[@value='Zaloguj się']"
        fbLogoXpath =       "//a[contains(@href,'https://www.facebook.com/?ref=logo')][1]"

        # Web driver bedzie czekal maksymalnie 10 sek na wyswietlenie emailField, jesli sie wyswietli to zapisze go do
        # FieldElement, jeśli nie, zwróci TimeOut exception
        emailFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath((loginButtonXpath)))

        # czysci pole nazwy uzytkownika i wstawia tam dane ze zmiennej facebookUsername
        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)

        # czysci pole hasla i wstawia tam dane ze zmiennej facebookPassword
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)

        # klikniecie przycisku logowania
        loginButtonElement.click()

        # oczekiwanie na wyswietlenie sie loga fb po zalogowaniu
        WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath((fbLogoXpath)))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    HTMLTestRunner.main()