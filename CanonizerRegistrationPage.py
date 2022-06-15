import time
from time import sleep

from CanonizerBase import Page
from Identifiers import RegistrationPageIdentifiers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


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

        self.hover(*RegistrationPageIdentifiers.REGISTER)
        self.find_element(*RegistrationPageIdentifiers.REGISTER).click()
        return CanonizerRegisterPage(self.driver)

    def enter_first_name(self, firstname):
        print(firstname,"First name")
        self.find_element(*RegistrationPageIdentifiers.FIRST_NAME).send_keys(firstname)

    def enter_last_name(self, lastname,):
        self.find_element(*RegistrationPageIdentifiers.LAST_NAME).send_keys(lastname)

    def enter_email(self, user):
        self.find_element(*RegistrationPageIdentifiers.EMAIL).send_keys(user)

    def enter_password(self, password):
        self.find_element(*RegistrationPageIdentifiers.PASSWORD).send_keys(password)

    def enter_confirm_password(self, confirmpassword):
        self.find_element(*RegistrationPageIdentifiers.CONFIRM_PASSWORD).send_keys(confirmpassword)

    def click_create_account_button(self):
        """
        This function clicks the Create Account Button
        :return:
        """
        self.find_element(*RegistrationPageIdentifiers.CREATE_ACCOUNT).click()

    def register(self, *args):
        self.enter_first_name(args[0])
        self.enter_last_name(args[1])
        self.enter_email(args[2])
        self.enter_password(args[3])
        self.enter_confirm_password(args[4])
        time.sleep(5)
        self.click_create_account_button()

    def registration_with_blank_first_name(self, REG_LIST_3):
        self.register(REG_LIST_3[0], REG_LIST_3[1], REG_LIST_3[2], REG_LIST_3[3], REG_LIST_3[4])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_FIRST_NAME).text
        print(error)
        if error == 'Please input your first name!':
            return CanonizerRegisterPage(self.driver)

    def registration_with_blank_last_name(self, REG_LIST_4):
        self.register(REG_LIST_4[0], REG_LIST_4[1], REG_LIST_4[2], REG_LIST_4[3], REG_LIST_4[4])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_LAST_NAME).text
        print(error)
        if error == 'Please input your last name!':
            return CanonizerRegisterPage(self.driver)

    def registration_with_blank_email(self, REG_LIST_5):
        self.register(REG_LIST_5[0], REG_LIST_5[1], REG_LIST_5[2], REG_LIST_5[3], REG_LIST_5[4])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_EMAIL).text
        print(error)
        if error == 'Please input your E-mail!.':
            return CanonizerRegisterPage(self.driver)

    def registration_with_blank_password(self, REG_LIST_6):
        self.register(REG_LIST_6[0], REG_LIST_6[1], REG_LIST_6[2], REG_LIST_6[3], REG_LIST_6[4])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_PASSWORD).text
        print(error)
        if error == 'Please input your password!.':
            return CanonizerRegisterPage(self.driver)

    def registration_with_invalid_password_length(self, REG_LIST_7):
        self.register(REG_LIST_7[0], REG_LIST_7[1], REG_LIST_7[2], REG_LIST_7[3], REG_LIST_7[4])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_PASSWORD).text
        print(error)
        if error == 'Password must be contain small, capital letter, number and special character like Abc@1234.':
            return CanonizerRegisterPage(self.driver)

    def registration_with_different_confirmation_password(self, REG_LIST_8):
        self.register(REG_LIST_8[0], REG_LIST_8[1], REG_LIST_8[2], REG_LIST_8[3], REG_LIST_8[4])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_CONFIRMATION).text
        print(error)
        if error == 'Confirm Password does not match!':
            return CanonizerRegisterPage(self.driver)

    def registration_with_blank_spaces_first_name(self, REG_LIST_1):
        self.register(REG_LIST_1[0], REG_LIST_1[1], REG_LIST_1[2], REG_LIST_1[3], REG_LIST_1[4])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_FIRST_NAME).text
        print(error)
        if error == 'Please input your first name!.':
            return CanonizerRegisterPage(self.driver)

    def registration_with_invalid_first_name(self, REG_LIST_10):
        self.register(REG_LIST_10[0], REG_LIST_10[1], REG_LIST_10[2], REG_LIST_10[3], REG_LIST_10[4])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_FIRST_NAME).text
        print(error)
        if error == 'The first name should only contain alphabets and spaces.':
            return CanonizerRegisterPage(self.driver)

    def registration_with_invalid_last_name(self, REG_LIST_11):
        self.register(REG_LIST_11[0], REG_LIST_11[1], REG_LIST_11[2], REG_LIST_11[3], REG_LIST_11[4])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_LAST_NAME).text
        print(error)
        if error == 'The last name should only contain alphabets and spaces.':
            return CanonizerRegisterPage(self.driver)

    def registration_with_invalid_email(self, REG_LIST_14):
        self.register(REG_LIST_14[0], REG_LIST_14[1], REG_LIST_14[2], REG_LIST_14[3], REG_LIST_14[4])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_EMAIL).text
        print(error)
        if error == 'The input is not valid E-mail!':
            return CanonizerRegisterPage(self.driver)

    def click_on_register_button(self):
        self.find_element(*RegistrationPageIdentifiers.REGISTER).click()
        tittle = self.find_element(*RegistrationPageIdentifiers.TITLE).text
        print(tittle)
        if tittle == 'Register Now on Canonizer':
            return CanonizerRegisterPage(self.driver)

    def check_login_page_open_click_login_here_link(self):
        self.find_element(*RegistrationPageIdentifiers.REGISTER).click()
        time.sleep(5)
        self.find_element(*RegistrationPageIdentifiers.LOGIN).click()
        time.sleep(5)
        tittle = self.find_element(*RegistrationPageIdentifiers.LOGIN_TITTLE).text
        print(tittle)
        if tittle == 'Log in to Canonizer':
            return CanonizerRegisterPage(self.driver)

    def Verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(self,REG_LIST_15):
        self.register(REG_LIST_15[0], REG_LIST_15[1], REG_LIST_15[2], REG_LIST_15[3], REG_LIST_15[4])
        return CanonizerRegisterPage(self.driver)


