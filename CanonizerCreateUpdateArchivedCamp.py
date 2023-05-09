import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from CanonizerBase import Page
from Config import DEFAULT_TOPIC
from Identifiers import CreateCampIdentifiers, CampStatementIdentifiers, CreateTopicIdentifiers, CampForumIdentifiers, \
    CampHistoryIdentifiers
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from CanonizerValidationCheckMessages import message
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import *
from selenium import webdriver


class CanonizerCreateUpdateArchivedCamp(Page):

    def driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def load_create_camp_page(self, topic_name):
        self.driver.implicitly_wait(20)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'siteHeader_navWrap__yilWi false')))
        except TimeoutException:
            pass

        # Browse to Browse Page
        self.hover(*CampForumIdentifiers.BROWSE)
        self.find_element(*CampForumIdentifiers.BROWSE).click()

        # Click on Search Topic
        self.hover(*CampForumIdentifiers.SEARCH_TOPIC)
        self.find_element(*CampForumIdentifiers.SEARCH_TOPIC).send_keys(topic_name)
        self.hover(*CampForumIdentifiers.SEARCH_ICON)
        self.find_element(*CampForumIdentifiers.SEARCH_ICON).click()
        self.hover(*CampForumIdentifiers.TOPIC_CLICK)
        self.find_element(*CampForumIdentifiers.TOPIC_CLICK).click()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'ant-btn ant-btn-default ant-btn-lg btn')))
        except TimeoutException:
            pass

        # Click on Create New Camp Button
        self.hover(*CreateCampIdentifiers.CREATE_NEW_CAMP_BUTTON)
        self.find_element(*CreateCampIdentifiers.CREATE_NEW_CAMP_BUTTON).click()

        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//div[text()="sania_talentelgia"]')))
        except TimeoutException:
            pass
        self.hover(*CreateCampIdentifiers.NEW_CAMP_TITLE)
        return CanonizerCreateUpdateArchivedCamp(self.driver)


    def new_camp_mandatory_fields_are_marked_with_asterisk(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'createNewTopic_cardTitle__NEIpU')))
        except TimeoutException:
            pass
        return \
            self.find_element(*CreateCampIdentifiers.NICK_NAME_ASTERISK) and \
            self.find_element(*CreateCampIdentifiers.CAMP_NAME_ASTERISK) and \
            self.find_element(*CreateCampIdentifiers.PARENT_CAMP_ASTERISK)

    def enter_nick_name(self, nickname):
        self.find_element(*CreateCampIdentifiers.CAMP_NICKNAME).send_keys(nickname)

    def enter_parent_camp_name(self, parent_camp_name):
        self.find_element(*CreateCampIdentifiers.PARENT_CAMP).send_keys(parent_camp_name)

    def enter_camp_name(self, camp_name):
        self.find_element(*CreateCampIdentifiers.CAMP_NAME).send_keys(camp_name)

    def enter_keywords(self, keywords):
        self.find_element(*CreateCampIdentifiers.KEYWORDS).send_keys(keywords)

    def enter_note(self, note):
        self.find_element(*CreateCampIdentifiers.CAMP_EDIT_SUMMARY).send_keys(note)

    def enter_camp_about_url(self, camp_about_url):
        self.hover(*CreateCampIdentifiers.CAMP_ABOUT_URL)
        self.find_element(*CreateCampIdentifiers.CAMP_ABOUT_URL).send_keys(camp_about_url)

    def enter_camp_about_nick_name(self, camp_about_nick_name):
        self.hover(*CreateCampIdentifiers.CAMP_ABOUT_NICK_NAME)
        self.find_element(*CreateCampIdentifiers.CAMP_ABOUT_NICK_NAME).send_keys(camp_about_nick_name)

    def click_create_camp_button(self):
        self.hover(*CreateCampIdentifiers.CREATE_CAMP_BUTTON)
        self.find_element(*CreateCampIdentifiers.CREATE_CAMP_BUTTON).click()

    def create_camp(self, *args):
        args = list(args[0])
        self.enter_nick_name(args[0])
        self.enter_parent_camp_name(args[1])
        self.enter_camp_name(args[2])
        self.enter_keywords(args[3])
        self.enter_note(args[4])
        self.enter_camp_about_url(args[5])
        self.click_create_camp_button()

    def create_archived_camp_with_valid_data(self, create_camp_list1):
        self.driver.implicitly_wait(20)
        self.hover(*CampHistoryIdentifiers.ARCHIEVED)
        self.driver.find_element(*CampHistoryIdentifiers.ARCHIEVED).click()
        self.create_camp(create_camp_list1)


        return CanonizerCreateUpdateArchivedCamp(self.driver)

    def create_archived_camp_with_blank_camp_name(self, create_camp_list2):
        self.driver.implicitly_wait(20)
        self.hover(*CampHistoryIdentifiers.ARCHIEVED)
        self.driver.find_element(*CampHistoryIdentifiers.ARCHIEVED).click()
        self.create_camp(create_camp_list2)
        self.hover(*CreateCampIdentifiers.BLANK_CAMP_NAME_ERROR)
        error = self.find_element(*CreateCampIdentifiers.BLANK_CAMP_NAME_ERROR).text
        if error == message['Create_Camp']['BLANK_CAMP_NAME_ERROR']:
            return CanonizerCreateUpdateArchivedCamp(self.driver)
        else:
            print("Error not found or is not matching")

    def create_archived_camp_with_duplicate_camp_name(self, create_camp_list_3):
        self.driver.implicitly_wait(20)
        self.hover(*CampHistoryIdentifiers.ARCHIEVED)
        self.driver.find_element(*CampHistoryIdentifiers.ARCHIEVED).click()
        self.create_camp(create_camp_list_3)
        self.hover(*CreateCampIdentifiers.DUPLICATE_CAMP_NAME_ERROR)
        error = self.find_element(*CreateCampIdentifiers.DUPLICATE_CAMP_NAME_ERROR).text
        if error == message['Create_Camp']['BLANK_CAMP_NAME_ERROR']:
            return CanonizerCreateUpdateArchivedCamp(self.driver)
        else:
            print("Error not found or is not matching")

    def create_archived_camp_with_invalid_camp_about_url(self,create_camp_list_4 ):
        self.driver.implicitly_wait(20)
        self.hover(*CampHistoryIdentifiers.ARCHIEVED)
        self.driver.find_element(*CampHistoryIdentifiers.ARCHIEVED).click()
        self.create_camp(create_camp_list_4)
        self.hover(*CreateCampIdentifiers.INVALID_CAMP_ABOUT_URL_ERROR)
        error = self.find_element(*CreateCampIdentifiers.INVALID_CAMP_ABOUT_URL_ERROR).text
        if error == message['Create_Camp']['INVALID_CAMP_ABOUT_URL_ERROR']:
            return CanonizerCreateUpdateArchivedCamp(self.driver)
        else:
            print("Error not found or is not matching")

    def camp_archived_cancel_button(self):
        self.driver.implicitly_wait(20)
        self.hover(*CampHistoryIdentifiers.ARCHIEVED)
        self.driver.find_element(*CampHistoryIdentifiers.ARCHIEVED).click()
        self.hover(*CreateCampIdentifiers.CANCEL_BUTTON)
        self.find_element(*CreateCampIdentifiers.CANCEL_BUTTON).click()
        self.hover(*CreateCampIdentifiers.CANCEL_TITLE)
        return CanonizerCreateUpdateArchivedCamp(self.driver)


