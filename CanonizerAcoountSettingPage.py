from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import datetime

from CanonizerBase import Page
from Identifiers import AccountSettingPageIdentifier


class CanonizerAccountSettingPage(Page):

    def click_account_settings_page_button(self):
        """
        This function is to click on the Account Settings button

        -> Hover to the Account Settings button
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        # sleep(10)
        self.hover(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN)
        self.find_element(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN).click()
        # sleep(6)
        self.find_element(*AccountSettingPageIdentifier.ACCOUNT_SETTING_BUTTON).click()
        return CanonizerAccountSettingPage(self.driver)

    def verifying_profile_button(self):
        sleep(3)
        self.hover(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN)
        self.find_element(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN).click()
        # sleep(3)
        self.find_element(*AccountSettingPageIdentifier.ACCOUNT_SETTING_BUTTON).click()
        self.hover(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN)
        self.find_element(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN).click()
        self.hover(*AccountSettingPageIdentifier.PROFILE_BUTTON)
        self.find_element(*AccountSettingPageIdentifier.PROFILE_BUTTON).click()
        # sleep(3)
        return CanonizerAccountSettingPage(self.driver)

    def verifying_social_oauth_verification(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.SOCIAL_OAUTH_VERIFICATION)
        self.find_element(*AccountSettingPageIdentifier.SOCIAL_OAUTH_VERIFICATION).click()
        tittle = self.find_element(*AccountSettingPageIdentifier.SOCIAL_OAUTH_VERIFICATION).text
        print(tittle)
        if tittle == 'Social Oauth Verification':
            return CanonizerAccountSettingPage(self.driver)

    def verifying_change_password(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.CHANGE_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        tittle = self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).text
        print(tittle)
        if tittle == 'Change Password':
            return CanonizerAccountSettingPage(self.driver)

    def verifying_nick_name(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.NICK_NAME)
        self.find_element(*AccountSettingPageIdentifier.NICK_NAME).click()
        tittle = self.find_element(*AccountSettingPageIdentifier.NICK_NAME).text
        print(tittle)
        if tittle == 'Nick Names':
            return CanonizerAccountSettingPage(self.driver)

    def verifying_supported_camps(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.SUPPORTED_CAMPS)
        self.find_element(*AccountSettingPageIdentifier.SUPPORTED_CAMPS).click()
        tittle = self.find_element(*AccountSettingPageIdentifier.SUPPORTED_CAMPS).text
        print(tittle)
        if tittle == 'Supported Camps':
            return CanonizerAccountSettingPage(self.driver)

    def Check_the_validation_for_Phone_Number_field(self, number):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.PROFILE_BUTTON)
        self.find_element(*AccountSettingPageIdentifier.PROFILE_BUTTON).click()
        self.hover(*AccountSettingPageIdentifier.PHONE_NUMBER)
        self.find_element(*AccountSettingPageIdentifier.PHONE_NUMBER).send_keys(number)
        tittle = self.find_element(*AccountSettingPageIdentifier.PHONE_NUMBER_ERROR).text
        print(tittle)
        if tittle == 'Phone number must be at least 10 digits!':
            return CanonizerAccountSettingPage(self.driver)

    def Check_the_Functionality_of_verify_button_without_entering_the_data(self):
        self.click_account_settings_page_button()
        self.find_element(*AccountSettingPageIdentifier.PROFILE_BUTTON).click()
        self.hover(*AccountSettingPageIdentifier.PHONE_NUMBER)
        sleep(5)
        self.hover(*AccountSettingPageIdentifier.MOBILE_CARRIER)
        self.find_element(*AccountSettingPageIdentifier.VERIFY_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def Verify_the_functionality_of_mobile_carrier_drop_down(self):
        self.click_account_settings_page_button()
        self.find_element(*AccountSettingPageIdentifier.PROFILE_BUTTON).click()
        sleep(5)
        self.hover(*AccountSettingPageIdentifier.MOBILE_CARRIER)
        self.find_element(*AccountSettingPageIdentifier.MOBILE_CARRIER).click()

        return CanonizerAccountSettingPage(self.driver)

    def Verify_all_the_fields_are_present_in_Personal_Information_field(self):
        self.click_account_settings_page_button()
        self.hover(*AccountSettingPageIdentifier.FIRST_NAME)
        self.hover(*AccountSettingPageIdentifier.MIDDLE_NAME)
        self.hover(*AccountSettingPageIdentifier.LAST_NAME)
        self.hover(*AccountSettingPageIdentifier.GENDER)

        return CanonizerAccountSettingPage(self.driver)

    def Verify_the_validation_for_first_name(self, first):
        self.click_account_settings_page_button()
        sleep(5)
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).click()
        sleep(5)
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).send_keys(first)
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def Update_the_first_name_and_check_if_it_is_updating_same_for_username(self, first_name):
        self.click_account_settings_page_button()
        sleep(3)
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).click()
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).send_keys(first_name)
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def Verify_the_functionality_of_radio_button_in_selecting_the_gender(self):
        self.click_account_settings_page_button()
        sleep(5)
        self.find_element(*AccountSettingPageIdentifier.GENDER).click()
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    #def Verify_the_functionality_of_selecting_the_DOB(self, dob):
        self.click_account_settings_page_button()
        sleep(3)
        self.find_element(*AccountSettingPageIdentifier.DATA_BIRTH).click()
        sleep(3)
        self.find_element(*AccountSettingPageIdentifier.DATA_BIRTH).clear()
        self.find_element(*AccountSettingPageIdentifier.DATA_BIRTH).send_keys(dob)
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def Verify_when_user_updated_the_Personal_Information_and_logs_out_and_logIn_again(self, first, middle, last):
        self.click_account_settings_page_button()
        sleep(3)
        self.find_element(*AccountSettingPageIdentifier.FIRST_NAME).send_keys(first)
        self.find_element(*AccountSettingPageIdentifier.MIDDLE_NAME).send_keys(middle)
        self.find_element(*AccountSettingPageIdentifier.LAST_NAME).send_keys(last)
        self.find_element(*AccountSettingPageIdentifier.GENDER).click()
        self.find_element(*AccountSettingPageIdentifier.UPDATE_BUTTON).click()
        self.find_element(*AccountSettingPageIdentifier.CLICK_ON_DROPDOWN).click()
        self.find_element(*AccountSettingPageIdentifier.LOGOUT).click()

        return CanonizerAccountSettingPage(self.driver)

    def Verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields(self, first, middle, last):
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

    def Verify_when_user_click_on_change_password_tab_its_navigating_to_change_Password_Page(self):
        self.click_account_settings_page_button()
        sleep(5)
        self.hover(*AccountSettingPageIdentifier.CHANGE_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()

        return CanonizerAccountSettingPage(self.driver)

    def Verify_self_current_password_new_password_confirm_password_is_present_save_button(self):
        self.click_account_settings_page_button()
        sleep(5)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.hover(*AccountSettingPageIdentifier.CURRENT_PASSWORD)
        self.hover(*AccountSettingPageIdentifier.NEW_PASSWORD)
        self.hover(*AccountSettingPageIdentifier.CONFIRM_PASSWORD)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def Verify_keeping_all_the_fields_empty_and_click_on_save(self, current, new, confirm):
        self.click_account_settings_page_button()
        sleep(5)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.find_element(*AccountSettingPageIdentifier.CURRENT_PASSWORD).send_keys(current)
        self.find_element(*AccountSettingPageIdentifier.NEW_PASSWORD).send_keys(new)
        self.find_element(*AccountSettingPageIdentifier.CONFIRM_PASSWORD).send_keys(confirm)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def test_Verify_entering_the_invalid_current_password(self, current):
        self.click_account_settings_page_button()
        sleep(5)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.find_element(*AccountSettingPageIdentifier.CURRENT_PASSWORD).send_keys(current)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()
        tittle = self.find_element(*AccountSettingPageIdentifier.CURRENT_PASSWORD_ERROR).text
        print(tittle)
        if tittle == 'Incorrect Current Password':
            return CanonizerAccountSettingPage(self.driver)

    def Verify_entering_the_invalid_new_password(self, new):
        self.click_account_settings_page_button()
        sleep(5)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.find_element(*AccountSettingPageIdentifier.NEW_PASSWORD).send_keys(new)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()
        tittle = self.find_element(*AccountSettingPageIdentifier.NEW_PASSWORD_ERROR).text
        print(tittle)
        if tittle == 'Password must be contain small, capital letter, number and special character like Abc@1234.':
            return CanonizerAccountSettingPage(self.driver)

    def Verify_entering_the_invalid_confirm_password(self, confirm):
        self.click_account_settings_page_button()
        sleep(5)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.find_element(*AccountSettingPageIdentifier.CONFIRM_PASSWORD).send_keys(confirm)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()
        tittle = self.find_element(*AccountSettingPageIdentifier.CONFIRM_PASSWORD_ERROR).text
        print(tittle)
        if tittle == 'Confirm Password does not match.':
            return CanonizerAccountSettingPage(self.driver)

    def Verify_when_both_new_Password_and_confirm_Password_does_not_match(self, new, confirm):
        self.click_account_settings_page_button()
        sleep(5)
        self.find_element(*AccountSettingPageIdentifier.CHANGE_PASSWORD).click()
        self.find_element(*AccountSettingPageIdentifier.NEW_PASSWORD).send_keys(new)
        self.find_element(*AccountSettingPageIdentifier.CONFIRM_PASSWORD).send_keys(confirm)
        self.find_element(*AccountSettingPageIdentifier.SAVE_BUTTON).click()
        tittle = self.find_element(*AccountSettingPageIdentifier.CONFIRM_PASSWORD_ERROR).text
        print(tittle)
        if tittle == 'Confirm Password does not match.':
            return CanonizerAccountSettingPage(self.driver)

    def Verify_when_user_click_on_Nick_Name_tab(self):
        self.click_account_settings_page_button()
        self.find_element(*AccountSettingPageIdentifier.NICK_NAME).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_all_the_headers_in_nick_name_tab(self):
        self.click_account_settings_page_button()
        self.find_element(*AccountSettingPageIdentifier.NICK_NAME).click()
        self.hover(*AccountSettingPageIdentifier.SERIAL_NUMBER)
        self.hover(*AccountSettingPageIdentifier.NICK_NAME_ID)
        self.hover(*AccountSettingPageIdentifier.NICK_NAME)
        self.hover(*AccountSettingPageIdentifier.VISIBILITY_STATUS)

        return CanonizerAccountSettingPage(self.driver)

    def verify_with_Add_nick_name_button_is_present(self):
        self.click_account_settings_page_button()
        self.find_element(*AccountSettingPageIdentifier.NICK_NAME).click()
        self.find_element(*AccountSettingPageIdentifier.ADD_NEW_NICK_NAME).click()
        sleep(5)
        tittle = self.find_element(*AccountSettingPageIdentifier.ADD_NEW_NICK_NAME_TITTLE).text
        print(tittle)
        if tittle == 'Add New Nick Name':
            return CanonizerAccountSettingPage(self.driver)

    def Verify_the_functionality_of_add_nickname_button(self):
        self.click_account_settings_page_button()
        self.find_element(*AccountSettingPageIdentifier.NICK_NAME).click()
        self.find_element(*AccountSettingPageIdentifier.ADD_NEW_NICK_NAME).click()

        return CanonizerAccountSettingPage(self.driver)

    def Verify_validation_for_entering_nick_name_field(self, sai_deekshith):
        sleep(3)
        self.click_account_settings_page_button()
        self.find_element(*AccountSettingPageIdentifier.NICK_NAME).click()
        self.find_element(*AccountSettingPageIdentifier.ADD_NEW_NICK_NAME).click()
        self.find_element(*AccountSettingPageIdentifier.POP_UP_NICK_NAME).click()
        self.find_element(*AccountSettingPageIdentifier.POP_UP_NICK_NAME).send_keys(sai_deekshith)
        self.find_element(*AccountSettingPageIdentifier.POPO_UP_CREATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def Verify_validation_for_without_entering_nick_name_field(self, sai_deekshith):
        self.click_account_settings_page_button()
        self.find_element(*AccountSettingPageIdentifier.NICK_NAME).click()
        self.find_element(*AccountSettingPageIdentifier.ADD_NEW_NICK_NAME).click()
        self.find_element(*AccountSettingPageIdentifier.POP_UP_NICK_NAME).click()
        self.find_element(*AccountSettingPageIdentifier.POP_UP_NICK_NAME).send_keys(sai_deekshith)
        self.find_element(*AccountSettingPageIdentifier.POPO_UP_CREATE_BUTTON).click()
        sleep(5)
        tittle = self.find_element(*AccountSettingPageIdentifier.POP_UP_NICK_NAME_ERROR).text
        print(tittle)
        if tittle == 'Please Enter Nick Name!': 
            return CanonizerAccountSettingPage(self.driver)



