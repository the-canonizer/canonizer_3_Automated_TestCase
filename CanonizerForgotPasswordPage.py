import CanonizerValidationCheckMessages
from CanonizerBase import Page
from Identifiers import ForgotPasswordIdentifiers
from selenium import webdriver


class CanonizerForgotPasswordPage(Page):

    def click_forgot_password_link(self):
        self.find_element(*ForgotPasswordIdentifiers.LOGIN).click()
        self.hover(*ForgotPasswordIdentifiers.FORGOT_PASSWORD_LINK)
        self.find_element(*ForgotPasswordIdentifiers.FORGOT_PASSWORD_LINK).click()
        self.hover(*ForgotPasswordIdentifiers.FORGOT_PASSWORD_TITLE)
        label = self.find_element(*ForgotPasswordIdentifiers.FORGOT_PASSWORD_TITLE).text
        if label == CanonizerValidationCheckMessages.FORGOT_PASSWORD_PAGE_HEADING:
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Confirmation text is not matching")

    def login_and_forgot_password(self):
        self.hover(*ForgotPasswordIdentifiers.LOGIN)
        self.find_element(*ForgotPasswordIdentifiers.LOGIN).click()
        self.hover(*ForgotPasswordIdentifiers.FORGOT_PASSWORD_LINK)
        self.find_element(*ForgotPasswordIdentifiers.FORGOT_PASSWORD_LINK).click()
        return CanonizerForgotPasswordPage(self.driver)

    def enter_email(self, email):
        self.hover(*ForgotPasswordIdentifiers.EMAIL)
        self.find_element(*ForgotPasswordIdentifiers.EMAIL).send_keys(email)

    def click_submit_button(self):
        self.hover(*ForgotPasswordIdentifiers.SUBMIT_BUTTON)
        self.find_element(*ForgotPasswordIdentifiers.SUBMIT_BUTTON).click()

    def click_otp_submit_button(self):
        self.hover(*ForgotPasswordIdentifiers.SUBMIT_OTP_BUTTON)
        self.find_element(*ForgotPasswordIdentifiers.SUBMIT_OTP_BUTTON).click()

    def submit(self, email):
        self.enter_email(email)
        self.click_submit_button()
        title = self.find_element(*ForgotPasswordIdentifiers.OTP_PAGE_TITLE).text
        if title == CanonizerValidationCheckMessages.PASSWORD_VERIFICATION_TITLE:
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Title is not matching")

    def click_submit_button_with_valid_email(self, email):
        self.submit(email)
        return CanonizerForgotPasswordPage(self.driver)

    def click_submit_button_with_invalid_email(self, email):
        self.enter_email(email)
        self.click_submit_button()
        self.hover(*ForgotPasswordIdentifiers.INVALID_EMAIL)
        error = self.find_element(*ForgotPasswordIdentifiers.INVALID_EMAIL).text
        if error == CanonizerValidationCheckMessages.INVALID_EMAIL_ERROR:
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Error not found or not matching")

    def click_submit_button_with_empty_email(self, email):
        self.enter_email(email)
        self.click_submit_button()
        self.hover(*ForgotPasswordIdentifiers.INVALID_EMAIL)
        error = self.find_element(*ForgotPasswordIdentifiers.INVALID_EMAIL).text
        if error == CanonizerValidationCheckMessages.EMPTY_EMAIL_ERROR:
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Error not found or not matching")

    def submit_empty_otp(self, email):
        self.enter_email(email)
        self.click_submit_button()
        self.hover(*ForgotPasswordIdentifiers.OTP_ENTER)
        self.find_element(*ForgotPasswordIdentifiers.OTP_ENTER).click()
        self.click_otp_submit_button()
        self.hover(*ForgotPasswordIdentifiers.EMPTY_OTP)
        error = self.find_element(*ForgotPasswordIdentifiers.EMPTY_OTP).text
        if error == CanonizerValidationCheckMessages.EMPTY_OTP_ERROR:
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Error not found or not matching")

    def submit_invalid_otp(self, email, otp):
        self.enter_email(email)
        self.click_submit_button()
        self.hover(*ForgotPasswordIdentifiers.OTP_ENTER)
        self.find_element(*ForgotPasswordIdentifiers.OTP_ENTER).send_keys(otp)
        self.click_otp_submit_button()
        self.hover(*ForgotPasswordIdentifiers.INVALID_OTP)
        error = self.find_element(*ForgotPasswordIdentifiers.INVALID_OTP).text
        if error == CanonizerValidationCheckMessages.INVALID_OTP_ERROR:
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Error not found or not matching")

    def cross_icon_on_forgot_page(self):
        self.find_element(*ForgotPasswordIdentifiers.CROSS_ICON_FORGOT_MODAL).click()
        confirmation_text = self.find_element(*ForgotPasswordIdentifiers.LOGIN).text
        if confirmation_text == CanonizerValidationCheckMessages.LOGIN_BUTTON_LABEL:
            return CanonizerForgotPasswordPage(self.driver)
        else:
            print("Text is not matching or not found")







