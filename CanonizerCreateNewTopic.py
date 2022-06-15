from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from CanonizerBase import Page
from Identifiers import CreateTopicIdentifiers


from datetime import datetime
from time import time
import time


class CanonizerCreateNewTopic(Page):

    def click_create_new_topic_page_button(self):
        """
        This function is to click on the login button

        -> Hover to the login button
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        time.sleep(4)
        self.hover(*CreateTopicIdentifiers.CREATE_NEW_TOPIC)
        self.find_element(*CreateTopicIdentifiers.CREATE_NEW_TOPIC).click()
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE_TITLE)
        page_title = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE_TITLE).text
        if page_title == 'Create New Topic':
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Title not found or  is not matching")

    def click_create_topic_without_user_login(self):
        self.hover(*CreateTopicIdentifiers.CREATE_NEW_TOPIC)
        self.find_element(*CreateTopicIdentifiers.CREATE_NEW_TOPIC).click()
        self.hover(*CreateTopicIdentifiers.LOGIN_PAGE)
        page_title = self.find_element(*CreateTopicIdentifiers.LOGIN_PAGE).text
        if page_title == 'Login to Canonizer':
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Confirmation text is not matching")

    def enter_nick_name(self,nick_name):
        self.find_element(*CreateTopicIdentifiers.NICK_NAME).send_keys(nick_name)
        #select = Select(self.find_element(*CreateTopicIdentifiers.NICK_NAME))
        #select.select_by_value("1")


    def enter_topic_name(self, topic_name):
        self.find_element(*CreateTopicIdentifiers.TOPIC_NAME).send_keys(topic_name)

    def enter_namespace(self, namespace):
        self.find_element(*CreateTopicIdentifiers.NAMESPACE).send_keys(namespace)

    def enter_summary(self, summary):
        self.find_element(*CreateTopicIdentifiers.EDIT_SUMMARY).send_keys(summary)

    def click_create_topic_button(self):
        self.find_element(*CreateTopicIdentifiers.CREATE_TOPIC).click()

    def entering_data_fields(self, nick_name, topic_name, namespace, summary):
        self.enter_nick_name(nick_name)
        self.enter_topic_name(topic_name)
        self.enter_namespace(namespace)
        self.enter_summary(summary)

    def create_topic(self, nick_name, topic_name, namespace, summary):
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="create_new_topic"]/div/div[1]/div[1]/div[2]/div[2]')))
        self.entering_data_fields(nick_name, topic_name, namespace, summary)
        print(nick_name)
        self.click_create_topic_button()

    def create_topic_with_blank_topic_name(self, nickname, namespace, note):
        try:
            nick_name1 = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             '#create_new_topic > div > div:nth-child(1) > div:nth-child(1) > div.ant-col.ant-form-item-control > div.ant-form-item-control-input > div > div > div > span.ant-select-selection-item')))
            nick_name = nick_name1.text
        except TimeoutException:
            pass
        print(nick_name)
        self.create_topic(nick_name, '', namespace, note)
        error = self.find_element(*CreateTopicIdentifiers.ERROR_TOPIC_NAME).text
        if error == "Please enter topic name":
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Error message is not correct")

    def create_topic_with_blank_spaces_topic_name(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, "    ", namespace, summary)
        error = self.find_element(*CreateTopicIdentifiers.ERROR_TOPIC_NAME).text
        if error == "Topic name is required.":
            return CanonizerCreateNewTopic(self.driver)

    def create_topic_with_valid_data(self, nick_name, topic_name, namespace, summary):
        try:
            nick_name1 = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                             '#create_new_topic > div > div:nth-child(1) > div:nth-child(1) > div.ant-col.ant-form-item-control > div.ant-form-item-control-input > div > div > div > span.ant-select-selection-item')))
            nick_name = nick_name1.text
        except TimeoutException:
            pass
        self.create_topic(nick_name, topic_name, namespace, summary)
        return CanonizerCreateNewTopic(self.driver)

