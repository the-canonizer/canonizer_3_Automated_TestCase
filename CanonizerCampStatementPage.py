import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from CanonizerBase import Page
from Identifiers import CampForumIdentifiers, CampStatementIdentifiers, CreateTopicIdentifiers
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from CanonizerValidationCheckMessages import message


class CanonizerCampStatementPage(Page):

    def load_new_topic_page(self):
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
                return CanonizerCampStatementPage(self.driver)
            else:
                print("Title not found or  is not matching")

    def enter_topic_nick_name(self, nickname):
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
        self.enter_topic_nick_name(nickname)
        self.enter_topic_name(topic_name)
        self.enter_namespace(namespace)
        self.enter_summary(summary)

    def create_topic(self, nickname, topic_name, namespace, summary):
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="create_new_topic"]/div/div[1]/div[1]/div[2]/div[2]')))
        self.entering_data_fields(nickname, topic_name, namespace, summary)
        self.click_create_topic_button()

    def create_topic_with_valid_data(self, nickname, topic_name, namespace, summary):
        self.create_topic(nickname, topic_name, namespace, summary)
        self.hover(*CreateTopicIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CreateTopicIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Create_Topic']['CREATE_TOPIC_TITLE']:
            return CanonizerCampStatementPage(self.driver)
        else:
            print("Page not found")

    def load_add_camp_statement_page(self):
        # Click on Create New Camp Statement Button
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-btn ant-btn-default btn-green')))
        except TimeoutException:
            pass
        self.hover(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON)
        self.find_element(*CampStatementIdentifiers.ADD_STATEMENT_BUTTON).click()
        self.hover(*CampStatementIdentifiers.ADD_STATEMENT_TITLE)
        page_title = self.find_element(*CampStatementIdentifiers.ADD_STATEMENT_TITLE).text
        if page_title == message['Add_Camp_Statement']['ADD_CAMP_STATEMENT_TITLE']:
            return CanonizerCampStatementPage(self.driver)
        else:
            print("Title not found or is not matching")

    def enter_nick_name(self, nickname):
        self.find_element(*CampStatementIdentifiers.NICK_NAME).send_keys(nickname)

    def enter_camp_statement(self, statement):
        self.find_element(*CampStatementIdentifiers.STATEMENT).send_keys(statement)

    def enter_edit_summary(self, edit_summary):
        self.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).send_keys(edit_summary)

    def click_submit_button(self):
        self.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_BUTTON).click()

    def create_camp_statement(self, nickname, statement, edit_summary):
        self.enter_nick_name(nickname)
        self.enter_camp_statement(statement)
        self.enter_edit_summary(edit_summary)
        self.click_submit_button()

    def submit_statement_with_blank_statement(self, nickname, edit_summary):
        self.create_camp_statement(nickname, '', edit_summary)
        self.hover(*CampStatementIdentifiers.STATEMENT_FIELD_ERROR)
        error = self.find_element(*CampStatementIdentifiers.STATEMENT_FIELD_ERROR).text
        if error == message['Add_Camp_Statement']['STATEMENT_FIELD_ERROR']:
            return CanonizerCampStatementPage(self.driver)
        else:
            print("Error not found or is not matching")

    def add_camp_statement_page(self, nickname, statement, edit_summary):
        time.sleep(6)
        self.create_camp_statement(nickname, statement, edit_summary)
        self.hover(*CampStatementIdentifiers.CAMP_STATEMENT_HISTORY)
        page_title = self.find_element(*CampStatementIdentifiers.CAMP_STATEMENT_HISTORY).text
        if page_title == message['Add_Camp_Statement']['CAMP_HISTORY_PAGE']:
            return CanonizerCampStatementPage(self.driver)
        else:
            print("Title not found or is not matching")

    def add_camp_statement_page_mandatory_fields_are_marked_with_asterisk(self):
        return \
            self.find_element(*CampStatementIdentifiers.NICK_NAME_ASTERISK) and \
            self.find_element(*CampStatementIdentifiers.STATEMENT_ASTERISK)

    def add_camp_statement_page_without_mandatory_fields(self, statement):
        self.enter_camp_statement(statement)
        self.click_submit_button()
        self.hover(*CampStatementIdentifiers.STATEMENT_FIELD_ERROR)
        error = self.find_element(*CampStatementIdentifiers.STATEMENT_FIELD_ERROR).text
        if error == message['Add_Camp_Statement']['STATEMENT_FIELD_ERROR']:
            return CanonizerCampStatementPage(self.driver)
        else:
            print("Error not found or is not matching")

    def add_camp_statement_page_valid_data(self, statement, edit_summary):
        self.enter_camp_statement(statement)
        self.enter_edit_summary(edit_summary)
        self.click_submit_button()
        self.hover(*CampStatementIdentifiers.CAMP_STATEMENT_HISTORY)
        page_title = self.find_element(*CampStatementIdentifiers.CAMP_STATEMENT_HISTORY).text
        if page_title == message['Add_Camp_Statement']['CAMP_HISTORY_PAGE']:
            return CanonizerCampStatementPage(self.driver)
        else:
            print("Title not found or is not matching")

    def click_on_statement_cancel_button(self):
        self.hover(*CampStatementIdentifiers.CANCEL_BUTTON)
        self.find_element(*CampStatementIdentifiers.CANCEL_BUTTON).click()
        self.hover(*CampStatementIdentifiers.TOPIC_PAGE)
        topic_page_confirmation = self.find_element(*CampStatementIdentifiers.TOPIC_PAGE).text
        if topic_page_confirmation == message['Add_Camp_Statement']['CANCEL_STATEMENT_TITLE']:
            return CanonizerCampStatementPage(self.driver)
        else:
            print("Page not found")

    def click_on_statement_preview_button(self):
        self.hover(*CampStatementIdentifiers.PREVIEW_PAGE)
        self.find_element(*CampStatementIdentifiers.PREVIEW_PAGE).click()
        self.hover(*CampStatementIdentifiers.PREVIEW_MODAL_TITLE)
        page_title = self.find_element(*CampStatementIdentifiers.PREVIEW_MODAL_TITLE).text
        if page_title == message['Add_Camp_Statement']['PREVIEW_MODAL_TITLE']:
            return CanonizerCampStatementPage(self.driver)
        else:
            print("Title not found or is not matching")

    def create_statement_on_click_preview_button(self):
        self.hover(*CampStatementIdentifiers.PREVIEW_PAGE)
        self.find_element(*CampStatementIdentifiers.PREVIEW_PAGE).click()
        self.hover(*CampStatementIdentifiers.SUBMIT_PREVIEW)
        self.find_element(*CampStatementIdentifiers.SUBMIT_PREVIEW).click()
        self.hover(*CampStatementIdentifiers.PREVIEW_MODAL_TITLE)
        page_title = self.find_element(*CampStatementIdentifiers.PREVIEW_MODAL_TITLE).text
        if page_title == message['Add_Camp_Statement']['PREVIEW_MODAL_TITLE']:
            return CanonizerCampStatementPage(self.driver)
        else:
            print("Title not found or is not matching")


