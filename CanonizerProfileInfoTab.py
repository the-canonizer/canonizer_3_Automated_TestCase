from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import datetime

from CanonizerBase import Page
from Identifiers import AccountSettingPageIdentifier, CanonizerManageNickNameIdentifiersPage, \
    CanonizerSupportCampIdentifiersPage, CanonizerChangePasswordIdentifierPage


class CanonizerAccountSettingPage(Page):

    def click_account_settings_page_button(self):
        """
        This function is to click on the Account Settings button

        -> Hover to the Account Settings button
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        self.hover(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN)
        self.find_element(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN).click()
        self.find_element(*AccountSettingPageIdentifier.ACCOUNT_SETTING_BUTTON).click()
        return CanonizerAccountSettingPage(self.driver)

    def verifying_profile_button(self):
        self.hover(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN)
        self.find_element(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN).click()
        self.find_element(*AccountSettingPageIdentifier.ACCOUNT_SETTING_BUTTON).click()
        self.hover(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN)
        self.find_element(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN).click()
        self.hover(*AccountSettingPageIdentifier.PROFILE_BUTTON)
        self.find_element(*AccountSettingPageIdentifier.PROFILE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verifying_social_oauth_verification(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.SOCIAL_OAUTH_VERIFICATION)
        self.find_element(*AccountSettingPageIdentifier.SOCIAL_OAUTH_VERIFICATION).click()
        res = self.find_element(*AccountSettingPageIdentifier.SOCIAL_OAUTH_VERIFICATION).text
        if res == 'Social Oauth Verification':
            return CanonizerAccountSettingPage(self.driver)

    def verifying_change_password(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.CHANGE_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        title = self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).text
        if title == 'Change Password':
            return CanonizerAccountSettingPage(self.driver)

    def verifying_nick_name(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.NICK_NAME)
        self.find_element(*AccountSettingPageIdentifier.NICK_NAME).click()
        title = self.find_element(*AccountSettingPageIdentifier.NICK_NAME).text
        if title == 'Nick Names':
            return CanonizerAccountSettingPage(self.driver)

    def verifying_supported_camps(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.SUPPORTED_CAMPS)
        self.find_element(*AccountSettingPageIdentifier.SUPPORTED_CAMPS).click()
        title = self.find_element(*AccountSettingPageIdentifier.SUPPORTED_CAMPS).text
        if title == 'Supported Camps':
            return CanonizerAccountSettingPage(self.driver)

    def check_the_validation_for_phone_number_field(self, number):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.PROFILE_BUTTON)
        self.find_element(*AccountSettingPageIdentifier.PROFILE_BUTTON).click()
        self.hover(*AccountSettingPageIdentifier.PHONE_NUMBER)
        self.find_element(*AccountSettingPageIdentifier.PHONE_NUMBER).send_keys(number)
        title = self.find_element(*AccountSettingPageIdentifier.PHONE_NUMBER_ERROR).text
        if title == 'Phone number must be at least 10 digits!':
            return CanonizerAccountSettingPage(self.driver)

    def check_the_functionality_of_verify_button_without_entering_the_data(self):
        self.click_account_settings_page_button()
        self.find_element(*AccountSettingPageIdentifier.PROFILE_BUTTON).click()
        self.hover(*AccountSettingPageIdentifier.PHONE_NUMBER)
        self.hover(*AccountSettingPageIdentifier.MOBILE_CARRIER)
        self.find_element(*AccountSettingPageIdentifier.VERIFY_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_the_functionality_of_mobile_carrier_drop_down(self):
        self.click_account_settings_page_button()
        self.find_element(*AccountSettingPageIdentifier.PROFILE_BUTTON).click()
        self.hover(*AccountSettingPageIdentifier.MOBILE_CARRIER)
        self.hover(*AccountSettingPageIdentifier.MOBILE_CARRIER)
        self.find_element(*AccountSettingPageIdentifier.MOBILE_CARRIER).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_all_the_fields_are_present_in_personal_information_field(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.FIRST_NAME)
        self.hover(*AccountSettingPageIdentifier.MIDDLE_NAME)
        self.hover(*AccountSettingPageIdentifier.LAST_NAME)
        self.hover(*AccountSettingPageIdentifier.GENDER)

        return CanonizerAccountSettingPage(self.driver)

    def verify_the_validation_for_first_name(self, first):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.FIRST_NAME)
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).click()
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).send_keys(first)
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def update_the_first_name_and_check_if_it_is_updating_same_for_username(self, first_name):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.FIRST_NAME)
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).click()
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).send_keys(first_name)
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_the_functionality_of_radio_button_in_selecting_the_gender(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.GENDER)
        self.find_element(*AccountSettingPageIdentifier.GENDER).click()
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_when_user_updated_the_personal_information_and_logs_out_and_login_again(self, first, middle, last):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.FIRST_NAME)
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).send_keys(first)
        self.find_element(*AccountSettingPageIdentifier.MIDDLE_NAME).send_keys(middle)
        self.find_element(*AccountSettingPageIdentifier.LAST_NAME).send_keys(last)
        self.find_element(*AccountSettingPageIdentifier.GENDER).click()
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()
        self.find_element(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN).click()
        self.find_element(*AccountSettingPageIdentifier.LOGOUT).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields(self, first, middle, last):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.FIRST_NAME)
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).clear()
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).send_keys(first)
        self.find_element(*AccountSettingPageIdentifier.MIDDLE_NAME).send_keys(middle)
        self.find_element(*AccountSettingPageIdentifier.LAST_NAME).send_keys(last)
        self.find_element(*AccountSettingPageIdentifier.GENDER).click()
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()
        self.find_element(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN).click()
        self.find_element(*AccountSettingPageIdentifier.LOGOUT).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_the_functionality_of_Algorithm_drop_down(self):
        self.click_account_settings_page_button()

