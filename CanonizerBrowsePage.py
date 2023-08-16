#from selenium.webdriver import Keys, ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from selenium.common.exceptions import TimeoutException
from CanonizerBase import Page
from Identifiers import BrowsePageIdentifiers
from selenium.webdriver.support.ui import Select
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

import sys


class CanonizerBrowsePage(Page):

    def driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def click_browse_page_button(self):
        """
        This function is to click on the Browse link
        -> Hover to the Browse link
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        self.driver.implicitly_wait(10)
        if self.find_element(*BrowsePageIdentifiers.BROWSE):
            self.hover(*BrowsePageIdentifiers.BROWSE)
            self.find_element(*BrowsePageIdentifiers.BROWSE).click()
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "topicsList_head__IooBi topicsList_browsePage__cb2G_")))

    def click_only_my_topics_button(self):
        self.click_browse_page_button()
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        return CanonizerBrowsePage(self.driver)

    def select_dropdown_value(self):
        self.driver.implicitly_wait(20)
        self.click_browse_page_button()
        self.hover(*BrowsePageIdentifiers.NAMESPACE)
        self.find_element(*BrowsePageIdentifiers.NAMESPACE).click()
        return CanonizerBrowsePage(self.driver)

    def scroll_sandbox(self):
        print("came in scroll down")
        self.driver.implicitly_wait(20)
        action = ActionChains(self.driver)

        self.i = 100
        self.current_name_list = []

        while self.i >= 1:
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.ENTER).perform()
            print(self.i)
            self.i = self.i - 1
            time.sleep(0.4)
            self.current_name = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/span[2]").text
            if self.current_name == "sandbox testing":
                time.sleep(10)
                break
    def scroll_namespaces(self):
        self.driver.implicitly_wait(20)
        action = ActionChains(self.driver)
        self.i = 1000
        self.current_name_list = []

        while self.i >= 1:
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.ENTER).perform()
            self.i = self.i - 1
            time.sleep(0.4)
            # Check
            self.driver.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
            # Uncheck
            self.driver.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()

            self.driver.find_element(*BrowsePageIdentifiers.NAMESPACE).click()
            self.current_name = self.driver.find_element(*BrowsePageIdentifiers.SELECTED_TITLE).text
            if self.current_name == "All":
               self.current_name_list.append(self.current_name)
               break
            self.current_name_list.append(self.current_name)

    def select_all_namespaces(self):
        self.driver.implicitly_wait(20)
        self.click_browse_page_button()
        if self.driver.find_element(*BrowsePageIdentifiers.NAMESPACE):
            self.driver.find_element(*BrowsePageIdentifiers.NAMESPACE).click()
            self.scroll_namespaces()
        else:
            print("Not Found")
        return CanonizerBrowsePage(self.driver)
    def search_archived_camp(self):
        self.driver.implicitly_wait(20)
        if self.driver.find_element(By.ID, "name-space-dropdown"):
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div").click()
            self.scroll_sandbox()
        else:
            print("Not Found")

        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/aside/div/div/div[1]/div[2]/div/div[6]/div/label/span[1]/input").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/ul/li[1]/a/span[1]").click()
        return CanonizerBrowsePage(self.driver)
