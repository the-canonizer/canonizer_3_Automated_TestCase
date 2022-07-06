from CanonizerBase import Page
from Identifiers import ForgotPasswordIdentifiers
from selenium import webdriver


class CanonizerForgotPasswordPage(Page):

    def click_forgot_password_link(self):
        self.find_element(*ForgotPasswordIdentifiers.LOGIN).click()
        self.hover(*ForgotPasswordIdentifiers.FORGOTPASSWORDLINK)
        self.find_element(*ForgotPasswordIdentifiers.FORGOTPASSWORDLINK).click()
        self.hover(*ForgotPasswordIdentifiers.FIELD_LABEL)
        label = self.find_element(*ForgotPasswordIdentifiers.FIELD_LABEL).text
        if label == 'Email ID*':
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Confirmation text is not matching")

    def login_and_forgot_password(self):
        self.hover(*ForgotPasswordIdentifiers.LOGIN)
        self.find_element(*ForgotPasswordIdentifiers.LOGIN).click()
        self.hover(*ForgotPasswordIdentifiers.FORGOTPASSWORDLINK)
        self.find_element(*ForgotPasswordIdentifiers.FORGOTPASSWORDLINK).click()
        return CanonizerForgotPasswordPage(self.driver)

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
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Title is not matching")

    def click_submit_button_with_valid_email(self, email):
        self.submit(email)
        return CanonizerForgotPasswordPage(self.driver)

    def click_submit_button_with_invalid_email(self, email):
        self.enter_email(email)
        self.click_submit_button()
        self.hover(*ForgotPasswordIdentifiers.INVALIDEMAIL_ERROR)
        error = self.find_element(*ForgotPasswordIdentifiers.INVALIDEMAIL_ERROR).text
        if error == 'The input is not valid E-mail!':
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Error not found or not matching")

    def click_submit_button_with_empty_email(self, email):
        self.enter_email(email)
        self.click_submit_button()
        self.hover(*ForgotPasswordIdentifiers.INVALIDEMAIL_ERROR)
        error = self.find_element(*ForgotPasswordIdentifiers.INVALIDEMAIL_ERROR).text
        if error == 'Please input your E-mail!':
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Error not found or not matching")

    def submit_empty_otp(self, email):
        self.enter_email(email)
        self.click_submit_button()
        self.hover(*ForgotPasswordIdentifiers.OTP_ENTER)
        self.find_element(*ForgotPasswordIdentifiers.OTP_ENTER).click()
        self.click_otp_submit_button()
        self.hover(*ForgotPasswordIdentifiers.OTP_EMPTY_ERROR)
        error = self.find_element(*ForgotPasswordIdentifiers.OTP_EMPTY_ERROR).text
        if error == 'Please input your OTP!':
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Error not found or not matching")

    def submit_invalid_otp(self, email, otp):
        self.enter_email(email)
        self.click_submit_button()
        self.hover(*ForgotPasswordIdentifiers.OTP_ENTER)
        self.find_element(*ForgotPasswordIdentifiers.OTP_ENTER).send_keys(otp)
        self.click_otp_submit_button()
        error = self.find_element(*ForgotPasswordIdentifiers.INVALID_OTP_ERROR).text
        if error == 'OTP should be min/max 6 characters long!':
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Error not found or not matching")

    def cross_icon_on_forgot_page(self):
        self.find_element(*ForgotPasswordIdentifiers.CROSS_ICON_FORGOT_MODAL).click()
        confirmation_text = self.find_element(*ForgotPasswordIdentifiers.LOGIN).text
        if confirmation_text == "Log in":
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Text is not matching or not found")

    def cross_icon_on_otp_page(self, email):
        self.enter_email(email)
        self.click_submit_button()
        self.hover(*ForgotPasswordIdentifiers.CROSS_ICON_OTP_MODAL)
        self.find_element(*ForgotPasswordIdentifiers.CROSS_ICON_OTP_MODAL).click()
        confirmation_text = self.find_element(*ForgotPasswordIdentifiers.LOGIN).text
        if confirmation_text == "Log in":
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Text is not matching or not found")






