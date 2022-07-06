import unittest
#from unittest import result

from selenium.common.exceptions import TimeoutException

import CanonizerBrowsePage
from CanonizerAcoountSettingPage import CanonizerAccountSettingPage
from CanonizerCreateNewTopicPage import CanonizerCreateNewTopic
from CanonizerHomePage import *
from CanonizerLoginPage import CanonizerLoginPage
from CanonizerRegistrationPage import CanonizerRegisterPage
from CanonizerForgotPasswordPage import *
from CanonizerTestCases import test_cases
from Config import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import string
import random


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
                                                                                                 DEFAULT_PASSWORD).get_url()
        self.assertIn("", result)
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/h3')))
        except TimeoutException:
            pass

    # TC_CLICK_ON_REGISTER_BUTTON
    def test_canonizer_click_register_page(self, ):
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_BUTTON')))
        result = CanonizerRegisterPage(self.driver).click_register_button().get_url()
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
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_last_name(
            REG_LIST_4).get_url()
        self.assertIn("", result)

    # TC_REGISTRATION_WITH_BLANK_EMAIL
    def test_registration_with_blank_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_EMAIL')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_email(
            REG_LIST_5)

    # TC_REGISTRATION_WITH_BLANK_PASSWORD
    def test_registration_with_blank_password(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_PASSWORD')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_password(
            REG_LIST_6)

    # TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH
    def test_registration_with_invalid_password_length(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_password_length(
            REG_LIST_7)

    # TC_REGISTRATION_WITH_DIFFERENT_CONFIRM_PASSWORD
    def test_registration_with_different_confirmation_password(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_DIFFERENT_CONFIRM_PASSWORD')))
        result = CanonizerRegisterPage(
            self.driver).click_register_button().registration_with_different_confirmation_password(
            REG_LIST_8)

    # TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME
    def test_registration_with_blank_spaces_first_name(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_spaces_first_name(
            REG_LIST_1)

    # TC_REGISTRATION_WITH_INVALID_FIRST_NAME
    def test_registration_with_invalid_first_name(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_FIRST_NAME')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_first_name(
            REG_LIST_10)

    # TC_REGISTRATION_WITH_INVALID_LAST_NAME
    def test_registration_with_invalid_last_name(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_LAST_NAME')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_last_name(
            REG_LIST_11)

    # TC_REGISTRATION_WITH_INVALID_EMAIL
    def test_registration_with_invalid_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_EMAIL')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_email(
            REG_LIST_14)

    # TC_CLICK_ON_REGISTER_BUTTON
    def test_click_on_register_button(self):
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_BUTTON')))
        result = CanonizerRegisterPage(self.driver).click_on_register_button()

    # TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK
    def test_check_login_page_open_click_login_here_link(self):
        # print("\n" + str(test_cases('TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK')))
        result = CanonizerRegisterPage(self.driver).check_login_page_open_click_login_here_link()

    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS
    def test_Verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTERATION_WITH_MANDATORY_FIELDS')))
        result = CanonizerRegisterPage(
            self.driver).click_register_button().Verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(
            REG_LIST_15)

    # TC_VERIFYING_ACCOUNT_PROFILE
    def test_click_on_account_setting_page(self):
        self.login_to_canonizer_app()
        print("\n" + str(test_cases(' TC_VERIFYING_ACCOUNT_PROFILE')))
        result = CanonizerAccountSettingPage(self.driver).click_account_settings_page_button()
        print(result)

    # TC_CLICK_ON_LOGIN_BUTTON
    def test_click_on_login_button(self):
        print("\n" + str(test_cases('TC_CLICK_ON_LOGIN_BUTTON')))
        result = CanonizerLoginPage(self.driver).click_on_login_button().get_url()
        print(result)

    # TC_VERIFY_LOGIN_PAGE
    def test_verify_login_page(self):
        print("\n" + str(test_cases('TC_VERIFY_LOGIN_PAGE')))
        result = CanonizerLoginPage(self.driver).verify_canonizer_login_page().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_CLOSE_ICON_ON_LOGIN_PAGE
    def test_click_close_icon_on_login_page(self):
        print("\n" + str(test_cases('TC_CLICK_CLOSE_ICON_ON_LOGIN_PAGE')))
        result = CanonizerLoginPage(self.driver).click_on_close_icon_button().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_LOGIN_WITH_REGISTERED_CREDENTIALS
    def test_login_with_registered_credentials(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        result = CanonizerLoginPage(self.driver).verify_the_Login_Functionality_by_entering_the_registered_credential(
            DEFAULT_USER, DEFAULT_PASS).get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_LOGIN_WITH_INVALID_EMAIL
    def test_login_with_invalid_email(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_INVALID_EMAIL')))
        result = CanonizerLoginPage(self.driver).verify_the_login_with_invalid_email_format(DEFAULT_INVALID_USER,
                                                                                            DEFAULT_INVALID_PASSWORD).get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_VERIFYING_REMEMBER_CHECK_BOX
    def test_click_on_remember_check_box(self):
        print("\n" + str(test_cases('TC_VERIFYING_REMEMBER_CHECK_BOX')))
        result = CanonizerLoginPage(self.driver).verify_the_Remember_me_checkbox(DEFAULT_USER,
                                                                                 DEFAULT_PASS).get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_VERIFYING_EMPTY_SPACE_FOR_EMAIL_FILED
    def test_verify_login_button_with_empty_space(self):
        print("\n" + str(test_cases('TC_VERIFYING_EMPTY_SPACE_FOR_EMAIL_FILED')))
        result = CanonizerLoginPage(self.driver).verify_the_login_button_by_entering_the_empty_space("",
                                                                                                     DEFAULT_PASS).get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    #  TC_VERIFY_FORGET_PASSWORD
    def test_verify_forget_password_button(self):
        print("\n" + str(test_cases(' TC_VERIFY_FORGET_PASSWORD')))
        result = CanonizerLoginPage(self.driver).verify_the_forget_password_button().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_ON_REGISTER_NOW_LINK
    def test_click_on_register_now_link(self):
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_NOW_LINK')))
        result = CanonizerLoginPage(self.driver).click_on_register_now_button_on_login_page().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON
    def test_click_on_request_one_time_code(self):
        print("\n" + str(test_cases('TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON')))
        result = CanonizerLoginPage(self.driver).verify_one_time_request_code_without_entering_email().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON_WITH_INVALID-EMAIL
    def test_click_on_request_one_time_code_with_invalid_email(self):
        print("\n" + str(test_cases('TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON_WITH_INVALID-EMAIL')))
        result = CanonizerLoginPage(self.driver).verify_one_time_request_code_with_invalid_email(
            "sai@122gmail", "Sai@1998").get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_VERIFYING_SOCIAL LINKS
    def test_verifying_social_account_links(self):
        print("\n" + str(test_cases('TC_VERIFYING_SOCIAL LINKS')))
        result = CanonizerLoginPage(self.driver).verifying_social_account_links().get_url()
        print(result)
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

    # ACCOUNT_SETTING_PAGE:
    # TC_VERIFYING_ACCOUNT_PROFILE_PAGE
    def test_verifying_account_profile_page(self):
        self.login_to_canonizer_app()
        print("\n" + str(test_cases('TC_VERIFYING_ACCOUNT_PROFILE_PAGE')))
        result = CanonizerAccountSettingPage(self.driver).verifying_profile_button().get_url()
        print(result)
        self.assertIn("", result)

    # TC-VERIFYING_SOCIAL_OAUTH_VERIFICATION
    def test_verifying_social_oauth_page(self):
        print("\n" + str(test_cases('TC-VERIFYING_SOCIAL_OAUTH_VERIFICATION')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verifying_social_oauth_verification().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFICATION_CHANGE_PASSWORD
    def test_verifying_change_password(self):
        print("\n" + str(test_cases('TC_VERIFICATION_CHANGE_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verifying_change_password().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_NICK_NAME
    def test_verifying_nick_name(self):
        print("\n" + str(test_cases('TC_VERIFYING_NICK_NAME')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verifying_nick_name().get_url()
        print(result)
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
        result = CanonizerAccountSettingPage(self.driver).Check_the_validation_for_Phone_Number_field(
            "988874467444444").get_url()
        self.assertIn("", result)

    # TC_VERIFYING_VERIFY_BUTTON_WITH_BLANK_FIELDS
    def test_verifying_verify_button_without_entering_data(self):
        print("\n" + str(test_cases('TC_VERIFYING_VERIFY_BUTTON_WITH_BLANK_FIELDS')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Check_the_Functionality_of_verify_button_without_entering_the_data().get_url()
        self.assertIn("", result)

    # TC_VERIFYING_CLICK_ON_MOBILE_CARRIER_DROP_DOWN
    def test_click_on_mobile_carrier_drop_down(self):
        print("\n" + str(test_cases('TC_VERIFYING_CLICK_ON_MOBILE_CARRIER_DROP_DOWN')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_the_functionality_of_mobile_carrier_drop_down().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_ALL_THE_FIELDS_ARE_PERSONAL_INFORMATION
    def test_verifying_all_the_feilds_are_personal_information(self):
        print("\n" + str(test_cases('TC_VERIFYING_ALL_THE_FIELDS_ARE_PERSONAL_INFORMATION')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_all_the_fields_are_present_in_Personal_Information_field().get_url()
        self.assertIn("", result)

    # TC_VERIFYING_FIRST_NAME_FIELD_WITHOUT_ENTERING_DATA
    def test_verifying_validation_for_first_name_fields(self):
        print("\n" + str(test_cases('TC_VERIFYING_FIRST_NAME_FIELD_WITHOUT_ENTERING_DATA')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_the_validation_for_first_name(" ").get_url()
        self.assertIn("", result)

    # TC_UPDATE_THE_FIRST_NAME_AND_CHECK_IF_IT_IS_UPDATING_SAME_FOR_USERNAME
    def test_Update_the_first_name_and_check_if_it_is_updating_same_for_username(self):
        print("\n" + str(test_cases('TC_UPDATE_THE_FIRST_NAME_AND_CHECK_IF_IT_IS_UPDATING_SAME_FOR_USERNAME')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Update_the_first_name_and_check_if_it_is_updating_same_for_username("saideekshith").get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_RADIO_BUTTON_IN_SELECTING_THE_GENDER
    def test_Verify_the_functionality_of_radio_button_in_selecting_the_gender(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_RADIO_BUTTON_IN_SELECTING_THE_GENDER')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_the_functionality_of_radio_button_in_selecting_the_gender().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_SELECTING_THE_DOB
    def test_Verify_the_functionality_of_selecting_the_DOB(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_SELECTING_THE_DOB')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_the_functionality_of_selecting_the_DOB(
            DEFAULT_USER).get_url()
        self.assertIn("", result)

    # TC_VERIFY_WHEN_USER_UPDATE_THE_PERSONAL_INFORMATION_AND_LOGS_OUT_AND_LOGIN_AGAIN
    def test_Verify_when_user_updated_the_Personal_Information_and_logs_out_and_logIn_again(self):
        print(
            "\n" + str(test_cases('TC_VERIFY_WHEN_USER_UPDATE_THE_PERSONAL_INFORMATION_AND_LOGS_OUT_AND_LOGIN_AGAIN')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_when_user_updated_the_Personal_Information_and_logs_out_and_logIn_again("sai",
                                                                                                        "deekshith",
                                                                                                        "masuldari").get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_SPACES_ARE_TRIMMED_IN_THE_FIRSTNAME_LASTNAME_MIDDLENAME_fields
    def test_Verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_SPACES_ARE_TRIMMED_IN_THE_FIRSTNAME_LASTNAME_MIDDLENAME_fields')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields("sssss  sssss",
                                                                                                   "dddd dd     dd",
                                                                                                   "dsd sd   dsd").get_url()

    # TC VERIFY_WHEN_USER_CLICK_ON_CHANGE_PASSWORD
    def test_Verify_when_user_click_on_change_password(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_USER_CLICK_ON_CHANGE_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_when_user_click_on_change_password_tab_its_navigating_to_change_Password_Page().get_url()
        self.assertIn("", result)

    # TC VERIFYING_CURRENT_PASSWORD_NEW_PASSWORD_CONFIRM_PASSWORD
    def test_Verify_self_current_password_new_password_confirm_password_is_present_save_button(self):
        print("\n" + str(test_cases('TC VERIFYING_CURRENT_PASSWORD_NEW_PASSWORD_CONFIRM_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_self_current_password_new_password_confirm_password_is_present_save_button()

    # TC VERIFY_KEEPING_ALL_THE_FIELDS_EMPTY_AND_CLICK_ON_SAVE
    def test_Verify_keeping_all_the_fields_empty_and_click_on_save(self):
        print("\n" + str(test_cases('TC VERIFY_KEEPING_ALL_THE_FIELDS_EMPTY_AND_CLICK_ON_SAVE')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_keeping_all_the_fields_empty_and_click_on_save("", "",
                                                                                                                "").get_url()
        self.assertIn("", result)

    # TC VERIFY_ENTERING_THE_INVALID_CURRENT_PASSWORD
    def test_Verify_entering_the_invalid_current_password(self):
        print("\n" + str(test_cases('TC VERIFY_ENTERING_THE_INVALID_CURRENT_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).test_Verify_entering_the_invalid_current_password(
            "sai@    12333",
        ).get_url()
        self.assertIn("", result)

    # TC VERIFY_ENTERING_THE_INVALID_NEW_PASSWORD
    def test_Verify_entering_the_invalid_new_password(self):
        print("\n" + str(test_cases('TC_VERIFY_ENTERING_THE_INVALID_NEW_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_entering_the_invalid_new_password(
            "sai@    123333").get_url()
        self.assertIn("", result)

    # TC VERIFY_ENTERING_THE_INVALID_CONFIRM_PASSWORD
    def test_Verify_entering_the_invalid_confirm_password(self):
        print("\n" + str(test_cases('TC VERIFY_ENTERING_THE_INVALID_CONFIRM_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_entering_the_invalid_confirm_password(
            "sai@   12333333").get_url()
        self.assertIn("", result)

    # TC VERIFY_WHEN_BOTH_NEW_PASSWORD_AND_CONFIRM_PASSWORD_DOES_NOT_MATCH
    def test_Verify_when_both_new_Password_and_confirm_Password_does_not_match(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_BOTH_NEW_PASSWORD_AND_CONFIRM_PASSWORD_DOES_NOT_MATCH')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_when_both_new_Password_and_confirm_Password_does_not_match("Sai@199828",
                                                                                           "Sai@166666").get_url()
        self.assertIn("", result)

    # TC VERIFY_WHEN_USER_CLICK_ON_NICK_NAME_TAB
    def test_Verify_when_user_click_on_Nick_Name_tab(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_USER_CLICK_ON_NICK_NAME_TAB')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_when_user_click_on_Nick_Name_tab().get_url()
        self.assertIn("", result)

    # TC_VERIFY_ALL_THE_HEADERS_IN_NICK_NAME_TAB
    def test_Verify_all_the_headers_In_nick_name_tab(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_all_the_headers_in_nick_name_tab().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFY_WITH_ADD_NICKNAME_BUTTON_IS_PRESENT
    def test_verify_with_Add_nick_name_button_is_present(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verify_with_Add_nick_name_button_is_present().get_url()
        self.assertIn("", result)

    # Tc_VERIFY_THE_FUNCTIONALITY_OF_ADD_NICKNAME_BUTTON
    def test_Verify_the_functionality_of_add_nickname_button(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_the_functionality_of_add_nickname_button().get_url()
        self.assertIn("", result)

    # TC_VERIFY_VALIDATION_FOR_ENTERING_NICK_NAME_FIELDS
    def test_Verify_validation_for_entering_nick_name_field(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_validation_for_entering_nick_name_field(
            "saideekshith").get_url()
        self.assertIn("", result)

    # TC_VERIFY_VALIDATION_FOR_WITHOUT_ENTERING_NICK_NAME_FIELDS
    def test_Verify_validation_for_without_entering_nick_name_field(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_validation_for_without_entering_nick_name_field(
            "").get_url()
        self.assertIn("", result)


    # TC_VERIFY_ALL_THE_SPECIFIED_FIELDS_ARE_PRESENT_ON_THE_BROWSE_PAGE
    def test_Verify_all_the_specified_fields_are_present_on_the_Browse_page(self):
        self.login_to_canonizer_app()
        result = CanonizerBrowsePage.CanonizerBrowsePage(
            self.driver).Verify_all_the_specified_fields_are_present_on_the_Browse_page().get_url()
        self.assertIn("", result)

    # TC_CHECK_FOR_THE_VALIDATION_OF_SELECT_NAMESPACE_DROP_DOWN
    def test_Check_for_the_validation_of_Select_Namespace_drop_down(self):
        self.login_to_canonizer_app()
        result = CanonizerBrowsePage.CanonizerBrowsePage(self.driver).Check_for_the_validation_of_Select_Namespace_drop_down().get_url()
        self.assertIn("", result)

    # 01
    def test_canonizer_home_page_load(self):
        print("\n" + str(test_cases(0)))
        self.assertTrue(CanonizerMainPage(self.driver).check_home_page_loaded())

    # ----- FORGOT PASSWORD Test Cases Start -----
    # TC_CLICK_FORGOT_PASSWORD_LINK
    def test_click_forgot_password_link(self):
        print("\n" + str(test_cases('TC_CLICK_FORGOT_PASSWORD_LINK')))
        result = CanonizerForgotPasswordPage(self.driver).click_forgot_password_link().get_url()
        self.assertIn("", result)

    # TC_SUBMIT_BUTTON_WITH_VALID_EMAIL_AND_CHECK_OTP_SCREEN
    def test_click_submit_button_with_valid_email(self):
        print("\n" + str(test_cases('TC_SUBMIT_BUTTON_WITH_VALID_EMAIL_AND_CHECK_OTP_SCREEN')))
        result = CanonizerForgotPasswordPage(self.driver).login_and_forgot_password()\
            .click_submit_button_with_valid_email(DEFAULT_USER).get_url()
        self.assertIn("", result)

    # TC_SUBMIT_BUTTON_WITH_INVALID_EMAIL
    def test_click_submit_button_with_invalid_email(self):
        print("\n" + str(test_cases('TC_SUBMIT_BUTTON_WITH_INVALID_EMAIL')))
        result = CanonizerForgotPasswordPage(self.driver).login_and_forgot_password() \
            .click_submit_button_with_invalid_email(DEFAULT_USER_INVALID).get_url()
        self.assertIn("", result)

    # TC_SUBMIT_BUTTON_WITH_EMPTY_EMAIL
    def test_click_submit_button_with_empty_email(self):
        print("\n" + str(test_cases('TC_SUBMIT_BUTTON_WITH_EMPTY_EMAIL')))
        result = CanonizerForgotPasswordPage(self.driver).login_and_forgot_password() \
            .click_submit_button_with_empty_email(" ").get_url()
        self.assertIn("", result)

    # TC_SUBMIT_EMPTY_OTP
    def test_submit_empty_OTP(self):
        print("\n" + str(test_cases('TC_SUBMIT_EMPTY_OTP')))
        result = CanonizerForgotPasswordPage(self.driver).login_and_forgot_password()\
            .submit_empty_otp(DEFAULT_USER).get_url()
        self.assertIn("", result)

    # TC_SUBMIT_INVALID_LENGTH_OTP
    def test_invalid_otp(self):
        print("\n" + str(test_cases('TC_SUBMIT_INVALID_LENGTH_OTP')))
        result = CanonizerForgotPasswordPage(self.driver).login_and_forgot_password()\
            .submit_invalid_otp(DEFAULT_USER, INVALID_LONG_OTP).get_url()
        self.assertIn("", result)

    # TC_CROSS_ICON_ON_FORGOT_MODAL
    def test_cross_icon_on_forgot_page(self):
        print("\n" + str(test_cases('TC_CROSS_ICON_ON_FORGOT_MODAL')))
        result = CanonizerForgotPasswordPage(self.driver).login_and_forgot_password()\
            .cross_icon_on_forgot_page().get_url()
        self.assertIn("", result)

    # TC_CROSS_ICON_ON_OTP_MODAL
    def test_cross_icon_on_otp_page(self):
        print("\n" + str(test_cases('TC_CROSS_ICON_ON_OTP_MODAL')))
        result = CanonizerForgotPasswordPage(self.driver).login_and_forgot_password()\
            .cross_icon_on_otp_page(DEFAULT_USER).get_url()
        self.assertIn("", result)

        # ----- FORGOT PASSWORD Test Cases end -----
        # ----- CREATE TOPIC Test Cases Start -----
        # TC_CLICK_CREATE_TOPIC_WITH_USER_LOGIN
    def test_click_create_new_topic_page_button(self):
        print("\n" + str(test_cases('TC_CLICK_CREATE_TOPIC_WITH_USER_LOGIN')))
        self.login_to_canonizer_app()
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button().get_url()
        self.assertIn("/create/topic", result)

    # TC_CLICK_CREATE_TOPIC_WITHOUT_USER_LOGIN
    def test_click_create_topic_without_user_login(self):
        print("\n" + str(test_cases('TC_CLICK_CREATE_TOPIC_WITHOUT_USER_LOGIN')))
        result = CanonizerCreateNewTopic(self.driver).click_create_topic_without_user_login().get_url()
        self.assertIn("/login?returnUrl=%2Fcreate%2Ftopic", result)

    # TC_CREATE_TOPIC_WITH_BLANK_TOPIC_NAME
    def test_create_topic_with_blank_topic_name(self):
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_BLANK_TOPIC_NAME')))
        self.login_to_canonizer_app()
        # Click on the Create New Topic link and check if topic name is blank
        result = CanonizerCreateNewTopic(
            self.driver).click_create_new_topic_page_button().create_topic_with_blank_topic_name(
            DEFAULT_NICK_NAME,
            DEFAULT_NAMESPACE,
            DEFAULT_SUMMARY).get_url()
        self.assertIn("create/topic", result)

    # TC_CREATE_NEW_TOPIC_WITH_VALID_DATA
    def test_create_topic_name_with_valid_data(self):
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button().create_topic_with_valid_data(
            DEFAULT_NICK_NAME,
            "New Topic " + add_name,
            DEFAULT_NAMESPACE,
            DEFAULT_SUMMARY
            ).get_url()
        self.assertIn("topic", result)

    # TC_CREATE_NEW_TOPIC_WITH_ENTER_KEY
    def test_create_topic_name_with_enter_key(self):
        print("\n", str(test_cases('TC_CREATE_NEW_TOPIC_WITH_ENTER_KEY')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button() \
            .create_topic_name_with_enter_key(
            DEFAULT_NICK_NAME,
            "New Topic " + add_name,
            DEFAULT_NAMESPACE,
            DEFAULT_SUMMARY
            ).get_url()
        self.assertIn("topic", result)

    # TC_CREATE_TOPIC_WITH_BLANK_SPACES_TOPIC_NAME
    def test_create_topic_with_blank_spaces_topic_name(self):
        print("\n", str(test_cases('TC_CREATE_TOPIC_WITH_BLANK_SPACES_TOPIC_NAME')))
        self.login_to_canonizer_app()
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button() \
            .create_topic_with_blank_spaces_topic_name(
            "       ",
            DEFAULT_NICK_NAME,
            DEFAULT_NAMESPACE,
            DEFAULT_SUMMARY).get_url()
        self.assertIn("create/topic", result)

    # TC_CREATE_NEW_TOPIC_WITH_TRAILING_SPACES
    def test_create_topic_name_with_trailing_space(self):
        print("\n", str(test_cases('TC_CREATE_NEW_TOPIC_WITH_TRAILING_SPACES')))
        self.login_to_canonizer_app()
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button() \
            .create_topic_name_with_trailing_space(
            DEFAULT_NICK_NAME,
            "        Topic with Trailing spaces",
            DEFAULT_NAMESPACE,
            DEFAULT_SUMMARY
            ).get_url()
        self.assertIn("topic", result)

    # TC_CREATE_TOPIC_WITH_DUPLICATE_NAME
    def test_create_topic_with_duplicate_topic_name(self):
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_DUPLICATE_NAME')))
        # Click on the Login Page and Create a Login Session and for further actions.
        self.login_to_canonizer_app()
        # Click on the Create New Topic link and check for duplicate topic name
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button().create_topic_with_duplicate_topic_name(
            DEFAULT_NICK_NAME,
            DUPLICATE_TOPIC_NAME,
            DEFAULT_NAMESPACE,
            DEFAULT_SUMMARY).get_url()
        self.assertIn("create/topic", result)

    # TC_CREATE_NEW_TOPIC_WITH_INVALID_DATA
    def test_create_topic_with_invalid_data(self):
        print("\n", str(test_cases('TC_CREATE_NEW_TOPIC_WITH_INVALID_DATA')))
        self.login_to_canonizer_app()
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button() \
            .create_topic_with_invalid_data(
            DEFAULT_NICK_NAME,
            INVALID_TOPIC_NAME,
            DEFAULT_NAMESPACE,
            DEFAULT_SUMMARY).get_url()
        self.assertIn("create/topic", result)

    # TC_CREATE_NEW_WITHOUT_MANDATORY_FIELDS_DATA
    def test_create_topic_without_entering_mandatory_fields(self):
        print("\n", str(test_cases('TC_CREATE_NEW_WITHOUT_MANDATORY_FIELDS_DATA')))
        self.login_to_canonizer_app()
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button() \
            .create_topic_without_entering_mandatory_fields(
            "",
            "",
            "",
            "",).get_url()
        self.assertIn("create/topic", result)

    # TC_CREATE_NEW_TOPIC_ENTERING_DATA_ONLY_IN_MANDATORY_FIELDS
    def test_create_topic_with_entering_data_only_in_mandatory_fields(self):
        print("\n", str(test_cases('TC_CREATE_NEW_TOPIC_ENTERING_DATA_ONLY_IN_MANDATORY_FIELDS')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button() \
            .create_topic_with_entering_data_only_in_mandatory_fields(
            DEFAULT_NICK_NAME,
            "New Topic " + add_name,
            DEFAULT_NAMESPACE,
            "",
            ).get_url()
        self.assertIn("topic", result)

    # TC_CLICK_ON_CANCEL_BUTTON
    def test_click_on_cancel_button(self):
        print("\n", str(test_cases('TC_CLICK_ON_CANCEL_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button().click_on_cancel_button()
        self.assertIn("canonizer.com", result.get_url())

    # TC_TOPIC_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK
    def test_topic_page_mandatory_fields_are_marked_with_asterisk(self):
        print("\n" + str(test_cases('TC_TOPIC_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK')))
        self.login_to_canonizer_app()
        self.assertTrue(CanonizerCreateNewTopic(
            self.driver).click_create_new_topic_page_button().topic_page_mandatory_fields_are_marked_with_asterisk())







    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
