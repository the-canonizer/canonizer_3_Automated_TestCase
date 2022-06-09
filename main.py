import unittest
from unittest import result

import self as self
from selenium.webdriver.remote.webelement import WebElement

import CanonizerBrowsePage
from CanonizerAcoountSettingPage import CanonizerAccountSettingPage, CanonizerManageNickNameTab, CanonizerSupportCamps
from CanonizerLoginPage import CanonizerLoginPage
from CanonizerRegistrationPage import CanonizerRegisterPage

from CanonizerTestCases import test_cases
from Config import *
from selenium import webdriver

from Identifiers import CanonizerManageNickNameIdentifiersPage


class TestPages(unittest.TestCase):

    def setUp(self):
        """
            Initialize the Things
            :return:
        """
        driver_location = DEFAULT_CHROME_DRIVER_LOCATION

        options = webdriver.ChromeOptions()
        options.binary_location = DEFAULT_BINARY_LOCATION

        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(driver_location, options=options)
        self.driver.get(DEFAULT_BASE_URL)

    def login_to_canonizer_app(self):
        """
            This Application will allow you to login to canonizer App on need basis
        :param flag:
        :return:
        """
        result = CanonizerLoginPage(self.driver).click_login_page_button().login_with_valid_user(DEFAULT_USER,
                                                                                                 DEFAULT_PASS).get_url()
        self.assertIn("", result)

    # TC_CLICK_ON_REGISTER_BUTTON
    def test_click_on_register_button(self):
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_BUTTON')))
        result = CanonizerRegisterPage(self.driver).click_on_register_button().get_url()
        self.assertIn("", result)

    # TC_REGISTER_WITH_BLANK_FIRST_NAME
    def test_registration_with_blank_first_name(self, ):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_FIRST_NAME')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_first_name(
            REG_LIST_3).get_url()
        self.assertIn("", result)

    # TC_REGISTER_WITH_BLANK_LAST_NAME
    def test_registration_with_blank_last_name(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_LAST_NAME')))
        CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_last_name(
            REG_LIST_4).get_url()

    # TC_REGISTRATION_WITH_BLANK_EMAIL
    def test_registration_with_blank_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_EMAIL')))
        CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_email(
            REG_LIST_5)

    # TC_REGISTRATION_WITH_BLANK_PASSWORD
    def test_registration_with_blank_password(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_PASSWORD')))
        CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_password(
            REG_LIST_6)

    # TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH
    def test_registration_with_invalid_password_length(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH')))
        CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_password_length(
            REG_LIST_7)

    # TC_REGISTRATION_WITH_DIFFERENT_CONFIRM_PASSWORD
    def test_registration_with_different_confirmation_password(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_DIFFERENT_CONFIRM_PASSWORD')))
        CanonizerRegisterPage(
            self.driver).click_register_button().registration_with_different_confirmation_password(
            REG_LIST_8)

    # TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME
    def test_registration_with_blank_spaces_first_name(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME')))
        CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_spaces_first_name(
            REG_LIST_1)

    # TC_REGISTRATION_WITH_INVALID_FIRST_NAME
    def test_registration_with_invalid_first_name(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_FIRST_NAME')))
        CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_first_name(
            REG_LIST_10)

    # TC_REGISTRATION_WITH_INVALID_LAST_NAME
    def test_registration_with_invalid_last_name(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_LAST_NAME')))
        CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_last_name(
            REG_LIST_11)

    # TC_REGISTRATION_WITH_INVALID_EMAIL
    def test_registration_with_invalid_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_EMAIL')))
        CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_email(
            REG_LIST_14).get_url()

    # TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK
    def test_check_login_page_open_click_login_here_link(self):
        print("\n" + str(test_cases('TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK')))
        result = CanonizerRegisterPage(self.driver).check_login_page_open_click_login_here_link().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS
    def test_Verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS')))
        CanonizerRegisterPage(
            self.driver).click_register_button().verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(
            REG_LIST_15)

    # TC_VERIFYING_ACCOUNT_PROFILE
    def test_click_on_account_setting_page(self):
        self.login_to_canonizer_app()
        print("\n" + str(test_cases('TC_VERIFYING_ACCOUNT_PROFILE')))
        CanonizerAccountSettingPage(self.driver).click_account_settings_page_button()

    # TC_CLICK_ON_LOGIN_BUTTON
    def test_click_on_login_button(self):
        print("\n" + str(test_cases('TC_CLICK_ON_LOGIN_BUTTON')))
        result = CanonizerLoginPage(self.driver).click_on_login_button()

    # TC_CLICK_CLOSE_ICON_ON_LOGIN_PAGE
    def test_click_close_icon_on_login_page(self):
        print("\n" + str(test_cases('TC_CLICK_CLOSE_ICON_ON_LOGIN_PAGE')))
        result = CanonizerLoginPage(self.driver).click_on_close_icon_button().get_url()
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_LOGIN_WITH_REGISTERED_CREDENTIALS
    def test_login_with_registered_credentials(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        result = CanonizerLoginPage(self.driver).verify_the_Login_Functionality_by_entering_the_registered_credential(
            DEFAULT_USER, DEFAULT_PASS).get_url()
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_LOGIN_WITH_INVALID_EMAIL
    def test_login_with_invalid_email(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_INVALID_EMAIL')))
        result = CanonizerLoginPage(self.driver).verify_the_login_with_invalid_email_format(DEFAULT_INVALID_USER,
                                                                                            DEFAULT_INVALID_PASSWORD).get_url()
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_VERIFYING_REMEMBER_CHECK_BOX
    def test_click_on_remember_check_box(self):
        print("\n" + str(test_cases('TC_VERIFYING_REMEMBER_CHECK_BOX')))
        result = CanonizerLoginPage(self.driver).verify_the_Remember_me_checkbox(DEFAULT_USER,
                                                                                 DEFAULT_PASS).get_url()
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_VERIFYING_EMPTY_SPACE_FOR_EMAIL_FILED
    def test_verify_login_button_with_empty_space(self):
        print("\n" + str(test_cases('TC_VERIFYING_EMPTY_SPACE_FOR_EMAIL_FILED')))
        result = CanonizerLoginPage(self.driver).verify_the_login_button_by_entering_the_empty_space("",
                                                                                                     DEFAULT_PASS).get_url()
        self.assertIn("canonizer3.canonizer.com", result)

    #  TC_VERIFY_FORGET_PASSWORD
    def test_verify_forget_password_button(self):
        print("\n" + str(test_cases(' TC_VERIFY_FORGET_PASSWORD')))
        result = CanonizerLoginPage(self.driver).verify_the_forget_password_button().get_url()
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_ON_REGISTER_NOW_LINK
    def test_click_on_register_now_link(self):
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_NOW_LINK')))
        result = CanonizerLoginPage(self.driver).click_on_register_now_button_on_login_page().get_url()
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON
    def test_click_on_request_one_time_code(self):
        print("\n" + str(test_cases('TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON')))
        result = CanonizerLoginPage(self.driver).verify_one_time_request_code_without_entering_email().get_url()
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON_WITH_INVALID-EMAIL
    def test_click_on_request_one_time_code_with_invalid_email(self):
        print("\n" + str(test_cases('TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON_WITH_INVALID-EMAIL')))
        result = CanonizerLoginPage(self.driver).verify_one_time_request_code_with_invalid_email(
            DEFAULT_INVALID_USER, DEFAULT_PASS).get_url()
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_VERIFYING_SOCIAL LINKS
    def test_verifying_social_account_links(self):
        print("\n" + str(test_cases('TC_VERIFYING_SOCIAL LINKS')))
        result = CanonizerLoginPage(self.driver).verifying_social_account_links().get_url()
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_VERIFYING_FACEBOOK_LINK
    def test_verifying_facebook_link(self):
        print("\n" + str(test_cases('Tc_verifying_facebook_link')))
        result = CanonizerLoginPage(self.driver).verifying_facebook_icon().get_url()
        self.assertIn("", result)

    # TC_VERIFYING_GOOGLE_LINK
    def test_verify_google_link(self):
        print("\n" + str(test_cases('TC_VERIFYING_GOOGLE_LINK')))
        result = CanonizerLoginPage(self.driver).verifying_google_link().get_url()
        self.assertIn("", result)

    # TC_VERIFYING_TWITTER_LINK
    def test_verify_twitter_link(self):
        print("\n" + str(test_cases('TC_VERIFYING_TWITTER_LINK')))
        result = CanonizerLoginPage(self.driver).verifying_twitter_link().get_url()
        self.assertIn("", result)

    # TC_VERIFYING_LINKEDIN_LINK
    def test_verify_linkedin_link(self):
        print("\n" + str(test_cases('TC_VERIFYING_LINKEDIN_LINK')))
        result = CanonizerLoginPage(self.driver).verifying_linkedin_link().get_url()
        self.assertIn("", result)

    # TC_VERIFYING_GITHUB_LINK
    def test_verify_github_link(self):
        print("\n" + str(test_cases('TC_VERIFYING_GITHUB_LINK')))
        result = CanonizerLoginPage(self.driver).verifying_github_link().get_url()
        self.assertIn("", result)

    # TC_VERIFYING_LOGIN_PLACEHOLDERS
    def test_verify_login_placeholders(self):
        print("\n" + str(test_cases('TC_VERIFYING_LOGIN_PLACEHOLDERS')))
        CanonizerLoginPage(self.driver).verify_login_placeholders()

    # ACCOUNT_SETTING_PAGE:
    # TC_VERIFYING_ACCOUNT_PROFILE_PAGE
    def test_verifying_account_profile_page(self):
        self.login_to_canonizer_app()
        print("\n" + str(test_cases('TC_VERIFYING_ACCOUNT_PROFILE_PAGE')))
        result = CanonizerAccountSettingPage(self.driver).verifying_profile_button().get_url()
        self.assertIn("", result)

    # TC-VERIFYING_SOCIAL_OAUTH_VERIFICATION
    def test_verifying_social_oauth_page(self):
        print("\n" + str(test_cases('TC-VERIFYING_SOCIAL_OAUTH_VERIFICATION')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verifying_social_oauth_verification().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFICATION_CHANGE_PASSWORD
    def test_verifying_change_password(self):
        print("\n" + str(test_cases('TC_VERIFICATION_CHANGE_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verifying_change_password().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_NICK_NAME
    def test_verifying_nick_name(self):
        print("\n" + str(test_cases('TC_VERIFYING_NICK_NAME')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verifying_nick_name().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_SUPPORTED_CHANGES
    def test_verifying_supported_camps(self):
        print("\n" + str(test_cases('TC_VERIFYING_SUPPORTED_CHANGES')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verifying_supported_camps().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_VALIDATION_FOR_PROFILE_INFO_PHONE_NUMBER
    def test_verifying_invalid_phone_number(self):
        print("\n" + str(test_cases('TC_VERIFYING_VALIDATION_FOR_PROFILE_INFO_PHONE_NUMBER')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).check_the_validation_for_Phone_Number_field(
            "988874467444444").get_url()
        self.assertIn("", result)

    # TC_VERIFYING_VERIFY_BUTTON_WITH_BLANK_FIELDS
    def test_verifying_verify_button_without_entering_data(self):
        print("\n" + str(test_cases('TC_VERIFYING_VERIFY_BUTTON_WITH_BLANK_FIELDS')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).check_the_Functionality_of_verify_button_without_entering_the_data().get_url()
        self.assertIn("", result)

    # TC_VERIFYING_CLICK_ON_MOBILE_CARRIER_DROP_DOWN
    def test_click_on_mobile_carrier_drop_down(self):
        print("\n" + str(test_cases('TC_VERIFYING_CLICK_ON_MOBILE_CARRIER_DROP_DOWN')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).verify_the_functionality_of_mobile_carrier_drop_down().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_ALL_THE_FIELDS_ARE_PERSONAL_INFORMATION
    def test_verifying_all_the_feilds_are_personal_information(self):
        print("\n" + str(test_cases('TC_VERIFYING_ALL_THE_FIELDS_ARE_PERSONAL_INFORMATION')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).verify_all_the_fields_are_present_in_Personal_Information_field().get_url()
        self.assertIn("", result)

    # TC_VERIFYING_FIRST_NAME_FIELD_WITHOUT_ENTERING_DATA
    def test_verifying_validation_for_first_name_fields(self):
        print("\n" + str(test_cases('TC_VERIFYING_FIRST_NAME_FIELD_WITHOUT_ENTERING_DATA')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verify_the_validation_for_first_name(" ").get_url()
        self.assertIn("", result)

    # TC_UPDATE_THE_FIRST_NAME_AND_CHECK_IF_IT_IS_UPDATING_SAME_FOR_USERNAME
    def test_Update_the_first_name_and_check_if_it_is_updating_same_for_username(self):
        print("\n" + str(test_cases('TC_UPDATE_THE_FIRST_NAME_AND_CHECK_IF_IT_IS_UPDATING_SAME_FOR_USERNAME')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).update_the_first_name_and_check_if_it_is_updating_same_for_username("saideekshith").get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_RADIO_BUTTON_IN_SELECTING_THE_GENDER
    def test_Verify_the_functionality_of_radio_button_in_selecting_the_gender(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_RADIO_BUTTON_IN_SELECTING_THE_GENDER')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).verify_the_functionality_of_radio_button_in_selecting_the_gender().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_SELECTING_THE_DOB
    def test_Verify_the_functionality_of_selecting_the_DOB(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_SELECTING_THE_DOB')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verify_the_functionality_of_selecting_the_DOB(
            DEFAULT_USER).get_url()
        self.assertIn("", result)

    # TC_VERIFY_WHEN_USER_UPDATE_THE_PERSONAL_INFORMATION_AND_LOGS_OUT_AND_LOGIN_AGAIN
    def test_Verify_when_user_updated_the_Personal_Information_and_logs_out_and_logIn_again(self):
        print(
            "\n" + str(test_cases('TC_VERIFY_WHEN_USER_UPDATE_THE_PERSONAL_INFORMATION_AND_LOGS_OUT_AND_LOGIN_AGAIN')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).verify_when_user_updated_the_Personal_Information_and_logs_out_and_logIn_again("sai",
                                                                                                        "deekshith",
                                                                                                        "masuldari").get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_SPACES_ARE_TRIMMED_IN_THE_FIRSTNAME_LASTNAME_MIDDLENAME_fields
    def test_Verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_SPACES_ARE_TRIMMED_IN_THE_FIRSTNAME_LASTNAME_MIDDLENAME_fields')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields(DEFAULT_FIRST_NAME,
                                                                                                   DEFAULT_MIDDLE_NAME,
                                                                                                   DEFAULT_LAST_NAME).get_url()

    # TC VERIFY_WHEN_USER_CLICK_ON_CHANGE_PASSWORD
    def test_Verify_when_user_click_on_change_password(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_USER_CLICK_ON_CHANGE_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).verify_when_user_click_on_change_password_tab_its_navigating_to_change_Password_Page().get_url()
        self.assertIn("", result)

    # TC VERIFYING_CURRENT_PASSWORD_NEW_PASSWORD_CONFIRM_PASSWORD
    def test_Verify_self_current_password_new_password_confirm_password_is_present_save_button(self):
        print("\n" + str(test_cases('TC VERIFYING_CURRENT_PASSWORD_NEW_PASSWORD_CONFIRM_PASSWORD')))
        self.login_to_canonizer_app()
        CanonizerAccountSettingPage(
            self.driver).verify_current_password_new_password_confirm_password_is_present_save_button()

    # TC VERIFY_KEEPING_ALL_THE_FIELDS_EMPTY_AND_CLICK_ON_SAVE
    def test_Verify_keeping_all_the_fields_empty_and_click_on_save(self):
        print("\n" + str(test_cases('TC VERIFY_KEEPING_ALL_THE_FIELDS_EMPTY_AND_CLICK_ON_SAVE')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verify_keeping_all_the_fields_empty_and_click_on_save("", "",
                                                                                                                "").get_url()
        self.assertIn("", result)

    # TC VERIFY_ENTERING_THE_INVALID_CURRENT_PASSWORD
    def test_Verify_entering_the_invalid_current_password(self):
        print("\n" + str(test_cases('TC VERIFY_ENTERING_THE_INVALID_CURRENT_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verify_entering_the_invalid_current_password(
            INVALID_CURRENT_PASSWORD,
        ).get_url()
        self.assertIn("", result)

    # TC VERIFY_ENTERING_THE_INVALID_NEW_PASSWORD
    def test_Verify_entering_the_invalid_new_password(self):
        print("\n" + str(test_cases('TC_VERIFY_ENTERING_THE_INVALID_NEW_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verify_entering_the_invalid_new_password(
            INVALID_NEW_PASSWORD).get_url()
        self.assertIn("", result)

    # TC VERIFY_ENTERING_THE_INVALID_CONFIRM_PASSWORD
    def test_Verify_entering_the_invalid_confirm_password(self):
        print("\n" + str(test_cases('TC VERIFY_ENTERING_THE_INVALID_CONFIRM_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verify_entering_the_invalid_confirm_password(
            "DEFAULT_INVALID_CONFIRM_PASSWORD").get_url()
        self.assertIn("", result)

    # TC VERIFY_WHEN_BOTH_NEW_PASSWORD_AND_CONFIRM_PASSWORD_DOES_NOT_MATCH
    def test_Verify_when_both_new_Password_and_confirm_Password_does_not_match(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_BOTH_NEW_PASSWORD_AND_CONFIRM_PASSWORD_DOES_NOT_MATCH')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).verify_when_both_new_Password_and_confirm_Password_does_not_match(DEFAULT_NEW_PASSWORD,
                                                                                           DEFAULT_CONFIRM_PASSWORD).get_url()
        self.assertIn("", result)

    # TC VERIFY_WHEN_USER_CLICK_ON_NICK_NAME_TAB
    def test_Verify_when_user_click_on_Nick_Name_tab(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_USER_CLICK_ON_NICK_NAME_TAB')))
        self.login_to_canonizer_app()
        CanonizerManageNickNameTab(self.driver).verify_when_user_click_on_Nick_Name_tab().get_url()

    # TC_VERIFY_ALL_THE_HEADERS_IN_NICK_NAME_TAB
    def test_Verify_all_the_headers_In_nick_name_tab(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(self.driver).verify_all_the_headers_in_nick_name_tab().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFY_WITH_ADD_NICKNAME_BUTTON_IS_PRESENT0
    def test_verify_with_Add_nick_name_button_is_present(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(self.driver).verify_with_Add_nick_name_button_is_present().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # Tc_VERIFY_THE_FUNCTIONALITY_OF_ADD_NICKNAME_BUTTON
    def test_Verify_the_functionality_of_add_nickname_button(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(
            self.driver).verify_the_functionality_of_add_nickname_button().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFY_VALIDATION_FOR_ENTERING_NICK_NAME_FIELDS
    def test_Verify_validation_for_entering_nick_name_field(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(self.driver).verify_validation_for_entering_nick_name_field(
            DEFAULT_NICK_NAME).get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFY_VALIDATION_FOR_WITHOUT_ENTERING_NICK_NAME_FIELDS
    def test_Verify_validation_for_without_entering_nick_name_field(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(self.driver).verify_validation_for_without_entering_nick_name_field(
            "").get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFY_ENTERING_THE_NICK_NAME_WITH_MORE_THAN_ONE_SPACE
    def test_verify_entering_the_nick_name_with_more_than_one_space(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(self.driver).verify_entering_the_nick_name_with_more_than_one_space(
            DEFAULT_INVALID_NICK_NAME).get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFY_user_navigate_to_support_camp_page
    def test_verify_user_is_navigating_to_Supported_camp_page_when_clicks_on_supported_camps_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_user_navigate_to_support_camp_page')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCamps(
            self.driver).verify_user_is_navigating_to_Supported_camp_page_when_clicks_on_supported_camps_tab() \
            .get_url()
        self.assertIn("", result)

    # TC_VERIFY_DIRECT_SUPPORTED_CAMPS
    def test_verify_direct_supported_camps(self):
        print("\n" + str(test_cases('TC_VERIFY_DIRECT_SUPPORTED_CAMPS')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCamps(self.driver).verify_direct_supported_camps().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_SEARCH_BAR_IS_NEXT_TO_DELEGATED_SUPPORT_CAMP_TAB
    def test_verify_the_search_bar_is_present_next_the_delegate_support_camp_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_SEARCH_BAR_IS_NEXT_TO_DELEGATED_SUPPORT_CAMP_TAB')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCamps(self.driver).verify_the_search_bar_is_present_next_the_delegate_support_camp_tab(
        ).get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_DIRECT_SUPPORT_CAMP
    def test_verify_the_functionality_of_Direct_Support_Camp(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_DIRECT_SUPPORT_CAMP')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCamps(self.driver).verify_the_functionality_of_Direct_Support_Camp().get_url()
        self.assertIn("", result)

    #  TC_VERIFY_THE_FUNCTIONALITY_OF_DELEGATE_SUPPORT_CAMP
    def test_verify_the_functionality_of_Delegate_support_camp_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_DELEGATE_SUPPORT_CAMP')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCamps(self.driver).verify_the_functionality_of_Direct_Support_Camp().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_SEARCH_FUNCTIONALITY_IN_SUPPORTED_CAMPS_PAGE
    def test_verify_the_search_functionality_in_supported_camps_page(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_SEARCH_FUNCTIONALITY_IN_SUPPORTED_CAMPS_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCamps(self.driver).verify_the_search_functionality_in_supported_camps_page(
            DEFAULT_TOPIC_NAME).get_url()
        self.assertIn("", result)

    # TC_VERIFY_TOPIC_NAME_AND_AGREEMENT_CAMP_NAME_IN DIRECT_SUPPORT_CAMP
    def test_Verify_topic_name_and_agreement_camp_name_is_present_in_direct_support_camp_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_TOPIC_NAME_AND_AGREEMENT_CAMP_NAME_IN DIRECT_SUPPORT_CAMP')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCamps \
            (self.driver).Verify_topic_name_and_agreement_camp_name_is_present_in_direct_support_camp_tab().get_url()
        self.assertIn("", result)

    # TC_TOPIC_NAME_AND_CAMP_NAME_CLICKABLE
    def test_topic_name_and_camp_name_is_clickable(self):
        print("\n" + str(test_cases('TC_TOPIC_NAME_AND_CAMP_NAME_CLICKABLE')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCamps(self.driver).topic_name_and_camp_name_is_clickable().get_url()
        self.assertIn("", result)

    def test_verify_Remove_Support_button_functionality(self):
        self.login_to_canonizer_app()
        result = CanonizerSupportCamps(self.driver).verify_Remove_Support_button_functionality().get_url()
        self.assertIn("", result)


    # TC_CLICK_ON_BROWSE_PAGE
    def test_click_on_browse_page(self):
        self.assertIn("", result)

    # TC_VERIFY_ALL_THE_SPECIFIED_FIELDS_ARE_PRESENT_ON_THE_BROWSE_PAGE
    def test_Verify_all_the_specified_fields_are_present_on_the_Browse_page(self):
        self.login_to_canonizer_app()
        result = CanonizerBrowsePage.CanonizerBrowsePage(
            self.driver).verify_all_the_specified_fields_are_present_on_the_Browse_page().get_url()
        self.assertIn("", result)

    # TC_CHECK_FOR_THE_VALIDATION_OF_SELECT_NAMESPACE_DROP_DOWN
    def test_Check_for_the_validation_of_Select_Namespace_drop_down(self):
        self.login_to_canonizer_app()
        result = CanonizerBrowsePage.CanonizerBrowsePage(
            self.driver).Check_for_the_validation_of_Select_Namespace_drop_down().get_url()
        self.assertIn("", result)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
