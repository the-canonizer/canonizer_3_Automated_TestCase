import unittest
from subprocess import run
import HtmlTestRunner
import requests
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from CanonizerAddEditNewsPage import CanonizerEditNewsPage
from CanonizerAddEditNewsPage import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import mailer
from CanonizerAddEditNewsPage import CanonizerAddNewsPage
from CanonizerEditNewsPage import CanonizerEditNewsPage
from CanonizerBrowsePage import CanonizerBrowsePage
from CanonizerCampStatementPage import CanonizerCampStatementPage
#from CanonizerCampStatementPage import CanonizerEditCampStatementPage
from CanonizerCampStatementPage import *
from CanonizerChangePasswordTab import CanonizerChangePasswordTab
from CanonizerCreateUpdateCampPage import CanonizerCreateCampPage, CanonizerEditCampPage
from CanonizerFooter import CanonizerFooter
from CanonizerLogoutPage import CanonizerLogoutPage
from CanonizerHomePage import CanonizerTermsAndPrivacyPolicy, CanonizerHomePage
from CanonizerManageNickNameTab import CanonizerManageNickNameTab
from CanonizerProfileInfoTab import CanonizerAccountSettingPage
from CanonizerRegistrationPage import CanonizerRegisterPage
from CanonizerCampForum import CanonizerCampForumPage
from selenium.common.exceptions import TimeoutException
from CanonizerCreateUpdateTopicPage import CanonizerCreateNewTopic, CanonizerUpdateTopicPage
from CanonizerCreateUpdateArchivedCamp import CanonizerCreateUpdateArchivedCamp, CanonizerEditArchivedCampPage
from CanonizerLoginPage import CanonizerLoginPage
from CanonizerForgotPasswordPage import *
from CanonizerSupportValue import CanonizerSupportValue
from CanonizerSupportedCampsTab import CanonizerSupportCampsTab
from CanonizerTestCases import test_cases
from CanonizerUploadFilePage import CanonizerUploadFilePage
from Config import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import string
import random
import time
from Identifiers import *



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

        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(DEFAULT_BASE_URL)

    def driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def login_to_canonizer_app(self):
        """
            This Application will allow you to login to canonizer App on need basis
        :param flag:
        :return:
        """
        #result = CanonizerLoginPage(self.driver).click_login_page_button().login_with_valid_user(DEFAULT_USER, DEFAULT_PASS).get_url()
        self.driver.implicitly_wait(10)
        CanonizerLoginPage(self.driver).click_login_page_button()
        result = CanonizerLoginPage(self.driver).login_with_valid_user(DEFAULT_USER, DEFAULT_PASS)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/h3')))
        except TimeoutException:
            pass
        #self.driver.maximize_window()

    # TC_CLICK_ON_REGISTER_BUTTON
    def test_click_on_register_button(self):
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_BUTTON')))
        result = CanonizerRegisterPage(self.driver).click_on_register_button().get_url()
        self.assertIn("", result)

    # TC_REGISTER_PAGE_MANDATORY_FIELDS_MARKED_WITH_ASTERISK
    def test_register_page_mandatory_fields_are_marked_with_asterisk(self):
        self.assertTrue(CanonizerRegisterPage(
            self.driver).click_register_button().register_page_mandatory_fields_are_marked_with_asterisk())

    # TC_REGISTER_WITH_BLANK_FIRST_NAME
    def test_registration_with_blank_first_name(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_FIRST_NAME')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_first_name(
            reg_list_3).get_url()
        self.assertIn("", result)

    # TC_REGISTRATION_WITH_BLANK_EMAIL
    def test_registration_with_blank_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_EMAIL')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_email(
            reg_list_5).get_url()
        self.assertIn("", result)

    # TC_REGISTER_WITH_BLANK_LAST_NAME
    def test_registration_with_blank_last_name(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_LAST_NAME')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_last_name(
            reg_list_4).get_url()
        self.assertIn("", result)

    # TC_REGISTRATION_WITH_BLANK_PASSWORD
    def test_registration_with_blank_password(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_BLANK_PASSWORD')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_blank_password(
            reg_list_6).get_url()
        self.assertIn("", result)

    # TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH
    def test_registration_with_invalid_password_length(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_password_length(
            reg_list_7).get_url()
        self.assertIn("", result)

    # TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME
    def test_registration_with_spaces_first_name(self):
        print("\n" + str(test_cases('TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_spaces_first_name(
            reg_list_1).get_url()
        self.assertIn("", result)

    # TC_REGISTRATION_WITH_INVALID_EMAIL
    def test_registration_with_invalid_email(self):
        print("\n" + str(test_cases('TC_REGISTRATION_WITH_INVALID_EMAIL')))
        result = CanonizerRegisterPage(self.driver).click_register_button().registration_with_invalid_email(
            reg_list_14).get_url()
        self.assertIn("", result)

    # TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK
    def test_check_login_page_open_click_login_here_link(self):
        print("\n" + str(test_cases('TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK')))
        result = CanonizerRegisterPage(self.driver).check_login_page_open_click_login_here_link().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS
    def test_verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MANDATORY_FIELDS')))
        result = CanonizerRegisterPage(
            self.driver).click_register_button(
        ).verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(
            reg_list_15).get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS
    def test_verify_the_functionality_0f_registration_with_entering_data_in_mobile_number_field(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTRATION_WITH_MOBILE_NUMBER_FIELDS')))
        result = CanonizerRegisterPage(
            self.driver).click_register_button(
        ).verify_the_functionality_0f_registration_with_entering_data_in_mobile_number_field(
            reg_list_16).get_url()
        self.assertIn("", result)

    # LOGIN PAGE:
    def test_login_page_mandatory_fields_are_marked_with_asterisk(self):
        self.assertTrue(CanonizerLoginPage(
            self.driver).click_login_page_button().login_page_mandatory_fields_are_marked_with_asterisk())

    # TC_CLICK_ON_LOGIN_BUTTON
    def test_click_on_login_button(self):
        print("\n" + str(test_cases('TC_CLICK_ON_LOGIN_BUTTON')))
        CanonizerLoginPage(self.driver).click_on_login_button()

    # TC_CLICK_CLOSE_ICON_ON_LOGIN_PAGE
    def test_click_close_icon_on_login_page(self):
        print("\n" + str(test_cases('TC_CLICK_CLOSE_ICON_ON_LOGIN_PAGE')))
        result = CanonizerLoginPage(self.driver).click_on_close_icon_button().get_url()
        self.assertIn("", result)

    # TC_LOGIN_WITH_REGISTERED_CREDENTIALS
    def test_login_with_registered_credentials(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        self.driver.implicitly_wait(30)
        CanonizerLoginPage(self.driver).verify_the_login_functionality_by_entering_the_registered_credential(DEFAULT_USER, DEFAULT_PASS)
        result = self.driver.current_url
        self.assertIn("", result)

    # TC_VERIFY_THE_LOGIN_WITH_BLANK_EMAIL
    def test_verify_the_login_with_blank_email(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_REGISTERED_CREDENTIALS')))
        result = CanonizerLoginPage(self.driver).verify_the_login_with_blank_email("", DEFAULT_PASS).get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_LOGIN_WITH_BLANK_PASSWORD
    def test_verify_the_login_with_blank_password(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_LOGIN_WITH_BLANK_PASSWORD')))
        result = CanonizerLoginPage(self.driver).verify_the_login_with_blank_password(DEFAULT_USER, "").get_url()
        self.assertIn("", result)

    # TC_LOGIN_WITH_INVALID_EMAIL
    def test_login_with_invalid_email(self):
        print("\n" + str(test_cases('TC_LOGIN_WITH_INVALID_EMAIL')))
        result = CanonizerLoginPage(self.driver).verify_the_login_with_invalid_email_format(DEFAULT_INVALID_USER,
                                                                                            DEFAULT_PASS).get_url()
        self.assertIn("", result)

    # TC_VERIFY_ONE_TIME_REQUEST_CODE_WITH_VALID_CREDENTIALS
    def test_verify_one_time_request_code_with_valid_credentials(self):
        print("\n" + str(test_cases('TC_VERIFY_ONE_TIME_REQUEST_CODE_WITH_VALID_CREDENTIALS')))
        result = CanonizerLoginPage(
            self.driver).verify_one_time_request_code_with_valid_credentials(DEFAULT_USER, DEFAULT_PASS).get_url()
        self.assertIn("", result)

    # TC_VERIFYING_REMEMBER_CHECK_BOX
    def test_click_on_remember_check_box(self):
        print("\n" + str(test_cases('TC_VERIFYING_REMEMBER_CHECK_BOX')))
        result = CanonizerLoginPage(self.driver).verify_the_remember_me_checkbox(DEFAULT_USER,
                                                                                 DEFAULT_PASS).get_url()
        self.assertIn("", result)

    # TC_CLICK_ON_REGISTER_NOW_LINK
    def test_click_on_register_now_link(self):
        print("\n" + str(test_cases('TC_CLICK_ON_REGISTER_NOW_LINK')))
        result = CanonizerLoginPage(self.driver).click_on_register_now_button_on_login_page()
        self.assertIn("", result.get_url())

    # TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON_WITH_INVALID-EMAIL
    def test_click_on_request_one_time_code_with_invalid_email(self):
        print("\n" + str(test_cases('TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON_WITH_INVALID-EMAIL')))
        result = CanonizerLoginPage(self.driver).verify_one_time_request_code_with_invalid_email(
            DEFAULT_INVALID_USER, DEFAULT_PASS).get_url()
        self.assertIn("", result)

    # TC_VERIFYING_GOOGLE_LINK
    def test_verifying_google_account_link(self):
        print("\n" + str(test_cases('TC_VERIFYING_GOOGLE_LINK')))
        result = CanonizerLoginPage(self.driver).verifying_google_link().get_url()
        self.assertIn("/o/oauth2/auth/", result)

    # TC_VERIFYING_FACEBOOK_LINK
    def test_verifying_facebook_link(self):
        print("\n" + str(test_cases('Tc_verifying_facebook_link')))
        result = CanonizerLoginPage(self.driver).verifying_facebook_link().get_url()
        self.assertIn("/login.php?", result)

    # TC_VERIFYING_TWITTER_LINK
    def test_verifying_twitter_link(self):
        print("\n" + str(test_cases('TC_VERIFYING_TWITTER_LINK')))
        result = CanonizerLoginPage(self.driver).verifying_twitter_link().get_url()
        self.assertIn("/api.twitter.com/oauth/authorize?", result)

    # TC_VERIFYING_LINKEDIN_LINK
    def test_verifying_linkedin_link(self):
        self.driver.implicitly_wait(20)
        print("\n" + str(test_cases('TC_VERIFYING_LINKEDIN_LINK')))
        CanonizerLoginPage(self.driver).verifying_linkedin_link()
        result  = self.driver.find_element(*LoginPageIdentifiers.LINKEDIN_SIGNIN).text
        self.assertIn("Sign in", result)
    def test_verifying_github_link(self):
        self.driver.implicitly_wait(20)
        print("\n" + str(test_cases('TC_VERIFYING_LINKEDIN_LINK')))
        CanonizerLoginPage(self.driver).verifying_github_link()
        result = self.driver.find_element(*LoginPageIdentifiers.GITHUB_SIGNIN).text
        self.assertIn("", result)    

        # ----- FORGOT PASSWORD Test Cases Start -----
        # TC_CLICK_FORGOT_PASSWORD_LINK
    def test_click_forgot_password_link(self):
        print("\n" + str(test_cases('TC_CLICK_FORGOT_PASSWORD_LINK')))
        CanonizerForgotPasswordPage(self.driver).click_forgot_password_link()
        result = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/section/form/h2").text
        self.assertIn("Forgot Your Password?", result)

    # TC_SUBMIT_BUTTON_WITH_VALID_EMAIL_AND_CHECK_OTP_SCREEN
    def test_click_submit_button_with_valid_email(self):
        print("\n" + str(test_cases('TC_SUBMIT_BUTTON_WITH_VALID_EMAIL_AND_CHECK_OTP_SCREEN')))
        result = CanonizerForgotPasswordPage(self.driver).login_and_forgot_password() \
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
        result = CanonizerForgotPasswordPage(self.driver).login_and_forgot_password() \
            .submit_empty_otp(DEFAULT_USER).get_url()
        self.assertIn("", result)

    # TC_SUBMIT_INVALID_LENGTH_OTP
    def test_invalid_otp(self):
        print("\n" + str(test_cases('TC_SUBMIT_INVALID_LENGTH_OTP')))
        result = CanonizerForgotPasswordPage(self.driver).login_and_forgot_password() \
            .submit_invalid_otp(DEFAULT_USER, INVALID_LONG_OTP).get_url()
        self.assertIn("", result)

    # TC_CROSS_ICON_ON_FORGOT_MODAL
    def test_cross_icon_on_forgot_page(self):
        print("\n" + str(test_cases('TC_CROSS_ICON_ON_FORGOT_MODAL')))
        CanonizerForgotPasswordPage(self.driver).click_forgot_password_link()
        CanonizerForgotPasswordPage(self.driver).cross_icon_on_forgot_page()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[3]/div[1]/button[1]/span").text
        self.assertIn("Log In", result)

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
        self.login_to_canonizer_app()
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button().create_topic_with_blank_topic_name(
            DEFAULT_NICK_NAME,
            DEFAULT_NAMESPACE,
            DEFAULT_SUMMARY).get_url()
        self.assertIn("create/topic", result)

    # TC_CREATE_NEW_TOPIC_WITH_VALID_DATA
    def test_create_topic_name_with_valid_data(self):
        print("\n" + str(test_cases('TC_CREATE_TOPIC_WITH_VALID_DATA')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        print(add_name)

        CanonizerCreateNewTopic(self.driver).click_create_topic_button()
        result = CanonizerCreateNewTopic(self.driver).create_topic_with_valid_data("new summary", "New Topic " + add_name, DEFAULT_NAMESPACE).get_url()

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
        add_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button() \
            .create_topic_name_with_trailing_space(
            DEFAULT_NICK_NAME,
            "      New Topic " + add_name,
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
        result = CanonizerCreateNewTopic(
            self.driver).click_create_new_topic_page_button().create_topic_with_duplicate_topic_name(
            DEFAULT_NICK_NAME,
            DUPLICATE_TOPIC_NAME,
            DEFAULT_NAMESPACE,
            DEFAULT_SUMMARY).get_url()
        self.assertIn("create/topic", result)

    # TC_CREATE_NEW_TOPIC_WITH_SPECIAL_CHARS
    def test_create_topic_with_special_chars(self):
        print("\n", str(test_cases('TC_CREATE_NEW_TOPIC_WITH_SPECIAL_CHARS')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button() \
            .create_topic_with_special_chars(
            DEFAULT_NICK_NAME,
            "Topic&^&#$(# " + add_name,
            DEFAULT_NAMESPACE,
            DEFAULT_SUMMARY).get_url()
        self.assertIn("topic", result)

    # TC_CREATE_NEW_WITHOUT_MANDATORY_FIELDS_DATA
    def test_create_topic_without_entering_mandatory_fields(self):
        print("\n", str(test_cases('TC_CREATE_NEW_WITHOUT_MANDATORY_FIELDS_DATA')))
        self.login_to_canonizer_app()
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button() \
            .create_topic_without_entering_mandatory_fields(
            "",
            "",
            "",
            "", ).get_url()
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

    # ----- CREATE TOPIC Test Cases end -----

    # ----- UPDATE TOPIC Test Cases Start -----

    # TC_LOAD_TOPIC_HISTORY_PAGE
    def test_load_topic_history_page(self):
        print("\n" + str(test_cases('TC_LOAD_TOPIC_HISTORY_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC)
        self.assertIn("/topic/history/", result.get_url())

    # TC_VERIFY_TOPIC_NAME_ON_TOPIC_HISTORY_PAGE
    def test_verify_topic_name_on_topic_history_page(self):
        print("\n" + str(test_cases('TC_VERIFY_TOPIC_NAME_ON_TOPIC_HISTORY_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).verify_topic_name_on_topic_history_page(DEFAULT_TOPIC)
        self.assertIn("/topic/history/", result.get_url())

    # TC_VERIFY_SUBMITTER_NICK_NAME_LINK_ON_USER_PROFILE
    def test_verify_submitter_nick_name_link_on_user_profile(self):
        print("\n" + str(test_cases('TC_VERIFY_SUBMITTER_NICK_NAME_LINK_ON_USER_PROFILE')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC)\
            .verify_submitter_nick_name_link_on_user_profile()
        self.assertIn("/user/supports/", result.get_url())

    # TC_VERIFY_SUBMIT_TOPIC_UPDATE_BUTTON
    def test_verify_submit_topic_update_button(self):
        print("\n" + str(test_cases('TC_VERIFY_SUBMIT_TOPIC_UPDATE_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC)\
            .verify_submit_topic_update_button()
        self.assertIn("manage/topic/", result.get_url())

    # TC_UPDATE_TOPIC_WITH_DUPLICATE_NAME
    def test_update_topic_with_duplicate_name(self):
        print("\n" + str(test_cases('TC_UPDATE_TOPIC_WITH_DUPLICATE_NAME')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .update_topic_with_duplicate_name(DUPLICATE_TOPIC_NAME)
        self.assertIn("manage/topic/", result.get_url())

    # TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE
    def test_verify_cancel_button_functionality_on_topic_update_page(self):
        print("\n" + str(test_cases('TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .verify_cancel_button_functionality_on_topic_update_page()
        self.assertIn("/topic/history/", result.get_url())

    # TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE
    def test_verify_preview_button_functionality_on_topic_update_page(self):
        print("\n" + str(test_cases('TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_TOPIC_UPDATE_PAGE')))
        self.login_to_canonizer_app()
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .verify_preview_button_functionality_on_topic_update_page()

    # TC_VERIFY_SUBMITTER_NICK_NAME_ON_PREVIEW_MODAL
    def test_verify_submitter_nick_name_on_preview_modal(self):
        print("\n" + str(test_cases('TC_VERIFY_SUBMITTER_NICK_NAME_ON_PREVIEW_MODAL')))
        self.login_to_canonizer_app()
        CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .verify_submitter_nick_name_on_preview_modal()

    # TC_VERIFY_CANCEL_BUTTON_ON_PREVIEW_MODAL
    def test_verify_cancel_button_on_preview_modal(self):
        print("\n" + str(test_cases('TC_VERIFY_CANCEL_BUTTON_ON_PREVIEW_MODAL')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .verify_cancel_button_on_preview_modal()
        self.assertIn("/manage/topic/", result.get_url())

    # TC_UPDATE_TOPIC_NAME_AND_VERIFY_SUBMIT_UPDATE_BUTTON
    def test_update_topic_name_and_verify_submit_update_button(self):
        print("\n" + str(test_cases('TC_UPDATE_TOPIC_NAME_AND_VERIFY_SUBMIT_UPDATE_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .update_topic_name_and_verify_submit_update_button(DEFAULT_UPDATE_TOPIC_NAME)
        self.assertIn("topic/history/", result.get_url())

    # TC_VERIFY_COMPARE_TOPICS_BUTTON_FUNCTIONALITY
    def test_verify_compare_topics_button_functionality(self):
        #print("\n" + str(test_cases('TC_VERIFY_COMPARE_TOPICS_BUTTON_FUNCTIONALITY')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .verify_compare_topics_button_functionality()
        self.assertIn("/statement/compare/", result.get_url())

    # TC_VERIFY_AGREEMENT_LINK_ON_TOPIC_COMPARISON_PAGE
    def test_verify_agreement_link_on_topic_comparison_page(self):
        print("\n" + str(test_cases('TC_VERIFY_AGREEMENT_LINK_ON_TOPIC_COMPARISON_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .verify_agreement_link_on_topic_comparison_page()
        self.assertIn("/topic/", result.get_url())

    # TC_VERIFY_CREATE_TOPIC_BUTTON_FUNCTIONALITY_ON_TOPIC_COMPARISON_PAGE
    def test_verify_create_topic_button_functionality_on_topic_comparison_page(self):
        print("\n" + str(test_cases('TC_VERIFY_CREATE_TOPIC_BUTTON_FUNCTIONALITY_ON_TOPIC_COMPARISON_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC)\
            .verify_create_topic_button_functionality_on_topic_comparison_page()
        self.assertIn("/create/topic", result.get_url())

    # TC_VERIFY_CREATE_CAMP_BUTTON_FUNCTIONALITY_ON_TOPIC_COMPARISON_PAGE
    def test_verify_create_camp_button_functionality_on_topic_comparison_page(self):
        print("\n" + str(test_cases('TC_VERIFY_CREATE_CAMP_BUTTON_FUNCTIONALITY_ON_TOPIC_COMPARISON_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .verify_create_camp_button_functionality_on_topic_comparison_page()
        self.assertIn("/camp/create/", result.get_url())

    # TC_VERIFY_BACK_ARROW_ICON_ON_TOPIC_COMPARISON_PAGE
    def test_verify_back_arrow_icon_on_topic_comparison_page(self):
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .verify_back_arrow_icon_on_topic_comparison_page()
        self.assertIn("/topic/history/", result.get_url())

    # TC_VERIFY_VIEW_THIS_VERSION_BUTTON_FUNCTIONALITY
    def test_verify_view_this_version_button_functionality(self):
        self.login_to_canonizer_app()
        result = CanonizerUpdateTopicPage(self.driver).load_topic_history_page(DEFAULT_TOPIC) \
            .verify_view_this_version_button_functionality()
        self.assertIn("/topic/", result.get_url())

    # ----- UPDATE TOPIC Test Cases End -----

    # ----- CAMP FORUM Test Cases Start -----
    # TC_CLICK_CAMP_FORUM_BUTTON
    def test_load_camp_forum_page(self):
        print("\n" + str(test_cases('TC_CLICK_CAMP_FORUM_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).get_url()
        self.assertIn("/forum", result)

        # TC_LOAD_ALL_THREADS_PAGE
    def test_load_all_threads_page(self):
        print("\n" + str(test_cases('TC_LOAD_ALL_THREADS_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).load_all_threads_page().get_url()
        self.assertIn("/threads?by=all", result)

        # TC_LOAD_MY_THREADS_PAGE
    def test_load_my_threads_page(self):
        print("\n" + str(test_cases('TC_LOAD_MY_THREADS_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).load_my_threads_page().get_url()
        self.assertIn("/threads?by=my", result)

        # TC_LOAD_MY_PARTICIPATION_PAGE
    def test_load_my_participation_page(self):
        print("\n" + str(test_cases('TC_LOAD_MY_PARTICIPATION_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC)\
            .load_my_participation_page().get_url()
        self.assertIn("/threads?by=participate", result)

        # TC_LOAD_TOP_10_THREADS_PAGE
    def test_load_top_10_threads_page(self):
        print("\n" + str(test_cases('TC_LOAD_TOP_10_THREADS_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC)\
            .load_top_10_threads_page().get_url()
        self.assertIn("/threads?by=most_replies", result)

        # TC_CHECK_NO_THREAD_AVAILABILITY
    def test_check_no_thread_availability(self):
        print("\n" + str(test_cases('TC_CHECK_NO_THREAD_AVAILABILITY')))
        self.login_to_canonizer_app()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC).create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "camp-forum-btn")))
        CanonizerCampForumPage(self.driver).check_no_thread_availability()
        result = self.driver.find_element(By.CLASS_NAME, "ant-empty-description").text
        self.assertIn("No data", result)

    # TC_CLICK_CREATE_THREAD_BUTTON
    def test_click_create_thread_button(self):
        print("\n" + str(test_cases('TC_CLICK_CREATE_THREAD_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC)\
            .click_create_thread_button().get_url()
        self.assertIn("/threads/create", result)

    # TC_CREATE_THREAD_WITH_VALID_DATA
    def test_create_thread_with_valid_data(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_VALID_DATA')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).click_create_thread_button()\
            .create_thread_with_valid_data("New Thread " + add_name).get_url()
        self.assertIn("/1-Agreement/threads", result)

    # TC_CREATE_THREAD_WITH_BLANK_TITLE
    def test_create_thread_with_blank_title(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_BLANK_TITLE')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).click_create_thread_button()\
            .create_thread_with_blank_title_name("  ").get_url()
        self.assertIn("/1-Agreement/threads", result)

    # TC_CREATE_THREAD_WITH_SPECIAL_CHARS
    def test_create_thread_with_special_chars(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_SPECIAL_CHARS')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).click_create_thread_button()\
            .create_thread_with_special_chars("Thread&^%$@#@ " + add_name).get_url()
        self.assertIn("/1-Agreement/threads", result)

    # TC_CREATE_THREAD_WITH_BLANK_MANDATORY_FIELDS
    def test_create_thread_with_blank_mandatory_fields(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_BLANK_MANDATORY_FIELDS')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).click_create_thread_button()\
            .create_thread_with_blank_mandatory_fields("").get_url()
        self.assertIn("/1-Agreement/threads", result)

    # TC_CREATE_THREAD_WITH_DUPLICATE_TITLE
    def test_create_thread_with_duplicate_title(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_DUPLICATE_TITLE')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).click_create_thread_button() \
            .create_thread_with_duplicate_title(DUPLICATE_THREAD_TITLE).get_url()
        self.assertIn("/1-Agreement/threads", result)

    # TC_CREATE_THREAD_WITH_VALID_DATA_WITH_ENTER_KEY
    def test_create_thread_with_valid_data_with_enter_key(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_VALID_DATA_WITH_ENTER_KEY')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).click_create_thread_button() \
            .create_thread_with_valid_data_with_enter_key("New Thread " + add_name).get_url()
        self.assertIn("/1-Agreement/threads", result)

    # TC_CREATE_THREAD_WITH_TRAILING_SPACES
    def test_create_thread_with_trailing_spaces(self):
        print("\n" + str(test_cases('TC_CREATE_THREAD_WITH_TRAILING_SPACES')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).click_create_thread_button() \
            .create_thread_with_trailing_spaces("      New Thread " + add_name)
        self.assertIn("/1-Agreement/threads", result.get_url())

    # TC_THREAD_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK
    def test_thread_page_mandatory_fields_are_marked_with_asterisk(self):
        print("\n" + str(test_cases('TC_THREAD_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK')))
        self.login_to_canonizer_app()
        self.assertTrue(CanonizerCampForumPage(
            self.driver).load_camp_forum_page(DEFAULT_TOPIC).click_create_thread_button()
                        .thread_page_mandatory_fields_are_marked_with_asterisk())

    # TC_CLICK_ON_BACK_BUTTON
    def test_click_on_back_button(self):
        print("\n", str(test_cases('TC_CLICK_ON_BACK_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).click_create_thread_button()\
            .click_on_back_button()
        self.assertIn("/1-Agreement/threads", result.get_url())

    # TC_LOAD_EDIT_THREAD_PAGE
    def test_load_edit_thread_page(self):
        print("\n", str(test_cases('TC_LOAD_EDIT_THREAD_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).load_edit_thread_page()
        self.assertIn("/1-Agreement/threads/edit", result.get_url())

    # TC_UPDATE_THREAD
    def test_update_thread_title(self):
        print("\n", str(test_cases('TC_UPDATE_THREAD')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC)\
            .update_thread_title("Edit Thread " + add_name)
        self.assertIn("/1-Agreement/threads", result.get_url())

    # TC_EDIT_THREAD_WITH_DUPLICATE_TITLE
    def test_edit_thread_with_duplicate_title(self):
        print("\n", str(test_cases('TC_UPDATE_THREAD')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC)\
            .edit_thread_with_duplicate_title(DUPLICATE_THREAD_TITLE)
        self.assertIn("/1-Agreement/threads/edit", result.get_url())

    # TC_EDIT_THREAD_WITH_SPECIAL_CHARS
    def test_edit_thread_with_special_chars(self):
        print("\n" + str(test_cases('TC_EDIT_THREAD_WITH_SPECIAL_CHARS')))
        self.login_to_canonizer_app()
        add_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC) \
            .edit_thread_with_special_chars("Edit Thread&^%$@ " + add_name).get_url()
        self.assertIn("/1-Agreement/threads", result)

    # TC_CLICK_ON_EDIT_BACK_BUTTON
    def test_click_on_edit_back_button(self):
        print("\n", str(test_cases('TC_CLICK_ON_EDIT_BACK_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(
                DEFAULT_TOPIC).click_on_edit_back_button()
        self.assertIn("/1-Agreement/threads", result.get_url())

    # TC_LOAD_THREAD_POSTS_PAGE
    def test_load_thread_posts_page(self):
        print("\n" + str(test_cases('TC_LOAD_THREAD_POSTS_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(
            DEFAULT_TOPIC).load_thread_posts_page()
        self.assertIn("/1-Agreement/threads", result.get_url())

    # TC_THREAD_POST_WITH_VALID_DATA
    def test_thread_post_with_valid_data(self):
        print("\n" + str(test_cases('TC_THREAD_POST_WITH_VALID_DATA')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).load_thread_posts_page()\
            .thread_post_with_valid_data("Test reply to a thread")
        self.assertIn("/1-Agreement/threads", result.get_url())

    # TC_THREAD_POST_WITH_EMPTY_REPLY
    def test_thread_post_with_empty_reply(self):
        print("\n" + str(test_cases('TC_THREAD_POST_WITH_EMPTY_REPLY')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).load_thread_posts_page()\
            .thread_post_with_empty_reply("")
        self.assertIn("/1-Agreement/threads", result.get_url())

    # TC_CLICK_ON_POST_BACK_BUTTON
    def test_click_on_post_back_button(self):
        print("\n" + str(test_cases('TC_CLICK_ON_POST_BACK_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).load_thread_posts_page() \
            .click_on_post_back_button()
        self.assertIn("/1-Agreement/threads", result.get_url())

    # TC_VERIFY_NICK_NAME_LINK_ON_POST_PAGE
    def test_verify_nick_name_link_on_post_page(self):
        print("\n" + str(test_cases('TC_VERIFY_NICK_NAME_LINK_ON_POST_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).load_thread_posts_page() \
            .verify_nick_name_on_post_page()
        self.assertIn("/user/supports/", result.get_url())

    # TC_VERIFY_EDIT_REPLY_TO_THREAD
    def test_edit_reply_to_thread(self):
        print("\n" + str(test_cases('TC_VERIFY_EDIT_REPLY_TO_THREAD')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).load_thread_posts_page() \
            .edit_reply_to_thread("Edit thread reply")
        self.assertIn("/1-Agreement/threads", result.get_url())

    # TC_VERIFY_DELETE_REPLY_TO_THREAD
    def test_delete_reply_to_thread(self):
        print("\n" + str(test_cases('TC_VERIFY_DELETE_REPLY_TO_THREAD')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC).load_thread_posts_page() \
            .delete_reply_to_thread()
        self.assertIn("/1-Agreement/threads", result.get_url())

    # TC_VERIFY_POST_EDIT_ICON FUNCTIONALITY
    def test_verify_edit_post_icon(self):
        print("\n" + str(test_cases('TC_VERIFY_POST_EDIT_ICON')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC)\
            .verify_edit_post_icon()
        self.assertIn("/forum/", result.get_url())

    # TC_VERIFY_POST_EDIT_FUNCTIONALITY
    def test_verify_post_edit_functionality(self):
        print("\n" + str(test_cases('TC_VERIFY_POST_EDIT_FUNCTIONALITY')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC) \
            .verify_post_edit_functionality("post updated4")
        self.assertIn("/forum/", result.get_url())

    # TC_VERIFY_POST_DELETE_FUNCTIONALITY
    def test_verify_post_delete_functionality(self):
        print("\n" + str(test_cases('TC_VERIFY_POST_DELETE_FUNCTIONALITY')))
        self.login_to_canonizer_app()
        result = CanonizerCampForumPage(self.driver).load_camp_forum_page(DEFAULT_TOPIC) \
            .test_verify_post_delete_functionality()
        self.assertIn("/forum/", result.get_url())

    # ----- CAMP FORUM Test Cases End -----

    # CHANGE PASSWORD TAB:-
    def test_verifying_astrk_present_in_change_password_tab(self):
        self.login_to_canonizer_app()
        self.assertTrue(CanonizerChangePasswordTab(self.driver).verify_click_on_change_password_tab_its_navigating_to_change_password_page()
                        .verifying_astrk_present_in_change_password_tab())

    # TC VERIFY_WHEN_USER_CLICK_ON_CHANGE_PASSWORD
    def test_verify_when_user_click_on_change_password(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_USER_CLICK_ON_CHANGE_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(
            self.driver).verify_click_on_change_password_tab_its_navigating_to_change_password_page().get_url()
        self.assertIn("/settings?tab=change_password", result)

    # TC VERIFY_THE_CURRENT_PASSWORD_FIELDS_EMPTY_AND_CLICK_ON_SAVE
    def test_verify_the_current_field_empty_and_click_on_save(self):
        print("\n" + str(test_cases('TC VERIFY_THE_CURRENT_PASSWORD_FIELDS_EMPTY_AND_CLICK_ON_SAVE')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(
            self.driver).verify_the_current_field_empty_and_click_on_save().get_url()
        self.assertIn("/settings?tab=change_password", result)

    # TC_VERIFY_THE_NEW_PASSWORD_FIELD_EMPTY_AND_CLICK_ON_SAVE
    def test_verify_the_new_password_field_empty_and_click_on_save(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_NEW_PASSWORD_FIELD_EMPTY_AND_CLICK_ON_SAVE')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(
            self.driver).verify_the_new_password_field_empty_and_click_on_save().get_url()
        self.assertIn("/settings?tab=change_password", result)

    # TC_VERIFY_THE_CONFIRM_PASSWORD_FIELD_EMPTY_AND_CLICK-ON_SAVE
    def test_verify_the_confirm_password_field_empty_and_click_on_save(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_CONFIRM_PASSWORD_FIELD_EMPTY_AND_CLICK')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(
            self.driver).verify_the_confirm_password_field_empty_and_click_on_save().get_url()
        self.assertIn("/settings?tab=change_password", result)

    # TC VERIFY_ENTERING_THE_INVALID_NEW_PASSWORD
    def test_verify_entering_the_invalid_new_password(self):
        print("\n" + str(test_cases('TC_VERIFY_ENTERING_THE_INVALID_NEW_PASSWORD')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(self.driver).verify_entering_the_invalid_new_password(
            INVALID_NEW_PASSWORD).get_url()
        self.assertIn("/settings?tab=change_password", result)

    # TC VERIFY_WHEN_BOTH_NEW_PASSWORD_AND_CONFIRM_PASSWORD_DOES_NOT_MATCH
    def test_verify_when_both_new_password_and_confirm_password_does_not_match(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_BOTH_NEW_PASSWORD_AND_CONFIRM_PASSWORD_DOES_NOT_MATCH')))
        self.login_to_canonizer_app()
        result = CanonizerChangePasswordTab(
            self.driver).verify_when_both_new_password_and_confirm_password_does_not_match(DEFAULT_NEW_PASSWORD,
                                                                                           DEFAULT_CONFIRM_PASSWORD).get_url()
        self.assertIn("/settings?tab=change_password", result)

    # CANONIZER_SUPPORTED_CAMPS_TAB:-

    # TC_VERIFY_USER_NAVIGATE_SUPPORT_CAMP_PAGE
    def test_verify_user_is_navigating_to_supported_camp_page_when_clicks_on_supported_camps_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_USER_NAVIGATE_SUPPORT_CAMP_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(
            self.driver).verify_user_is_navigating_to_supported_camp_page_when_clicks_on_supported_camps_tab() \
            .get_url()
        self.assertIn("/settings?tab=supported_camps", result)

    # TC_VERIFY_THE_SEARCH_BAR_IS_NEXT_TO_DELEGATED_SUPPORT_CAMP_TAB
    def test_verify_the_search_bar_is_present_next_the_delegate_support_camp_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_SEARCH_BAR_IS_NEXT_TO_DELEGATED_SUPPORT_CAMP_TAB')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(
            self.driver).verify_the_search_bar_is_present_next_the_delegate_support_camp_tab(
        ).get_url()
        self.assertIn("/settings?tab=supported_camps", result)

    # TC_VERIFY_THE_FUNCTIONALITY_OF_DIRECT_SUPPORT_CAMP
    def test_verify_the_functionality_of_direct_support_camp(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_DIRECT_SUPPORT_CAMP')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_the_functionality_of_direct_support_camp().get_url()
        self.assertIn("/settings?tab=supported_camps", result)

    # TC_VERIFY_THE_SEARCH_FUNCTIONALITY_IN_SUPPORTED_CAMPS_PAGE
    def test_verify_the_search_functionality_in_supported_camps_page(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_SEARCH_FUNCTIONALITY_IN_SUPPORTED_CAMPS_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_the_search_functionality_in_supported_camps_page(
            DEFAULT_TOPIC_NAME).get_url()
        self.assertIn("/settings?tab=supported_camps", result)

    # TC_VERIFY_TOPIC_NAME_LINK_NAME_IN DIRECT_SUPPORT_CAMP
    def test_verify_topic_name_link_in_direct_support_camp_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_TOPIC_NAME_AND_AGREEMENT_CAMP_NAME_IN DIRECT_SUPPORT_CAMP')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab \
            (self.driver).verify_topic_name_link_in_direct_support_camp_tab().get_url()
        self.assertIn("/settings?tab=supported_camps", result)

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

    #  TC_VERIFY_THE_FUNCTIONALITY_OF_DELEGATE_SUPPORT_CAMP
    def test_verify_the_functionality_of_delegate_support_camp_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FUNCTIONALITY_OF_DELEGATE_SUPPORT_CAMP')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_the_functionality_of_delegate_support_camp_tab().get_url()
        self.assertIn("/settings?tab=supported_camps", result)

    # TC_VERIFY_NICK_NAME_LINK_ON_DELEGATED_TAB
    def test_verify_nick_name_link_on_delegated_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_NICK_NAME_LINK_ON_DELEGATED_TAB')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_nick_name_link_on_delegated_tab().get_url()
        self.assertIn("/user/supports/", result)

    # TC_VERIFY_SUPPORT_DELEGATED_TO_USER_LINK
    def test_verify_support_delegated_to_user_link(self):
        print("\n" + str(test_cases('TC_VERIFY_SUPPORT_DELEGATED_TO_USER_LINK')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_support_delegated_to_user_link().get_url()
        self.assertIn("/user/supports/", result)

    # TC_VERIFY_CURRENT_SUPPORTED_CAMP_LINK
    def test_verify_current_supported_camp_link(self):
        print("\n" + str(test_cases('TC_VERIFY_CURRENT_SUPPORTED_CAMP_LINK')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_current_supported_camp_link().get_url()
        self.assertIn("/topic/", result)

    # TC_VERIFY_TOPIC_LINK_ON_DIRECT_SUPPORTED_TAB
    def test_verify_topic_link_on_direct_supported_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_TOPIC_LINK_ON_DIRECT_SUPPORTED_TAB')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_topic_link_on_direct_supported_tab().get_url()
        self.assertIn("/topic/", result)

    # TC_VERIFY_AGREEMENT_SUPPORT_LINK_ON_DIRECT_SUPPORTED_TAB
    def test_verify_agreement_support_link_on_direct_supported_tab(self):
        print("\n" + str(test_cases('TC_VERIFY_TOPIC_LINK_ON_DIRECT_SUPPORTED_TAB')))
        self.login_to_canonizer_app()
        result = CanonizerSupportCampsTab(self.driver).verify_agreement_support_link_on_direct_supported_tab().get_url()
        self.assertIn("/1-Agreement", result)

    # MANAGE NICK NAME TAB:-
    # TC VERIFY_WHEN_USER_CLICK_ON_NICK_NAME_TAB
    def test_verify_when_user_click_on_nick_name_tab(self):
        print("\n" + str(test_cases('TC VERIFY_WHEN_USER_CLICK_ON_NICK_NAME_TAB')))
        self.login_to_canonizer_app()
        CanonizerManageNickNameTab(self.driver).verify_when_user_click_on_nick_name_tab().get_url()

    # TC_VERIFY_ALL_THE_HEADERS_IN_NICK_NAME_TAB
    def test_verify_all_the_headers_in_nick_name_tab(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(self.driver).verify_all_the_headers_in_nick_name_tab().get_url()
        self.assertIn("/settings?tab=nick_name", result)

    # TC_VERIFY_WITH_ADD_NICKNAME_BUTTON_IS_PRESENT
    def test_verify_with_add_nick_name_button_is_present(self):
        self.login_to_canonizer_app()
        CanonizerManageNickNameTab(self.driver).verify_with_add_nick_name_button_is_present()

    # TC_VERIFY_THE_FUNCTIONALITY_OF_ADD_NICKNAME_BUTTON
    def test_verify_the_functionality_of_add_nickname_button(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(
            self.driver).verify_the_functionality_of_add_nickname_button("nicknew").get_url()
        self.assertIn("/settings?tab=nick_name", result)

    # TC_VERIFY_VALIDATION_FOR_ENTERING_NICK_NAME_FIELDS
    def test_verify_validation_for_entering_nick_name_field(self):
        self.login_to_canonizer_app()
        result = CanonizerManageNickNameTab(self.driver).verify_validation_for_entering_nick_name_field(
            DEFAULT_NICK_NAME).get_url()
        self.assertIn("/settings?tab=nick_name", result)

    # TC_VERIFY_VALIDATION_FOR_WITHOUT_ENTERING_NICK_NAME_FIELDS
    def test_verify_validation_for_without_entering_nick_name_field(self):
        self.login_to_canonizer_app()
        CanonizerManageNickNameTab(self.driver).verify_validation_for_without_entering_nick_name_field("")

    # TC_VERIFY_ENTERING_THE_NICK_NAME_WITH_SPACE
    def test_verify_entering_the_nick_name_with_space(self):
        self.login_to_canonizer_app()
        url = CanonizerManageNickNameTab(self.driver).verify_entering_the_nick_name_with_space(
            DEFAULT_INVALID_NICK_NAME).get_url()
        self.assertIn("", url)

    # HOMEPAGE:

    # TC_VERIFY_THE_FACEBOOK_LINK
    def test_verify_the_facebook_link(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_FACEBOOK_LINK')))
        self.login_to_canonizer_app()
        result = CanonizerHomePage(self.driver).verify_the_facebook_link().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_INSTA_LINK
    def test_verify_the_insta_link(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_INSTA_LINK')))
        self.login_to_canonizer_app()
        result = CanonizerHomePage(self.driver).verify_the_insta_link().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_YOUTUBE_LINK
    def test_verify_the_youtube_link(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_YOUTUBE_LINK')))
        self.login_to_canonizer_app()
        result = CanonizerHomePage(self.driver).verify_the_youtube_link().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_TWITTER_LINK
    def test_verify_the_twitter_link(self):
        print("\n" + str(test_cases('TC_VERIFY_THE_TWITTER_LINK')))
        self.login_to_canonizer_app()
        result = CanonizerHomePage(self.driver).verify_the_twitter_link().get_url()
        self.assertIn("", result)

    # Tc_verify_the_linkedin_link
    def test_verify_the_linkedin_link(self):
        print("\n" + str(test_cases('Tc_verify_the_linkedin_link')))
        self.login_to_canonizer_app()
        result = CanonizerHomePage(self.driver).verify_the_linkedin_link().get_url()
        self.assertIn("", result)

    # TC_LOAD_PRIVACY_POLICY_PAGE
    def test_load_privacy_policy_page(self):
        self.login_to_canonizer_app()
        CanonizerTermsAndPrivacyPolicy(self.driver).verify_privacy_policy_page()
        result = self.driver.find_element(*HomePageIdentifiers.PRIVACY_PAGE_TITLE).text
        self.assertIn("Canonizer Privacy Policy.", result)

    # TC_LOAD_TERMS_AND_SERVICES_PAGE
    def test_load_terms_and_services(self):
        self.login_to_canonizer_app()
        result = self.driver.find_element(*HomePageIdentifiers.TERM_AND_SERVICES_TITLE).text
        self.assertIn("Terms of Service", result)

    # TC_VERIFY_THE_BROWSE_BUTTON
    def test_verify_the_browse_button(self):
        self.login_to_canonizer_app()
        result = CanonizerTermsAndPrivacyPolicy(self.driver).verify_browse_button().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_CREATE_NEW_TOPIC
    def test_verify_the_create_new_topic(self):
        self.login_to_canonizer_app()
        result = CanonizerTermsAndPrivacyPolicy(self.driver).verify_create_new_topic().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_UPLOAD_FILE
    def test_verify_the_upload_file(self):
        self.login_to_canonizer_app()
        result = CanonizerTermsAndPrivacyPolicy(self.driver).verify_upload_file().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_HELP
    def test_verify_the_help(self):
        self.login_to_canonizer_app()
        result = CanonizerTermsAndPrivacyPolicy(self.driver).verify_the_help().get_url()
        self.assertIn("", result)

    # TC_TEST_VERIFY_THE_WHITE_PAPER
    def test_verify_the_white_paper(self):
        self.login_to_canonizer_app()
        result = CanonizerTermsAndPrivacyPolicy(self.driver).verify_the_white_paper().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_BLOG
    def test_verify_the_blog(self):
        self.login_to_canonizer_app()
        result = CanonizerTermsAndPrivacyPolicy(self.driver).verify_the_blog().get_url()
        self.assertIn("", result)

    # TC_VERIFY_THE_JOBS
    def test_verify_the_jobs(self):
        self.login_to_canonizer_app()
        result = CanonizerTermsAndPrivacyPolicy(self.driver).verify_the_jobs().get_url()
        self.assertIn("", result)

    # TC_CLICK_ON_CANONIZER_LOGO
    def test_click_on_canonizer_logo(self):
        self.login_to_canonizer_app()
        result = CanonizerTermsAndPrivacyPolicy(self.driver).click_on_canonizer_logo().get_url()
        self.assertIn("", result)

    # TC_CLICK_ON_SUPPORT_CANONIZER
    def test_click_on_support_canonizer(self):
        self.login_to_canonizer_app()
        result = CanonizerTermsAndPrivacyPolicy(self.driver).click_on_support_canonizer().get_url()
        self.assertIn("", result)

    # TC_CLICK_ON_ALGORITHM_DROPDOWN_BUTTON
    def test_click_on_algorithm_dropdown(self):
        self.login_to_canonizer_app()
        url = CanonizerTermsAndPrivacyPolicy(self.driver).click_on_algorithm_dropdown_button().get_url()
        self.assertIn("", url)

    def test_click_on_as_of_filter(self):
        self.login_to_canonizer_app()
        url = CanonizerTermsAndPrivacyPolicy(self.driver)

    # ACCOUNT_SETTING_PAGE PROFILE INFO TAB:
    # TC_VERIFYING_ACCOUNT_PROFILE_PAGE
    def test_verifying_account_profile_page(self):
        self.login_to_canonizer_app()
        print("\n" + str(test_cases('TC_VERIFYING_ACCOUNT_PROFILE_PAGE')))
        result = CanonizerAccountSettingPage(self.driver).verifying_profile_button().get_url()
        self.assertIn("/settings", result)

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
        result = CanonizerAccountSettingPage(self.driver).check_the_validation_for_phone_number_field(
            INVALID_MOBILE_NUMBER).get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_VERIFY_BUTTON_WITH_BLANK_FIELDS
    def test_verifying_verify_button_without_entering_data(self):
        print("\n" + str(test_cases('TC_VERIFYING_VERIFY_BUTTON_WITH_BLANK_FIELDS')))
        self.login_to_canonizer_app()
        CanonizerAccountSettingPage(
            self.driver).check_the_functionality_of_verify_button_without_entering_the_data()

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
            self.driver).verify_all_the_fields_are_present_in_personal_information_field().get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFYING_FIRST_NAME_FIELD_WITHOUT_ENTERING_DATA
    def test_verifying_validation_for_first_name_fields(self):
        print("\n" + str(test_cases('TC_VERIFYING_FIRST_NAME_FIELD_WITHOUT_ENTERING_DATA')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(self.driver).verify_the_validation_for_first_name(" ").get_url()
        self.assertIn("canonizer3.canonizer.com/settings", result)

    # TC_VERIFY_WHEN_USER_UPDATE_THE_PERSONAL_INFORMATION_AND_LOGS_OUT_AND_LOGIN_AGAIN
    def test_verify_when_user_updated_the_personal_information_and_logs_out_and_login_again(self):
        print(
            "\n" + str(
                test_cases('TC_VERIFY_WHEN_USER_UPDATE_THE_PERSONAL_INFORMATION_AND_LOGS_OUT_AND_LOGIN_AGAIN')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).verify_when_user_updated_the_personal_information_and_logs_out_and_login_again(FIRST_NAME,
                                                                                                        MIDDLE_NAME,
                                                                                                      LAST_NAME).get_url()
        self.assertIn("https://canonizer3.canonizer.com/", result)

    # TC_VERIFY_THE_SPACES_ARE_TRIMMED_IN_THE_FIRSTNAME_LASTNAME_MIDDLENAME_fields
    def test_verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields(self):
        print(
            "\n" + str(test_cases('TC_VERIFY_THE_SPACES_ARE_TRIMMED_IN_THE_FIRSTNAME_LASTNAME_MIDDLENAME_fields')))
        self.login_to_canonizer_app()
        result = CanonizerAccountSettingPage(
            self.driver).verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields(
            DEFAULT_FIRST_NAME,
            DEFAULT_MIDDLE_NAME,
            DEFAULT_LAST_NAME).get_url()
        self.assertIn("https://canonizer3.canonizer.com/", result)

    # TC_VERIFYING_ACCOUNT_PROFILE
    def test_click_on_account_setting_page(self):
        self.login_to_canonizer_app()
        print("\n" + str(test_cases('TC_VERIFYING_ACCOUNT_PROFILE')))
        CanonizerAccountSettingPage(self.driver).click_account_settings_page_button()

        # ----- ADD NEWS Test Cases START -----

    # TC_LOAD_ADD_NEWS_FEED_PAGE
    def test_load_add_news_page(self):
        print("\n" + str(test_cases('TC_LOAD_ADD_NEWS_FEED_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC)
        self.assertIn("/addnews/", result.get_url())

    # TC_ADD_NEWS_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK
    def test_add_news_page_mandatory_fields_are_marked_with_asterisk(self):
        print("\n" + str(test_cases('TC_ADD_NEWS_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK')))
        self.login_to_canonizer_app()
        # Click on the Add News link
        self.assertTrue(CanonizerAddNewsPage( self.driver).load_add_news_page(DEFAULT_TOPIC)
                        .add_news_page_mandatory_fields_are_marked_with_asterisk())

    # TC_CREATE_NEWS_WITH_VALID_DATA
    def test_create_news_with_valid_data(self):
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_VALID_DATA')))
        self.login_to_canonizer_app()
        result = CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).create_news_with_valid_data(
            "Test 7News",
            "https://www.google.com/").get_url()
        self.assertIn("/1-Agreement", result)

    # TC_CREATE_NEWS_WITH_BLANK_DISPLAY_TEXT
    def test_create_news_with_blank_display_text(self):
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_BLANK_DISPLAY_TEXT')))
        self.login_to_canonizer_app()
        result = CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC)\
            .create_news_with_blank_display_text("https://www.google.com/").get_url()
        self.assertIn("/addnews", result)

    # TC_CREATE_NEWS_WITH_BLANK_LINK
    def test_create_news_with_blank_link(self):
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_BLANK_LINK')))
        self.login_to_canonizer_app()
        result = CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC)\
            .create_news_with_blank_link("Test News2").get_url()
        self.assertIn("/addnews", result)

    # TC_NEW_FEED_WITH_BLANK_FIELDS
    def test_create_new_with_blank_fields(self):
        print("\n", str(test_cases('TC_NEW_FEED_WITH_BLANK_FIELDS')))
        self.login_to_canonizer_app()
        result = CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).create_new_with_blank_fields(
            "",
            ""
        ).get_url()
        self.assertIn("/addnews", result)

    # TC_CLICK_ADD_NEWS_CANCEL_BUTTON
    def test_click_add_news_cancel_button(self):
        print("\n" + str(test_cases('TC_CLICK_ADD_NEWS_CANCEL_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).click_add_news_cancel_button()
        self.assertIn("/topic", result.get_url())

    # TC_CREATE_NEWS_WITH_INVALID_LINK_FORMAT
    def test_create_news_with_invalid_link_format(self):
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_INVALID_LINK_FORMAT')))
        self.login_to_canonizer_app()
        result = CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).\
            create_news_with_invalid_link_format("news test", DEFAULT_INVALID_LINK).get_url()
        self.assertIn("addnews/", result)

    # TC_CREATE_NEWS_WITH_ENTER_KEY
    def test_create_news_with_enter_key(self):
        print("\n", str(test_cases("TC_CREATE_NEWS_WITH_ENTER_KEY")))
        self.login_to_canonizer_app()
        result = CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).create_news_with_enter_key(
            "Test automated news",
            "https://www.google.com/").get_url()
        self.assertIn("topic", result)

    # TC_CREATE_NEWS_WITH_DUPLICATE_DATA
    def test_create_news_with_duplicate_data(self):
        print("\n" + str(test_cases('TC_CREATE_NEWS_WITH_DUPLICATE_DATA')))
        self.login_to_canonizer_app()
        result = CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).create_news_with_duplicate_data(
            "Test automated news",
            "https://www.google.com/").get_url()
        self.assertIn("/topic/704-automated-topic/1-Agreement", result)

    # TC_CREATE_NEWS_WITH_TRAILING_SPACES
    def test_create_news_with_trailing_spaces(self):
        print("\n", str(test_cases("TC_CREATE_NEWS_WITH_TRAILING_SPACES")))
        self.login_to_canonizer_app()
        result = CanonizerAddNewsPage(self.driver).load_add_news_page(DEFAULT_TOPIC).create_news_with_trailing_spaces(
            "             News Trailing Spaces",
            "https://www.google.com/").get_url()
        self.assertIn("/topic/704-automated-topic/1-Agreement", result)
        # ----- Add News Test Cases End -----

        # ----- Edit News Test Cases Start -----

    # TC_LOAD_EDIT_NEWS
    def test_load_edit_news_page(self):
        self.login_to_canonizer_app()
        result = CanonizerEditNewsPage(self.driver).load_edit_news_page(DEFAULT_TOPIC)
        self.assertIn("/1-Agreement", result.get_url())

    # TC_UPDATE_NEWS_WITH_BLANK_DISPLAY_TEXT
    def test_update_news_with_blank_display_text(self):
        print("\n" + str(test_cases('TC_UPDATE_NEWS_WITH_BLANK_DISPLAY_TEXT')))
        self.login_to_canonizer_app()
        result = CanonizerEditNewsPage(self.driver).load_edit_news_page(DEFAULT_TOPIC)\
            .update_news_with_blank_display_text(" ").get_url()
        self.assertIn("/1-Agreement", result)

    # TC_UPDATE_NEWS_WITH_BLANK_LINK
    def test_update_news_with_blank_link(self):
        print("\n" + str(test_cases('TC_UPDATE_NEWS_WITH_BLANK_LINK')))
        self.login_to_canonizer_app()
        result = CanonizerEditNewsPage(self.driver).load_edit_news_page(DEFAULT_TOPIC) \
            .update_news_with_blank_link("text_update", " ").get_url()
        self.assertIn("/editnews/", result)

    # TC_EDIT_NEWS_WITH_CANCEL_BUTTON
    def test_click_edit_news_cancel_button(self):
        self.login_to_canonizer_app()
        result = CanonizerEditNewsPage(self.driver).load_edit_news_page(DEFAULT_TOPIC) \
            .click_edit_news_cancel_button().get_url()
        self.assertIn("/topic/", result)

        # ----- Edit News Test Cases End -----

        # ----- Log out Test Cases Start -----
    # TC_CLICK_LOGOUT_PAGE_BUTTON
    def test_click_log_out_page_button(self):
        print("\n" + str(test_cases('TC_CLICK_LOGOUT_PAGE_BUTTON')))
        self.login_to_canonizer_app()
        # Click on the Username and click on Log Out
        result = CanonizerLogoutPage(self.driver).click_log_out_page_button().get_url()
        self.assertIn("/canonizer3.canonizer.com", result)

    # ----- Log out Test Cases End -----

        # ----- Create New Camp Statement and Edit Camp Statement Test Cases Start -----
    # TC_LOAD_ADD_NEW_CAMP_STATEMENT_PAGE
    def test_load_camp_statement_page(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).add_camp_statement())

    def test_add_camp_statement_page_with_asterisk(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).add_camp_statement_asterisk())

    def test_add_camp_statement_without_mandatory_field(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).add_camp_statement_without_mandatory_data())

    def test_add_camp_statement_with_trailing_spaces(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).add_camp_statement_with_trailing_spaces())

    def test_add_camp_statement_with_blank_data(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).add_camp_statement_with_blank_data())

    def test_load_edit_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).load_edit_camp_statement())

    def test_update_camp_statement_with_mandatory_field(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).update_camp_statement_with_mandatory_field())

    def test_edit_camp_statement_with_trailing_spaces(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        self.assertTrue(CanonizerCampStatementPage(self.driver).edit_camp_statement_with_trailing_spaces())

    def test_edit_camp_statement_with_blank_data(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).edit_camp_statement_with_blank_data())

    def test_compare_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).compare_camp_statement())

    def test_add_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).edit_camp_statement())

    def test_edit_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).edit_camp_statement())
    # TC_LOAD_CREATE_CAMP_PAGE
    def test_load_create_camp_page(self):
        print("\n" + str(test_cases('TC_LOAD_CREATE_CAMP_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC)
        self.assertIn("/camp/create/", result.get_url())

    # TC_NEW_CAMP_FIELDS_ARE_MARKED_WITH_ASTERISK
    def test_new_camp_mandatory_fields_are_marked_with_asterisk(self):
        print("\n" + str(test_cases('TC_NEW_CAMP_FIELDS_ARE_MARKED_WITH_ASTERISK')))
        self.login_to_canonizer_app()
        self.assertTrue(CanonizerCreateCampPage(
            self.driver).load_create_camp_page(DEFAULT_TOPIC).new_camp_mandatory_fields_are_marked_with_asterisk())

    # TC_CREATE_CAMP_WITH_VALID_DATA
    def test_create_camp_with_valid_data(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_VALID_DATA')))
        self.login_to_canonizer_app()
        result = CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC)\
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertIn("/topic/", result.get_url())

    # TC_CREATE_CAMP_WITH_BLANK_CAMP_NAME
    def test_create_camp_with_blank_camp_name(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_BLANK_CAMP_NAME')))
        self.login_to_canonizer_app()
        result = CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_blank_camp_name(CREATE_CAMP_LIST_2)
        self.assertIn("/camp/create/", result.get_url())

    # TC_CREATE_CAMP_WITH_DUPLICATE_CAMP_NAME
    def test_create_camp_with_invalid_data(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_DUPLICATE_CAMP_NAME')))
        self.login_to_canonizer_app()
        result = CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_duplicate_camp_name(CREATE_CAMP_LIST_3)
        self.assertIn("/camp/create/", result.get_url())

    # TC_CREATE_CAMP_WITHOUT_ENTERING_DATA_IN_MANDATORY_FIELDS
    def test_create_camp_without_entering_data_in_mandatory_fields(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITHOUT_ENTERING_DATA_IN_MANDATORY_FIELDS')))
        self.login_to_canonizer_app()
        result = CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_blank_camp_name(CREATE_CAMP_LIST_2)
        self.assertIn("/camp/create/", result.get_url())

    # TC_CREATE_CAMP_WITH_INVALID_CAMP_ABOUT_URL
    def test_create_camp_with_invalid_camp_about_url(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_INVALID_CAMP_ABOUT_URL')))
        self.login_to_canonizer_app()
        result = CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_invalid_camp_about_url(CREATE_CAMP_LIST_4)
        self.assertIn("/camp/create/", result.get_url())

    # TC_CAMP_CANCEL_BUTTON
    def test_camp_cancel_button(self):
        print("\n" + str(test_cases('TC_CAMP_CANCEL_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC).camp_cancel_button()
        self.assertIn("/topic/", result.get_url())

    # TC_LOAD_CAMP_MANAGE_EDIT_PAGE
    def test_load_camp_manage_edit_page(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC).load_camp_manage_edit_page()
        self.assertIn("/camp/history/", result.get_url())

    # TC_VERIFY_SUBMITTER_NICK_NAME_ON_CAMP_HISTORY_PAGE
    def test_verify_submitter_nick_name_on_camp_history_page(self):
        print("\n" + str(test_cases('TC_VERIFY_SUBMITTER_NICK_NAME_ON_CAMP_HISTORY_PAGE')))
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .verify_submitter_nick_name_on_camp_history_page()
        self.assertIn("/user/supports/", result.get_url())

    # TC_VERIFY_SUBMIT_CAMP_UPDATE_BUTTON
    def test_verify_submit_camp_update_button(self):
        print("\n" + str(test_cases('TC_VERIFY_SUBMIT_CAMP_UPDATE_BUTTON')))
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC).verify_submit_camp_update_button()
        self.assertIn("/manage/camp/", result.get_url())

    # TC_UPDATE_CAMP_WITH_INVALID_URL
    def test_submit_camp_update_with_invalid_url(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .submit_camp_update_with_invalid_url(INVALID_CAMP_ABOUT_URL)
        self.assertIn("/manage/camp/", result.get_url())

    # TC_UPDATE_CAMP_WITH_DUPLICATE_CAMP_NAME
    def test_update_camp_with_duplicate_camp_name(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .update_camp_with_duplicate_camp_name(DUPLICATE_CAMP_NAME)
        self.assertIn("/manage/camp/", result.get_url())

    # TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_CAMP_UPDATE_PAGE
    def test_verify_cancel_button_functionality_on_camp_update_page(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .verify_cancel_button_functionality_on_camp_update_page()
        self.assertIn("/camp/history/", result.get_url())

    # TC_VERIFY_PREVIEW_BUTTON_FUNCTIONALITY_ON_CAMP_UPDATE_PAGE
    def test_verify_preview_button_functionality_on_camp_update_page(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC) \
            .verify_preview_button_functionality_on_camp_update_page()
        self.assertIn("/manage/camp/", result.get_url())

    # TC_VERIFY_FIELDS_ON_PREVIEW_MODAL
    def test_verify_camp_name_on_preview_modal(self):
        self.login_to_canonizer_app()
        CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC).verify_fields_on_preview_modal()

    # TC_VERIFY_CANCEL_BUTTON_FUNCTIONALITY_ON_PREVIEW_MODAL
    def test_verify_cancel_button_on_preview_modal(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC) \
            .verify_cancel_button_on_preview_modal()
        self.assertIn("/manage/camp/", result.get_url())

    # TC_VERIFY_SUBMITTER_NICK_NAME_ON_PREVIEW_MODAL
    def test_submitter_nick_name_on_preview_modal(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC) \
            .verify_submitter_nick_name_on_preview_modal()
        self.assertIn("/user/supports/", result.get_url())

    # TC_VERIFY_COMPARE_CAMPS_BUTTON_FUNCTIONALITY
    def test_verify_compare_camps_button_functionality(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC)\
            .verify_compare_camps_button_functionality()
        self.assertIn("/statement/compare/", result.get_url())

    # TC_VERIFY_CAMPS_NAME_ON_CAMP_HISTORY_COMPARISON_PAGE
    def test_verify_camps_name_on_camp_history_comparison_page(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC) \
            .verify_camps_name_on_camp_history_comparison_page().get_url()
        self.assertIn("/statement/compare/", result)

    def test_click_only_my_topics_button(self):
        # print("\n" + str(test_cases(23)))
        # Click on the Login Page and Create a Login Session and for further actions.
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).click_only_my_topics_button())

    def test_select_dropdown_value(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_dropdown_value())

    def test_select_all_namespaces(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        CanonizerBrowsePage(self.driver).select_all_namespaces()
        result = self.driver.find_element(*BrowsePageIdentifiers.SELECTED_TITLE).text
        self.assertIn("All", result)
    #Upload Files
    def test_upload_file_without_admin_login(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerUploadFilePage(self.driver).upload_file_with_user_login())

    def test_upload_file_with_admin_login(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerUploadFilePage(self.driver).upload_file_with_user_login())

    def test_upload_more_than_5mb_file_with_user_login(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(20)
        CanonizerUploadFilePage(self.driver).upload_more_than_5mb_file_with_user_login()
        result = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/form/div/div[2]/div[1]/span/div[2]/div/div/div/div/p").text
        self.assertIn("This file is exceeding the max limit and will not be uploaded", result)

    def test_upload_file_with_invalid_file_name_format(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(20)
        CanonizerUploadFilePage(self.driver).upload_file_with_invalid_file_name_format()
        result = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/form/div/div[2]/div[1]/span/div[2]/div/div/div/div/p").text
        self.assertIn("This file format is invalid", result)

    def test_click_upload_button(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(20)
        CanonizerUploadFilePage(self.driver).click_upload_button()
        result = self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/nav/ul/li[2]").text
        self.assertIn("Upload File", result)

    def test_support_value_new_topic(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()

        self.assertTrue(CanonizerSupportValue(self.driver).support_value_new_topic())

    #Url redirection

    def test_url_redirection(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)

        res = requests.get("http://canonizer3.canonizer.com/topic.asp/88-Theories-of-Consciousness/1-Agreement")
        res = str(res.status_code)
        print(res)
        if "200" == res:
            print("pass")
            self.driver.get("http://canonizer3.canonizer.com/topic.asp/88-Theories-of-Consciousness/1-Agreement")
            resp = self.driver.current_url
            print(resp)
        else:
            print("url does not exist")

        self.assertIn("/topic/88-Theories-of-Consciousness/1-Agreement", resp)

    def test_unknown_topic(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)
        import string
        N = 10
        self.n = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        self.n = str(self.n)
        url = ("http://canonizer3.canonizer.com/topic/" + self.n)
        print(url)
        self.driver.get(url)
        resp = requests.get(url)
        resp = str(resp.status_code)
        print(resp)
        if resp == "404":
            pass

        else:
            mailer.mailern()
            print("failed")

        self.assertIn("404", resp)

    def test_asp_url_redirection(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)
        self.n = random.randint(0, 10000)
        self.n = str(self.n)
        self.driver.get("http://canonizer3.canonizer.com/topic.asp/" + self.n)
        resp = self.driver.current_url
        reslt = ("/topic/" + self.n)
        print(resp)
        print(reslt)
        if resp == reslt:
            pass
        else:
            mailer.mailern()
            print("failed")

        self.assertIn(reslt, resp)

    def test_video_url(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)
        res = requests.get("https://canonizer.com/videos/consciousness?chapter=representational_qualia_consensus")
        res = str(res.status_code)
        print(res)
        if "200" == res:
            url = ("https://" + "canonizer3" + ".canonizer.com/videos/consciousness?chapter=representational_qualia_consensus")
            self.driver.get(url)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div/label[1]/span[1]/input").click()

            self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/video").click()
            if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/video"):
                self.resp = "passed"
                # resp = self.driver.current_url
                print(self.resp)
        else:
            print("url does not exist")
        self.assertIn("passed", self.resp)

    def test_support_list_asp_url_redirection(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)
        self.driver.get("http://canonizer3.canonizer.com/support_list.asp?nick_name_id=1")
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/h3"):
            self.status = "200"
        else:
            self.status = "404"

        self.assertIn("200", self.status)

    def test_thread_asp_url_redirection(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)

        self.driver.get("http://canonizer3.canonizer.com/thread.asp/23/13/4")
        if self.driver.find_element(By.ID, "create-btn"):
            self.status = "200"
        else:
            self.status = "404"

        self.assertIn("200", self.status)

    def test_forum_asp_url_redirection(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)

        self.driver.get("http://canonizer3.canonizer.com/forum.asp/88/1")
        if self.driver.find_element(By.ID, "create-btn"):
            self.status = "200"
        else:
            self.status = "404"

        self.assertIn("200", self.status)

    def test_topoc_asp_url_redirection(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)

        self.driver.get("http://canonizer3.canonizer.com/topoc.asp/85")
        if self.driver.find_element(By.ID, "camp-forum-btn"):
            self.status = "200"
        else:
            self.status = "404"

        self.assertIn("200", self.status)

    def test_manage_asp_url_redirection(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)
        self.driver.get("http://canonizer3.canonizer.com/manage.asp/2/2?class=camp")
        if self.driver.find_element(By.ID, "create-topic-btn"):
            self.status = "200"
        else:
            self.status = "404"

        self.assertIn("200", self.status)

    def test_statement_asp_url_redirection(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)
        self.driver.get("http://canonizer3.canonizer.com/statement.asp/2/2")
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/button[1]/span"):
            self.status = "200"
        else:
            self.status = "404"

        self.assertIn("200", self.status)

    def test_stmt_asp_url_redirection(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)

        self.driver.get("http://canonizer3.canonizer.com/stmt.asp/2/2")
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/button[1]/span"):
            self.status = "200"
        else:
            self.status = "404"

        self.assertIn("200", self.status)

    def test_sitemap_url(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)

        resp = requests.get("https://canonizer.com/sitemap.xml")
        self.res = str(resp.status_code)
        if "200" == self.res:
            self.driver.get("https://canonizer3.canonizer.com/sitemap.xml")
            self.resf = requests.get("https://canonizer3.canonizer.com/sitemap.xml").text
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(self.resf, "html.parser")
        else:
            self.driver.get("https://canonizer3.canonizer.com/sitemap.xml")
            print("url does not exist")

        self.assertIn("XML Sitemap", soup.h1)

    def test_load_camp_statement_page(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).add_camp_statement())

    def test_add_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).add_camp_statement())

    def test_add_camp_statement_page_with_asterisk(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).add_camp_statement_asterisk())

    def test_add_camp_statement_without_mandatory_field(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).add_camp_statement_without_mandatory_data())

    def test_add_camp_statement_with_trailing_spaces(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).add_camp_statement_with_trailing_spaces())

    def test_add_camp_statement_with_blank_data(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerCreateCampPage(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_camp_with_valid_data(CREATE_CAMP_LIST_1)
        self.assertTrue(CanonizerCampStatementPage(self.driver).add_camp_statement_with_blank_data())

    def test_load_edit_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        self.assertTrue(CanonizerCampStatementPage(self.driver).load_edit_camp_statement())

    def test_update_camp_statement_with_mandatory_field(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        self.assertTrue(CanonizerCampStatementPage(self.driver).update_camp_statement_with_mandatory_field())

    def test_edit_camp_statement_with_trailing_spaces(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        self.assertTrue(CanonizerCampStatementPage(self.driver).edit_camp_statement_with_trailing_spaces())

    def test_edit_camp_statement_with_blank_data(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        self.assertTrue(CanonizerCampStatementPage(self.driver).edit_camp_statement_with_blank_data())

    def test_compare_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        self.assertTrue(CanonizerCampStatementPage(self.driver).compare_camp_statement())


    def test_edit_camp_statement(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        self.assertTrue(CanonizerCampStatementPage(self.driver).edit_camp_statement())

    def test_update_news(self):
        #print("\n" + str(test_cases('TC_UPDATE_NEWS')))
        self.login_to_canonizer_app()
        result = CanonizerEditNewsPage(self.driver).load_edit_news_page(DEFAULT_TOPIC) \
            .update_news("text_update", "staging.canonizer.com/support").get_url()
        self.assertIn("/editnews/", result)


    def test_submit_camp_update(self):
        self.login_to_canonizer_app()
        result = CanonizerEditCampPage(self.driver).load_topic_detail_page(DEFAULT_TOPIC) \
            .submit_camp_update("www.google.com")
        self.assertIn("/manage/camp/", result.get_url())

    def test_footer_browse(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerFooter(self.driver).footer_browse()
        result = self.driver.current_url
        self.assertIn("https://canonizer3.canonizer.com/browse", result)

    def test_footer_create_new_topic(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerFooter(self.driver).footer_create_new_topic()
        result = self.driver.current_url
        self.assertIn("https://canonizer3.canonizer.com/create/topic", result)

    def test_footer_upload(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerFooter(self.driver).footer_upload()
        result = self.driver.current_url
        self.assertIn("https://canonizer3.canonizer.com/uploadFile", result)

    def test_footer_sitemap(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerFooter(self.driver).footer_sitemap()
        result = self.driver.current_url
        print(result)
        self.assertIn("https://canonizer3.canonizer.com/sitemap.xml", result)

    def test_footer_help(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerFooter(self.driver).footer_help()
        result = self.driver.current_url

        self.assertIn("https://canonizer3.canonizer.com/topic/132-Help/1-Agreement", result)

    def test_footer_white_paper(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerFooter(self.driver).footer_white_paper()
        #action = ActionChains(self.driver)
        #action.key_down(Keys.CONTROL).send_keys('W').key_up(Keys.CONTROL).perform()
        #self.driver.close
        result = self.driver.current_url
        self.assertIn("https://canonizer3.canonizer.com/files/2012_amplifying_final.pdf", result)

    def test_footer_blog(self):
        self.driver.implicitly_wait(20)
        self.login_to_canonizer_app()
        CanonizerFooter(self.driver).footer_blog()
        result = self.driver.current_url
        self.assertIn("https://canonizer3.canonizer.com/", result)

    def test_footer_jobs(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        CanonizerFooter(self.driver).footer_jobs()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div/div[1]/div[1]/span[2]"):
           result = self.driver.current_url

        self.assertIn("https://canonizer3.canonizer.com/topic/6-Canonizer-Jobs/1-Agreement", result)
    def test_create_archived_camp_with_valid_data(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_VALID_DATA')))
        self.login_to_canonizer_app()
        CanonizerCreateUpdateArchivedCamp(self.driver).load_create_camp_page(DEFAULT_TOPIC)\
            .create_archived_camp_with_valid_data(CREATE_CAMP_LIST_1)
        result = self.driver.current_url
        self.assertIn("/camp/create/", result)

    def test_create_archived_camp_with_blank_camp_name(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_BLANK_CAMP_NAME')))
        self.login_to_canonizer_app()
        CanonizerCreateUpdateArchivedCamp(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_archived_camp_with_blank_camp_name(CREATE_CAMP_LIST_2)
        result = self.driver.current_url

        self.assertIn("/camp/create/", result)

    def test_create_archived_camp_with_duplicate_camp_name(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_DUPLICATE_CAMP_NAME')))
        self.login_to_canonizer_app()
        CanonizerCreateUpdateArchivedCamp(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_archived_camp_with_duplicate_camp_name(CREATE_CAMP_LIST_3)
        result = self.driver.current_url

        self.assertIn("/camp/create/", result)

    def test_create_archived_camp_without_entering_data_in_mandatory_fields(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITHOUT_ENTERING_DATA_IN_MANDATORY_FIELDS')))
        self.login_to_canonizer_app()
        CanonizerCreateUpdateArchivedCamp(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_archived_camp_with_blank_camp_name(CREATE_CAMP_LIST_2)
        result = self.driver.current_url

        self.assertIn("/camp/create/", result)

    def test_create_archived_camp_with_invalid_camp_about_url(self):
        print("\n" + str(test_cases('TC_CREATE_CAMP_WITH_INVALID_CAMP_ABOUT_URL')))
        self.login_to_canonizer_app()
        CanonizerCreateUpdateArchivedCamp(self.driver).load_create_camp_page(DEFAULT_TOPIC) \
            .create_archived_camp_with_invalid_camp_about_url(CREATE_CAMP_LIST_4)
        result = self.driver.current_url

        self.assertIn("/camp/create/", result)

    def test_camp_archived_cancel_button(self):
        print("\n" + str(test_cases('TC_CAMP_CANCEL_BUTTON')))
        self.login_to_canonizer_app()
        CanonizerCreateUpdateArchivedCamp(self.driver).load_create_camp_page(DEFAULT_TOPIC).camp_archived_cancel_button()
        result = self.driver.current_url
        self.assertIn("/topic/", result)
    
    def test_check_unarchived_camp(self):
        self.driver.implicitly_wait(20)
        self.login_to_canonizer_app()
        CanonizerEditArchivedCampPage(self.driver).check_unarchived_camp()
        result = self.driver.find_element(*CampHistoryIdentifiers.ARCHIEVED_STATUS).text
        self.assertIn("No", result)
    def test_do_archive_camp(self):
        self.driver.implicitly_wait(20)
        self.login_to_canonizer_app()
        CanonizerEditArchivedCampPage(self.driver).do_archive_camp()
        result = self.driver.find_element(*CampHistoryIdentifiers.ARCHIEVED_STATUS).text
        self.assertIn("Yes", result)    
    def test_archive_camp_score_after_making_archive(self):
        self.driver.implicitly_wait(20)
        self.login_to_canonizer_app()
        self.assertTrue(CanonizerEditArchivedCampPage(self.driver).archive_camp_score_after_making_archive())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test'))



