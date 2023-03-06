import random

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
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys
from Config import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import *


class CanonizerSupportValue(Page):


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
        #title = self.find_element(*BrowsePageIdentifiers.TITLE)
        #print(title)
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
        return CanonizerSupportValue(self.driver)


    def scroll_down(self):
        self.driver.implicitly_wait(20)
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        action = ActionChains(self.driver)
        # self.response = requests.get("https://api3.canonizer.com/api/v3/get-all-namespaces")
        # self.r = self.response.json()["data"]
        # print(self.r)
        # self.i = len(self.r)
        self.i = 100
        self.current_name_list = []

        while self.i >= 1:
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.ENTER).perform()
            print("element selected")
            print(self.i)
            self.i = self.i - 1
            time.sleep(0.4)

            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div[3]/div/div[2]/div/div/div/div/span[2]').click()
            self.current_name = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div[3]/div/div[2]/div/div/div/div/span[2]").text
            if self.current_name == "/sandbox testing/":
                action.key_down(Keys.ENTER).perform()
                break

            #time.sleep(0.4)


    def support_value_new_topic(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://canonizer3.canonizer.com/browse")
        print("Getting Dropdown")
        self.create_new_topic()
        return CanonizerSupportValue(self.driver)

    def create_new_topic(self):
        self.driver.implicitly_wait(30)
        self.n = random.randint(0, 10000)
        self.n = str(self.n)
        print(self.n)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/aside/div/div[1]/button/span").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div[2]/form/div[1]/div[2]/div/div/div[2]/div/div/textarea").send_keys("test_new_topic1")
        self.topic = ("test_new_topic1" + self.n)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div/input").send_keys(self.topic)
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div[3]/div/div[2]/div/div/div/div/span[2]"):
            print("Found")
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div[3]/div/div[2]/div/div/div/div/span[2]").click()
            print("Clicked on namespace")
        else:
            print("Not Found")
        self.scroll_down()
        self.driver.find_element(By.ID, "create-topic-btn").click()
        self.create_camp()
        return CanonizerSupportValue(self.driver)
    
    def create_camp(self):
        # Create Camp
        # Click on Plus Icon
        self.n = random.randint(0, 10000)
        self.n = str(self.n)
        print(self.n)
        self.driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div/span[2]/span").click()
        # CLicking on Start CAmp Here
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[2]/span[3]/span").click()
        print("Creating Camp")
        self.camp = ("camp_new1" + self.n)
        self.driver.find_element(By.ID, "create_new_camp_camp_name").send_keys(self.camp)
        self.driver.find_element(By.ID, "create_new_camp_key_words").send_keys(self.camp)
        self.driver.find_element(By.ID, "create_new_camp_note").send_keys(self.camp)
        self.driver.find_element(By.ID, "create_new_camp_camp_about_url").send_keys("https://www.google.com")
        self.driver.find_element(By.ID, "camp-about-nick-dropdown").click()
        self.driver.find_element(By.ID, "camp-about-nick-301").click()

        self.driver.find_element(By.ID, "crate-camp-btn").click()
        #Ceate New Camp
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[2]/span[2]/span").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[3]/span[3]/span").click()

        self.camp2= ("camp_new2"+ self.n)
        self.driver.find_element(By.ID, "create_new_camp_camp_name").send_keys(self.camp2)
        self.driver.find_element(By.ID, "create_new_camp_key_words").send_keys(self.camp2)
        self.driver.find_element(By.ID, "create_new_camp_note").send_keys(self.camp2)
        self.driver.find_element(By.ID, "create_new_camp_camp_about_url").send_keys("https://www.google.com")
        self.driver.find_element(By.ID, "camp-about-nick-dropdown").click()
        self.driver.find_element(By.ID, "camp-about-nick-301").click()
        self.driver.find_element(By.ID, "crate-camp-btn").click()  
        
        #Support first camp
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[2]/span[3]/span/div/div/span[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[5]/div/div[2]/div/div[2]/a/button/span").click()
        self.driver.find_element(By.ID, "uploadBtn").click()
        return CanonizerSupportValue(self.driver)
