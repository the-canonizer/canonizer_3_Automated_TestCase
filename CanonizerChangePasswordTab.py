from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from CanonizerBase import Page
from CanonizerValidationCheckMessages import message
from Identifiers import CanonizerChangePasswordIdentifierPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CanonizerChangePasswordTab(Page):

    def verifying_astrk_present_in_change_password_tab(self):
        """
                This Function checks, if Mandatory fields on change password tab Page Marked with *
                current password,new password, Confirm Password are Mandatory Fields

                :return: the element value
                """
        return \
            self.find_element(*CanonizerChangePasswordIdentifierPage.CURRENT_ASTRK) and \
            self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_ASTRK) and \
            self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_ASTRK)

    def click_account_settings(self):
        self.hover(*CanonizerChangePasswordIdentifierPage.CLICK_ON_DROPDOWN)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.ACCOUNT_SETTING_BUTTON).click()
        return CanonizerChangePasswordTab(self.driver)

    def verify_click_on_change_password_tab_its_navigating_to_change_password_page(self):
        self.click_account_settings()
        self.hover(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD).click()
        try:
            WebDriverWait(self.driver, 6).until(
                EC.visibility_of_element_located((By.ID, 'saveBtn')))
        except TimeoutException:
            pass
        self.hover(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON)
        title = self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).text
        if title == message['Change_Password']['SAVE_BUTTON']:
            return CanonizerChangePasswordTab(self.driver)
        else:
            print("title not found")

    def verify_the_current_field_empty_and_click_on_save(self):
        self.verify_click_on_change_password_tab_its_navigating_to_change_password_page()
        self.hover(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD).click()
        self.hover(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON)
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()
        self.hover(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD_ERROR)
        title = self.find_element(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD_ERROR).text
        if title == message['Change_Password']['CURRENT_PASSWORD_ERROR']:
            return CanonizerChangePasswordTab(self.driver)
        else:
            print("title not found")

    def verify_the_new_password_field_empty_and_click_on_save(self):
        self.verify_click_on_change_password_tab_its_navigating_to_change_password_page()
        self.hover(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD).click()
        self.hover(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON)
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()
        self.hover(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD_ERROR)
        title = self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD_ERROR).text
        if title == message['Change_Password']['NEW_PASSWORD_ERROR']:
            return CanonizerChangePasswordTab(self.driver)
        else:
            print("title not found")

    def verify_the_confirm_password_field_empty_and_click_on_save(self):
        self.verify_click_on_change_password_tab_its_navigating_to_change_password_page()
        self.hover(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD).click()
        self.hover(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON)
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()
        self.hover(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD_ERROR)
        title = self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD_ERROR).text
        if title == message['Change_Password']['ERROR_CONFIRM_PASSWORD']:
            return CanonizerChangePasswordTab(self.driver)
        else:
            print("title not found")

    def verify_entering_the_invalid_new_password(self, INVALID_NEW_PASSWORD):
        self.verify_click_on_change_password_tab_its_navigating_to_change_password_page()
        self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD).send_keys(INVALID_NEW_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()
        title = self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD_ERROR).text
        if title == message['Change_Password']['ERROR_NEW_PASSWORD']:
            return CanonizerChangePasswordTab(self.driver)
        else:
            print("Error message not found")

    def verify_entering_the_invalid_current_password(self, INVALID_CURRENT_PASSWORD):
        self.verify_click_on_change_password_tab_its_navigating_to_change_password_page()
        self.hover(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD).send_keys(
            INVALID_CURRENT_PASSWORD)
        self.hover(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON)
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()
        error = self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD_ERROR).text
        if error == message['Change_Password']['CONFIRM_PASSWORD_ERROR']:
            return CanonizerChangePasswordTab(self.driver)
        else:
            print("Error message not found")

    def verify_current_password_new_password_confirm_password_is_present_save_button(self):
        self.verify_click_on_change_password_tab_its_navigating_to_change_password_page()
        self.find_element(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()

        return CanonizerChangePasswordTab(self.driver)

    def verify_when_both_new_password_and_confirm_password_does_not_match(self, DEFAULT_NEW_PASSWORD,
                                                                          DEFAULT_CONFIRM_PASSWORD):
        self.verify_click_on_change_password_tab_its_navigating_to_change_password_page()
        self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD).send_keys(DEFAULT_NEW_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD).send_keys(DEFAULT_CONFIRM_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()
        title = self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD_ERROR).text
        if title == message['Change_Password']['CONFIRM_PASSWORD_ERROR']:
            return CanonizerChangePasswordTab(self.driver)
        else:
            print("Error message not found")










