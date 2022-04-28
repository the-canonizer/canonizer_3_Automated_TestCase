import time
from time import sleep

from CanonizerBase import Page
from Identifiers import RegisterPageIdentifiers


class CanonizerRegisterPage(Page):
    """
        Class Name: CanonizerRegisterPage

        """

    def click_register_button(self):
        """
        -> Hover the control towards the register button. Identifiers are loaded from Identifiers Class
        -> Find the register button and Click on it.

        :return:
            Return the control to the main Program
        """

        self.hover(*RegisterPageIdentifiers.CLICK_REGISTER_BUTTON)
        self.find_element(*RegisterPageIdentifiers.CLICK_REGISTER_BUTTON).click()
        return CanonizerRegisterPage(self.driver)

    def click_register_page_and_enter_fields_with_valid_data(self, first, last, email, password, confirm_password):
        self.click_register_button()
        self.find_element(*RegisterPageIdentifiers.FIRST_NAME).send_keys(first)
        self.find_element(*RegisterPageIdentifiers.LAST_NAME).send_keys(last)
        self.find_element(*RegisterPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*RegisterPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*RegisterPageIdentifiers.CONFIRM_PASSWORD).send_keys(confirm_password)
        sleep(3)
        self.find_element(*RegisterPageIdentifiers.REGISTER_NOW).click()
        return CanonizerRegisterPage(self.driver)

    def click_on_close_icon_register_page(self):
        self.click_register_button()
        sleep(3)
        self.hover(*RegisterPageIdentifiers.CLOSE_ICON)
        self.find_element(*RegisterPageIdentifiers.CLOSE_ICON).click()
        return CanonizerRegisterPage(self.driver)

    def craete_canonizer_register_page_without_entering_data(self, first, last, email, password, confirm_password):
        self.click_register_button()
        self.find_element(*RegisterPageIdentifiers.FIRST_NAME).send_keys(first)
        self.find_element(*RegisterPageIdentifiers.LAST_NAME).send_keys(last)
        self.find_element(*RegisterPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*RegisterPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*RegisterPageIdentifiers.CONFIRM_PASSWORD).send_keys(confirm_password)
        self.find_element(*RegisterPageIdentifiers.REGISTER_NOW).click()
        return CanonizerRegisterPage(self.driver)

    def create_canonizer_register_page_entering_with_invalid_data(self, first, last, email, password, confirm_password):
        self.click_register_button()
        self.find_element(*RegisterPageIdentifiers.FIRST_NAME).send_keys(first)
        self.find_element(*RegisterPageIdentifiers.LAST_NAME).send_keys(last)
        self.find_element(*RegisterPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*RegisterPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*RegisterPageIdentifiers.CONFIRM_PASSWORD).send_keys(confirm_password)
        self.find_element(*RegisterPageIdentifiers.REGISTER_NOW).click()
        return CanonizerRegisterPage(self.driver)

    def create_canonizer_page_with_existed_data(self, first, last, email, password, confirm_password):
        self.click_register_button()
        self.find_element(*RegisterPageIdentifiers.FIRST_NAME).send_keys(first)
        self.find_element(*RegisterPageIdentifiers.LAST_NAME).send_keys(last)
        self.find_element(*RegisterPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*RegisterPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*RegisterPageIdentifiers.CONFIRM_PASSWORD).send_keys(confirm_password)
        sleep(3)
        self.hover(*RegisterPageIdentifiers.REGISTER_NOW)
        self.find_element(*RegisterPageIdentifiers.REGISTER_NOW).click()
        sleep(4)
        return CanonizerRegisterPage(self.driver)

    def create_registration_page_without_entering_in_one_mandatary_field(self, first, email, password,
                                                                         confirm_password):
        self.click_register_button()
        self.find_element(*RegisterPageIdentifiers.FIRST_NAME).send_keys(first)
        self.find_element(*RegisterPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*RegisterPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*RegisterPageIdentifiers.CONFIRM_PASSWORD).send_keys(confirm_password)
        self.find_element(*RegisterPageIdentifiers.REGISTER_NOW).click()
        return CanonizerRegisterPage(self.driver)

    def registration_title_identification(self):
        self.click_register_button()
        self.hover(*RegisterPageIdentifiers.TITLE)
        sleep(3)
        title = self.find_element(*RegisterPageIdentifiers.TITLE).text
        print(title)
        if title == 'Register Now on Canonizer':
            return CanonizerRegisterPage(self.driver)

    def verify_firstname_empty(self, Name):
        self.click_register_button()
        self.hover(*RegisterPageIdentifiers.FNAME_HEADING)
        title = self.find_element(*RegisterPageIdentifiers.FNAME).text
        print(title)
        self.find_element(*RegisterPageIdentifiers.FIRST_NAME).send_keys(Name)
        self.find_element(*RegisterPageIdentifiers.LAST_NAME).click()
        # self.find_element(*RegistrationPageIdentifiers.Register_now).click()
        # self.hover(*RegistrationPageIdentifiers.error)
        err = self.find_element(*RegisterPageIdentifiers.error).text
        print(err)
        if err == 'Please input your first name!':
            return CanonizerRegisterPage(self.driver)

    def verify_all_fields_empty(self):
        self.click_register_button()
        self.find_element(*RegisterPageIdentifiers.REGISTER_NOW).click()
        self.hover(*RegisterPageIdentifiers.error)
        err = self.find_element(*RegisterPageIdentifiers.error).text
        print(err)
        if err == 'Please input your first name!':
            return CanonizerRegisterPage(self.driver)

    def verify_invalid_password_format(self, fname, lname, email, password):
        self.click_register_button()
        self.hover(*RegisterPageIdentifiers.FNAME_HEADING)
        self.find_element(*RegisterPageIdentifiers.FIRST_NAME).send_keys(fname)
        self.find_element(*RegisterPageIdentifiers.LAST_NAME).send_keys(lname)
        self.find_element(*RegisterPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*RegisterPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*RegisterPageIdentifiers.REGISTER_NOW).click()
        # self.hover(*RegisterPageIdentifiers.INVALID_PASSWORD_ERROR)
        err = self.find_element(*RegisterPageIdentifiers.INVALID_PASSWORD_ERROR).text
        print("1234----")
        print(err)
        if err == 'Password must be contain small, capital letter, number and special character like Abc@1234.':
            return CanonizerRegisterPage(self.driver)

    def verify_invalid_confirm_password(self, fname, lname, email, password, confirm_password, ):
        self.click_register_button()
        self.hover(*RegisterPageIdentifiers.FNAME_HEADING)
        self.find_element(*RegisterPageIdentifiers.FIRST_NAME).send_keys(fname)
        self.find_element(*RegisterPageIdentifiers.LAST_NAME).send_keys(lname)
        self.find_element(*RegisterPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*RegisterPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*RegisterPageIdentifiers.CONFIRM_PASSWORD).send_keys(confirm_password)
        self.find_element(*RegisterPageIdentifiers.REGISTER_NOW).click()
        # self.hover(*RegisterPageIdentifiers.INVALID_CONFIRM_PASSWORD_ERROR)
        err = self.find_element(*RegisterPageIdentifiers.INVALID_CONFIRM_PASSWORD_ERROR).text
        print(err)
        if err == 'Confirm Password does not match!.':
            return CanonizerRegisterPage(self.driver)

    def verify_invalid_email_format(self, fname, lname, email, password, confirm_password):
        self.click_register_button()
        self.hover(*RegisterPageIdentifiers.FNAME_HEADING)
        self.find_element(*RegisterPageIdentifiers.FIRST_NAME).send_keys(fname)
        self.find_element(*RegisterPageIdentifiers.LAST_NAME).send_keys(lname)
        self.find_element(*RegisterPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*RegisterPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*RegisterPageIdentifiers.CONFIRM_PASSWORD).send_keys(confirm_password)
        self.find_element(*RegisterPageIdentifiers.REGISTER_NOW).click()
        # self.hover(*RegisterPageIdentifiers.INVALID_CONFIRM_PASSWORD_ERROR)
        err = self.find_element(*RegisterPageIdentifiers.EMAIL_INVALID_ERROR).text
        print(err)
        if err == 'The input is not valid E-mail!.':
            return CanonizerRegisterPage(self.driver)

    def verify_captcha_field(self, fname, lname, email, password, confirm_password):
        self.click_register_button()
        self.hover(*RegisterPageIdentifiers.FNAME_HEADING)
        self.find_element(*RegisterPageIdentifiers.FIRST_NAME).send_keys(fname)
        self.find_element(*RegisterPageIdentifiers.LAST_NAME).send_keys(lname)
        self.find_element(*RegisterPageIdentifiers.EMAIL).send_keys(email)
        self.find_element(*RegisterPageIdentifiers.PASSWORD).send_keys(password)
        self.find_element(*RegisterPageIdentifiers.CONFIRM_PASSWORD).send_keys(confirm_password)
        self.find_element(*RegisterPageIdentifiers.REGISTER_NOW).click()
        err = self.find_element(*RegisterPageIdentifiers.CAPTCHA_ERROR_MESSAGE).text
        print(err)
        if err == 'Please check the captcha!.':
            return CanonizerRegisterPage(self.driver)




