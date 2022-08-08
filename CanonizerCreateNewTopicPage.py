from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CanonizerValidationCheckMessages import message
from CanonizerBase import Page
from Identifiers import CreateTopicIdentifiers


class CanonizerCreateNewTopic(Page):

    def click_create_new_topic_page_button(self):
        """
        This function is to click on the create new topic button

        -> Hover to the create new topic  button
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-btn ant-btn-default ant-btn-lg mb-3 btn')))
        except TimeoutException:
            pass
        self.hover(*CreateTopicIdentifiers.CREATE_NEW_TOPIC)
        self.find_element(*CreateTopicIdentifiers.CREATE_NEW_TOPIC).click()
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE_TITLE)
        page_title = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE_TITLE).text
        if page_title == message['Create_Topic']['New_Topic_Page_Title']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Title not found or  is not matching")

    def click_create_topic_without_user_login(self):
        self.hover(*CreateTopicIdentifiers.CREATE_NEW_TOPIC)
        self.find_element(*CreateTopicIdentifiers.CREATE_NEW_TOPIC).click()
        self.hover(*CreateTopicIdentifiers.LOGIN_PAGE)
        page_title = self.find_element(*CreateTopicIdentifiers.LOGIN_PAGE).text
        if page_title == message['Create_Topic']['Login_Title']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Confirmation text is not matching")

    def enter_nick_name(self, nickname):
        self.find_element(*CreateTopicIdentifiers.NICK_NAME).send_keys(nickname)

    def enter_topic_name(self, topic_name):
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'create_new_topic_topic_name')))
        self.find_element(*CreateTopicIdentifiers.TOPIC_NAME).send_keys(topic_name)

    def enter_namespace(self, namespace):
        self.find_element(*CreateTopicIdentifiers.NAMESPACE).send_keys(namespace)

    def enter_summary(self, summary):
        self.find_element(*CreateTopicIdentifiers.EDIT_SUMMARY).send_keys(summary)

    def click_create_topic_button(self):
        self.find_element(*CreateTopicIdentifiers.CREATE_TOPIC_BUTTON).click()

    def entering_data_fields(self, nickname, topic_name, namespace, summary):
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="create_new_topic"]/div/div[1]/div[1]/div[2]/div[2]')))
        self.enter_nick_name(nickname)
        self.enter_topic_name(topic_name)
        self.enter_namespace(namespace)
        self.enter_summary(summary)

    def create_topic(self, nickname, topic_name, namespace, summary):
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="create_new_topic"]/div/div[1]/div[1]/div[2]/div[2]')))
        self.entering_data_fields(nickname, topic_name, namespace, summary)
        self.click_create_topic_button()

    def create_topic_with_blank_topic_name(self, nickname, namespace, note):
        self.create_topic(nickname, '', namespace, note)
        self.hover(*CreateTopicIdentifiers.ERROR_TOPIC_NAME)
        error = self.find_element(*CreateTopicIdentifiers.ERROR_TOPIC_NAME).text
        if error == message['Create_Topic']['Blank_Topic_Error']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Error message is not correct")

    def create_topic_with_blank_spaces_topic_name(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, "    ", namespace, summary)
        self.hover(*CreateTopicIdentifiers.ERROR_TOPIC_NAME)
        error = self.find_element(*CreateTopicIdentifiers.ERROR_TOPIC_NAME).text
        if error == message['Create_Topic']['Blank_Topic_Error']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Error message is not correct")

    def create_topic_with_valid_data(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, topic_name, namespace, summary)
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['Create_Topic_Title']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def create_topic_name_with_enter_key(self, nickname, topic_name, namespace, summary):
        self.entering_data_fields(nickname, topic_name, namespace, summary)
        self.hover(*CreateTopicIdentifiers.CREATE_TOPIC_BUTTON)
        self.find_element(*CreateTopicIdentifiers.CREATE_TOPIC_BUTTON).send_keys(Keys.ENTER)
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['Create_Topic_Title']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def create_topic_name_with_trailing_space(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, topic_name, namespace, summary)
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['Create_Topic_Title']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def create_topic_with_duplicate_topic_name(self, nick_name, topic_name, namespace, summary):
        self.create_topic(nick_name, topic_name, namespace, summary)
        self.hover(*CreateTopicIdentifiers.ERROR_DUPLICATE_TOPIC_NAME)
        error = self.find_element(*CreateTopicIdentifiers.ERROR_DUPLICATE_TOPIC_NAME).text
        if error == message['Create_Topic']['Duplicate_Topic_Error']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Error message not found or is incorrect")

    def create_topic_with_special_chars(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, topic_name, namespace, summary)
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['Create_Topic_Title']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def create_topic_without_entering_mandatory_fields(self, nickname, topic_name, namespace, summary):
        self.create_topic('', '', '', '')
        self.hover(*CreateTopicIdentifiers.ERROR_TOPIC_NAME)
        error = self.find_element(*CreateTopicIdentifiers.ERROR_TOPIC_NAME).text
        if error == message['Create_Topic']['Blank_Topic_Error']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Error message not found or is incorrect")

    def create_topic_with_entering_data_only_in_mandatory_fields(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, topic_name, namespace, '')
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['Create_Topic_Title']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def click_on_cancel_button(self):
        self.hover(*CreateTopicIdentifiers.CANCEL_BUTTON)
        self.find_element(*CreateTopicIdentifiers.CANCEL_BUTTON).click()
        self.hover(*CreateTopicIdentifiers.MAIN_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.MAIN_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['Topic_Label']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def topic_page_mandatory_fields_are_marked_with_asterisk(self):
        """
        This Function checks, if Mandatory fields on Create topic Page Marked with *
        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-form-item-extra')))
        except TimeoutException:
            pass

        return \
            self.find_element(*CreateTopicIdentifiers.NICK_NAME_ASTERISK) and \
            self.find_element(*CreateTopicIdentifiers.TOPIC_NAME_ASTERISK) and \
            self.find_element(*CreateTopicIdentifiers.NAMESPACE_ASTERISK)




