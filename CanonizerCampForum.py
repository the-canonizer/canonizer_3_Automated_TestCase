import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CanonizerValidationCheckMessages import message
from CanonizerBase import Page
from Identifiers import CampForumIdentifiers, CreateTopicIdentifiers
from selenium.webdriver.common.keys import Keys
import string
import random
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import *
from selenium import webdriver




class CanonizerCampForumPage(Page):

    def driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def load_camp_forum_page(self, topic_name):
        self.driver.implicitly_wait(20)
        # Browse to Browse Page
        self.hover(*CampForumIdentifiers.BROWSE)
        self.find_element(*CampForumIdentifiers.BROWSE).click()

        # Click on Search Topic
        self.hover(*CampForumIdentifiers.SEARCH_TOPIC)
        self.find_element(*CampForumIdentifiers.SEARCH_TOPIC).send_keys(topic_name)
        self.find_element(*CampForumIdentifiers.SEARCH_TOPIC).send_keys(Keys.ENTER)
        #self.hover(*CampForumIdentifiers.SEARCH_ICON)
        #self.find_element(*CampForumIdentifiers.SEARCH_ICON).click()
        self.hover(*CampForumIdentifiers.TOPIC_CLICK)
        self.find_element(*CampForumIdentifiers.TOPIC_CLICK).click()


        self.find_element(*CampForumIdentifiers.CAMP_FORUM_BUTTON).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "Forum_cardTitle__VagbD")))
        return CanonizerCampForumPage(self.driver)

    def load_all_threads_page(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, "all-thread-btn").click()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, "ant-table-cell ant-table-cell-row-hover")))
        return CanonizerCampForumPage(self.driver)

    def load_my_threads_page(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, "my-thread-btn").click()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, "ant-table-cell ant-table-cell-row-hover")))
        return CanonizerCampForumPage(self.driver)

    def load_my_participation_page(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, "participate-btn").click()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, "ant-table-cell ant-table-cell-row-hover")))
        return CanonizerCampForumPage(self.driver)

    def load_top_10_threads_page(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, "most-rep-btn").click()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, "ant-table-cell ant-table-cell-row-hover")))
        return CanonizerCampForumPage(self.driver)

    def create_new_topic(self):
        try:
            WebDriverWait(self.driver, 8).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-btn ant-btn-default ant-btn-lg mb-3 btn')))
        except TimeoutException:
            pass
        self.hover(*CreateTopicIdentifiers.CREATE_NEW_TOPIC)
        self.find_element(*CreateTopicIdentifiers.CREATE_NEW_TOPIC).click()
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, '//*[@id="create_new_topic"]/div/div[1]/div[1]/div[2]/div[2]')))
        topic_name = ''.join(random.choices(string.ascii_uppercase +string.digits, k=7))
        print(topic_name)
        self.hover(*CreateTopicIdentifiers.TOPIC_NAME)
        self.find_element(*CreateTopicIdentifiers.TOPIC_NAME).send_keys("New Topic" + topic_name)
        self.find_element(*CreateTopicIdentifiers.CREATE_TOPIC_BUTTON).click()

    def check_no_thread_availability(self):
        self.driver.implicitly_wait(20)
        self.find_element(*CampForumIdentifiers.CAMP_FORUM_BUTTON).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "Forum_cardTitle__VagbD")))
        self.driver.find_element(By.ID, "all-thread-btn").click()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, "ant-empty ant-empty-normal")))
        return CanonizerCampForumPage(self.driver)

    def click_create_thread_button(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, "create-btn").click()
        time.sleep(10)
        return CanonizerCampForumPage(self.driver)

    def enter_thread_title(self, title):
        self.find_element(By.ID, "create_new_thread_thread_title").send_keys(title)


    def enter_nickname(self, nickname):
        self.hover(*CampForumIdentifiers.NICK_NAME)
        self.find_element(*CampForumIdentifiers.NICK_NAME).send_keys(nickname)

    def click_submit_button(self):
        self.driver.find_element(By.ID, "submit-btn").click()

    def create_thread(self, title):
        self.enter_thread_title(title)
        self.click_submit_button()

    def create_thread_with_valid_data(self, title):
        self.create_thread(title)
        self.hover(*CampForumIdentifiers.CAMP_FORUM_TITLE)
        return CanonizerCampForumPage(self.driver)


    def create_thread_with_blank_title_name(self, title):
        self.create_thread('')
        return CanonizerCampForumPage(self.driver)

    def create_thread_with_special_chars(self, title):
        self.create_thread(title)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Camp Forum"]')))
        self.hover(*CampForumIdentifiers.CAMP_FORUM_TITLE)
        page_title = self.find_element(*CampForumIdentifiers.CAMP_FORUM_TITLE).text
        if page_title == message['Camp_Forum']['CAMP_FORUM_TITLE']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Title not found or is not matching")

    def create_thread_with_blank_mandatory_fields(self, title):
        self.create_thread('')
        self.hover(*CampForumIdentifiers.ERROR_BLANK_TITLE)
        error = self.find_element(*CampForumIdentifiers.ERROR_BLANK_TITLE).text
        if error == message['Camp_Forum']['BLANK_TITLE_ERROR']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Title not found or is not matching")

    def create_thread_with_duplicate_title(self, title):
        self.create_thread(title)
        self.create_thread(title)
        self.hover(*CampForumIdentifiers.DUPLICATE_TITLE_ERROR)
        error = self.find_element(*CampForumIdentifiers.DUPLICATE_TITLE_ERROR).text
        if error == message['Camp_Forum']['DUPLICATE_THREAD']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Title not found or is not matching")

    def create_thread_with_valid_data_with_enter_key(self, title):
        self.driver.implicitly_wait(20)
        self.enter_thread_title(title)
        self.hover(By.ID, "submit-btn")
        self.driver.find_element(By.ID, "submit-btn").send_keys(Keys.ENTER)
        return CanonizerCampForumPage(self.driver)

    def create_thread_with_trailing_spaces(self, title):
        self.enter_thread_title(title)
        self.hover(*CampForumIdentifiers.SUBMIT_THREAD)
        self.find_element(*CampForumIdentifiers.SUBMIT_THREAD).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Camp Forum"]')))
        self.hover(*CampForumIdentifiers.CAMP_FORUM_TITLE)
        page_title = self.find_element(*CampForumIdentifiers.CAMP_FORUM_TITLE).text
        if page_title == message['Camp_Forum']['CAMP_FORUM_TITLE']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Title not found or is not matching")

    def thread_page_mandatory_fields_are_marked_with_asterisk(self):
        return \
            self.find_element(*CampForumIdentifiers.THREAD_TITLE_ASTERISK) and \
            self.find_element(*CampForumIdentifiers.NICK_NAME_ASTERISK)

    def click_on_back_button(self):
        self.hover(*CampForumIdentifiers.BACK_BUTTON)
        self.find_element(*CampForumIdentifiers.BACK_BUTTON).click()
        self.hover(*CampForumIdentifiers.CAMP_FORUM_TITLE)
        page_title = self.find_element(*CampForumIdentifiers.CAMP_FORUM_TITLE).text
        if page_title == message['Camp_Forum']['CAMP_FORUM_TITLE']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Title not found or is not matching")

    def load_edit_thread_page(self):
        self.driver.implicitly_wait(10)
        self.load_my_threads_page()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "Forum_cardTitle__VagbD")))
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]").click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "submit-btn")))
        return CanonizerCampForumPage(self.driver)

    def edit_thread(self, title):
        self.driver.implicitly_wait(10)
        self.load_my_threads_page()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "Forum_cardTitle__VagbD")))
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/a/span").click()
        # self.find_element(*CampForumIdentifiers.EDIT_THREAD_ICON).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "submit-btn")))
        self.driver.find_element(By.ID, "create_new_thread_thread_title").send_keys(title)
        return CanonizerCampForumPage(self.driver)

    def update_thread_title(self, title):
        self.load_my_threads_page()
        self.edit_thread(title)
        self.click_submit_button()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Camp Forum"]')))
        page_title = self.find_element(*CampForumIdentifiers.CAMP_FORUM_TITLE).text
        if page_title == message['Camp_Forum']['CAMP_FORUM_TITLE']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Title not found or is not matching")

    def edit_thread_with_duplicate_title(self, title):
        self.load_my_threads_page()
        self.edit_thread(title)
        self.click_submit_button()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Camp Forum"]')))
        error = self.find_element(*CampForumIdentifiers.DUPLICATE_TITLE_ERROR).text
        if error == message['Camp_Forum']['DUPLICATE_THREAD']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Title not found or is not matching")

    def edit_thread_with_special_chars(self, title):
        self.load_my_threads_page()
        self.edit_thread(title)
        self.click_submit_button()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Camp Forum"]')))
        page_title = self.find_element(*CampForumIdentifiers.CAMP_FORUM_TITLE).text
        if page_title == message['Camp_Forum']['CAMP_FORUM_TITLE']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Title not found or is not matching")

    def click_on_edit_back_button(self):
        self.load_my_threads_page()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "Forum_cardTitle__VagbD")))
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]/a/a/span").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "submit-btn")))
        self.driver.find_element(By.ID, "back-btn").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "Forum_cardTitle__VagbD")))
        return CanonizerCampForumPage(self.driver)

    def load_thread_posts_page(self):
        self.load_all_threads_page()
        self.driver.find_element(By.CLASS_NAME, "Forum_threadListTitle__eSVW8").click()
        return CanonizerCampForumPage(self.driver)

    def enter_post_reply(self, reply):
        self.hover(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[1]/div/div/div[2]/div[1]")
        self.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[1]/div/div/div[2]/div[1]").send_keys(reply)

    def click_post_submit_button(self):
        self.hover(By.ID, "submit-btn")
        self.find_element(By.ID, "submit-btn").click()

    def post_thread_reply(self, reply):
        self.enter_post_reply(reply)
        self.click_post_submit_button()

    def thread_post_with_valid_data(self, reply):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "Forum_cardTitle__VagbD")))
        self.driver.implicitly_wait(20)
        self.post_thread_reply(reply)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "Forum_cardTitle__VagbD")))
        return CanonizerCampForumPage(self.driver)

    def thread_post_with_empty_reply(self, reply):
        self.post_thread_reply(reply)
        self.hover(*CampForumIdentifiers.EMPTY_REPLY_ERROR)
        error = self.find_element(*CampForumIdentifiers.EMPTY_REPLY_ERROR).text
        if error == message['Camp_Forum']['EMPTY_POST_REPLY']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Error not found or is not matching")

    def click_on_post_back_button(self):
        self.hover(*CampForumIdentifiers.BACK_BUTTON)
        self.find_element(*CampForumIdentifiers.BACK_BUTTON).click()
        self.hover(*CampForumIdentifiers.CAMP_FORUM_TITLE)
        page_title = self.find_element(*CampForumIdentifiers.CAMP_FORUM_TITLE).text
        if page_title == message['Camp_Forum']['CAMP_FORUM_TITLE']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Title not found or is not matching")

    def verify_nick_name_link_on_post_page(self):
        self.hover(*CampForumIdentifiers.NICK_NAME_LINK_ON_POST_PAGE)
        self.find_element(*CampForumIdentifiers.NICK_NAME_LINK_ON_POST_PAGE).click()
        self.hover(*CampForumIdentifiers.USER_PROFILE_TITLE)
        page_title = self.find_element(*CampForumIdentifiers.USER_PROFILE_TITLE).text
        if page_title == message['Camp_Forum']['USER_PROFILE_TITLE']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Title not found or is not matching")

    def edit_reply_to_thread(self, reply):
        self.hover(*CampForumIdentifiers.EDIT_REPLY)
        self.find_element(*CampForumIdentifiers.EDIT_REPLY).click()
        self.hover(*CampForumIdentifiers.REPLY_FIELD)
        self.find_element(*CampForumIdentifiers.REPLY_FIELD).clear()

        self.find_element(*CampForumIdentifiers.REPLY_FIELD).send_keys(reply)
        self.click_post_submit_button()
        self.hover(*CampForumIdentifiers.REPLY_UPDATED_MESSAGE)
        success_message = self.find_element(*CampForumIdentifiers.REPLY_UPDATED_MESSAGE).text
        if success_message == message['Camp_Forum']['UPDATE_POST_SUCCESS_MESSAGE']:
            return CanonizerCampForumPage(self.driver)

    def verify_edit_post_icon(self):
        self.hover(*CampForumIdentifiers.THREAD_LINK)
        self.find_element(*CampForumIdentifiers.THREAD_LINK).click()
        self.hover(*CampForumIdentifiers.EDIT_POST_ICON)
        self.find_element(*CampForumIdentifiers.EDIT_POST_ICON).click()
        self.hover(*CampForumIdentifiers.VERIFY_POST_REPLY)
        text1 = self.find_element(*CampForumIdentifiers.VERIFY_POST_REPLY).text
        self.hover(*CampForumIdentifiers.POST_REPLY)
        text2 = self.find_element(*CampForumIdentifiers.POST_REPLY).text
        if text1 == text2:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Post edit title not matching")

    def verify_post_edit_functionality(self, reply):
        self.hover(*CampForumIdentifiers.THREAD_LINK)
        self.find_element(*CampForumIdentifiers.THREAD_LINK).click()
        self.hover(*CampForumIdentifiers.EDIT_POST_ICON)
        self.find_element(*CampForumIdentifiers.EDIT_POST_ICON).click()
        for i in range(0, 100):
            self.find_element(*CampForumIdentifiers.POST_REPLY).send_keys(Keys.BACKSPACE)
        self.find_element(*CampForumIdentifiers.POST_REPLY).send_keys(reply)
        self.hover(*CampForumIdentifiers.POST_SUBMIT)
        self.find_element(*CampForumIdentifiers.POST_SUBMIT).click()
        validation_message = self.find_element(*CampForumIdentifiers.POST_UPDATE_MESSAGE).text
        if validation_message == message['Camp_Forum']['POST_UPDATE_MESSAGE']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Title not found or is not matching")

    def test_verify_post_delete_functionality(self):
        self.hover(*CampForumIdentifiers.THREAD_LINK)
        self.find_element(*CampForumIdentifiers.THREAD_LINK).click()
        self.hover(*CampForumIdentifiers.DELETE_POST_ICON)
        self.find_element(*CampForumIdentifiers.DELETE_POST_ICON).click()
        self.hover(*CampForumIdentifiers.DELETE_CONFIRM)
        self.find_element(*CampForumIdentifiers.DELETE_CONFIRM).click()
        try:
            WebDriverWait(self.driver, 6).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'ant-message-notice-content')))
        except TimeoutException:
            pass
        validation_message = self.find_element(*CampForumIdentifiers.POST_DELETE_MESSAGE).text
        if validation_message == message['Camp_Forum']['POST_DELETE_MESSAGE']:
            return CanonizerCampForumPage(self.driver)
        else:
            print("Message not found or is not matching")




















