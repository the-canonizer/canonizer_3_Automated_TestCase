from selenium.webdriver import ActionChains

from CanonizerBase import Page
from Identifiers import UploadFileIdentifiers
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import string
import random



class CanonizerUploadFilePage(Page):
    """
    Class Name: CanonizerUploadFilePage

    """
    def driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def upload_file_name(self):
        N = 7
        self.res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    def click_upload_file_page_button(self):
        """
        -> Hover the control towards the upload file button. Identifiers are loaded from Identifiers Class
        -> Find the upload file button and Click on it.

        :return:
            Return the control to the main Program
        """
        title = self.find_element(*UploadFileIdentifiers.TITLE).text
        if title == 'Canonizer Main Page':
            self.hover(*UploadFileIdentifiers.UPLOADBUTTON)
            self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()
            upload_title = self.find_element(*UploadFileIdentifiers.UPLOAD_TITLE).text
            if upload_title in 'Upload Files, Max size 5 MB':
                return CanonizerUploadFilePage(self.driver)
        return CanonizerUploadFilePage(self.driver)


    def click_upload_button(self):
        """
        This function clicks the Upload Button
        :return:
        """
        self.driver.implicitly_wait(20)
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()

    def upload_file_with_user_login(self):
        self.driver.implicitly_wait(20)
        self.hover(*UploadFileIdentifiers.UPLOADBUTTON)
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()
        self.driver.find_element(*UploadFileIdentifiers.ADD_FILE_BUTTON).click()
        originalfilename = "/home/akashroshan/PycharmProjects/Test/sample.csv"
        self.find_element(*UploadFileIdentifiers.UPLOAD).send_keys(originalfilename)
        self.upload_file_name()
        self.driver.find_element(*UploadFileIdentifiers.ENTER_FILE_NAME).send_keys(self.res)
        self.driver.find_element(*UploadFileIdentifiers.UPLOADBUTTON_ID).click()
        return CanonizerUploadFilePage(self.driver)

    def upload_more_than_5mb_file_with_user_login(self):
        self.driver.implicitly_wait(20)
        self.hover(*UploadFileIdentifiers.UPLOADBUTTON)
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()
        originalfilename = "/home/akashroshan/PycharmProjects/Test/more_than_5mb.jpg"
        self.find_element(*UploadFileIdentifiers.UPLOAD).send_keys(originalfilename)
        return CanonizerUploadFilePage(self.driver)




    def upload_file_with_same_file_name(self, originalfilename, file_name):
        self.driver.implicitly_wait(20)
        self.hover(*UploadFileIdentifiers.UPLOADBUTTON)
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()
        self.driver.find_element(By.ID, 'addAFileBtn').click()
        originalfilename = "/home/akashroshan/PycharmProjects/Test/sample.csv"
        self.find_element(*UploadFileIdentifiers.UPLOAD).send_keys(originalfilename)
        self.upload_file_name()
        self.driver.find_element(*UploadFileIdentifiers.ENTER_FILE_NAME).send_keys(self.res)


        self.driver.find_element(By.ID, "uploadBtn").click()

        return CanonizerUploadFilePage(self.driver)

    def upload_file_with_invalid_file_name_format(self):
        self.driver.implicitly_wait(20)
        self.hover(*UploadFileIdentifiers.UPLOADBUTTON)
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()
        self.driver.find_element(*UploadFileIdentifiers.ADD_FILE_BUTTON).click()
        originalfilename = "/home/akashroshan/PycharmProjects/Test/t.xxx"
        self.find_element(*UploadFileIdentifiers.UPLOAD).send_keys(originalfilename)

        return CanonizerUploadFilePage(self.driver)
