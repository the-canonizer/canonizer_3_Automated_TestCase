
from selenium.webdriver.chrome import webdriver
from CanonizerBase import Page
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.remote.webelement import *
from Identifiers import CanonizerFooterIdentifiers

class CanonizerFooter(Page):

    def driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def footer_browse(self):
        self.driver.implicitly_wait(30)
        self.hover(*CanonizerFooterIdentifiers.FOOTER_BROWSE)
        self.driver.find_element(*CanonizerFooterIdentifiers.FOOTER_BROWSE).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "topicsList_head__IooBi topicsList_browsePage__cb2G_")))

    def footer_create_new_topic(self):
        self.driver.implicitly_wait(30)
        self.hover(*CanonizerFooterIdentifiers.FOOTER_NEW_TOPIC)
        self.driver.find_element(*CanonizerFooterIdentifiers.FOOTER_NEW_TOPIC).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "topicsList_head__IooBi topicsList_browsePage__cb2G_")))

    def footer_upload(self):
        self.driver.implicitly_wait(30)
        self.hover(*CanonizerFooterIdentifiers.FOOTER_UPLOAD)
        self.driver.find_element(*CanonizerFooterIdentifiers.FOOTER_UPLOAD).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "topicsList_head__IooBi topicsList_browsePage__cb2G_")))

    def footer_sitemap(self):
        self.driver.implicitly_wait(30)
        self.hover(*CanonizerFooterIdentifiers.FOOTER_SITEMAP)
        self.driver.find_element(*CanonizerFooterIdentifiers.FOOTER_SITEMAP).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "topicsList_head__IooBi topicsList_browsePage__cb2G_")))

    def footer_help(self):
        self.driver.implicitly_wait(30)
        self.hover(*CanonizerFooterIdentifiers.FOOTER_HELP)
        self.driver.find_element(*CanonizerFooterIdentifiers.FOOTER_HELP).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "topicsList_head__IooBi topicsList_browsePage__cb2G_")))


    def footer_white_paper(self):
        self.driver.implicitly_wait(30)
        self.hover(*CanonizerFooterIdentifiers.FOOTER_WHITEPAPER)
        self.driver.find_element(*CanonizerFooterIdentifiers.FOOTER_WHITEPAPER).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "topicsList_head__IooBi topicsList_browsePage__cb2G_")))



    def footer_blog(self):
        self.driver.implicitly_wait(30)
        self.hover(*CanonizerFooterIdentifiers.FOOTER_BLOG)
        self.driver.find_element(*CanonizerFooterIdentifiers.FOOTER_BLOG).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "topicsList_head__IooBi topicsList_browsePage__cb2G_")))


    def footer_jobs(self):
        self.driver.implicitly_wait(30)
        self.hover(*CanonizerFooterIdentifiers.FOOTER_JOBS)
        self.driver.find_element(*CanonizerFooterIdentifiers.FOOTER_JOBS).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "topicsList_head__IooBi topicsList_browsePage__cb2G_")))
