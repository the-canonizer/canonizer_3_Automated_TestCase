from Identifiers import ProfileInfoIdentifiersPage


class CanonizerAccountSettingPage(Page):

    def click_account_settings_page_button(self):
        """
        This function is to click on the Account Settings button

        -> Hover to the Account Settings button
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
        self.hover(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*ProfileInfoIdentifiersPage.ACCOUNT_SETTING_BUTTON).click()
        return CanonizerAccountSettingPage(self.driver)

    def verifying_profile_button(self):
        self.hover(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*ProfileInfoIdentifiersPage.ACCOUNT_SETTING_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.hover(*ProfileInfoIdentifiersPage.PROFILE_BUTTON)
        self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verifying_social_oauth_verification(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.SOCIAL_OAUTH_VERIFICATION)
        self.find_element(*ProfileInfoIdentifiersPage.SOCIAL_OAUTH_VERIFICATION).click()
        res = self.find_element(*ProfileInfoIdentifiersPage.SOCIAL_OAUTH_VERIFICATION).text
        if res == 'Social Oauth Verification':
            return CanonizerAccountSettingPage(self.driver)

    def verifying_change_password(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.CHANGE_PASSWORD)
        self.find_element(*ProfileInfoIdentifiersPage.CHANGE_PASSWORD).click()
        title = self.find_element(*ProfileInfoIdentifiersPage.CHANGE_PASSWORD).text
        if title == 'Change Password':
            return CanonizerAccountSettingPage(self.driver)

    def verifying_nick_name(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.NICK_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.NICK_NAME).click()
        title = self.find_element(*ProfileInfoIdentifiersPage.NICK_NAME).text
        if title == 'Nick Names':
            return CanonizerAccountSettingPage(self.driver)

    def verifying_supported_camps(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.SUPPORTED_CAMPS)
        self.find_element(*ProfileInfoIdentifiersPage.SUPPORTED_CAMPS).click()
        title = self.find_element(*ProfileInfoIdentifiersPage.SUPPORTED_CAMPS).text
        if title == 'Supported Camps':
            return CanonizerAccountSettingPage(self.driver)

    def check_the_validation_for_phone_number_field(self, number):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.PROFILE_BUTTON)
        self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.PHONE_NUMBER)
        self.find_element(*ProfileInfoIdentifiersPage.PHONE_NUMBER).send_keys(number)
        title = self.find_element(*ProfileInfoIdentifiersPage.PHONE_NUMBER_ERROR).text
        if title == 'Phone number must be at least 10 digits!':
            return CanonizerAccountSettingPage(self.driver)

    def check_the_functionality_of_verify_button_without_entering_the_data(self):
        self.click_account_settings_page_button()
        self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.PHONE_NUMBER)
        self.hover(*ProfileInfoIdentifiersPage.MOBILE_CARRIER)
        self.find_element(*ProfileInfoIdentifiersPage.VERIFY_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_the_functionality_of_mobile_carrier_drop_down(self):
        self.click_account_settings_page_button()
        self.find_element(*ProfileInfoIdentifiersPage.PROFILE_BUTTON).click()
        self.hover(*ProfileInfoIdentifiersPage.MOBILE_CARRIER)
        self.hover(*ProfileInfoIdentifiersPage.MOBILE_CARRIER)
        self.find_element(*ProfileInfoIdentifiersPage.MOBILE_CARRIER).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_all_the_fields_are_present_in_personal_information_field(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.FIRST_NAME)
        self.hover(*ProfileInfoIdentifiersPage.MIDDLE_NAME)
        self.hover(*ProfileInfoIdentifiersPage.LAST_NAME)
        self.hover(*ProfileInfoIdentifiersPage.GENDER)

        return CanonizerAccountSettingPage(self.driver)

    def verify_the_validation_for_first_name(self, first):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.FIRST_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).click()
        self.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).send_keys(first)
        self.find_element(*ProfileInfoIdentifiersPage.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def update_the_first_name_and_check_if_it_is_updating_same_for_username(self, first_name):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.FIRST_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).click()
        self.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).send_keys(first_name)
        self.find_element(*ProfileInfoIdentifiersPage.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_the_functionality_of_radio_button_in_selecting_the_gender(self):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.GENDER)
        self.find_element(*ProfileInfoIdentifiersPage.GENDER).click()
        self.find_element(*ProfileInfoIdentifiersPage.UPDATE_BUTTON).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_when_user_updated_the_personal_information_and_logs_out_and_login_again(self, first, middle, last):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.FIRST_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).send_keys(first)
        self.find_element(*ProfileInfoIdentifiersPage.MIDDLE_NAME).send_keys(middle)
        self.find_element(*ProfileInfoIdentifiersPage.LAST_NAME).send_keys(last)
        self.find_element(*ProfileInfoIdentifiersPage.GENDER).click()
        self.find_element(*ProfileInfoIdentifiersPage.UPDATE_BUTTON).click()
        self.find_element(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*ProfileInfoIdentifiersPage.LOGOUT).click()

        return CanonizerAccountSettingPage(self.driver)

    def verify_the_spaces_are_trimmed_in_the_firstname_lastname_middlename_fields(self, first, middle, last):
        self.click_account_settings_page_button()
        self.hover(*ProfileInfoIdentifiersPage.FIRST_NAME)
        self.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).clear()
        self.find_element(*ProfileInfoIdentifiersPage.FIRST_NAME).send_keys(first)
        self.find_element(*ProfileInfoIdentifiersPage.MIDDLE_NAME).send_keys(middle)
        self.find_element(*ProfileInfoIdentifiersPage.LAST_NAME).send_keys(last)
        self.find_element(*ProfileInfoIdentifiersPage.GENDER).click()
        self.find_element(*ProfileInfoIdentifiersPage.UPDATE_BUTTON).click()
        self.find_element(*ProfileInfoIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*ProfileInfoIdentifiersPage.LOGOUT).click()

        return CanonizerAccountSettingPage(self.driver)
