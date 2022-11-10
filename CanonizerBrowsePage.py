from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from CanonizerBase import Page
from Identifiers import BrowsePageIdentifiers
from selenium.webdriver.support.ui import Select
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import sys


class CanonizerBrowsePage(Page):

    def click_browse_page_button(self):
        """
        This function is to click on the Browse link
        -> Hover to the Browse link
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        #title = self.find_element(*BrowsePageIdentifiers.TITLE)
        #print(title)
        if self.find_element(*BrowsePageIdentifiers.BROWSE):
            self.hover(*BrowsePageIdentifiers.BROWSE)
            wait = WebDriverWait(self.driver, 5)
            #wait.until(EC.element_to_be_clickable(*BrowsePageIdentifiers.BROWSE))
            self.find_element(*BrowsePageIdentifiers.BROWSE).click()
            wait = WebDriverWait(self.driver, 5)

    def click_only_my_topics_button(self):
        self.click_browse_page_button()
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        return CanonizerBrowsePage(self.driver)

    def select_dropdown_value(self):
        self.click_browse_page_button()
        self.hover(*BrowsePageIdentifiers.NAMESPACE)
        self.find_element(*BrowsePageIdentifiers.NAMESPACE).click()
        return CanonizerBrowsePage(self.driver)

    def scroll_down(self):
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        action = ActionChains(self.driver)
        #i = 10
        while self.i >= 0:
            action.key_down(Keys.DOWN).perform()
            print(self.i)
            self.i = self.i - 1
            time.sleep(0.4)
    def select_by_value_general(self):
        #select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        #select.select_by_value("1")
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.find_element(*BrowsePageIdentifiers.GENERAL).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_general_only_my_topics(self):
        self.select_by_value_general()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_corporations(self):
        #select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        #time.sleep(3)
        #select.select_by_value("2")
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.find_element(*BrowsePageIdentifiers.CORPORATIONS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_corporations_only_my_topics(self):
        self.select_by_value_corporations()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_crypto_currency(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.CRYPTOCURRENCY).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_crypto_currency_only_my_topics(self):
        self.select_by_value_crypto_currency()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_family(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.FAMILY).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_family_only_my_topics(self):
        self.select_by_value_family()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_family_jesperson_oscar_f(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.FAMILYJESPERSON).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_family_jesperson_oscar_f_only_my_topics(self):
        self.select_by_value_family_jesperson_oscar_f()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_occupy_wall_street(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.OCCUPYWALLSTREET).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_occupy_wall_street_only_my_topics(self):
        self.select_by_value_occupy_wall_street()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.ORGANIZATION).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)


    def select_by_value_organizations_only_my_topics(self):
        self.select_by_value_organizations()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations_canonizer(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONCANONIZER).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_canonizer_only_my_topics(self):
        self.select_by_value_organizations_canonizer()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations_canonizer_help(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONCANONIZERHELP).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_canonizer_help_only_my_topics(self):
        self.select_by_value_organizations_canonizer_help()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations_mta(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONMTA).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_mta_only_my_topics(self):
        self.select_by_value_organizations_mta()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations_tv07(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONTV07).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_tv07_only_my_topics(self):
        self.select_by_value_organizations_tv07()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_organizations_wta(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 10
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONWTA).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_wta_only_my_topics(self):
        self.select_by_value_organizations_wta()
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_personal_attributes(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 15
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.PERSONALATTRIBUTE).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_personal_attributes_only_my_topics(self):
        self.select_by_value_personal_attributes()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_personal_reputations(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 15
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.PERSONALREPUTATION).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_personal_reputations_only_my_topics(self):
        self.select_by_value_personal_reputations()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_professional_services(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 15
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.PROFESSIONALSERVICES).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_professional_services_only_my_topics(self):
        self.select_by_value_professional_services()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sandbox(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 15
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.SANDBOX).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sandbox_only_my_topics(self):
        self.select_by_value_sandbox()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_terminology(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 15
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.TERMINOLOGY).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_terminology_only_my_topics(self):
        self.select_by_value_terminology()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_www(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 20
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.WWW).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_www_only_my_topics(self):
        self.select_by_value_www()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sandbox_testing(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 20
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.SANDBOXTESTING).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sandbox_testing_only_my_topics(self):
        self.select_by_value_sandbox_testing()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_crypto_currency_ethereum(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 25
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.CRYPTOCURRENCYETHEREUM).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_crypto_currency_ethereum_only_my_topics(self):
        self.select_by_value_crypto_currency_ethereum()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_void(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 25
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.VOID).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_void_only_my_topics(self):
        self.select_by_value_void()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_mormon_canon_project(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 25
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.MORMONCANONPROJECT).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_mormon_canon_project_only_my_topics(self):
        self.select_by_value_mormon_canon_project()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_united_utah_party(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 25
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONUNITEDUTAHPARTY).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_united_utah_party_only_my_topics(self):
        self.select_by_value_organizations_united_utah_party()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 25
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.GOVERNMENT).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government_only_my_topics(self):
        self.select_by_value_government()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government_sandy_city(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 25
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.GOVERNMENTSANDYCITY).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government_sandy_city_only_my_topics(self):
        self.select_by_value_government_sandy_city()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sports(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 25
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.SPORT).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_sports_only_my_topics(self):
        self.select_by_value_sports()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_sports_sbcl(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 25
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.SPORTSBCL).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_sports_sbcl_only_my_topics(self):
        self.select_by_value_sports_sbcl()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_plateform_of_the_people(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 30
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.PLATEFORMOFTHEPEOPLE).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_plateform_of_the_people_only_my_topics(self):
        self.select_by_plateform_of_the_people()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 30
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.FICTION).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_fiction_only_my_topics(self):
        self.select_by_value_fiction()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_fiction_lord_of_the_ring(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 30
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.FICTIONLORDOFTHERINGS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction_lord_of_the_ring_only_my_topics(self):
        self.select_by_value_fiction_lord_of_the_ring()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction_star_wars(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 30
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.FICTIONSTARWARS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction_star_wars_only_my_topics(self):
        self.select_by_value_fiction_star_wars()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction_world_of_warcraft(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 30
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.FICTIONWORLDOFWARCRAFT).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_fiction_world_of_warcraft_only_my_topics(self):
        self.select_by_value_fiction_world_of_warcraft()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)
    def select_by_value_all(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        time.sleep(3)
        self.i = 31
        self.scroll_down()
        self.find_element(*BrowsePageIdentifiers.ALL).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_all_only_my_topics(self):
        self.select_by_value_all()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)




