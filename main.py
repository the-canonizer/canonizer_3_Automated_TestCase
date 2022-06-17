import unittest
from unittest import result

import self as self
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException

from CanonizerLoginPage import CanonizerLoginPage
from CanonizerRegistrationPage import CanonizerRegisterPage

from CanonizerChangePasswordTab import CanonizerChangePasswordTab
from CanonizerManageNickNameTab import CanonizerManageNickNameTab
from CanonizerSupportCampsTab import CanonizerSupportCampsTab


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
        CanonizerRegisterPage(self.driver).click_on_register_button()

    # TC_REGISTER_WITH_BLANK_FIRST_NAME
    def test_registration_with_blank_first_name(self, ):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_FIRST_NAME')))
        CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_first_name(
            REG_LIST_3)

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
    def test_verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS')))
        CanonizerRegisterPage(
            self.driver).click_register_button().verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(
            REG_LIST_15)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS
    def test_verify_the_functionality_0f_registration_with_entering_data_in_mobile_number_field(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS')))
        CanonizerRegisterPage(
            self.driver).click_register_button().verify_the_functionality_0f_registration_with_entering_data_in_mobile_number_field(
            REG_LIST_16)

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
        result = CanonizerLoginPage(self.driver).verify_the_login_functionality_by_entering_the_registered_credential(
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
        result = CanonizerLoginPage(self.driver).verify_the_remember_me_checkbox(DEFAULT_USER,
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


    # TC VERIFY_WHEN_USER_CLICK_ON_CHANGE_PASSWORD
    def test_verify_when_user_click_on_change_password(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_USER_CLICK_ON_CHANGE_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(
            self.driver).verify_click_on_change_password_tab_its_navigating_to_change_password_page().get_url()
        self.assertIn("", result)

    # TC VERIFY_KEEPING_ALL_THE_FIELDS_EMPTY_AND_CLICK_ON_SAVE
    def test_verify_keeping_all_the_fields_empty_and_click_on_save(self):
        print("\n" + str(test_cases('TC VERIFY_KEEPING_ALL_THE_FIELDS_EMPTY_AND_CLICK_ON_SAVE')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(
            self.driver).verify_keeping_all_the_fields_empty_and_click_on_save().get_url()
        self.assertIn("", result)

    # TC VERIFY_ENTERING_THE_INVALID_CURRENT_PASSWORD
    def test_verify_entering_the_invalid_current_password(self):
        print("\n" + str(test_cases('TC VERIFY_ENTERING_THE_INVALID_CURRENT_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(self.driver).verify_entering_the_invalid_current_password(
            INVALID_CURRENT_PASSWORD,
        ).get_url()
        self.assertIn("", result)

    # TC VERIFY_ENTERING_THE_INVALID_NEW_PASSWORD
    def test_verify_entering_the_invalid_new_password(self):
        print("\n" + str(test_cases('TC_VERIFY_ENTERING_THE_INVALID_NEW_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(self.driver).verify_entering_the_invalid_new_password(
            INVALID_NEW_PASSWORD).get_url()
        self.assertIn("", result)

    # TC VERIFY_ENTERING_THE_INVALID_CONFIRM_PASSWORD
    def test_verify_entering_the_invalid_confirm_password(self):
        print("\n" + str(test_cases('TC VERIFY_ENTERING_THE_INVALID_CONFIRM_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(self.driver).verify_entering_the_invalid_confirm_password(
            "DEFAULT_INVALID_CONFIRM_PASSWORD").get_url()
        self.assertIn("", result)

    # TC VERIFY_WHEN_BOTH_NEW_PASSWORD_AND_CONFIRM_PASSWORD_DOES_NOT_MATCH
    def test_verify_when_both_new_password_and_confirm_password_does_not_match(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_BOTH_NEW_PASSWORD_AND_CONFIRM_PASSWORD_DOES_NOT_MATCH')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(
            self.driver).verify_when_both_new_password_and_confirm_password_does_not_match(DEFAULT_NEW_PASSWORD,
                                                                                           DEFAULT_CONFIRM_PASSWORD).get_url()
        self.assertIn("", result)

    # TC VERIFY_WHEN_USER_CLICK_ON_NICK_NAME_TAB
    def test_verify_when_user_click_on_nick_name_tab(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_USER_CLICK_ON_NICK_NAME_TAB')))
        self.login_to_canonizer_app()
        CanonizerManageNickNameTab(self.driver).verify_when_user_click_on_nick_name_tab().get_url()

    # TC_VERIFY_ALL_THE_HEADERS_IN_NICK_NAME_TAB
    def test_verify_all_the_headers_in_nick_name_tab(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(self.driver).verify_all_the_headers_in_nick_name_tab().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFY_WITH_ADD_NICKNAME_BUTTON_IS_PRESENT0
    def test_verify_with_add_nick_name_button_is_present(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(self.driver).verify_with_add_nick_name_button_is_present().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # Tc_VERIFY_THE_FUNCTIONALITY_OF_ADD_NICKNAME_BUTTON
    def test_verify_the_functionality_of_add_nickname_button(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(
            self.driver).verify_the_functionality_of_add_nickname_button().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFY_VALIDATION_FOR_ENTERING_NICK_NAME_FIELDS
    def test_verify_validation_for_entering_nick_name_field(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(self.driver).verify_validation_for_entering_nick_name_field(
            DEFAULT_NICK_NAME).get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFY_VALIDATION_FOR_WITHOUT_ENTERING_NICK_NAME_FIELDS
    def test_verify_validation_for_without_entering_nick_name_field(self):
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

    # TC_VERIFY_USER_NAVIGATE_SUPPORT_CAMP_PAGE
    def test_verify_user_is_navigating_to_supported_camp_page_when_clicks_on_supported_camps_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_USER_NAVIGATE_SUPPORT_CAMP_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(
            self.driver).verify_user_is_navigating_to_supported_camp_page_when_clicks_on_supported_camps_tab() \
            .get_url()
        self.assertIn("", result)

    # TC_VERIFY_DIRECT_SUPPORTED_CAMPS
    def test_verify_direct_supported_camps(self):
        print("\n" + str(test_cases('TC_VERIFY_DIRECT_SUPPORTED_CAMPS')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_direct_supported_camps().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_SEARCH_BAR_IS_NEXT_TO_DELEGATED_SUPPORT_CAMP_TAB
    def test_verify_the_search_bar_is_present_next_the_delegate_support_camp_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_SEARCH_BAR_IS_NEXT_TO_DELEGATED_SUPPORT_CAMP_TAB')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(
            self.driver).verify_the_search_bar_is_present_next_the_delegate_support_camp_tab(
        ).get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_DIRECT_SUPPORT_CAMP
    def test_verify_the_functionality_of_direct_support_camp(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_DIRECT_SUPPORT_CAMP')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_the_functionality_of_direct_support_camp().get_url()
        self.assertIn("", result)

    #  TC_VERIFY_THE_FUNCTIONALITY_OF_DELEGATE_SUPPORT_CAMP
    def test_verify_the_functionality_of_delegate_support_camp_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_DELEGATE_SUPPORT_CAMP')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_the_functionality_of_delegate_support_camp_tab().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_SEARCH_FUNCTIONALITY_IN_SUPPORTED_CAMPS_PAGE
    def test_verify_the_search_functionality_in_supported_camps_page(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_SEARCH_FUNCTIONALITY_IN_SUPPORTED_CAMPS_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_the_search_functionality_in_supported_camps_page(
            DEFAULT_TOPIC_NAME).get_url()
        self.assertIn("", result)

    # TC_VERIFY_TOPIC_NAME_AND_AGREEMENT_CAMP_NAME_IN DIRECT_SUPPORT_CAMP
    def test_verify_topic_name_and_agreement_camp_name_is_present_in_direct_support_camp_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_TOPIC_NAME_AND_AGREEMENT_CAMP_NAME_IN DIRECT_SUPPORT_CAMP')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab \
            (self.driver).verify_topic_name_and_agreement_camp_name_is_present_in_direct_support_camp_tab().get_url()
        self.assertIn("", result)

    # TC_TOPIC_NAME_AND_CAMP_NAME_CLICKABLE
    def test_topic_name_and_camp_name_is_clickable(self):
        print("\n" + str(test_cases('TC_TOPIC_NAME_AND_CAMP_NAME_CLICKABLE')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).topic_name_and_camp_name_is_clickable().get_url()
        self.assertIn("", result)

    # TC_VERIFY_REMOVE_SUPPORT_BUTTON
    def test_verify_remove_support_button_functionality(self):
        print("\n" + str(test_cases('TC_VERIFY_REMOVE_SUPPORT_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_remove_support_button_functionality().get_url()
        self.assertIn("", result)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
