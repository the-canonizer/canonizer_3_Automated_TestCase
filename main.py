import unittest
from unittest import result

from selenium.webdriver.remote.webelement import WebElement

import CanonizerAcoountSettingPage
from CanonizerAcoountSettingPage import CanonizerAccountSettingPage
from CanonizerHomePage import *
from CanonizerLoginPage import CanonizerLoginPage
from CanonizerRegistrationPage import CanonizerRegisterPage

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
    def test_canonizer_click_register_page(self, TC_CLICK_ON_REGISTER_BUTTON):
        print("\n" + str(test_cases(TC_CLICK_ON_REGISTER_BUTTON)))
        result = CanonizerRegisterPage(self.driver).click_register_button().get_url()
        self.assertIn("", result)

    # TC_CLICK_ON_"REGISTER_NOW"_WITH_VALID_DATA
    def test_click_register_page_entering_fields_with_valid_data(self):
        print("\n" + str(test_cases(2)))
        result = CanonizerRegisterPage(self.driver).click_register_page_and_enter_fields_with_valid_data('kumar',
                                                                                                         'file',
                                                                                                         'saideekshith@zibtek.in',
                                                                                                         'Sai@1998',
                                                                                                         'Sai@1998').get_url()
        self.assertIn("", result)

    # TC_cLICK_ON_CLOSE_ICON_IN_REGISTER_PAGE
    def test_click_on_register_page_and_click_on_close_icon(self):
        print("\n" + str(test_cases(3)))
        result = CanonizerRegisterPage(self.driver).click_on_close_icon_register_page().get_url()
        self.assertIn("", result)

    # TC_CLICK_ON_REGISTER_NOW_WITH_BLANK_FIELDS
    def test_create_register_page_without_entering_data(self):
        print("\n" + str(test_cases(4)))
        result = CanonizerRegisterPage(self.driver).craete_canonizer_register_page_without_entering_data("", "", "", "",
                                                                                                         "").get_url()
        self.assertIn("//canonizer3.canonizer.com/", result)

    # TC_CREATE_REGISTER_PAGE_WITH_INVALID_DATA
    def test_create_register_page_entering_invalid_data(self):
        print("\n" + str(test_cases(5)))
        result = CanonizerRegisterPage(self.driver).create_canonizer_register_page_entering_with_invalid_data(
            'kumar_sai', 'file    1', 'saideekshith@zibtek.in', 'Sai@1998', 'Sai@1998').get_url()
        self.assertIn("", result)

    # Tc_CREATE_REGISTRATION_PAGE_WITH_ALREADY_EXISTED_DATA
    def test_create_registration_page_with_existed_data(self):
        print("\n" + str(test_cases(6)))
        result = CanonizerRegisterPage(self.driver).create_canonizer_page_with_existed_data('kumar', 'file',
                                                                                            'saideekshith@zibtek.in',
                                                                                            'Sai@1998',
                                                                                            'Sai@1998').get_url()
        self.assertIn("", result)

    # TC_CLICK_ON_REGISTER_NOW_WITHOUT_FILLED_ONE_MANDATORY_FIELD
    def test_create_registration_page_without_entering_in_one_mandatary_field(self):
        print("\n" + str(test_cases(7)))
        result = CanonizerRegisterPage(self.driver).create_registration_page_without_entering_in_one_mandatary_field(
            'kumar', 'saideekshith@zibtek.in', 'Sai@1998', 'Sai@1998').get_url()
        self.assertIn("", result)

    # TC_VERIFY_TITTLE_IDENTIFICATION
    def test_registration_title_identification(self):
        print("\n" + str(test_cases(8)))
        result = CanonizerRegisterPage(self.driver).registration_title_identification().get_url()
        print(result)

    # TC_VERIFY_FIRST_NAME_EMPTY
    def test_verify_firstname_empty(self):
        print("\n" + str(test_cases(9)))
        result = CanonizerRegisterPage(self.driver).verify_firstname_empty('').get_url()
        print(result)

    # TC_ VERIFY_ALL_FIELDS_EMPTY
    def test_verify_all_fields_empty(self):
        print("\n" + str(test_cases(10)))
        result = CanonizerRegisterPage(self.driver).verify_all_fields_empty().get_url()
        print(result)

    # TC_VERIFY_INVALID_PASSWORD_FORMAT
    def test_verify_invalid_password_format(self):
        print("\n" + str(test_cases(11)))
        result = CanonizerRegisterPage(self.driver).verify_invalid_password_format("A", "bn", "son12@zibtek.in",
                                                                                   "Sonali@zibtek.in", ).get_url()
        print(result)

    # TC_VERIFY_INVALID_CONFIRM_PASSWORD
    def test_verify_invalid_confirm_password(self):
        print("\n" + str(test_cases(12)))
        result = CanonizerRegisterPage(self.driver).verify_invalid_confirm_password("user", "users",
                                                                                    "saideekshith@zibtek.in",
                                                                                    "Sai@1998", "Sai@123455")
        print(result)

    # VERIFY_EMAIL_VALIDATION
    def test_verify_email_validation(self):
        print("\n" + str(test_cases(13)))
        result = CanonizerRegisterPage(self.driver).verify_invalid_email_format("first", "last", "validation",
                                                                                "Sai@1998", "Sai@1998")
        print(result)

    # TC_VERIFY_ERROR_CAPTCHA
    def test_verify_error_captcha(self):
        print("\n" + str(test_cases(14)))
        result = CanonizerRegisterPage(self.driver).verify_captcha_field("first", "last", "saideekshith@zibtek.in",
                                                                         "Sai@1998", "Sai@1998")
        print(result)

    #
    def test_click_on_account_setting_page(self):
        self.login_to_canonizer_app()
        print("\n" + str(test_cases(15)))
        result = CanonizerAccountSettingPage(self.driver).click_account_settings_page_button()
        print(result)

    # TC_CLICK_ON_LOGIN_BUTTON
    def test_click_on_login_button(self):
        print("\n" + str(test_cases(16)))
        result = CanonizerLoginPage(self.driver).click_on_login_button().get_url()
        print(result)

    # TC_VERIFY_LOGIN_PAGE
    def test_verify_login_page(self):
        print("\n" + str(test_cases(17)))
        result = CanonizerLoginPage(self.driver).verify_canonizer_login_page().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_CLOSE_ICON_ON_LOGIN_PAGE
    def test_click_close_icon_on_login_page(self):
        print("\n" + str(test_cases(18)))
        result = CanonizerLoginPage(self.driver).click_on_close_icon_button().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_LOGIN_WITH_REGISTERED_CREDENTIALS
    def test_login_with_registered_credentials(self):
        print("\n" + str(test_cases(19)))
        result = CanonizerLoginPage(self.driver).Verify_the_Login_Functionality_by_entering_the_registered_credential(
            "saideekshith@zibtek.in", "Sai@1998").get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_LOGIN_WITH_INVALID_EMAIL
    def test_login_with_invalid_email(self):
        print("\n" + str(test_cases(20)))
        result = CanonizerLoginPage(self.driver).verify_the_login_with_invalid_email_format("sai@zibtek.in",
                                                                                            "Sai@1998").get_url()
        print(result)
        self.assertIn("", result)

    # TC_VERIFYING_REMEMBER_CHECK_BOX
    def test_click_on_remember_check_box(self):
        print("\n" + str(test_cases(21)))
        result = CanonizerLoginPage(self.driver).verify_the_Remember_me_checkbox("saideekshith@zibtek.in",
                                                                                 "Sai@1998").get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_VERIFYING_EMPTY_SPACE_FOR_EMAIL_FILED
    def test_verify_login_button_with_empty_space(self):
        print("\n" + str(test_cases(22)))
        result = CanonizerLoginPage(self.driver).verify_the_login_button_by_entering_the_empty_space("",
                                                                                                     "Sai@1998").get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    #  TC_VERIFY_FORGET_PASSWORD
    def test_verify_forget_password_button(self):
        print("\n" + str(test_cases(23)))
        result = CanonizerLoginPage(self.driver).verify_the_forget_password_button().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_ON_REGISTER_NOW_LINK
    def test_click_on_register_now_link(self):
        print("\n" + str(test_cases(24)))
        result = CanonizerLoginPage(self.driver).click_on_register_now_button_on_login_page().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON
    def test_click_on_request_one_time_code(self):
        print("\n" + str(test_cases(25)))
        result = CanonizerLoginPage(self.driver).verify_one_time_request_code_without_entering_email().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON_WITH_INVALID-EMAIL
    def test_click_on_request_one_time_code_with_invalid_email(self):
        print("\n" + str(test_cases(26)))
        result = CanonizerLoginPage(self.driver).verify_one_time_request_code_with_invalid_email(
            "sai@122gmail", "Sai@1998").get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_VERIFYING_SOCIAL LINKS
    def test_verifying_social_account_links(self):
        print("\n" + str(test_cases(27)))
        result = CanonizerLoginPage(self.driver).verifying_social_account_links().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com", result)

    # TC_VERIFYING_ACCOUNT_PROFILE_PAGE
    def test_verifying_account_profile_page(self):
        self.login_to_canonizer_app()
        print("\n" + str(test_cases(28)))
        result = CanonizerAccountSettingPage(self.driver).verifying_profile_button().get_url()
        print(result)
        self.assertIn("", result)

    # TC-VERIFYING_SOCIAL_OAUTH_VERIFICATION
    def test_verifying_social_oauth_page(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verifying_social_oauth_verification().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFICATION_CHANGE_PASSWORD
    def test_verifying_change_password(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verifying_change_password().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_NICK_NAME
    def test_verifying_nick_name(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verifying_nick_name().get_url()
        print(result)
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_SUPPORTED_CHANGES
    def test_verifying_supported_camps(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verifying_supported_camps().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_VALIDATION_FOR_PROFILE_INFO_PHONE_NUMBER
    def test_verifying_invalid_phone_number(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Check_the_validation_for_Phone_Number_field(
            "988874467444444").get_url()
        self.assertIn("", result)

    # TC_VERIFYING_VERIFY_BUTTON_WITH_BLANK_FIELDS
    def test_verifying_verify_button_without_entering_data(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Check_the_Functionality_of_verify_button_without_entering_the_data().get_url()
        self.assertIn("", result)

    # TC_VERIFYING_CLICK_ON_MOBILE_CARRIER_DROP_DOWN
    def test_click_on_mobile_carrier_drop_down(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_the_functionality_of_mobile_carrier_drop_down().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_ALL_THE_FIELDS_ARE_PERSONAL_INFORMATION
    def test_verifying_all_the_feilds_are_personal_information(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_all_the_fields_are_present_in_Personal_Information_field().get_url()
        self.assertIn("", result)

    # TC_VERIFYING_FIRST_NAME_FIELD_WITHOUT_ENTERING_DATA
    def test_verifying_validation_for_first_name_fields(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_the_validation_for_first_name(" ").get_url()
        self.assertIn("", result)

    # TC_UPDATE_THE_FIRST_NAME_AND_CHECK_IF_IT_IS_UPDATING_SAME_FOR_USERNAME
    def test_Update_the_first_name_and_check_if_it_is_updating_same_for_username(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Update_the_first_name_and_check_if_it_is_updating_same_for_username("saideekshith").get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_RADIO_BUTTON_IN_SELECTING_THE_GENDER
    def test_Verify_the_functionality_of_radio_button_in_selecting_the_gender(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_the_functionality_of_radio_button_in_selecting_the_gender().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_SELECTING_THE_DOB
    def test_Verify_the_functionality_of_selecting_the_DOB(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).Verify_the_functionality_of_selecting_the_DOB(
            "1998-02-28").get_url()
        self.assertIn("", result)

    # TC_VERIFY_WHEN_USER_UPDATE_THE_PERSONAL_INFORMATION_AND_LOGS_OUT_AND_LOGIN_AGAIN
    def test_Verify_when_user_updated_the_Personal_Information_and_logs_out_and_logIn_again(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_when_user_updated_the_Personal_Information_and_logs_out_and_logIn_again("sai",
                                                                                                        "deekshith",
                                                                                                        "masuldari").get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_SPACES_ARE_TRIMMED_IN_THE_FIRSTNAME_LASTNAME_MIDDLENAME_fields
    def test_Verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields(self):
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).Verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields("sssss  sssss",
                                                                                                   "dddd dd     dd",
                                                                                                   "dsd sd   dsd").get_url()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
