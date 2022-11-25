from selenium.webdriver import ActionChains

from CanonizerBase import Page
from Identifiers import UploadFileIdentifiers
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os



class CanonizerUploadFilePage(Page):
    """
    Class Name: CanonizerUploadFilePage

    """

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

    def upload_file_without_user_login(self):

        self.hover(*UploadFileIdentifiers.UPLOADBUTTON)
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()
        originalfilename = "/home/akashroshan/PycharmProjects/Test/sample.csv"
        self.find_element(*UploadFileIdentifiers.UPLOAD).send_keys(originalfilename)
        self.driver.find_element(By.ID, "enterFileName").send_keys("testfile")
        self.driver.find_element(By.ID, "uploadBtn").click()

        return CanonizerUploadFilePage(self.driver)

    def upload_file_with_user_login(self):

        self.hover(*UploadFileIdentifiers.UPLOADBUTTON)
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()
        originalfilename = "/home/akashroshan/PycharmProjects/Test/sample.csv"
        self.find_element(*UploadFileIdentifiers.UPLOAD).send_keys(originalfilename)
        self.driver.find_element(By.ID, "enterFileName").send_keys("testfile")
        self.driver.find_element(By.ID, "uploadBtn").click()

        return CanonizerUploadFilePage(self.driver)

    def upload_more_than_5mb_file_with_user_login(self):

        self.hover(*UploadFileIdentifiers.UPLOADBUTTON)
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()
        originalfilename = "/home/akashroshan/PycharmProjects/Test/more_than_5mb.jpg"
        self.find_element(*UploadFileIdentifiers.UPLOAD).send_keys(originalfilename)
        self.driver.find_element(By.ID, "enterFileName").send_keys("testfile")
        self.driver.find_element(By.ID, "uploadBtn").click()



    def click_upload_button(self):
        """
        This function clicks the Upload Button
        :return:
        """
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()


    def upload_file_with_blank_file(self):
        self.click_upload_button()
        return self.find_element(*UploadFileIdentifiers.ERROR_FILE_NAME).text


    def upload_file_with_valid_format(self, originalfilename, file_name):
        self.upload(originalfilename, file_name)
        success_message = self.find_element(*UploadFileIdentifiers.SUCCESS_MESSAGE).text
        if success_message == 'Success! File uploaded successfully!':
            return CanonizerUploadFilePage(self.driver)

    def upload_file_with_same_file_name(self, originalfilename, file_name):
        self.upload(originalfilename, file_name)
        return self.find_element(*UploadFileIdentifiers.SAME_FILE_NAME_ERROR).text

    def upload_file_with_size_zero_bytes(self, originalfilename, file_name):
        self.upload(originalfilename, file_name)
        return self.find_element(*UploadFileIdentifiers.ERROR_ZERO_FILE_SIZE).text

    def verify_recent_upload_file_name_from_list_of_files(self, originalfilename, file_name):
        self.upload(originalfilename, file_name)
        success_message = self.find_element(*UploadFileIdentifiers.SUCCESS_MESSAGE).text
        if success_message == 'Success! File uploaded successfully!':
            recent_file_name = self.find_element(*UploadFileIdentifiers.RECENT_FILE_NAME).text
            if file_name in recent_file_name:
                return CanonizerUploadFilePage(self.driver)

    def verify_uploaded_image_file_format(self, originalfilename, file_name):
        self.hover(*UploadFileIdentifiers.UPLOADBUTTON)
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'ant-card-head')))
        except TimeoutException:
            pass
        error_message = self.find_element(*UploadFileIdentifiers.UPLOADED_IMAGE).text
        if error_message  in 'Error! The type of the uploaded file should be an image.(jpeg,jpg,png,bmp,gif)':
            return CanonizerUploadFilePage(self.driver)

    def open_uploaded_file(self):
        self.hover(*UploadFileIdentifiers.UPLOADBUTTON)
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()
        self.hover(*UploadFileIdentifiers.UPLOADED_OPTION)
        self.find_element(*UploadFileIdentifiers.UPLOADED_OPTION).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'ant-dropdown-menu-title-content')))
        except TimeoutException:
            pass
        self.find_element(*UploadFileIdentifiers.UPLOADED_IMAGE_VIEW).click()
        try:
            WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'ant-modal modalStyle')))
        except TimeoutException:
            pass                                                                          
        return CanonizerUploadFilePage(self.driver)

    def upload_file_with_invalid_file_name_format(self, originalfilename):
        self.hover(*UploadFileIdentifiers.UPLOADBUTTON)
        self.find_element(*UploadFileIdentifiers.UPLOADBUTTON).click()
        #Uploading Invalid File Format
        originalfilename = "/home/akashroshan/PycharmProjects/Test/sample.xxx"
        self.find_element(*UploadFileIdentifiers.UPLOAD).send_keys(originalfilename)
        self.driver.find_element(By.ID, "enterFileName").send_keys("testfile")
        self.driver.find_element(By.ID, "uploadBtn").click()
        return CanonizerUploadFilePage(self.driver)
