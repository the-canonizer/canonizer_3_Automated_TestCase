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

    def select_dropdown_value(self):
        self.click_browse_page_button()
        self.hover(*BrowsePageIdentifiers.NAMESPACE)
        self.find_element(*BrowsePageIdentifiers.NAMESPACE).click()
        return CanonizerSupportValue(self.driver)

    def scroll_down(self):
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        action = ActionChains(self.driver)
        #i = 10
        while self.i >= 0:
            action.key_down(Keys.DOWN).perform()
            print(self.i)
            self.i = self.i - 1
            #time.sleep(0.4)


    def support_value_new_topic(self):
        self.n = random.randint(0, 10000)
        self.n = str(self.n)
        print(self.n)
        self.click_browse_page_button()
        self.select_dropdown_value()
        #self.i = 20
        #self.scroll_down()
        #self.find_element(*BrowsePageIdentifiers.SANDBOXTESTING).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/aside/div/div[1]/button/span')))
        except TimeoutException:
            pass
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/aside/div/div[1]/button/span").click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/form/div/div[2]/div/div[2]/div/div/textarea')))
        except TimeoutException:
            pass
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/form/div/div[2]/div/div[2]/div/div/textarea").send_keys("test_new_topic1")
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/form/div/div[1]/div[2]/div[2]/div[1]/div/input')))
        except TimeoutException:
            pass

        self.topic = ("test_new_topic1" + self.n)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/form/div/div[1]/div[2]/div[2]/div[1]/div/input").send_keys(self.topic)
        #Click On Create Topic Button

        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div[3]/div[2]/div/div/div/div/span[2]')))
        except TimeoutException:
            pass
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/form/div/div[1]/div[3]/div[2]/div/div/div/div/span[2]").click()
        self.i = 17
        self.scroll_down()
        action = ActionChains(self.driver)
        action.key_down(Keys.ENTER).perform()
        #self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]/span").click()
        #self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[2]/form/button[1]/span").click()
        self.driver.find_element(By.ID, "create-topic-btn").click()                
        #Topic Created
        # Create Camp
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div/span[2]/span").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[2]/span[3]/span").click()
        time.sleep(3)
        self.camp = ("camp_new1" + self.n)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[2]/form/div[2]/div[1]/div/div[2]/div[1]/div/input").send_keys(self.camp)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div/input").send_keys(self.camp)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[2]/form/div[2]/div[3]/div/div[2]/div/div/textarea").send_keys(self.camp)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[2]/form/div[2]/div[4]/div/div[2]/div/div/input").send_keys("https://www.google.com")
        time.sleep(3)
        self.driver.find_element(By.ID, "camp-about-nick-dropdown").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "camp-about-nick-301").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "crate-camp-btn").click()
        time.sleep(10)
        # Create second camp
        self.n = random.randint(0, 10000)
        self.n = str(self.n)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[1]/span[3]/span/div").click()
        # self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[2]/span[3]/span").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[2]/span[3]/span").click()
        time.sleep(3)
        self.camp = ("camp_new1" + self.n)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[2]/form/div[2]/div[1]/div/div[2]/div[1]/div/input").send_keys(self.camp)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[2]/form/div[2]/div[2]/div/div[2]/div/div/input").send_keys(self.camp)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[2]/form/div[2]/div[3]/div/div[2]/div/div/textarea").send_keys(self.camp)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[2]/form/div[2]/div[4]/div/div[2]/div/div/input").send_keys("https://www.google.com")
        time.sleep(3)
        self.driver.find_element(By.ID, "camp-about-nick-dropdown").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "camp-about-nick-301").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "crate-camp-btn").click()
        time.sleep(10)
        # Support first camp
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[5]/div/div/div/div[2]/div/div[2]/a/button/span").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "uploadBtn").click()
        time.sleep(10)
        # Support second camp
        # self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[3]/span[3]/span/div").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[3]/span[3]/span/div/div/span[1]").click()
        time.sleep(5)
        # self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[5]/div/div/div/div[2]/div/div[2]/a/button/span").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div[2]/div[5]/div/div/div/div[2]/div/div[2]/a/button").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "uploadBtn").click()
        time.sleep(10)
        self.topic_score = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[1]/span[3]/span/div/div/span[2]")
        self.topic_score = float(self.topic_score.text)
        self.camp1_score = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[2]/span[3]/span/div/div/span[2]")
        self.camp1_score = float(self.camp1_score.text)
        self.camp2_score = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[3]/span[3]/span/div/div/span[2]")
        self.camp2_score = float(self.camp2_score.text)
        self.camp_sum = self.camp1_score + self.camp2_score
        self.camp_sum = float(self.camp_sum)
        self.camp_sum = ("%.2f" % self.camp_sum)
        return CanonizerSupportValue(self.driver)
