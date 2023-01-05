from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CanonizerValidationCheckMessages import message
from CanonizerBase import Page
from Identifiers import CreateTopicIdentifiers, CampForumIdentifiers, UpdateTopicIdentifiers, CreateCampIdentifiers


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
        if page_title == message['Create_Topic']['NEW_TOPIC_PAGE_TITLE']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Title not found or  is not matching")

    def click_create_topic_without_user_login(self):
        self.hover(*CreateTopicIdentifiers.CREATE_NEW_TOPIC)
        self.find_element(*CreateTopicIdentifiers.CREATE_NEW_TOPIC).click()
        self.hover(*CreateTopicIdentifiers.LOGIN_PAGE)
        page_title = self.find_element(*CreateTopicIdentifiers.LOGIN_PAGE).text
        if page_title == message['Create_Topic']['LOGIN_TITLE']:
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
        if error == message['Create_Topic']['BLANK_TOPIC_ERROR']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Error message is not correct")

    def create_topic_with_blank_spaces_topic_name(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, "    ", namespace, summary)
        self.hover(*CreateTopicIdentifiers.ERROR_TOPIC_NAME)
        error = self.find_element(*CreateTopicIdentifiers.ERROR_TOPIC_NAME).text
        if error == message['Create_Topic']['BLANK_TOPIC_ERROR']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Error message is not correct")

    def create_topic_with_valid_data(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, topic_name, namespace, summary)
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['CREATE_TOPIC_TITLE']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def create_topic_name_with_enter_key(self, nickname, topic_name, namespace, summary):
        self.entering_data_fields(nickname, topic_name, namespace, summary)
        self.hover(*CreateTopicIdentifiers.CREATE_TOPIC_BUTTON)
        self.find_element(*CreateTopicIdentifiers.CREATE_TOPIC_BUTTON).send_keys(Keys.ENTER)
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['CREATE_TOPIC_TITLE']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def create_topic_name_with_trailing_space(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, topic_name, namespace, summary)
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['CREATE_TOPIC_TITLE']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def create_topic_with_duplicate_topic_name(self, nick_name, topic_name, namespace, summary):
        self.create_topic(nick_name, topic_name, namespace, summary)
        self.hover(*CreateTopicIdentifiers.ERROR_DUPLICATE_TOPIC_NAME)
        error = self.find_element(*CreateTopicIdentifiers.ERROR_DUPLICATE_TOPIC_NAME).text
        if error == message['Create_Topic']['DUPLICATE_TOPIC_ERROR']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Error message not found or is incorrect")

    def create_topic_with_special_chars(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, topic_name, namespace, summary)
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['CREATE_TOPIC_TITLE']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def create_topic_without_entering_mandatory_fields(self, nickname, topic_name, namespace, summary):
        self.create_topic('', '', '', '')
        self.hover(*CreateTopicIdentifiers.ERROR_TOPIC_NAME)
        error = self.find_element(*CreateTopicIdentifiers.ERROR_TOPIC_NAME).text
        if error == message['Create_Topic']['BLANK_TOPIC_ERROR']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Error message not found or is incorrect")

    def create_topic_with_entering_data_only_in_mandatory_fields(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, topic_name, namespace, '')
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['CREATE_TOPIC_TITLE']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")

    def click_on_cancel_button(self):
        self.hover(*CreateTopicIdentifiers.CANCEL_BUTTON)
        self.find_element(*CreateTopicIdentifiers.CANCEL_BUTTON).click()
        self.hover(*CreateTopicIdentifiers.MAIN_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.MAIN_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['TOPIC_LABEL']:
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


class CanonizerUpdateTopicPage(Page):
    def load_topic_history_page(self, topic_name):
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
        # Click on Manage/edit Topic
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-btn ant-btn-default btn-green')))
        except TimeoutException:
            pass
        self.hover(*UpdateTopicIdentifiers.MANAGE_EDIT_TOPIC_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.MANAGE_EDIT_TOPIC_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.TOPIC_HISTORY_TITLE)
        page_title = self.find_element(*UpdateTopicIdentifiers.TOPIC_HISTORY_TITLE).text
        if page_title == message['Update_Topic']['TOPIC_HISTORY_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_topic_name_on_topic_history_page(self, topic_name):
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
        # Click on Manage/edit Topic
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-btn ant-btn-default btn-green')))
        except TimeoutException:
            pass
        self.hover(*UpdateTopicIdentifiers.TOPIC_NAME_ON_CURRENT_TOPIC_RECORD)
        text1 = self.find_element(*UpdateTopicIdentifiers.TOPIC_NAME_ON_CURRENT_TOPIC_RECORD).text
        self.hover(*UpdateTopicIdentifiers.MANAGE_EDIT_TOPIC_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.MANAGE_EDIT_TOPIC_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.TOPIC_NAME_ON_HISTORY_PAGE)
        text2 = self.find_element(*UpdateTopicIdentifiers.TOPIC_NAME_ON_HISTORY_PAGE).text
        if text1 == text2:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Text not matching")

    def verify_submitter_nick_name_link_on_user_profile(self):
        self.hover(*UpdateTopicIdentifiers.SUBMITTER_NICK_NAME_LINK)
        text1 = self.find_element(*UpdateTopicIdentifiers.SUBMITTER_NICK_NAME_LINK).text
        self.find_element(*UpdateTopicIdentifiers.SUBMITTER_NICK_NAME_LINK).click()
        self.hover(*UpdateTopicIdentifiers.NICK_NAME_ON_PROFILE)
        text2 = self.find_element(*UpdateTopicIdentifiers.NICK_NAME_ON_PROFILE).text
        if text1 == text2:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Text not matching")

    def verify_submit_topic_update_button(self):
        self.hover(*UpdateTopicIdentifiers.SUBMIT_UPDATE)
        self.find_element(*UpdateTopicIdentifiers.SUBMIT_UPDATE).click()
        self.hover(*UpdateTopicIdentifiers.TOPIC_UPDATE_TITLE)
        page_title = self.find_element(*UpdateTopicIdentifiers.TOPIC_UPDATE_TITLE).text
        if page_title == message['Update_Topic']['TOPIC_UPDATE_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Title not found or is not matching")

    def update_topic_with_duplicate_name(self, duplicate_topic_name):
        self.verify_submit_topic_update_button()

        for i in range(0, 30):
            self.find_element(*UpdateTopicIdentifiers.UPDATE_TOPIC_NAME).send_keys(Keys.BACKSPACE)
        self.hover(*UpdateTopicIdentifiers.UPDATE_TOPIC_NAME)
        self.find_element(*UpdateTopicIdentifiers.UPDATE_TOPIC_NAME).send_keys(duplicate_topic_name)
        self.hover(*UpdateTopicIdentifiers.SUBMIT_UPDATE_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.SUBMIT_UPDATE_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.DUPLICATE_TOPIC_NAME_ERROR)
        error = self.find_element(*UpdateTopicIdentifiers.DUPLICATE_TOPIC_NAME_ERROR).text
        if error == message['Update_Topic']['DUPLICATE_TOPIC_NAME_ERROR']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Error not found or is not matching")

    def update_topic_name_and_verify_submit_update_button(self, topic_name):
        self.verify_submit_topic_update_button()

        for i in range(0, 30):
            self.find_element(*UpdateTopicIdentifiers.UPDATE_TOPIC_NAME).send_keys(Keys.BACKSPACE)
        self.hover(*UpdateTopicIdentifiers.UPDATE_TOPIC_NAME)
        self.find_element(*UpdateTopicIdentifiers.UPDATE_TOPIC_NAME).send_keys(topic_name)
        self.hover(*UpdateTopicIdentifiers.SUBMIT_UPDATE_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.SUBMIT_UPDATE_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.TOPIC_HISTORY_TITLE)
        title = self.find_element(*UpdateTopicIdentifiers.TOPIC_HISTORY_TITLE).text
        if title == message['Update_Topic']['TOPIC_HISTORY_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Error not found or is not matching")

    def verify_cancel_button_functionality_on_topic_update_page(self):
        self.verify_submit_topic_update_button()
        self.hover(*UpdateTopicIdentifiers.CANCEL_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.CANCEL_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.TOPIC_HISTORY_TITLE)
        page_title = self.find_element(*UpdateTopicIdentifiers.TOPIC_HISTORY_TITLE).text
        if page_title == message['Update_Topic']['TOPIC_HISTORY_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_preview_button_functionality_on_topic_update_page(self):
        self.verify_submit_topic_update_button()
        self.hover(*UpdateTopicIdentifiers.PREVIEW_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.PREVIEW_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.TOPIC_PREVIEW_TITLE)
        page_title = self.find_element(*UpdateTopicIdentifiers.TOPIC_PREVIEW_TITLE).text
        if page_title == message['Update_Topic']['TOPIC_PREVIEW_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_submitter_nick_name_on_preview_modal(self):
        self.verify_submit_topic_update_button()
        self.hover(*UpdateTopicIdentifiers.PREVIEW_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.PREVIEW_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.SUBMITTER_NICK_NAME_LINK_ON_PREVIEW_MODAL)
        text1 = self.find_element(*UpdateTopicIdentifiers.SUBMITTER_NICK_NAME_LINK_ON_PREVIEW_MODAL).text
        self.find_element(*UpdateTopicIdentifiers.SUBMITTER_NICK_NAME_LINK_ON_PREVIEW_MODAL).click()
        self.hover(*UpdateTopicIdentifiers.NICK_NAME_ON_PROFILE)
        text2 = self.find_element(*UpdateTopicIdentifiers.NICK_NAME_ON_PROFILE).text
        if text1 == text2:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Text not matching")

    def verify_cancel_button_on_preview_modal(self):
        self.verify_submit_topic_update_button()
        self.hover(*UpdateTopicIdentifiers.PREVIEW_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.PREVIEW_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.CANCEL_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.CANCEL_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.TOPIC_UPDATE_TITLE)
        error = self.find_element(*UpdateTopicIdentifiers.TOPIC_UPDATE_TITLE).text
        if error == message['Update_Topic']['TOPIC_UPDATE_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Error not found or is not matching")

    def verify_compare_topics_button_functionality(self):
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1).click()
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2).click()

        self.hover(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.TOPIC_HISTORY_COMPARISON_TITLE)
        page_title = self.find_element(*UpdateTopicIdentifiers.TOPIC_HISTORY_COMPARISON_TITLE).text
        if page_title == message['Update_Topic']['TOPIC_HISTORY_COMPARISON_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_agreement_link_on_topic_comparison_page(self):
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1).click()
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2).click()
        self.hover(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.AGREEMENT_LINK)
        self.find_element(*UpdateTopicIdentifiers.AGREEMENT_LINK).click()
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['CREATE_TOPIC_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Page not found")

    def verify_create_topic_button_functionality_on_topic_comparison_page(self):
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1).click()
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2).click()
        self.hover(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.CREATE_TOPIC_)
        self.find_element(*UpdateTopicIdentifiers.CREATE_TOPIC_).click()
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE_TITLE)
        page_title = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE_TITLE).text
        if page_title == message['Create_Topic']['NEW_TOPIC_PAGE_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Title not found or  is not matching")

    def verify_create_camp_button_functionality_on_topic_comparison_page(self):
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1).click()
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2).click()
        self.hover(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.CREATE_CAMP)
        self.find_element(*UpdateTopicIdentifiers.CREATE_CAMP).click()
        self.hover(*CreateCampIdentifiers.NEW_CAMP_TITLE)
        page_title = self.find_element(*CreateCampIdentifiers.NEW_CAMP_TITLE).text
        if page_title == message['Create_Camp']['CREATE_CAMP_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_back_arrow_icon_on_topic_comparison_page(self):
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX1).click()
        self.hover(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_CHECKBOX2).click()
        self.hover(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.COMPARE_TOPIC_BUTTON).click()
        self.hover(*UpdateTopicIdentifiers.BACK_ARROW_ICON)
        self.find_element(*UpdateTopicIdentifiers.BACK_ARROW_ICON).click()
        self.hover(*UpdateTopicIdentifiers.TOPIC_HISTORY_TITLE)
        page_title = self.find_element(*UpdateTopicIdentifiers.TOPIC_HISTORY_TITLE).text
        if page_title == message['Update_Topic']['TOPIC_HISTORY_TITLE']:
            return CanonizerUpdateTopicPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_view_this_version_button_functionality(self):
        self.hover(*UpdateTopicIdentifiers.VIEW_THIS_VERSION_BUTTON)
        self.find_element(*UpdateTopicIdentifiers.VIEW_THIS_VERSION_BUTTON).click()
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['CREATE_TOPIC_TITLE']:
            return CanonizerCreateNewTopic(self.driver)
        else:
            print("Page not found")












