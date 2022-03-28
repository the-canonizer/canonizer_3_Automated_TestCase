from selenium.webdriver.common.keys import Keys
from CanonizerBase import Page
from Identifiers import *
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
import urllib.request
import urllib.error

from datetime import datetime
from time import time


# Depends on the page functionality we can have more functions for new classes
#

##########################
#  Tests For Main Page   #
##########################

class CanonizerMainPage(Page):
    """
    Class Name: CanonizerMainPage
    Description: To load the main page and to navigate or load load pages for other URLs.

    Attributes: None
    """

    def check_home_page_loaded(self):
        """ To check if the Canonizer Home page loads properly"""
        if self.find_element(*HomePageIdentifiers.BODY):
            return CanonizerHomePage(self.driver)

    # def check_load_all_topic_text(self):
    #     """
    #     Verify the text to load all the Topics should be "Load All Topics"
    #
    #     :return:
    #         "Load All Topics" String to the main program
    #     """
    #     return self.find_element(*HomePageIdentifiers.LOADALLTOPICS).text

    def click_what_is_canonizer_page_link(self):
        """
        This Function is to verify if the canonizer main page loads properly
        :return:
            Return the result to the main page.check_home_page_loaded
        """
        self.hover(*HomePageIdentifiers.WHATISCANONIZER)
        self.find_element(*HomePageIdentifiers.WHATISCANONIZER).click()
        return CanonizerHomePage(self.driver)

    def check_home_page_loaded_logo_click(self):
        self.hover(*HomePageIdentifiers.CANONIZER_LOGO)
        self.find_element(*HomePageIdentifiers.CANONIZER_LOGO).click()
        return True if self.find_element(*HomePageIdentifiers.BODY) else False

    def check_scroll_to_top_click(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.hover(*HomePageIdentifiers.CANONIZER_LOGO)
        self.find_element(*HomePageIdentifiers.CANONIZER_LOGO).click()
        return CanonizerHomePage(self.driver)


##########################\
#  Tests For Login Page  #
##########################


class CanonizerHomePage(Page):
    """
    Class Name: CanonizerHomePage
    Description: Verify test cases for Canonizer Home Page.

    Attributes: None
    """

    def robots_txt_page_should_have_disallow_settings(self):
        """

        :return:
        """

        return self.find_element(*HomePageIdentifiers.TURNOFFSETTINGS).text
