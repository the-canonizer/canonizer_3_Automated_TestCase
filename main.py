import unittest

from CanonizerLoginPage import CanonizerLoginPage

from CanonizerRegistrationPage import CanonizerRegisterPage

from CanonizerChangePasswordTab import CanonizerChangePasswordTab

from CanonizerTestCases import test_cases
from Config import *
from selenium import webdriver


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

    # TC_REGISTER_PAGE_MANDATORY_FIELDS_MARKED_WITH_ASTERISK
    def test_register_page_mandatory_fields_are_marked_with_asterisk(self):
        self.assertTrue(CanonizerRegisterPage(
            self.driver).click_register_button().register_page_mandatory_fields_are_marked_with_asterisk())

    # TC_REGISTER_WITH_BLANK_FIRST_NAME
    def test_registration_with_blank_first_name(self, ):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_FIRST_NAME')))
        url = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_first_name(
            REG_LIST_3).get_url()
        self.assertIn("", url)

    # TC_REGISTER_WITH_BLANK_LAST_NAME
    def test_registration_with_blank_last_name(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_LAST_NAME')))
        url = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_last_name(
            REG_LIST_4).get_url()
        self.assertIn("", url)

    # TC_REGISTRATION_WITH_BLANK_EMAIL
    def test_registration_with_blank_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_EMAIL')))
        url = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_email(
            REG_LIST_5).get_url()
        self.assertIn("", url)

    # TC_REGISTRATION_WITH_BLANK_PASSWORD
    def test_registration_with_blank_password(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_PASSWORD')))
        url = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_password(
            REG_LIST_6).get_url()
        self.assertIn("", url)

    # TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH
    def test_registration_with_invalid_password_length(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH')))
        url = CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_password_length(
            REG_LIST_7).get_url()
        self.assertIn("", url)

    # TC_REGISTRATION_WITH_DIFFERENT_CONFIRM_PASSWORD
    def test_registration_with_different_confirmation_password(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_DIFFERENT_CONFIRM_PASSWORD')))
        url = CanonizerRegisterPage(
            self.driver).click_register_button().registration_with_different_confirmation_password(
            REG_LIST_8).get_url()
        self.assertIn("canonizer3.canonizer.com", url)

    # TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME
    def test_registration_with_blank_spaces_first_name(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME')))
        url = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_spaces_first_name(
            REG_LIST_1).get_url()
        self.assertIn(" ", url)

    # TC_REGISTRATION_WITH_INVALID_FIRST_NAME
    def test_registration_with_invalid_first_name(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_FIRST_NAME')))
        url = CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_first_name(
            REG_LIST_10).get_url()
        self.assertIn("", url)

    # TC_REGISTRATION_WITH_INVALID_LAST_NAME
    def test_registration_with_invalid_last_name(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_LAST_NAME')))
        url = CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_last_name(
            REG_LIST_11).get_url()
        self.assertIn("", url)

    # TC_REGISTRATION_WITH_INVALID_EMAIL
    def test_registration_with_invalid_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_EMAIL')))
        url = CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_email(
            REG_LIST_14).get_url()
        self.assertIn('', url)

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

    # LOGIN PAGE:
    #
    def test_login_page_mandatory_fields_are_marked_with_asterisk(self):
        self.assertTrue(CanonizerLoginPage(
            self.driver).click_login_page_button().login_page_mandatory_fields_are_marked_with_asterisk())

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
        self.assertIn("", result)

    # TC_LOGIN_WITH_INVALID_EMAIL
    def test_login_with_invalid_email(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_INVALID_EMAIL')))
        url = CanonizerLoginPage(self.driver).verify_the_login_with_invalid_email_format(DEFAULT_INVALID_USER,
                                                                                         DEFAULT_PASS).get_url()
        self.assertIn("canonizer3.canonizer.com", url)

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
        print("\n" + str(test_cases('TC_VERIFY_FORGET_PASSWORD')))
        result = CanonizerLoginPage(self.driver).verify_the_forget_password_button().get_url()
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_ON_REGISTER_NOW_LINK
    def test_click_on_register_now_link(self):
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_NOW_LINK')))
        result = CanonizerLoginPage(self.driver).click_on_register_now_button_on_login_page().get_url()
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

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
