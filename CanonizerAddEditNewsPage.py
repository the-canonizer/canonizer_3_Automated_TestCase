import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CanonizerValidationCheckMessages import message
from CanonizerBase import Page
from Identifiers import CampForumIdentifiers, AddNewsIdentifiers
from selenium.webdriver import Keys
import string
import random


class CanonizerAddNewsPage(Page):
    def load_add_news_page(self, topic_name):
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
        self.find_element(*CampForumIdentifiers.SEARCH_TOPIC).send_keys(Keys.ENTER)
        self.hover(*CampForumIdentifiers.TOPIC_CLICK)
        self.find_element(*CampForumIdentifiers.TOPIC_CLICK).click()

        # Click on Add News Link
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'ant-btn ant-btn-primary topicDetails_btnCampForum__xiKmO')))
        except TimeoutException:
            pass
        self.find_element(*AddNewsIdentifiers.ADD_NEWS_LINK).click()
        self.hover(*AddNewsIdentifiers.ADD_NEWS_PAGE_TITLE)
        page_title = self.find_element(*AddNewsIdentifiers.ADD_NEWS_PAGE_TITLE).text
        if page_title == message['Add_News']['ADD_NEWS_PAGE_TITLE']:
            return CanonizerAddNewsPage(self.driver)
        else:
            print("Title not found or is not matching")

    def enter_display_text(self, display_text):
        self.find_element(*AddNewsIdentifiers.DISPLAY_TEXT).send_keys(display_text)

    def enter_link(self, link):
        self.find_element(*AddNewsIdentifiers.LINK).send_keys(link)

    def click_create_news_button(self):
        self.find_element(*AddNewsIdentifiers.CREATE_NEWS_BUTTON).click()

    def check_available_for_child_camps(self):
        self.find_element(*AddNewsIdentifiers.AVAILABLE_FOR_CHILD_CAMP).click()

    def create_news(self, display_text, link):
        self.enter_display_text(display_text)
        self.enter_link(link)
        self.check_available_for_child_camps()
        self.click_create_news_button()

    def create_news_with_valid_data(self, display_text, link):
        self.create_news(display_text, link)
        self.hover(*AddNewsIdentifiers.NEWS_ADDED)
        page_title = self.find_element(*AddNewsIdentifiers.NEWS_ADDED).text
        if page_title == message['Add_News']['NEWS_ADDED']:
            return CanonizerAddNewsPage(self.driver)
        else:
            print("Title not found or is not matching")

    def add_news_page_mandatory_fields_are_marked_with_asterisk(self):
        try:
            WebDriverWait(self.driver, 8).until(
                EC.visibility_of_element_located((By.XPATH, '//div[text()="Add News"]')))
        except TimeoutException:
            pass

        return \
            self.find_element(*AddNewsIdentifiers.DISPLAY_TEXT_ASTERISK) and \
            self.find_element(*AddNewsIdentifiers.LINK_ASTERISK) and \
            self.find_element(*AddNewsIdentifiers.NICKNAME_ASTERISK)

    def create_news_with_blank_display_text(self, link):
        self.create_news('', link)
        self.hover(*AddNewsIdentifiers.BLANK_DISPLAY_TEXT_ERROR)
        error = self.find_element(*AddNewsIdentifiers.BLANK_DISPLAY_TEXT_ERROR).text
        if error == message['Add_News']['BLANK_DISPLAY_TEXT_ERROR']:
            return CanonizerAddNewsPage(self.driver)
        else:
            print("Title not found or is not matching")

    def create_news_with_blank_link(self, display_text):
        self.create_news(display_text, '')
        self.hover(*AddNewsIdentifiers.BLANK_LINK_ERROR)
        error = self.find_element(*AddNewsIdentifiers.BLANK_LINK_ERROR).text
        if error == message['Add_News']['BLANK_LINK_ERROR']:
            return CanonizerAddNewsPage(self.driver)
        else:
            print("Title not found or is not matching")

    def create_new_with_blank_fields(self, link, display_text):
        self.create_news(link, display_text)
        self.hover(*AddNewsIdentifiers.BLANK_DISPLAY_TEXT_ERROR)
        error_text = self.find_element(*AddNewsIdentifiers.BLANK_DISPLAY_TEXT_ERROR).text
        self.hover(*AddNewsIdentifiers.BLANK_LINK_ERROR)
        error_link = self.find_element(*AddNewsIdentifiers.BLANK_LINK_ERROR).text
        if error_text == message['Add_News']['BLANK_DISPLAY_TEXT_ERROR'] and error_link == message['Add_News']['BLANK_LINK_ERROR']:
            return CanonizerAddNewsPage(self.driver)
        else:
            print("Error not found or not matching")

    def click_add_news_cancel_button(self):
        self.hover(*AddNewsIdentifiers.CANCEL_BUTTON)
        self.find_element(*AddNewsIdentifiers.CANCEL_BUTTON).click()
        self.hover(*AddNewsIdentifiers.TOPIC_PAGE)
        heading = self.find_element(*AddNewsIdentifiers.TOPIC_PAGE).text
        if heading == message['Add_News']['CANCEL_NEWS_TITLE']:
            return CanonizerAddNewsPage(self.driver)
        else:
            print("Title not found or is not matching")

    def create_news_with_invalid_link_format(self, display_text, link):
        self.create_news(display_text, link)
        self.hover(*AddNewsIdentifiers.INVALID_LINK)
        error_text = self.find_element(*AddNewsIdentifiers.INVALID_LINK).text
        if error_text == message['Add_News']['INVALID_LINK_ERROR']:
            return CanonizerAddNewsPage(self.driver)
        else:
            print("Error not found or not matching")

    def create_news_with_enter_key(self, display_text, link):
        self.enter_display_text(display_text)
        self.enter_link(link)
        self.check_available_for_child_camps()
        self.find_element(*AddNewsIdentifiers.CREATE_NEWS_BUTTON).send_keys(Keys.ENTER)
        self.hover(*AddNewsIdentifiers.NEWS_ADDED)
        page_title = self.find_element(*AddNewsIdentifiers.NEWS_ADDED).text
        if page_title == message['Add_News']['NEWS_ADDED']:
            return CanonizerAddNewsPage(self.driver)
        else:
            print("Title not found or is not matching")

    def create_news_with_duplicate_data(self, display_text, link):
        self.create_news(display_text, link)
        self.hover(*AddNewsIdentifiers.NEWS_ADDED)
        page_title = self.find_element(*AddNewsIdentifiers.NEWS_ADDED).text
        if page_title == message['Add_News']['NEWS_ADDED']:
            return CanonizerAddNewsPage(self.driver)
        else:
            print("Title not found or is not matching")

    def create_news_with_trailing_spaces(self, display_text, link):
        self.create_news(display_text, link)
        self.hover(*AddNewsIdentifiers.NEWS_ADDED)
        page_title = self.find_element(*AddNewsIdentifiers.NEWS_ADDED).text
        if page_title == message['Add_News']['NEWS_ADDED']:
            return CanonizerAddNewsPage(self.driver)
        else:
            print("Title not found or is not matching")


