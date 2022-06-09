from time import sleep

# import page as page
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import datetime

from CanonizerBase import Page
from Identifiers import AccountSettingPageIdentifier, CanonizerManageNickNameIdentifiersPage, \
    CanonizerSupportCampIdentifiersPage


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

    def check_the_validation_for_Phone_Number_field(self, number):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.PROFILE_BUTTON)
        self.find_element(*AccountSettingPageIdentifier.PROFILE_BUTTON).click()
        self.hover(*AccountSettingPageIdentifier.PHONE_NUMBER)
        self.find_element(*AccountSettingPageIdentifier.PHONE_NUMBER).send_keys(number)
        title = self.find_element(*AccountSettingPageIdentifier.PHONE_NUMBER_ERROR).text
        if title == 'Phone number must be at least 10 digits!':
            return CanonizerAccountSettingPage(self.driver)

    def check_the_Functionality_of_verify_button_without_entering_the_data(self):
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

    def verify_all_the_fields_are_present_in_Personal_Information_field(self):
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

    def verify_the_functionality_of_selecting_the_DOB(self, dob):
        self.click_account_settings_page_button()
        sleep(3)
        self.find_element(*AccountSettingPageIdentifier.DATA_BIRTH).click()
        sleep(3)
        self.find_element(*AccountSettingPageIdentifier.DATA_BIRTH).clear()
        self.find_element(*AccountSettingPageIdentifier.DATA_BIRTH).send_keys(dob)
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_when_user_updated_the_Personal_Information_and_logs_out_and_logIn_again(self, first, middle, last):
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
        sleep(3)
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).clear()
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).send_keys(first)
        self.find_element(*AccountSettingPageIdentifier.MIDDLE_NAME).send_keys(middle)
        self.find_element(*AccountSettingPageIdentifier.LAST_NAME).send_keys(last)
        self.find_element(*AccountSettingPageIdentifier.GENDER).click()
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()
        self.find_element(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN).click()
        self.find_element(*AccountSettingPageIdentifier.LOGOUT).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_when_user_click_on_change_password_tab_its_navigating_to_change_Password_Page(self):
        self.click_account_settings_page_button()
        sleep(5)
        self.hover(*AccountSettingPageIdentifier.CHANGE_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_current_password_new_password_confirm_password_is_present_save_button(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.CHANGE_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.hover(*AccountSettingPageIdentifier.CURRENT_PASSWORD)
        self.hover(*AccountSettingPageIdentifier.NEW_PASSWORD)
        self.hover(*AccountSettingPageIdentifier.CONFIRM_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_keeping_all_the_fields_empty_and_click_on_save(self, current, new, confirm):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.CHANGE_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.find_element(*AccountSettingPageIdentifier.CURRENT_PASSWORD).send_keys(current)
        self.find_element(*AccountSettingPageIdentifier.NEW_PASSWORD).send_keys(new)
        self.find_element(*AccountSettingPageIdentifier.CONFIRM_PASSWORD).send_keys(confirm)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_entering_the_invalid_current_password(self, current):
        self.click_account_settings_page_button()
        sleep(5)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.find_element(*AccountSettingPageIdentifier.CURRENT_PASSWORD).send_keys(current)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()
        title = self.find_element(*AccountSettingPageIdentifier.CURRENT_PASSWORD_ERROR).text
        if title == 'Incorrect Current Password':
            return CanonizerAccountSettingPage(self.driver)

    def verify_entering_the_invalid_new_password(self, new):
        self.click_account_settings_page_button()
        sleep(5)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.find_element(*AccountSettingPageIdentifier.NEW_PASSWORD).send_keys(new)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()
        title = self.find_element(*AccountSettingPageIdentifier.NEW_PASSWORD_ERROR).text
        if title == 'Password must be contain small, capital letter, number and special character like Abc@1234.':
            return CanonizerAccountSettingPage(self.driver)

    def verify_entering_the_invalid_confirm_password(self, DEFAULT_INVALID_CONFIRM_PASSWORD):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.CHANGE_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.find_element(*AccountSettingPageIdentifier.CONFIRM_PASSWORD).send_keys(DEFAULT_INVALID_CONFIRM_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()
        title = self.find_element(*AccountSettingPageIdentifier.CONFIRM_PASSWORD_ERROR).text
        if title == 'Confirm Password does not match.':
            return CanonizerAccountSettingPage(self.driver)

    def verify_when_both_new_Password_and_confirm_Password_does_not_match(self, DEFAULT_NEW_PASSWORD, DEFAULT_CONFIRM_PASSWORD):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.CHANGE_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.find_element(*AccountSettingPageIdentifier.NEW_PASSWORD).send_keys(DEFAULT_NEW_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.CONFIRM_PASSWORD).send_keys(DEFAULT_CONFIRM_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()
        title = self.find_element(*AccountSettingPageIdentifier.CONFIRM_PASSWORD_ERROR).text
        if title == 'Confirm Password does not match.':
            return CanonizerAccountSettingPage(self.driver)


class CanonizerManageNickNameTab(Page):
    def click_account_settings_page(self):
        """
        This function is to click on the Account Settings button

        -> Hover to the Account Settings button
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        self.hover(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ACCOUNT_SETTING_BUTTON).click()
        return CanonizerManageNickNameTab(self.driver)

    def verify_when_user_click_on_Nick_Name_tab(self):
        self.click_account_settings_page()
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.NICK_NAME).click()
        return CanonizerManageNickNameTab(self.driver)

    def verify_all_the_headers_in_nick_name_tab(self):
        self.click_account_settings_page()
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.NICK_NAME).click()
        self.hover(*CanonizerManageNickNameIdentifiersPage.SERIAL_NUMBER)
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME_ID)
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME)
        self.hover(*CanonizerManageNickNameIdentifiersPage.VISIBILITY_STATUS)

        return CanonizerManageNickNameTab(self.driver)

    def verify_with_Add_nick_name_button_is_present(self):
        self.click_account_settings_page()
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME).click()
        title = self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME_TITLE).text
        if title == 'Add New Nick Name':
            return CanonizerManageNickNameTab(self.driver)

    def verify_the_functionality_of_add_nickname_button(self):
        self.click_account_settings_page()
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME).click()

        return CanonizerManageNickNameTab(self.driver)

    def verify_validation_for_entering_nick_name_field(self, DEFAULT_NICK_NAME):
        self.click_account_settings_page()
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).send_keys(DEFAULT_NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_CREATE_BUTTON).click()

        return CanonizerManageNickNameTab(self.driver)

    def verify_validation_for_without_entering_nick_name_field(self, nick_name):
        self.click_account_settings_page()
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).send_keys(nick_name)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_CREATE_BUTTON).click()
        title = self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME_ERROR).text
        if title == 'Please Enter Nick Name!':
            return CanonizerManageNickNameTab(self.driver)

    def verify_entering_the_nick_name_with_more_than_one_space(self, DEFAULT_INVALID_NICK_NAME):
        self.click_account_settings_page()
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).send_keys(DEFAULT_INVALID_NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_CREATE_BUTTON).click()

        return CanonizerManageNickNameTab(self.driver)


class CanonizerSupportCamps(Page):
    def click_account_settings_page(self):
        """
        This function is to click on the Account Settings button

        -> Hover to the Account Settings button
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        self.hover(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.ACCOUNT_SETTING_BUTTON).click()

        return CanonizerSupportCamps(self.driver)

    def click_on_supported_camp_tab(self):
        self.hover(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMPS).click()

        return CanonizerSupportCamps(self.driver)

    def verify_user_is_navigating_to_Supported_camp_page_when_clicks_on_supported_camps_tab(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()

        return CanonizerSupportCamps(self.driver)

    def verify_direct_supported_camps(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.hover(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS)
        self.hover(*CanonizerSupportCampIdentifiersPage.DELEGATED_SUPPORT_CAMPS)

        return CanonizerSupportCamps(self.driver)

    def verify_the_search_bar_is_present_next_the_delegate_support_camp_tab(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORT_CAMP_SEARCH_BAR).click()

        return CanonizerSupportCamps(self.driver)

    def verify_the_functionality_of_Direct_Support_Camp(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS).click()

        return CanonizerSupportCamps(self.driver)

    def verify_the_functionality_of_Delegate_support_camp_tab(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.DELEGATED_SUPPORT_CAMPS).click()

        return CanonizerSupportCamps(self.driver)

    def verify_the_search_functionality_in_supported_camps_page(self, DEFAULT_TOPIC_NAME):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORT_CAMP_SEARCH_BAR).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORT_CAMP_SEARCH_BAR).send_keys(DEFAULT_TOPIC_NAME)

        return CanonizerSupportCamps(self.driver)

    def Verify_topic_name_and_agreement_camp_name_is_present_in_direct_support_camp_tab(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS).click()

        return CanonizerSupportCamps(self.driver)

    def topic_name_and_camp_name_is_clickable(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICKING_ON_TOPIC_NAME).CLICK()
        title = self.find_element(*CanonizerSupportCampIdentifiersPage.TOPIC_NAME_TITLE).text
        if title == 'Topic: automation 123':
            return CanonizerSupportCamps(self.driver)
        else:
            print("title not found")

    def verify_Remove_Support_button_functionality(self):
        self.hover(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.ACCOUNT_SETTING_BUTTON).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.CLICK_ON_REMOVE_SUPPORT)
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICK_ON_REMOVE_SUPPORT).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.REMOVE_ON_POP_UP_BUTTON).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.REMOVE_TITLE)
        title = self.find_element(*CanonizerSupportCampIdentifiersPage.REMOVE_TITLE).text
        if title == 'Remove Support':
            return CanonizerSupportCamps(self.driver)
        else:
            print('title not found')