class CanonizerEditArchivedCampPage(Page):
    window_scroll = "window.scrollTo(0, document.body.scrollHeight);"
    def driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def load_topic_detail_page(self, topic_name):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'siteHeader_navWrap__yilWi false')))
        except TimeoutException:
            pass

            # Browse to Browse Page
        self.hover(*CampForumIdentifiers.BROWSE)
        self.find_element(*CampForumIdentifiers.BROWSE).click()
        print("came load topic")

        # Click on Search Topic
        self.hover(*CampForumIdentifiers.SEARCH_TOPIC)
        self.find_element(*CampForumIdentifiers.SEARCH_TOPIC).send_keys(topic_name)
        self.hover(*CampForumIdentifiers.SEARCH_ICON)
        self.find_element(*CampForumIdentifiers.SEARCH_ICON).click()
        self.hover(*CampForumIdentifiers.TOPIC_CLICK)
        self.find_element(*CampForumIdentifiers.TOPIC_CLICK).click()
        return CanonizerEditArchivedCampPage(self.driver)

    def load_camp_manage_edit_page(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'ant-btn ant-btn-default ant-btn-lg btn')))
        except TimeoutException:
            pass
        print("came in camp manage")
        self.find_element(*CreateCampIdentifiers.CAMP_NAME_CLICK).click()
        self.driver.execute_script(self.window_scroll)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'ant-btn ant-btn-default btn-green')))
        except TimeoutException:
            pass
        self.find_element(*CreateCampIdentifiers.MANAGE_EDIT_CAMP_BUTTON).click()
        self.hover(*CreateCampIdentifiers.CAMP_HISTORY_TITLE)
        page_title = self.find_element(*CreateCampIdentifiers.CAMP_HISTORY_TITLE).text
        if page_title == message['Create_Camp']['CAMP_HISTORY_TITLE']:
            return CanonizerEditArchivedCampPage(self.driver)
        else:
            print("Title not found or is not matching")



    def check_unarchived_camp(self):
        self.load_topic_detail_page(DEFAULT_TOPIC)
        self.load_camp_manage_edit_page()
        self.driver.implicitly_wait(20)
        self.find_element(*CampHistoryIdentifiers.THREEDOTS).click()
        # self.find_element(*CampHistoryIdentifiers.CAMP_EDIT_BUTTON).click()
        #self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[4]/i").click()
        self.driver.get("https://canonizer3.canonizer.com/camp/history/1002-email-testing-1348/1-Agreement")
        return CanonizerEditArchivedCampPage(self.driver)
    
    def do_archive_camp(self):
        self.load_topic_detail_page(DEFAULT_TOPIC)
        self.load_camp_manage_edit_page()
        self.driver.implicitly_wait(20)
        self.find_element(*CampHistoryIdentifiers.THREEDOTS).click()
        # self.find_element(*CampHistoryIdentifiers.CAMP_EDIT_BUTTON).click()
        #self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[4]/i").click()
        self.driver.get("https://canonizer3.canonizer.com/camp/history/1002-email-testing-1348/1-Agreement")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[2]/button[1]/span").click()
        self.driver.find_element(*CampHistoryIdentifiers.ARCHIEVED_EDIT).click()
        self.driver.find_element(*CampHistoryIdentifiers.CAMP_EDIT_SUBMIT).click()

        return CanonizerEditArchivedCampPage(self.driver)