class CanonizerEditNewsPage(Page):
    window_scroll = "window.scrollTo(0, document.body.scrollHeight);"

    def load_edit_news_page(self, topic_name):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'siteHeader_navWrap__yilWi false')))
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
            # Click on Edit News
            self.hover(*AddNewsIdentifiers.EDIT_NEWS)
            self.find_element(*AddNewsIdentifiers.EDIT_NEWS).click()
            self.driver.execute_script(self.window_scroll)
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((By.ID, 'news-edit-btn')))
            self.find_element(*AddNewsIdentifiers.EDIT_ICON).click()
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-card-head-title')))
            page_title = self.find_element(*AddNewsIdentifiers.EDIT_NEWS_TITlE).text
            if page_title == message['Edit_News']['EDIT_NEWS_TITLE']:
                return CanonizerEditNewsPage(self.driver)
            else:
                print("Title not found or is not matching")

    def update_display_text(self, display_text):
        self.find_element(*AddNewsIdentifiers.DISPLAY_TEXT).send_keys(display_text)

    def update_link(self, link):
        self.find_element(*AddNewsIdentifiers.LINK).send_keys(link)

    def click_create_news_button(self):
        self.find_element(*AddNewsIdentifiers.CREATE_NEWS_BUTTON).click()

    def update_available_for_child_camps(self):
        self.find_element(*AddNewsIdentifiers.AVAILABLE_FOR_CHILD_CAMP).click()

    def update_news(self, display_text, link):
        self.update_display_text(display_text)
        self.update_link(link)
        self.update_available_for_child_camps()
        self.click_create_news_button()

    def update_news_with_blank_display_text(self, link,):
        self.find_element(*AddNewsIdentifiers.DISPLAY_TEXT).clear()
        self.update_news('', link)
        self.hover(*AddNewsIdentifiers.BLANK_DISPLAY_TEXT_ERROR)
        error = self.find_element(*AddNewsIdentifiers.BLANK_DISPLAY_TEXT_ERROR).text
        if error == message['Add_News']['BLANK_DISPLAY_TEXT_ERROR']:
            return CanonizerEditNewsPage(self.driver)
        else:
            print("Title not found or is not matching")

    def update_news_with_blank_link(self, display_text):
        self.find_element(*AddNewsIdentifiers.LINK).clear()
        self.update_news(display_text, '')
        self.hover(*AddNewsIdentifiers.BLANK_LINK_ERROR)
        error = self.find_element(*AddNewsIdentifiers.BLANK_LINK_ERROR).text
        if error == message['Add_News']['BLANK_LINK_ERROR']:
            return CanonizerEditNewsPage(self.driver)
        else:
            print("Title not found or is not matching")

    def click_edit_news_cancel_button(self):
        self.hover(*AddNewsIdentifiers.EDIT_CANCEL_BUTTON)
        self.find_element(*AddNewsIdentifiers.EDIT_CANCEL_BUTTON).click()
        self.hover(AddNewsIdentifiers.EDIT_NEWS_TITlE)
        self.hover(*AddNewsIdentifiers.TOPIC_PAGE)
        heading = self.find_element(*AddNewsIdentifiers.TOPIC_PAGE).text
        if heading == message['Add_News']['CANCEL_NEWS_TITLE']:
            return CanonizerEditNewsPage(self.driver)



