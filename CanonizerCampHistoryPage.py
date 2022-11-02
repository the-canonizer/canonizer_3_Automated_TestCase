import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from CanonizerBase import Page
from Identifiers import CampForumIdentifiers, CampHistoryIdentifiers
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from CanonizerValidationCheckMessages import message


class CanonizerCampHistoryPage(Page):

    def load_topic_page(self, topic_name):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'siteHeader_navWrap__yilWi false')))
        except TimeoutException:
            pass
        # Browse to Browse Page
        self.hover(*CampForumIdentifiers.BROWSE)
        self.find_element(*CampForumIdentifiers.BROWSE).click()

        # Click on Search Topic
        self.hover(*CampHistoryIdentifiers.NAMESPACE)
        self.find_element(*CampHistoryIdentifiers.NAMESPACE).click()
        self.find_element(*CampHistoryIdentifiers.NAMESPACE_ALL).click()
        self.hover(*CampForumIdentifiers.SEARCH_TOPIC)
        self.find_element(*CampForumIdentifiers.SEARCH_TOPIC).send_keys(topic_name)
        self.hover(*CampForumIdentifiers.SEARCH_ICON)
        self.find_element(*CampForumIdentifiers.SEARCH_ICON).click()
        self.hover(*CampHistoryIdentifiers.HISTORY_TOPIC)
        self.find_element(*CampHistoryIdentifiers.HISTORY_TOPIC).click()
        return CanonizerCampHistoryPage

    def load_topic_history_page(self):
        self.hover(*CampHistoryIdentifiers.TOPIC_EDIT_BUTTON)
        self.find_element(*CampHistoryIdentifiers.TOPIC_EDIT_BUTTON).click()
        self.hover(*CampHistoryIdentifiers.TOPIC_HISTORY_TITLE)
        page_title = self.find_element(*CampHistoryIdentifiers.TOPIC_HISTORY_TITLE).text
        if page_title == message['Camp_History']['TOPIC_HISTORY_TITLE']:
            return CanonizerCampHistoryPage(self.driver)
        else:
            print("Title not found or is not matching")

    def load_camp_history_page(self):
        self.hover(*CampHistoryIdentifiers.CAMP_EDIT_BUTTON)
        self.find_element(*CampHistoryIdentifiers.CAMP_EDIT_BUTTON).click()
        self.hover(*CampHistoryIdentifiers.TOPIC_HISTORY_TITLE)
        page_title = self.find_element(*CampHistoryIdentifiers.TOPIC_HISTORY_TITLE).text
        if page_title == message['Camp_History']['TOPIC_HISTORY_TITLE']:
            return CanonizerCampHistoryPage(self.driver)
        else:
            print("Title not found or is not matching")

