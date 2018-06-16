#! /usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time


valid_name = "Tadek"
valid_lastname = "kowalski"
invalid_email = "tadek.pl"
valid_password = "Abcde1234"


class RyanReg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(20)


    def test_check_reg(self):
        driver = self.driver
        driver.get("https://www.ryanair.com/pl/pl/")
        driver.maximize_window()
        time.sleep(5)
        reg_btn = driver.find_element_by_xpath('//*[@id="myryanair-auth-signup"]/a/span')
        reg_btn.click()
        time.sleep(5)
        mail_field = driver.find_element_by_xpath('//*[@id="email360"]')
        mail_field.click()
        mail_field.send_keys(invalid_email)
        pass_field = self.driver.find_element_by_xpath('//*[@id="password385"]')
        pass_field.send_keys(valid_password)
        time.sleep(5)
        reg_btn = self.driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/signup-home-form/div/div/div[2]/div/dialog-body/div[2]/signup-home-tabs/div[2]/div/div/form/div[4]/button-spinner/button')
        reg_btn.click()
        time.sleep(1)
        error_notice = self.driver.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/signup-home-form/div/div/div[2]/div/dialog-body/div[2]/signup-home-tabs/div[2]/div/div/form/div[1]/ul/li')
        self.assertEqual(error_notice.text, u'Nieprawidłowy format adresu e-mail')


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

