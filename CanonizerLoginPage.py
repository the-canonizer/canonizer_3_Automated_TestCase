import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from CanonizerBase import Page
from CanonizerValidationCheckMessages import message
from Identifiers import LoginPageIdentifiers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import *
from selenium import webdriver


class CanonizerLoginPage(Page):
    """
    Class Name : CanonizerLoginPage
    Description : Test the functionality of the Login and Logout Page
                  Forgot Password Functionality also needs to be added on this Page.
    Attributes: None
    """

    def driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def click_login_page_button(self):
        """
        This function is to click on the login button
        -> Hover to the Login button
        -> Find the element and click it
        :return:
        Return the result to the main page.
        """
        self.hover(*LoginPageIdentifiers.LOGIN_BUTTON)
        self.find_element(*LoginPageIdentifiers.LOGIN_BUTTON).click()
        return CanonizerLoginPage(self.driver)

    def enter_email(self, user):
        """
        "Enter User Email to the Email Box."
        Args:
            :param user: Email ID of the User
        :return:
            SEND_KEYS is equivalent to entering keys using keyboard. And control return to the calling program.
        """
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(user)

    def enter_password(self, password):
        """
        This function is to entering the user password to the password field and return control.
        Args:
            :param password: Password of the User
        :return:
            After entering the password to the Password field. Function return control.
        """
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(password)

    def click_login_button(self):
        """
        This function verify if the login page loads properly
        :return:
            Once the page is loaded, return result to the main program.
        """
        self.find_element(*LoginPageIdentifiers.SUBMIT).click()

    def login(self, user, password):
        """
        This function is to click the login button and return result to the main program.
        Args:
            :param user: Email ID of the User
            :param password: Password of the User
        :return:
            After Entering the Username and Password, function clicks on the login button and returns the control.
        """
        self.enter_email(user)
        self.enter_password(password)
        self.click_login_button()

    def login_with_valid_user(self, user, password):
        """
        This function is a part of test case, test_login_with_valid_user and it verifies using valid username and
        password, application works properly and take the user to the home page.
        Args:
            :param user: Email ID of the User
            :param password: Password of User
        :return:
            Retrun the result to the main program
        """
        self.login(user, password)

        return CanonizerLoginPage(self.driver)

    def login_page_mandatory_fields_are_marked_with_asterisk(self):
        """
        This Function checks, if Mandatory fields on Register Page Marked with *
        First Name, Last Name, Email, Password, Confirm Password are Mandatory Fields

        :return: the element value

        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-form-item-required')))
        except TimeoutException:
            pass
        return \
            self.find_element(*LoginPageIdentifiers.EMAIL_ASTRK) and \
            self.find_element(*LoginPageIdentifiers.PASSWORD_ASTRK)

    def click_on_login_button(self):
        self.driver.implicitly_wait(30)
        self.hover(*LoginPageIdentifiers.LOGIN_BUTTON)
        self.find_element(*LoginPageIdentifiers.LOGIN_BUTTON).click()

        return CanonizerLoginPage(self.driver)

    def verify_the_login_page(self, email, password):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.EMAIL).clear()
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*LoginPageIdentifiers.SUBMIT).click()

    def click_on_close_icon_button(self):
        self.click_on_login_button()
        self.hover(*LoginPageIdentifiers.CLOSE_BUTTON)
        self.find_element(*LoginPageIdentifiers.CLOSE_BUTTON).click()
        self.hover(*LoginPageIdentifiers.LOGIN_BUTTON)
        title = self.find_element(*LoginPageIdentifiers.LOGIN_BUTTON).text
        if title == message['Login_Page']['LOGIN_TITLE']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Error message not found")

    def verify_the_login_with_invalid_email_format(self, default_invalid_user, default_pass):
        self.verify_the_login_page(default_invalid_user, default_pass)
        title = self.find_element(*LoginPageIdentifiers.INVALID_EMAIL_TITLE).text
        if title == message['Login_Page']['INVALID_EMAIL']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Error message not found")

    def verify_the_login_with_blank_email(self, blank_email, password):
        self.verify_the_login_page(blank_email, password)
        error = self.find_element(*LoginPageIdentifiers.BLANK_EMAIL_ERROR).text
        if error == message['Login_Page']['BLANK_EMAIL']:
            return CanonizerLoginPage(self.driver)

    def verify_the_login_with_blank_password(self, default_user, blank_password):
        self.verify_the_login_page(default_user, blank_password)
        self.hover(*LoginPageIdentifiers.BLANK_PASSWORD_ERROR)
        error = self.find_element(*LoginPageIdentifiers.BLANK_PASSWORD_ERROR).text
        if error == message['Login_Page']['BLANK_PASSWORD']:
            return CanonizerLoginPage(self.driver)

    def verify_the_login_functionality_by_entering_the_registered_credential(self, default_user, default_pass):
        self.verify_the_login_page(default_user, default_pass)
        return CanonizerLoginPage(self.driver)

    def verify_the_forget_password_button(self):
        self.click_on_login_button()
        self.hover(*LoginPageIdentifiers.FORGET_PASSWORD)
        self.find_element(*LoginPageIdentifiers.FORGET_PASSWORD).click()
        self.find_element(*LoginPageIdentifiers.FORGET_PASSWORD_TITLE).click()
        title = self.find_element(*LoginPageIdentifiers.FORGET_PASSWORD_TITLE).text
        if title == message['Login_Page']['FORGOT_PASSWORD']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Title not found")

    def verify_the_remember_me_checkbox(self, default_user, default_pass):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.EMAIL).clear()
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(default_user)
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(default_pass)
        self.find_element(*LoginPageIdentifiers.CHECK_BOX).click()
        self.find_element(*LoginPageIdentifiers.SUBMIT).click()

        return CanonizerLoginPage(self.driver)

    def click_on_register_now_button_on_login_page(self):
        self.click_on_login_button()
        try:
            WebDriverWait(self.driver, 6).until(
                EC.visibility_of_element_located((By.ID, 'dont-account-link-tag')))
        except TimeoutException:
            pass
        self.find_element(*LoginPageIdentifiers.REGISTER_NOW_LINK).click()
        self.hover(*LoginPageIdentifiers.LOGIN_TITLE)
        title = self.find_element(*LoginPageIdentifiers.LOGIN_TITLE).text
        if title == message['Login_Page']['REGISTER_PAGE_TITLE']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Title not found")

    def verify_one_time_request_code(self, default_invalid_user, default_pass):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.EMAIL).clear()
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(default_invalid_user)
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(default_pass)
        self.find_element(*LoginPageIdentifiers.REQUEST_CODE).click()

    def verify_one_time_request_code_with_invalid_email(self, default_invalid_user, default_pass):
        self.verify_one_time_request_code(default_invalid_user, default_pass)
        title = self.find_element(*LoginPageIdentifiers.EMAIL_ERROR_MESSAGE).text
        if title == message['Login_Page']['ONE_TIME_REQUEST_CODE_WITH_INVALID_EMAIL']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Title not found")

    def verify_one_time_request_code_with_valid_credentials(self, default_user, default_pass):
        self.verify_one_time_request_code(default_user, default_pass)
        self.hover(*LoginPageIdentifiers.ONE_TIME_REQUEST_TITLE)
        title = self.find_element(*LoginPageIdentifiers.ONE_TIME_REQUEST_TITLE).text
        if title == message['Login_Page']['ONE_TIME_REQUEST_CODE_WITH_VALID_PASSWORD']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Title not found")

    def verifying_facebook_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.FACEBOOK_LINK).click()
        self.hover(*LoginPageIdentifiers.FACEBOOK_TITLE)
        title = self.find_element(*LoginPageIdentifiers.FACEBOOK_TITLE).text
        if title == message['Log Into Facebook']['FACEBOOK_TITLE']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Title not found")

    def verifying_google_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.GOOGLE_LINK).click()
        self.hover(*LoginPageIdentifiers.GOOGLE_TITLE)
        title = self.find_element(*LoginPageIdentifiers.GOOGLE_TITLE).text
        if title == message['Login_Page']['GOOGLE_TITLE']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Title not found")

    def verifying_twitter_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.TWITTER_LINK).click()
        self.hover(*LoginPageIdentifiers.TWITTER_TITLE)
        title = self.find_element(*LoginPageIdentifiers.TWITTER_TITLE).text
        if title == message['Login_Page']['TWITTER_TITLE']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Title not found")

    def verifying_linkedin_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.LINKEDIN_LINK).click()
        self.hover(*LoginPageIdentifiers.LINKEDIN_TITLE)
        title = self.find_element(*LoginPageIdentifiers.LINKEDIN_TITLE).text
        if title == message['Login_Page']['LINKEDIN_TITLE']:
            return CanonizerLoginPage(self.driver)
        else:
            print("Title not found")

    def verifying_github_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.GITHUB_LINK).click()

        return CanonizerLoginPage(self.driver)
