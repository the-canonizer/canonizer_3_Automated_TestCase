import random

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
from Identifiers import *
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
        action = ActionChains(self.driver)
        self.i = 1000

        while self.i >= 1:
            action.key_down(Keys.DOWN).perform()
            action.key_down(Keys.ENTER).perform()
            print("element selected")
            print(self.i)
            self.i = self.i - 1
            time.sleep(0.4)
            self.current_name = self.driver.find_element(*CreateTopicIdentifiers.SELECTED_TITLE).text
            if self.current_name == "sandbox testing":
                print("Got Sandbox")
                print(self.current_name)
                time.sleep(10)
                break

    def support_value_new_topic(self):
        self.driver.implicitly_wait(30)
        self.driver.get("https://canonizer3.canonizer.com/browse")
        print("Getting Dropdown")
        self.create_new_topic()
        return CanonizerSupportValue(self.driver)

    def create_new_topic(self):
        self.driver.implicitly_wait(30)
        self.n = random.randint(0, 100000)
        self.n = str(self.n)
        print(self.n)
        self.driver.find_element(*SupportValueIdentifiers.CREATE_NEW_TOPIC).click()
        self.driver.find_element(*SupportValueIdentifiers.EDIT_SUMMARY).send_keys("test_new_topic1")

        self.topic = ("test_new_topic1" + self.n)
        self.driver.find_element(*SupportValueIdentifiers.TOPIC_NAME).send_keys(self.topic)

        if self.driver.find_element(*SupportValueIdentifiers.NAMESPACE):
            print("Found")
            self.driver.find_element(*SupportValueIdentifiers.NAMESPACE).click()
            print("Clicked on namespace")
        else:
            print("Not Found")
        self.scroll_down()
        print("Testing is here")
        self.driver.find_element(*SupportValueIdentifiers.CREATE_TOPIC_BUTTON).click()
        self.create_camp()

    def create_camp(self):
        # Create Camp
        # Click on Plus Icon
        self.n = random.randint(0, 10000)
        self.n = str(self.n)
        print(self.n)
        self.driver.implicitly_wait(40)
        self.driver.find_element(*SupportValueIdentifiers.TOPIC_DETAIL).click()
        # CLicking on Start CAmp Here
        self.driver.find_element(*SupportValueIdentifiers.START_NEW_CAMP).click()
        print("Creating Camp")
        self.camp = ("camp_new1" + self.n)
        self.driver.find_element(*SupportValueIdentifiers.CAMP_NAME).send_keys(self.camp)
        self.driver.find_element(*SupportValueIdentifiers.CAMP_KEYWORD).send_keys(self.camp)
        self.driver.find_element(*SupportValueIdentifiers.CAMP_NOTE).send_keys(self.camp)
        self.driver.find_element(*SupportValueIdentifiers.CAMP_ABOUT_URL).send_keys("https://www.google.com")
        self.driver.find_element(*SupportValueIdentifiers.NICK_NAME_DROPDOWN).click()
        self.driver.find_element(*SupportValueIdentifiers.SELECT_NICK_NAME).click()
        self.driver.find_element(*SupportValueIdentifiers.CREATE_CAMP).click()

        #Ceate Second Camp
        time.sleep(10)
        self.driver.find_element(*SupportValueIdentifiers.START_SECOND_NEW_CAMP).click()

        time.sleep(10)

        self.camp2= ("camp_new2"+ self.n)
        self.driver.find_element(*SupportValueIdentifiers.CAMP_NAME).send_keys(self.camp2)
        self.driver.find_element(*SupportValueIdentifiers.CAMP_KEYWORD).send_keys(self.camp2)
        self.driver.find_element(*SupportValueIdentifiers.CAMP_NOTE).send_keys(self.camp2)
        self.driver.find_element(*SupportValueIdentifiers.CAMP_ABOUT_URL).send_keys("https://www.google.com")
        self.driver.find_element(*SupportValueIdentifiers.NICK_NAME_DROPDOWN).click()
        self.driver.find_element(*SupportValueIdentifiers.SELECT_NICK_NAME).click()
        self.driver.find_element(*SupportValueIdentifiers.CREATE_CAMP).click()
#supportfirst camp
        print("supporting first camp")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[2]/span[3]/span/div/div/span[1]").click()
        time.sleep(20)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[5]/div/div[2]/div/div[2]/a/button/span").click()
        time.sleep(20)
        self.driver.find_element(*SupportValueIdentifiers.SUPPORT_SUBMIT_BUTTON).click()
        print("First camp Supported")
        print("Support second camp")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[4]/span[3]/span/div/div/span[1]").click()
        self.driver.find_element(*SupportValueIdentifiers.MANAGE_SUPPORT).click()
        self.driver.find_element(*SupportValueIdentifiers.SUPPORT_SUBMIT_BUTTON).click()
        print("Ready to calculate support")

        self.calculate_support_value()
        print(self.topic_score)
        print(self.camp_sum)
        if self.topic_score == 1.00 and self.camp1_score == 0.75:
            pass
            return CanonizerSupportValue(self.driver)
        else:
            print("Not right")

            #return CanonizerSupportValue(self.driver)
        '''if self.topic_score == 1.00:
            if self.camp1_score == 0.75:
                if self.camp2_score == 0.25:
                    return CanonizerSupportValue(self.driver)'''


    def calculate_support_value(self):
        self.driver.implicitly_wait(30)

        self.topic_score = self.driver.find_element(*SupportValueIdentifiers.TOPIC_SCORE)
        self.topic_score = float(self.topic_score.text)
        self.topic_score = ("%.2f" % self.topic_score)
        print("topic score")
        print(self.topic_score)

        self.camp1_score = self.driver.find_element(*SupportValueIdentifiers.CAMP1_SCORE)
        #print(self.camp1_score.text)
        self.camp1_score = float(self.camp1_score.text)
        print("camp1 score")
        print(self.camp1_score)

        self.camp2_score = self.driver.find_element(*SupportValueIdentifiers.CAMP2_SCORE)
        self.camp2_score = float(self.camp2_score.text)
        print("camp2 score")
        print(self.camp2_score)
        self.camp_sum = self.camp1_score + self.camp2_score
        self.camp_sum = float(self.camp_sum)
        #self.camp_sum = ("%.2f" % self.camp_sum)
        print("camp score")
        print(self.camp_sum)