class CanonizerEditCampStatementPage(Page):
    def load_edit_camp_statement_page(self, topic_name):
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

        # Click on Edit Camp Statement Button Topic
        time.sleep(6)
        self.hover(*CampStatementIdentifiers.EDIT_CAMP_STATEMENT_BUTTON)
        self.find_element(*CampStatementIdentifiers.EDIT_CAMP_STATEMENT_BUTTON).click()
        self.hover(*CampStatementIdentifiers.CAMP_HISTORY_TITLE)
        page_title = self.find_element(*CampStatementIdentifiers.CAMP_HISTORY_TITLE).text
        if page_title == message['Add_Camp_Statement']['CAMP_HISTORY_TITLE']:
            return CanonizerEditCampStatementPage(self.driver)
        else:
            print("Title not found or is not matching")

    def submit_statement_update_with_only_mandatory_fields(self, statement):
        self.hover(*CampStatementIdentifiers.SUBMIT_STATEMENT_UPDATE)
        self.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_UPDATE).click()
        WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, 'statement')))
        for i in range(0, 100):
            self.find_element(*CampStatementIdentifiers.STATEMENT).send_keys(Keys.BACKSPACE)
        self.find_element(*CampStatementIdentifiers.STATEMENT).send_keys(statement)
        self.find_element(*CampStatementIdentifiers.SUBMIT_UPDATE).click()
        self.hover(*CampStatementIdentifiers.CAMP_HISTORY_TITLE)
        page_title = self.find_element(*CampStatementIdentifiers.CAMP_HISTORY_TITLE).text
        if page_title == message['Add_Camp_Statement']['CAMP_HISTORY_TITLE']:
            return CanonizerEditCampStatementPage(self.driver)
        else:
            print("Title not found or is not matching")

    def enter_nick_name(self, nickname):
        self.find_element(*CampStatementIdentifiers.NICK_NAME).send_keys(nickname)

    def enter_camp_statement(self, statement):
        self.find_element(*CampStatementIdentifiers.STATEMENT).send_keys(statement)

    def enter_edit_summary(self, edit_summary):
        self.find_element(*CampStatementIdentifiers.EDIT_SUMMARY).send_keys(edit_summary)

    def update_camp_statement(self, nickname, statement, edit_summary):
        self.enter_nick_name(nickname)
        self.enter_camp_statement(statement)
        self.enter_edit_summary(edit_summary)
        self.find_element(*CampStatementIdentifiers.SUBMIT_UPDATE).click()

    def submit_statement_update_with_blank_statement(self, nickname, statement, edit_summary):
        self.hover(*CampStatementIdentifiers.SUBMIT_STATEMENT_UPDATE)
        self.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_UPDATE).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'statement')))
        for i in range(0, 100):
            self.find_element(*CampStatementIdentifiers.STATEMENT).send_keys(Keys.BACKSPACE)
            self.update_camp_statement(nickname, ' ', edit_summary)
            self.hover(*CampStatementIdentifiers.STATEMENT_FIELD_ERROR)
            error = self.find_element(*CampStatementIdentifiers.STATEMENT_FIELD_ERROR).text
            if error == message['Add_Camp_Statement']['STATEMENT_FIELD_ERROR']:
                return CanonizerEditCampStatementPage(self.driver)
            else:
                print("Error not found or is not matching")

    def verify_editable_fields_on_edit_camp_statement_page(self):
        self.hover(*CampStatementIdentifiers.SUBMIT_STATEMENT_UPDATE)
        self.find_element(*CampStatementIdentifiers.SUBMIT_STATEMENT_UPDATE).click()
        nickname_element = self.find_element(*CampStatementIdentifiers.NICK_NAME)
        statement_element = self.find_element(*CampStatementIdentifiers.STATEMENT)
        edit_summary_element = self.find_element(*CampStatementIdentifiers.EDIT_SUMMARY)
        if nickname_element.is_enabled() and statement_element.is_enabled() and edit_summary_element.is_enabled():
            return CanonizerEditCampStatementPage(self.driver)

    def load_edit_camp_statement_view_this_version(self):
        self.hover(*CampStatementIdentifiers.VIEW_THIS_VERSION_BUTTON)
        self.find_element(*CampStatementIdentifiers.VIEW_THIS_VERSION_BUTTON).click()
        self.hover(*CampStatementIdentifiers.TOPIC_PAGE)
        title = self.find_element(*CampStatementIdentifiers.TOPIC_PAGE).text
        if title == message['Add_Camp_Statement']['CANCEL_STATEMENT_TITLE']:
            return CanonizerEditCampStatementPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_history_on_edit_camp_statement_page(self):
        try:
            r_element = self.find_element(*CampStatementIdentifiers.OBJECTED_COLOR)
            r_bg = r_element.value_of_css_property("background-color")
            g_element = self.find_element(*CampStatementIdentifiers.LIVE_COLOR)
            g_bg = g_element.value_of_css_property("background-color")
            y_element = self.find_element(*CampStatementIdentifiers.IN_REVIEW)
            y_bg = y_element.value_of_css_property("background-color")
            b_element = self.find_element(*CampStatementIdentifiers.OLD)
            b_bg = b_element.value_of_css_property("background-color")
            if r_bg == 'rgba(255, 0, 0, 0.5)' and g_bg == 'rgba(0, 128, 0, 0.5)' and y_bg == 'rgba(255, 255, 0, 1)' and b_bg == 'rgba(21, 20, 237, 1)':
                return CanonizerEditCampStatementPage(self.driver)
        except NoSuchElementException:
            return False

    def compare_two_statements(self):
        self.hover(*CampStatementIdentifiers.COMPARE_STATEMENT1)
        self.find_element(*CampStatementIdentifiers.COMPARE_STATEMENT1).click()
        self.hover(*CampStatementIdentifiers.COMPARE_STATEMENT2)
        self.find_element(*CampStatementIdentifiers.COMPARE_STATEMENT2).click()
        self.hover(*CampStatementIdentifiers.COMPARE_STATEMENT_BUTTON)
        self.find_element(*CampStatementIdentifiers.COMPARE_STATEMENT_BUTTON).click()
        self.hover(*CampStatementIdentifiers.STATEMENT_COMPARE_HISTORY_TITLE)
        title = self.find_element(*CampStatementIdentifiers.STATEMENT_COMPARE_HISTORY_TITLE).text
        if title == message['Add_Camp_Statement']['STATEMENT_COMPARE_HISTORY_TITLE']:
            return CanonizerEditCampStatementPage(self.driver)
        else:
            print("Title not found or is not matching")
















