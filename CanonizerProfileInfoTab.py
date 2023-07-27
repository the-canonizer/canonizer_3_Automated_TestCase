import time

from selenium.webdriver.common.keys import Keys
from CanonizerBase import Page
from Identifiers import ProfileInfoIdentifiersPage
from CanonizerValidationCheckMessages import message
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import *
from selenium import webdriver


class CanonizerAccountSettingPage(Page):
    def driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def click_account_settings_page_button(self):
        """
        This function is to click on the Account Settings button

        -> Hover to the Account Settings button
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        self.hover(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*ProfileInfoIdentifiersPage.ACCOUNT_SETTING_BUTTON).click()
        return CanonizerAccountSettingPage(self.driver)

    def verifying_profile_button(self):
        self.hover(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*ProfileInfoIdentifiersPage.ACCOUNT_SETTING_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.hover(*ProfileInfoIdentifiersPage.PROFILE_BUTTON)
        self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).click()
        title = self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).text
        if title == message['Profile_tab']['TITLE_INFO']:
            return CanonizerAccountSettingPage(self.driver)
        else:
            print("Title not found or not matching")

    def verifying_social_oauth_verification(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.SOCIAL_OAUTH_VERIFICATION)
        self.find_element(*ProfileInfoIdentifiersPage.SOCIAL_OAUTH_VERIFICATION).click()
        title = self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).text
        if title == message['Profile_tab']['SOCIAL_TITLE']:
            return CanonizerAccountSettingPage(self.driver)
        else:
            print("Title not found or not matching")

    def verifying_change_password(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.CHANGE_PASSWORD)
        self.find_element(*ProfileInfoIdentifiersPage.CHANGE_PASSWORD).click()
        title = self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).text
        if title == message['Profile_tab']['CHANGE_PASSWORD']:
            return CanonizerAccountSettingPage(self.driver)
        else:
            print("Title not found or not matching")

    def verifying_nick_name(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.NICK_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.NICK_NAME).click()
        title = self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).text
        if title == message['Profile_tab']['NICK_NAMES']:
            return CanonizerAccountSettingPage(self.driver)
        else:
            print("Title not found or not matching")

    def verifying_supported_camps(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.SUPPORTED_CAMPS)
        self.find_element(*ProfileInfoIdentifiersPage.SUPPORTED_CAMPS).click()
        title = self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).text
        if title == message['Profile_tab']['SUPPORTED_CAMPS']:
            return CanonizerAccountSettingPage(self.driver)
        else:
            print("Title not found or not matching")

    def refresh_supported_camps(self):
        self.driver.get("https://canonizer3.canonizer.com/settings?tab=supported_camps")
        self.driver.refresh()

    def check_the_validation_for_phone_number_field(self, number):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.PROFILE_BUTTON)
        self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.PHONE_NUMBER)
        self.find_element(*ProfileInfoIdentifiersPage.PHONE_NUMBER).send_keys(number)
        self.hover(*ProfileInfoIdentifiersPage.PHONE_NUMBER_ERROR)
        title = self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).text
        if title == message['Profile_tab']['PHONE_NUMBER_VALIDATION']:
            return CanonizerAccountSettingPage(self.driver)
        else:
            print("Title not found or not matching")

    def check_the_functionality_of_verify_button_without_entering_the_data(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.PROFILE_BUTTON)
        self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.VERIFY_BUTTON)
        self.find_element(*ProfileInfoIdentifiersPage.VERIFY_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.PHONE_NUMBER)
        title = self.find_element(*ProfileInfoIdentifiersPage.PHONE_NUMBER).text
        self.hover(*ProfileInfoIdentifiersPage.MOBILE_CARRIER)
        title1 = self.find_element(*ProfileInfoIdentifiersPage.MOBILE_CARRIER).text

        if title == message['Profile_tab']['EMPTY_PHONE_VALIDATION'] \
                and title1 == message['Profile_tab']['EMPTY_MOBILE_CARRIER_VALIDATION']:
            return CanonizerAccountSettingPage(self.driver)

    def verify_the_functionality_of_mobile_carrier_drop_down(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.PROFILE_BUTTON)
        self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.MOBILE_CARRIER)
        self.find_element(*ProfileInfoIdentifiersPage.MOBILE_CARRIER).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_all_the_fields_are_present_in_personal_information_field(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.PROFILE_BUTTON)
        self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.FIRST_NAME)
        self.hover(*ProfileInfoIdentifiersPage.MIDDLE_NAME)
        self.hover(*ProfileInfoIdentifiersPage.LAST_NAME)
        self.hover(*ProfileInfoIdentifiersPage.GENDER)

        return CanonizerAccountSettingPage(self.driver)

    def verify_the_validation_for_first_name(self, first_name):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.PROFILE_BUTTON)
        self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.FIRST_NAME)

        for i in range(0, 100):
            self.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).send_keys(Keys.BACKSPACE)
        self.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).send_keys(first_name)

        self.find_element(*ProfileInfoIdentifiersPage.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_when_user_updated_the_personal_information_and_logs_out_and_login_again(self, first, middle, last):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.FIRST_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).send_keys(first)
        self.hover(*ProfileInfoIdentifiersPage.MIDDLE_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.MIDDLE_NAME).send_keys(middle)
        self.hover(*ProfileInfoIdentifiersPage.LAST_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.LAST_NAME).send_keys(last)
        self.hover(*ProfileInfoIdentifiersPage.UPDATE_BUTTON)
        self.find_element(*ProfileInfoIdentifiersPage.UPDATE_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.hover(*ProfileInfoIdentifiersPage.LOGOUT)
        self.find_element(*ProfileInfoIdentifiersPage.LOGOUT).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields(self, first, middle, last):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.FIRST_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).send_keys(first)
        self.hover(*ProfileInfoIdentifiersPage.MIDDLE_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.MIDDLE_NAME).send_keys(middle)
        self.hover(*ProfileInfoIdentifiersPage.LAST_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.LAST_NAME).send_keys(last)
        self.hover(*ProfileInfoIdentifiersPage.UPDATE_BUTTON)
        self.find_element(*ProfileInfoIdentifiersPage.UPDATE_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.hover(*ProfileInfoIdentifiersPage.LOGOUT)
        self.find_element(*ProfileInfoIdentifiersPage.LOGOUT).click()

        return CanonizerAccountSettingPage(self.driver)
