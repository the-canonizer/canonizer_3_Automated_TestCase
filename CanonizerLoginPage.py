import sys
from datetime import time
from lib2to3.pgen2 import driver
from pydoc import text
from telnetlib import EC
from time import sleep

import self
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CanonizerBase import Page
from Identifiers import HomePageIdentifiers, LoginPageIdentifiers


class CanonizerLoginPage(Page):
    """
    Class Name : CanonizerLoginPage
    Description : Test the functionality of the Login and Logout Page
                  Forgot Password Functionality also needs to be added on this Page.

    Attributes: None
    """

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
        title = self.find_element(*LoginPageIdentifiers.LOGIN_BUTTON).text
        if title == 'Log in':
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

    def click_on_login_button(self):
        self.hover(*LoginPageIdentifiers.LOGIN_BUTTON)
        self.find_element(*LoginPageIdentifiers.LOGIN_BUTTON).click()

        return CanonizerLoginPage(self.driver)

    def click_on_close_icon_button(self):
        self.click_on_login_button()
        self.hover(*LoginPageIdentifiers.CLOSE_BUTTON)
        self.find_element(*LoginPageIdentifiers.CLOSE_BUTTON).click()

        return CanonizerLoginPage(self.driver)

    def verify_the_Login_Functionality_by_entering_the_registered_credential(self, email, password):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.EMAIL).clear()
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*LoginPageIdentifiers.SUBMIT).click()

        return CanonizerLoginPage(self.driver)

    def verify_the_login_with_invalid_email_format(self, email, password):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.EMAIL).clear()
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*LoginPageIdentifiers.SUBMIT).click()
        self.find_element(*LoginPageIdentifiers.INVALID_EMAIL_TITLE).click()
        title = self.find_element(*LoginPageIdentifiers.INVALID_EMAIL_TITLE)
        if title == 'Your session has expired. Please log in again!':
            return CanonizerLoginPage(self.driver)

    def verify_the_Remember_me_checkbox(self, email, password):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.EMAIL).clear()
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*LoginPageIdentifiers.CHECK_BOX).click()
        self.find_element(*LoginPageIdentifiers.SUBMIT).click()

        return CanonizerLoginPage(self.driver)

    def verify_the_login_button_by_entering_the_empty_space(self, email, password):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.EMAIL).clear()
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*LoginPageIdentifiers.CHECK_BOX).click()
        self.find_element(*LoginPageIdentifiers.SUBMIT).click()

        return CanonizerLoginPage(self.driver)

    def verify_the_forget_password_button(self):
        self.click_on_login_button()
        self.hover(*LoginPageIdentifiers.FORGET_PASSWORD)
        self.find_element(*LoginPageIdentifiers.FORGET_PASSWORD).click()
        self.find_element(*LoginPageIdentifiers.FORGET_PASSWORD_TITLE).click()
        title = self.find_element(*LoginPageIdentifiers.FORGET_PASSWORD_TITLE).text
        if title == 'Forgot your password?':
            return CanonizerLoginPage(self.driver)

    def click_on_register_now_button_on_login_page(self):
        self.hover(*LoginPageIdentifiers.LOGIN_BUTTON)
        self.find_element(*LoginPageIdentifiers.LOGIN_BUTTON).click()
        self.find_element(*LoginPageIdentifiers.REGISTER_NOW_LINK).click()

        return CanonizerLoginPage(self.driver)

    def verify_one_time_request_code_without_entering_email(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys()
        self.find_element(*LoginPageIdentifiers.REQUEST_CODE).click()
        title = self.find_element(*LoginPageIdentifiers.EMAIL_ERROR_MESSAGE).text
        if title == 'Please input your Email / Phone Number!':
            return CanonizerLoginPage(self.driver)

    def verify_one_time_request_code_with_invalid_email(self, email, password):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.EMAIL).clear()
        self.find_element(*LoginPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*LoginPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*LoginPageIdentifiers.REQUEST_CODE).click()
        title = self.find_element(*LoginPageIdentifiers.EMAIL_ERROR_MESSAGE).text
        if title == 'Input is not valid!':
            return CanonizerLoginPage(self.driver)

    def verifying_social_account_links(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.SOCIAL_LINKS).click()

        return CanonizerLoginPage(self.driver)

    def verifying_facebook_icon(self):
        self.click_on_login_button()
        #self.hover(*LoginPageIdentifiers.FACEBOOK_LINK)
        self.find_element(*LoginPageIdentifiers.FACEBOOK_LINK).click()
        self.hover(*LoginPageIdentifiers.FACEBOOK_TITLE)
        title = self.find_element(*LoginPageIdentifiers.FACEBOOK_TITLE).text
        if title == 'Log in to Facebook':
            return CanonizerLoginPage(self.driver)

    def verifying_google_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.GOOGLE_LINK).click()

        return CanonizerLoginPage(self.driver)

    def verifying_twitter_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.TWITTER_LINK).click()
        self.hover(*LoginPageIdentifiers.TWITTER_TITLE)
        title = self.find_element(*LoginPageIdentifiers.TWITTER_TITLE).text
        if title == 'Authorize the_canonizer to access your account?':
            return CanonizerLoginPage(self.driver)

    def verifying_linkedin_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.LINKEDIN_LINK).click()

        return CanonizerLoginPage(self.driver)

    def verifying_github_link(self):
        self.click_on_login_button()
        self.find_element(*LoginPageIdentifiers.GITHUB_LINK).click()

        return CanonizerLoginPage(self.driver)

    def verify_login_placeholders(self):
        self.click_login_page_button()
        email = self.find_element(*LoginPageIdentifiers.EMAIL)
        password = self.find_element(*LoginPageIdentifiers.PASSWORD)
        email_placeholder = email.get_attribute('placeholder')
        password_placeholder = password.get_attribute('placeholder')
        if email_placeholder == 'Email / Phone Number' and password_placeholder == 'Password':
            return CanonizerLoginPage(self.driver)

