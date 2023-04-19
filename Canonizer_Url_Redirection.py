import random

#from selenium.webdriver import Keys, ActionChains
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from selenium.common.exceptions import TimeoutException

import mailer
from CanonizerBase import Page
from Identifiers import BrowsePageIdentifiers, CampStatementIdentifiers, CreateTopicIdentifiers
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


class CanonizerUrlRedirection(Page):


    def driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def asp_url_redirection(self):
        self.driver.implicitly_wait(30)

        self.n = random.randint(0, 10000)
        self.n = str(self.n)
        self.driver.get("http://canonizer3.canonizer.com/topic.asp/" + self.n)
        time.sleep(5)

        resp = self.driver.current_url
        reslt = ("/topic/" + self.n)
        print(resp)
        print(reslt)
        if resp == reslt:
            pass
        else:
            mailer.mailern()
            print("failed")
        return CanonizerUrlRedirection(self.driver)


    def video_url(self):
        self.driver.implicitly_wait(30)

        res = requests.get("https://canonizer.com/videos/consciousness?chapter=representational_qualia_consensus")
        res = str(res.status_code)
        print(res)
        if "200" == res:
            url = ("https://" + "canonizer3" + ".canonizer.com/videos/consciousness?chapter=representational_qualia_consensus")
            self.driver.get(url)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div/label[1]/span[1]/input").click()
            time.sleep(10)

            self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/video").click()
            if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/video"):
                self.resp = "passed"
                # resp = self.driver.current_url
                print(self.resp)
                return CanonizerUrlRedirection(self.driver)

        else:
            print("url does not exist")


    def support_list_asp_url_redirection(self):
        self.driver.implicitly_wait(30)

        self.driver.get("http://canonizer3.canonizer.com/support_list.asp?nick_name_id=1")
        time.sleep(30)
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/h3"):
            self.status = "200"
            return CanonizerUrlRedirection(self.driver)

        else:
            self.status = "404"

    def thread_asp_url_redirection(self):
        self.driver.implicitly_wait(30)

        self.driver.get("http://canonizer3.canonizer.com/thread.asp/23/13/4")
        time.sleep(20)
        if self.driver.find_element(By.ID, "create-btn"):
            self.status = "200"
            return CanonizerUrlRedirection(self.driver)

        else:
            self.status = "404"

    def forum_asp_url_redirection(self):
        self.driver.implicitly_wait(30)

        self.driver.get("http://canonizer3.canonizer.com/forum.asp/88/1")
        time.sleep(20)
        if self.driver.find_element(By.ID, "create-btn"):
            self.status = "200"
            return CanonizerUrlRedirection(self.driver)

        else:
            self.status = "404"

    def topoc_asp_url_redirection(self):
        self.driver.implicitly_wait(30)

        self.driver.get("http://canonizer3.canonizer.com/topoc.asp/85")
        time.sleep(20)
        if self.driver.find_element(By.ID, "camp-forum-btn"):
            self.status = "200"
            return CanonizerUrlRedirection(self.driver)

        else:
            self.status = "404"

    def manage_asp_url_redirection(self):
        self.driver.implicitly_wait(30)
        self.driver.get("http://canonizer3.canonizer.com/manage.asp/2/2?class=camp")
        time.sleep(20)
        if self.driver.find_element(By.ID, "create-topic-btn"):
            self.status = "200"
            return CanonizerUrlRedirection(self.driver)

        else:
            self.status = "404"


    def statement_asp_url_redirection(self):
        self.driver.implicitly_wait(30)
        self.driver.get("http://canonizer3.canonizer.com/statement.asp/2/2")
        #time.sleep(20)
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/button[1]/span"):
            self.status = "200"
            return CanonizerUrlRedirection(self.driver)

        else:
            self.status = "404"


    def stmt_asp_url_redirection(self):
        self.driver.implicitly_wait(30)
        self.driver.get("http://canonizer3.canonizer.com/stmt.asp/2/2")
        #time.sleep(20)
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/button[1]/span"):
            self.status = "200"
            return CanonizerUrlRedirection(self.driver)

        else:
            self.status = "404"

    def sitemap_url(self):
        self.driver.implicitly_wait(30)
        resp = requests.get("https://canonizer.com/sitemap.xml")
        self.res = str(resp.status_code)
        if "200" == self.res:
            # if json response have data = true parameter then redirect else return 404.
            self.driver.get("https://canonizer3.canonizer.com/sitemap.xml")
            self.resf = requests.get("https://canonizer3.canonizer.com/sitemap.xml").text
            time.sleep(5)
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(self.resf, "html.parser")
            print(soup.h1.text)
            return CanonizerUrlRedirection(self.driver)

        else:
            self.driver.get("https://canonizer3.canonizer.com/sitemap.xml")
            print("url does not exist")
