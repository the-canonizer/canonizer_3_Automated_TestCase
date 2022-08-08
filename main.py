import unittest
#from unittest import result

from selenium.common.exceptions import TimeoutException

from CanonizerCampForum import CanonizerCampForumPage
from CanonizerCreateNewTopicPage import CanonizerCreateNewTopic
from CanonizerHomePage import *
from CanonizerLoginPage import CanonizerLoginPage
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
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button().create_topic_with_duplicate_topic_name(
            DEFAULT_NICK_NAME,
            DUPLICATE_TOPIC_NAME,
            DEFAULT_NAMESPACE,
            DEFAULT_SUMMARY).get_url()
        self.assertIn("create/topic", result)

    # TC_CREATE_NEW_TOPIC_WITH_SPECIAL_CHARS
    def test_create_topic_with_special_chars(self):
        print("\n", str(test_cases('TC_CREATE_NEW_TOPIC_WITH_SPECIAL_CHARS')))
        self.login_to_canonizer_app()
        result = CanonizerCreateNewTopic(self.driver).click_create_new_topic_page_button() \
            .create_topic_with_special_chars(
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

    # ----- CREATE TOPIC Test Cases end -----
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
        result = CanonizerCampForumPage(self.driver).check_no_thread_availability().get_url()
        self.assertIn("/1-Agreement/threads", result)

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
            .create_thread_with_trailing_spaces("      New Thread " + add_name).get_url()
        self.assertIn("/1-Agreement/threads", result)

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









    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
