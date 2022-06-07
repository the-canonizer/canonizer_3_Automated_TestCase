from CanonizerBase import Page
from Identifiers import ChangePasswordIdentifiers
from Identifiers import HomePageIdentifiers
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from datetime import datetime
from time import time
import time


class CanonizerChangePassword(Page):

    def click_account_setting(self,email, password):
        self.find_element(*HomePageIdentifiers.LOGIN).click()
        self.find_element(*HomePageIdentifiers.EMAILLOGIN).send_keys(email)
        self.find_element(*HomePageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*HomePageIdentifiers.LOGIN_SUBMIT).click()
        time.sleep(7)
        self.find_element(*HomePageIdentifiers.ACCOUNT_HEADER).click()
        time.sleep(3)
        return CanonizerChangePassword(self.driver)



