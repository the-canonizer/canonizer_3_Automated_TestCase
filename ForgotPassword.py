from CanonizerBase import Page
from Identifiers import ForgotPasswordIdentifiers
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from datetime import datetime
from time import time
import time


class CanonizerForgotPage(Page):

    def click_forgot_password_link(self):
        self.find_element(*ForgotPasswordIdentifiers.LOGIN).click()
        self.find_element(*ForgotPasswordIdentifiers.FORGOTPASSWORD).click()
        confirmation_text = self.find_element(*ForgotPasswordIdentifiers.TITLE).text
        if confirmation_text == 'Forgot your password?':
            return CanonizerForgotPage(self.driver)
            print(confirmation_text)
        else:
            print("Confirmation text is not matching")

    def login_and_forgot_password(self):
        self.find_element(*ForgotPasswordIdentifiers.LOGIN).click()
        self.find_element(*ForgotPasswordIdentifiers.FORGOTPASSWORD).click()

    def enter_email(self, email):
        self.hover(*ForgotPasswordIdentifiers.EMAIL)
        self.find_element(*ForgotPasswordIdentifiers.EMAIL).send_keys(email)

    def click_submit_button(self):
        self.hover(*ForgotPasswordIdentifiers.SUBMITBUTTON)
        self.find_element(*ForgotPasswordIdentifiers.SUBMITBUTTON).click()

    def click_otp_submit_button(self):
        self.hover(*ForgotPasswordIdentifiers.SUBMIT_OTP_BUTTON)
        self.find_element(*ForgotPasswordIdentifiers.SUBMIT_OTP_BUTTON).click()

    def submit(self, email):
        self.enter_email(email)
        self.click_submit_button()
        title = self.find_element(*ForgotPasswordIdentifiers.OTPPAGETITLE).text
        if title == 'Create password verification code':
            print(title)
            return CanonizerForgotPage(self.driver)
        else:
            print("Title is not matching")

    def click_submit_button_with_valid_email(self, email):
        self.submit(email)

    def click_submit_button_with_invalid_email(self, email):
        self.enter_email(email)
        time.sleep(3)
        self.click_submit_button()
        return self.find_element(*ForgotPasswordIdentifiers.INVALIDEMAIL_ERROR).text

    def click_submit_button_with_empty_email(self, email):
        self.enter_email(email)
        time.sleep(4)
        self.click_submit_button()
        return self.find_element(*ForgotPasswordIdentifiers.INVALIDEMAIL_ERROR).text

    def submit_empty_otp(self, email):
        time.sleep(3)
        self.enter_email(email)
        self.click_submit_button()
        time.sleep(3)
        self.find_element(*ForgotPasswordIdentifiers.OTP_ENTER).click()
        self.click_otp_submit_button()
        time.sleep(3)
        return self.find_element(*ForgotPasswordIdentifiers.OTP_EMPTY_ERROR).text

    def submit_invalid_otp(self, email, otp):
        time.sleep(3)
        self.enter_email(email)
        self.click_submit_button()
        time.sleep(3)
        self.find_element(*ForgotPasswordIdentifiers.OTP_ENTER).send_keys(otp)
        self.click_otp_submit_button()
        time.sleep(3)
        return self.find_element(*ForgotPasswordIdentifiers.INVALID_OTP_ERROR).text

    def submit_unregsitered_email(self, email):
        self.enter_email(email)
        self.click_submit_button()
        return self.find_element(*ForgotPasswordIdentifiers.UNREGSITERED_EMAIL_ERROR).text

    def cross_icon_on_forgot_page(self):
        self.find_element(*ForgotPasswordIdentifiers.CROSS_ICON_FORGOT_MODAL).click
        confirmation_text = self.find_element(*ForgotPasswordIdentifiers.LOGIN).text
        if confirmation_text == "Log in":
            print(confirmation_text)
        return CanonizerForgotPage(self.driver)

    def cross_icon_on_otp_page(self):
        self.find_element(*ForgotPasswordIdentifiers.CROSS_ICON_OTP_MODAL).click
        confirmation_text = self.find_element(*ForgotPasswordIdentifiers.LOGIN).text
        if confirmation_text == "Log in":
            print(confirmation_text)
        return CanonizerForgotPage(self.driver)

    def enter_valid_otp(self, email):
        time.sleep(3)
        self.enter_email(email)
        self.click_submit_button()
        self.find_element(*ForgotPasswordIdentifiers.OTP_ENTER).click()
        " Enter OTP manually"
        time.sleep(22)
        self.click_otp_submit_button()
        confirmation_text = self.find_element(*ForgotPasswordIdentifiers.CHANGE_PASSWORD_TITLE).text
        if confirmation_text == 'Create new password':
            print(confirmation_text)
            return CanonizerForgotPage(self.driver)
        else:
            print("Text is not matching")




