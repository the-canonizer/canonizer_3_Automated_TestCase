from selenium.webdriver import Keys, ActionChains
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

import sys


class CanonizerBrowsePage(Page):

    def click_browse_page_button(self):
        """
        This function is to click on the Browse link
        -> Hover to the Browse link
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        #title = self.find_element(*BrowsePageIdentifiers.TITLE)
        if self.find_element(*BrowsePageIdentifiers.BROWSE):
            self.hover(*BrowsePageIdentifiers.BROWSE)
            wait = WebDriverWait(self.driver, 5)
            #wait.until(EC.element_to_be_clickable(*BrowsePageIdentifiers.BROWSE))
            self.find_element(*BrowsePageIdentifiers.BROWSE).click()
            wait = WebDriverWait(self.driver, 5)

    def click_only_my_topics_button(self):
        self.click_browse_page_button()
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        return CanonizerBrowsePage(self.driver)

    def select_dropdown_value(self):
        self.click_browse_page_button()
        self.hover(*BrowsePageIdentifiers.NAMESPACE)
        self.find_element(*BrowsePageIdentifiers.NAMESPACE).click()
        return CanonizerBrowsePage(self.driver)

    def scroll_down(self, i):
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        action = ActionChains(self.driver)
        #i = 10
        while self.i >= 0:
            action.key_down(Keys.DOWN).perform()
            self.i = self.i - 1
            time.sleep(0.4)
    def scroll_namespaces(self):
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        action = ActionChains(self.driver)
        self.response = requests.get("https://api3.canonizer.com/api/v3/get-all-namespaces")
        self.r = self.response.json()["data"]
        self.i = len(self.r)
        #Creating list from Api.
        self.namespaces_list = []
        for self.d in self.r:
            self.data = self.d['label']
            self.namespaces_list.append(self.data)
        #Creating list from Automation.
        self.current_name_list = []
        while self.i >= 1:
            self.driver.implicitly_wait(10)
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.ENTER).perform()
            self.i = self.i - 1
            time.sleep(0.4)
            # Check
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]/input").click()
            # Uncheck
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]/input").click()
            self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]').click()
            self.current_name = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]").text
            self.current_name_list.append(self.current_name)
    def select_by_value_general(self):
        #select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        #select.select_by_value("1")
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.find_element(*BrowsePageIdentifiers.GENERAL).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_general_only_my_topics(self):
        self.select_by_value_general()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_corporations(self):
        #select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        #time.sleep(3)
        #select.select_by_value("2")
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.find_element(*BrowsePageIdentifiers.CORPORATIONS).click()
        #check = driver.find_element(By.CLASS_NAME, "ant-select-selection-item")
        #check.value_of_css_property("title")
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_corporations_only_my_topics(self):
        self.select_by_value_corporations()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_crypto_currency(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.find_element(*BrowsePageIdentifiers.CRYPTOCURRENCY).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_crypto_currency_only_my_topics(self):
        self.select_by_value_crypto_currency()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_family(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.find_element(*BrowsePageIdentifiers.FAMILY).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_family_only_my_topics(self):
        self.select_by_value_family()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_family_jesperson_oscar_f(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.find_element(*BrowsePageIdentifiers.FAMILYJESPERSON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_family_jesperson_oscar_f_only_my_topics(self):
        self.select_by_value_family_jesperson_oscar_f()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_occupy_wall_street(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.find_element(*BrowsePageIdentifiers.OCCUPYWALLSTREET).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_occupy_wall_street_only_my_topics(self):
        self.select_by_value_occupy_wall_street()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.find_element(*BrowsePageIdentifiers.ORGANIZATION).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)


    def select_by_value_organizations_only_my_topics(self):
        self.select_by_value_organizations()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations_canonizer(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONCANONIZER).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_canonizer_only_my_topics(self):
        self.select_by_value_organizations_canonizer()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations_canonizer_help(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(8)
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONCANONIZERHELP).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_canonizer_help_only_my_topics(self):
        self.select_by_value_organizations_canonizer_help()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations_mta(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(9)
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONMTA).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_mta_only_my_topics(self):
        self.select_by_value_organizations_mta()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations_tv07(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(9)
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONTV07).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_tv07_only_my_topics(self):
        self.select_by_value_organizations_tv07()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations_wta(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(10)
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONWTA).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_wta_only_my_topics(self):
        self.select_by_value_organizations_wta()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_personal_attributes(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(15)
        self.find_element(*BrowsePageIdentifiers.PERSONALATTRIBUTE).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_personal_attributes_only_my_topics(self):
        self.select_by_value_personal_attributes()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_personal_reputations(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(15)
        self.find_element(*BrowsePageIdentifiers.PERSONALREPUTATION).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_personal_reputations_only_my_topics(self):
        self.select_by_value_personal_reputations()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_professional_services(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(15)
        self.find_element(*BrowsePageIdentifiers.PROFESSIONALSERVICES).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_professional_services_only_my_topics(self):
        self.select_by_value_professional_services()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sandbox(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(15)
        self.find_element(*BrowsePageIdentifiers.SANDBOX).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sandbox_only_my_topics(self):
        self.select_by_value_sandbox()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_terminology(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(15)
        self.find_element(*BrowsePageIdentifiers.TERMINOLOGY).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_terminology_only_my_topics(self):
        self.select_by_value_terminology()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_www(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(20)
        self.find_element(*BrowsePageIdentifiers.WWW).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_www_only_my_topics(self):
        self.select_by_value_www()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sandbox_testing(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(20)
        self.find_element(*BrowsePageIdentifiers.SANDBOXTESTING).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sandbox_testing_only_my_topics(self):
        self.select_by_value_sandbox_testing()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_crypto_currency_ethereum(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(25)
        self.find_element(*BrowsePageIdentifiers.CRYPTOCURRENCYETHEREUM).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_crypto_currency_ethereum_only_my_topics(self):
        self.select_by_value_crypto_currency_ethereum()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_void(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(25)
        self.find_element(*BrowsePageIdentifiers.VOID).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_void_only_my_topics(self):
        self.select_by_value_void()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_mormon_canon_project(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(25)
        self.find_element(*BrowsePageIdentifiers.MORMONCANONPROJECT).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_mormon_canon_project_only_my_topics(self):
        self.select_by_value_mormon_canon_project()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_united_utah_party(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(25)
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONUNITEDUTAHPARTY).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_united_utah_party_only_my_topics(self):
        self.select_by_value_organizations_united_utah_party()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(25)
        self.find_element(*BrowsePageIdentifiers.GOVERNMENT).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government_only_my_topics(self):
        self.select_by_value_government()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government_sandy_city(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(25)
        self.find_element(*BrowsePageIdentifiers.GOVERNMENTSANDYCITY).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government_sandy_city_only_my_topics(self):
        self.select_by_value_government_sandy_city()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sports(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(25)
        self.find_element(*BrowsePageIdentifiers.SPORT).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_sports_only_my_topics(self):
        self.select_by_value_sports()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_sports_sbcl(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(25)
        self.find_element(*BrowsePageIdentifiers.SPORTSBCL).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_sports_sbcl_only_my_topics(self):
        self.select_by_value_sports_sbcl()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_plateform_of_the_people(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(30)
        self.find_element(*BrowsePageIdentifiers.PLATEFORMOFTHEPEOPLE).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_plateform_of_the_people_only_my_topics(self):
        self.select_by_plateform_of_the_people()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(30)
        self.find_element(*BrowsePageIdentifiers.FICTION).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_fiction_only_my_topics(self):
        self.select_by_value_fiction()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_fiction_lord_of_the_ring(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(30)
        self.find_element(*BrowsePageIdentifiers.FICTIONLORDOFTHERINGS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction_lord_of_the_ring_only_my_topics(self):
        self.select_by_value_fiction_lord_of_the_ring()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction_star_wars(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(30)
        self.find_element(*BrowsePageIdentifiers.FICTIONSTARWARS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction_star_wars_only_my_topics(self):
        self.select_by_value_fiction_star_wars()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction_world_of_warcraft(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(30)
        self.find_element(*BrowsePageIdentifiers.FICTIONWORLDOFWARCRAFT).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction_world_of_warcraft_only_my_topics(self):
        self.select_by_value_fiction_world_of_warcraft()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_by_value_all(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_down(31)
        self.find_element(*BrowsePageIdentifiers.ALL).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)

    def select_by_value_all_only_my_topics(self):
        self.select_by_value_all()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH,
                 '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        return CanonizerBrowsePage(self.driver)
    def select_all_namespaces(self):
        self.driver.implicitly_wait(10)
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.scroll_namespaces()
        return CanonizerBrowsePage(self.driver)
     def select_all_namespaces(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.driver.implicitly_wait(10)
        action = ActionChains(driver)
        n = 40
        i = 1
        while n >= 0:
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.ENTER).perform()
            n = n - 1
            self.driver.implicitly_wait(10)
            # Check
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]/input").click()
            # Uncheck
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]/input").click()
            self.select_dropdown_value()

