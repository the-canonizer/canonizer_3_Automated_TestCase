from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CanonizerBase import Page
from Config import REG_LIST_3
from Identifiers import RegistrationPageIdentifiers


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

    def register_page_mandatory_fields_are_marked_with_asterisk(self):
        """
        This Function checks, if Mandatory fields on Register Page Marked with *
        First Name, Last Name, Email, Password, Confirm Password are Mandatory Fields

        :return: the element value
        """
        return \
            self.find_element(*RegistrationPageIdentifiers.FIRST_NAME_ASTRK) and \
            self.find_element(*RegistrationPageIdentifiers.LAST_NAME_ASTRK) and \
            self.find_element(*RegistrationPageIdentifiers.EMAIL_ASTRK) and \
            self.find_element(*RegistrationPageIdentifiers.PASSWORD_ASTRK) and \
            self.find_element(*RegistrationPageIdentifiers.CONFIRM_PASSWORD_ASTRK)

    def enter_first_name(self, firstname):
        self.find_element(*RegistrationPageIdentifiers.FIRST_NAME).send_keys(firstname)

    def enter_last_name(self, lastname, ):
        self.find_element(*RegistrationPageIdentifiers.LAST_NAME).send_keys(lastname)

    def enter_email(self, user):
        self.find_element(*RegistrationPageIdentifiers.EMAIL).send_keys(user)

    def enter_mobile_number(self, mobile_number):
        self.find_element(*RegistrationPageIdentifiers.MOBILE_NUMBER).send_keys(mobile_number)

    def enter_password(self, password):
        self.find_element(*RegistrationPageIdentifiers.PASSWORD).send_keys(password)

    def enter_confirm_password(self, confirmpassword):
        self.find_element(*RegistrationPageIdentifiers.CONFIRM_PASSWORD).send_keys(confirmpassword)

    def click_register_now_button(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'ant-btn ant-btn-primary ant-btn-block login-form-button')))
        except TimeoutException:
            pass
        self.find_element(*RegistrationPageIdentifiers.REGISTER_NOW).click()

    def register(self, *args):
        self.enter_first_name(args[0])
        self.enter_last_name(args[1])
        self.enter_email(args[2])
        self.enter_mobile_number(args[3])
        self.enter_password(args[4])
        self.enter_confirm_password(args[5])
        self.click_register_now_button()

    def registration_with_blank_first_name(self,REG_LIST_3):
        self.register(REG_LIST_3[0], REG_LIST_3[1], REG_LIST_3[2], REG_LIST_3[3], REG_LIST_3[4], REG_LIST_3[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_FIRST_NAME).text
        if error == 'Please input your first name!':
            return CanonizerRegisterPage(self.driver)
        else:
            print('title not found')

    def registration_with_blank_last_name(self, REG_LIST_4):
        self.register(REG_LIST_4[0], REG_LIST_4[1], REG_LIST_4[2], REG_LIST_4[3], REG_LIST_4[4], REG_LIST_4[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_LAST_NAME).text
        if error == 'Please input your last name!':
            return CanonizerRegisterPage(self.driver)
        else:
            print("title not found")

    def registration_with_blank_email(self, REG_LIST_5):
        self.register(REG_LIST_5[0], REG_LIST_5[1], REG_LIST_5[2], REG_LIST_5[3], REG_LIST_5[4], REG_LIST_5[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_EMAIL).text
        if error == 'Please input your E-mail!':
            return CanonizerRegisterPage(self.driver)
        else:
            print("title not found")

    def registration_with_blank_password(self, REG_LIST_6):
        self.register(REG_LIST_6[0], REG_LIST_6[1], REG_LIST_6[2], REG_LIST_6[3], REG_LIST_6[4], REG_LIST_6[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_PASSWORD).text
        if error == 'Please input your password!':
            return CanonizerRegisterPage(self.driver)

    def registration_with_invalid_password_length(self, REG_LIST_7):
        self.register(REG_LIST_7[0], REG_LIST_7[1], REG_LIST_7[2], REG_LIST_7[3], REG_LIST_7[4], REG_LIST_7[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_PASSWORD).text
        if error == 'Password must contain small, capital letter, number and special character like Abc@1234.':
            return CanonizerRegisterPage(self.driver)
        else:
            print('title not found')

    def registration_with_different_confirmation_password(self, REG_LIST_8):
        self.register(REG_LIST_8[0], REG_LIST_8[1], REG_LIST_8[2], REG_LIST_8[3], REG_LIST_8[4], REG_LIST_8[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_CONFIRMATION_PASSWORD).text
        if error == 'Confirm Password does not match!':
            return CanonizerRegisterPage(self.driver)
        else:
            print("title not found")

    def registration_with_blank_spaces_first_name(self, REG_LIST_1):
        self.register(REG_LIST_1[0], REG_LIST_1[1], REG_LIST_1[2], REG_LIST_1[3], REG_LIST_1[4], REG_LIST_1[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_FIRST_NAME).text
        if error == 'Please input your first name!':
            return CanonizerRegisterPage(self.driver)
        else:
            print("title not found")

    def registration_with_invalid_first_name(self, REG_LIST_10):
        self.register(REG_LIST_10[0], REG_LIST_10[1], REG_LIST_10[2], REG_LIST_10[3], REG_LIST_10[4], REG_LIST_10[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_FIRST_NAME).text
        if error == 'The first name should only contain alphabets and spaces.':
            return CanonizerRegisterPage(self.driver)
        else:
            print("title not found")

    def registration_with_invalid_last_name(self, REG_LIST_11):
        self.register(REG_LIST_11[0], REG_LIST_11[1], REG_LIST_11[2], REG_LIST_11[3], REG_LIST_11[4], REG_LIST_11[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_LAST_NAME).text
        if error == 'The last name should only contain alphabets and spaces.':
            return CanonizerRegisterPage(self.driver)

    def registration_with_invalid_email(self, REG_LIST_14):
        self.register(REG_LIST_14[0], REG_LIST_14[1], REG_LIST_14[2], REG_LIST_14[3], REG_LIST_14[4], REG_LIST_14[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_EMAIL).text
        if error == 'The input is not valid E-mail!':
            return CanonizerRegisterPage(self.driver)
        else:
            print("title not found")

    def verify_the_functionality_of_registration_with_entering_data_in_mandatory_fields(self, REG_LIST_15):
        self.register(REG_LIST_15[0], REG_LIST_15[1], REG_LIST_15[2], REG_LIST_15[3], REG_LIST_15[4], REG_LIST_15[5])

        return CanonizerRegisterPage(self.driver)

    def verify_the_functionality_0f_registration_with_entering_data_in_mobile_number_field(self, REG_LIST_16):
        self.register(REG_LIST_16[0], REG_LIST_16[1], REG_LIST_16[2], REG_LIST_16[3], REG_LIST_16[4], REG_LIST_16[5])
        error = self.find_element(*RegistrationPageIdentifiers.ERROR_MOBILE_NUMBER).text
        if error == 'Phone number must be at least 10 digits!':
            return CanonizerRegisterPage(self.driver)
        else:
            print("title not found")

        return CanonizerRegisterPage(self.driver)

    def check_login_page_open_click_login_here_link(self):
        self.find_element(*RegistrationPageIdentifiers.REGISTER).click()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-typography Registration_ft_link__tyQ1C')))
        except TimeoutException:
            pass
        self.hover(*RegistrationPageIdentifiers.LOGIN_HERE)
        self.find_element(*RegistrationPageIdentifiers.LOGIN_HERE).click()
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-typography Login_titles__nmC2y')))
        except TimeoutException:
            pass
        title = self.find_element(*RegistrationPageIdentifiers.LOGIN_TITLE).text
        if title == 'Login to Canonizer':
            return CanonizerRegisterPage(self.driver)
        else:
            print("title not found")

    def click_on_register_button(self):
        self.find_element(*RegistrationPageIdentifiers.REGISTER).click()
        self.hover(*RegistrationPageIdentifiers.TITLE)
        title = self.find_element(*RegistrationPageIdentifiers.TITLE).text
        if title == 'Register Now on Canonizer':
            return CanonizerRegisterPage(self.driver)
