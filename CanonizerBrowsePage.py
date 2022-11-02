from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

from CanonizerBase import Page
from Identifiers import BrowsePageIdentifiers
from selenium.webdriver.support.ui import Select
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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
            print('browse found')
            self.hover(*BrowsePageIdentifiers.BROWSE)
            wait = WebDriverWait(self.driver, 5)
            #wait.until(EC.element_to_be_clickable(*BrowsePageIdentifiers.BROWSE))
            self.find_element(*BrowsePageIdentifiers.BROWSE).click()
            wait = WebDriverWait(self.driver, 5)
            print('clicked on browse')

    def click_only_my_topics_button(self):
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        return CanonizerBrowsePage(self.driver)

    def select_dropdown_value(self):
        self.hover(*BrowsePageIdentifiers.NAMESPACE)
        self.find_element(*BrowsePageIdentifiers.NAMESPACE).click()
        return CanonizerBrowsePage(self.driver)

    def select_by_value_general(self):
        #select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        #select.select_by_value("1")
        self.find_element(*BrowsePageIdentifiers.GENERAL).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_general_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
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
        time.sleep(3)
        self.find_element(*BrowsePageIdentifiers.CORPORATIONS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_corporations_only_my_topics(self):
        self.find_element(*BrowsePageIdentifiers.CORPORATIONS).click()
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_crypto_currency(self):
        self.find_element(*BrowsePageIdentifiers.CRYPTOCURRENCY).click()
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        return CanonizerBrowsePage(self.driver)

    def select_by_value_family(self):
        self.find_element(*BrowsePageIdentifiers.FAMILY).click()
        return CanonizerBrowsePage(self.driver)

    def select_by_value_family_jesperson_oscar_f(self):
        self.find_element(*BrowsePageIdentifiers.FAMILYJESPERSON).click()
        return CanonizerBrowsePage(self.driver)

    def select_by_value_occupy_wall_street(self):
        self.find_element(*BrowsePageIdentifiers.OCCUPYWALLSTREET).click()
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations(self):
        self.find_element(*BrowsePageIdentifiers.ORGANIZATION).click()
        return CanonizerBrowsePage(self.driver)


    def select_by_value_organizations_canonizer(self):
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONCANONIZER).click()
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_canonizer_help(self):
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONCANONIZERHELP).click()
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_mta(self):
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONMTA).click()
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_tv07(self):
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONTV07).click()
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_wta(self):
        self.find_element(*BrowsePageIdentifiers.ORGANIZATIONWTA).click()
        return CanonizerBrowsePage(self.driver)

    def select_by_value_personal_attributes(self):
        self.find_element(*BrowsePageIdentifiers.PERSONALATTRIBUTE).click()
        return CanonizerBrowsePage(self.driver)

    def select_by_value_personal_attributes_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_personal_attributes()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_personal_reputations(self):
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_value("14")
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_personal_reputations_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_personal_reputations()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_professional_services(self):
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_value("15")
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_professional_services_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_professional_services()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sandbox(self):
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_value("16")
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_sandbox_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_sandbox()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_terminology(self):
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_value("17")
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_terminology_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_terminology()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_www(self):
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_value("18")
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_www_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_www()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_all(self):
        self.hover(*BrowsePageIdentifiers.ALL)
        self.find_element(*BrowsePageIdentifiers.ALL).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_all_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_all()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_all_default(self):
        self.hover(*BrowsePageIdentifiers.NAMESPACE)
        self.find_element(*BrowsePageIdentifiers.NAMESPACE).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_crypto_currency_ethereum(self):
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_value("21")
        return CanonizerBrowsePage(self.driver)

    def select_by_value_crypto_currency_ethereum_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_crypto_currency_ethereum()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_void(self):
        #select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        #select.select_by_value("22")
        self.hover(*BrowsePageIdentifiers.NAMESPACE)
        drop_down = self.find_element(*BrowsePageIdentifiers.NAMESPACE).click()
        ActionChains(driver).move_to_element(drop_down).perform()
        drop_down.click()

        option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[9]/div')))
        option.click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_void_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_void()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_mormon_canon_project(self):
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_value("24")
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_mormon_canon_project_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_mormon_canon_project()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_united_utah_party(self):
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_value("25")
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_organizations_united_utah_party_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_organizations_united_utah_party()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government(self):
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_value("26")
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_government()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government_sandy_city(self):
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_value("27")
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_by_value_government_sandy_city_only_my_topics(self):
        self.click_browse_page_button()
        self.select_dropdown_value()
        self.select_by_value_government_sandy_city()
        time.sleep(3)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_menu_item(self, menu_item):
        self.click_browse_page_button()
        self.hover(*BrowsePageIdentifiers.NAMESPACE)
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_visible_text(menu_item)
        self.hover(*BrowsePageIdentifiers.TOPIC_NAME)
        return CanonizerBrowsePage(self.driver)

    def select_menu_item_with_only_my_topics(self, menu_item):
        self.select_menu_item(menu_item)
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def select_menu_item_without_only_my_topics(self, menu_item):
        self.select_menu_item(menu_item)
        return CanonizerBrowsePage(self.driver)

    def one_by_one(self, menu_item):
        select = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        select.select_by_visible_text(menu_item)
        time.sleep(4)
        # self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        # self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        # time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    def one_by_one_only_my_topics(self):
        self.hover(*BrowsePageIdentifiers.ONLY_MY_TOPICS)
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        time.sleep(3)
        return CanonizerBrowsePage(self.driver)

    # def select_menu_items_one_by_one(self, topic_list):
    #     self.click_browse_page_button()
    #     self.hover(*BrowsePageIdentifiers.NAMESPACE)
    #     for topic in topic_list:
    #         result = self.one_by_one(topic)
    #         print('result', result.get_url())
    #     return CanonizerBrowsePage(self.driver)

    def select_menu_items_one_by_one(self):
        self.click_browse_page_button()
        self.hover(*BrowsePageIdentifiers.NAMESPACE)
        topics = Select(self.find_element(*BrowsePageIdentifiers.NAMESPACE))
        options = topics.options
        index = []
        topic_list = []
        for ele in options:
            index.append(ele.get_attribute("value"))
            topic_list.append(ele.text)
        index.pop(0)
        topic_list.pop(0)
        for i in range(len(topic_list)):
            result1 = self.one_by_one(topic_list[i])
            name_space1 = "https://staging.canonizer.com/browse?namespace=" + str(index[i])
            if name_space1 != result1.get_url():
                print("name space", name_space1)
                print("result Url:", result1.get_url())
                print("Fail")
                return False

            # name_space2 = "https://staging.canonizer.com/browse?namespace="+str(index[i])+"&my="+str(index[i])
            # result2 = self.one_by_one_only_my_topics()
            # if name_space2 != result2.get_url():
            #     print("name space Only My topic", name_space2)
            #     print("result Url Only My topic :", result2.get_url())
            #     print("Fail")
            #     return False

        return CanonizerBrowsePage(self.driver)



