from CanonizerBase import Page
from Identifiers import CanonizerChangePasswordIdentifierPage


class CanonizerChangePasswordTab(Page):

    def click_account_settings(self):
        self.hover(*CanonizerChangePasswordIdentifierPage.CLICK_ON_DROPDOWN)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.ACCOUNT_SETTING_BUTTON).click()
        return CanonizerChangePasswordTab(self.driver)

    def verify_click_on_change_password_tab_its_navigating_to_change_password_page(self):
        self.click_account_settings()
        self.hover(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD).click()

        return CanonizerChangePasswordTab(self.driver)

    def verify_keeping_all_the_fields_empty_and_click_on_save(self):
        self.click_account_settings()
        self.hover(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD).click()
        self.hover(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD).click()
        self.hover(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD).click()
        self.hover(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD).click()
        self.hover(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON)
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()

        return CanonizerChangePasswordTab(self.driver)

    def verify_current_password_new_password_confirm_password_is_present_save_button(self):
        self.click_account_settings()
        self.hover(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()

        return CanonizerChangePasswordTab(self.driver)

    def verify_entering_the_invalid_new_password(self, INVALID_NEW_PASSWORD):
        self.click_account_settings()
        self.hover(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD).send_keys(INVALID_NEW_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()
        title = self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD_ERROR).text
        if title == 'Password must contain small, capital letter, number and special character like Abc@1234.':
            return CanonizerChangePasswordTab(self.driver)
        else:
            print('title not found')

    def verify_entering_the_invalid_current_password(self, INVALID_CURRENT_PASSWORD):
        self.click_account_settings()
        self.hover(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD).click()
        self.hover(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CURRENT_PASSWORD).send_keys(
            INVALID_CURRENT_PASSWORD)
        self.hover(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON)
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()
        return CanonizerChangePasswordTab(self.driver)

    def verify_when_both_new_password_and_confirm_password_does_not_match(self, DEFAULT_NEW_PASSWORD,
                                                                          DEFAULT_CONFIRM_PASSWORD):
        self.click_account_settings()
        self.hover(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.NEW_PASSWORD).send_keys(DEFAULT_NEW_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD).send_keys(DEFAULT_CONFIRM_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()
        title = self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD_ERROR).text
        if title == 'Confirm Password does not match.':
            return CanonizerChangePasswordTab(self.driver)
        else:
            print('title not found')

    def verify_entering_the_invalid_confirm_password(self, DEFAULT_INVALID_CONFIRM_PASSWORD):
        self.click_account_settings()
        self.hover(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.CHANGE_PASSWORD).click()
        self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD).send_keys(
            DEFAULT_INVALID_CONFIRM_PASSWORD)
        self.find_element(*CanonizerChangePasswordIdentifierPage.SAVE_BUTTON).click()
        title = self.find_element(*CanonizerChangePasswordIdentifierPage.CONFIRM_PASSWORD_ERROR).text
        if title == 'Confirm Password does not match.':
            return CanonizerChangePasswordTab(self.driver)
        else:
            print('title not found')
