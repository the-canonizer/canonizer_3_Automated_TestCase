from CanonizerBase import Page
from CanonizerValidationCheckMessages import message
from Identifiers import CanonizerManageNickNameIdentifiersPage


class CanonizerManageNickNameTab(Page):

    def click_account_settings_page(self):
        self.hover(*CanonizerManageNickNameIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ACCOUNT_SETTING_BUTTON).click()

    def verify_when_user_click_on_nick_name_tab(self):
        self.click_account_settings_page()
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.NICK_NAME).click()
        self.hover(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME)
        title = self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME).text
        if title == message['Nick_name_tab']['ADD_NEW_NICK_NAME']:
            return CanonizerManageNickNameTab(self.driver)
        else:
            print("Title not found")

    def verify_all_the_headers_in_nick_name_tab(self):
        self.verify_when_user_click_on_nick_name_tab()
        self.hover(*CanonizerManageNickNameIdentifiersPage.SERIAL_NUMBER)
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME_ID)
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME)
        self.hover(*CanonizerManageNickNameIdentifiersPage.VISIBILITY_STATUS)

        return CanonizerManageNickNameTab(self.driver)

    def verify_with_add_nick_name_button_is_present(self):
        self.verify_when_user_click_on_nick_name_tab()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME).click()
        self.hover(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME_TITLE)
        title = self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME_TITLE).text
        if title == message['Nick_name_tab']['ADD_NEW_NICK_NAME_TITLE']:
            return CanonizerManageNickNameTab(self.driver)
        else:
            print("Title not found")

    def verify_validation_for_entering_nick_name_field(self, DEFAULT_NICK_NAME):
        self.verify_when_user_click_on_nick_name_tab()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).send_keys(DEFAULT_NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_CREATE_BUTTON).click()
        self.hover(*CanonizerManageNickNameIdentifiersPage.ERROR_NICK_NAME_EXISTS)
        error = self.find_element(*CanonizerManageNickNameIdentifiersPage.ERROR_NICK_NAME_EXISTS).text
        if error == message['Nick_name_tab']['ERROR_NICK_NAME_EXISTS']:
            return CanonizerManageNickNameTab(self.driver)
        else:
            print("Error not found")


        return CanonizerManageNickNameTab(self.driver)

    def verify_the_functionality_of_add_nickname_button(self, nick_name):
        self.click_account_settings_page()
        self.hover(*CanonizerManageNickNameIdentifiersPage.NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.NICK_NAME).click()
        self.hover(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME).click()
        self.hover(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).send_keys(nick_name)
        self.hover(*CanonizerManageNickNameIdentifiersPage.POP_UP_CREATE_BUTTON)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_CREATE_BUTTON).click()
        self.hover(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME_TITLE)
        title = self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME_TITLE).text
        if title == message['Nick_name_tab']['ADD_NEW_NICK_NAME_TITLE']:
            return CanonizerManageNickNameTab(self.driver)
        else:
            print("Title not found")


    def verify_validation_for_without_entering_nick_name_field(self, nick_name):
        self.verify_when_user_click_on_nick_name_tab()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME).click()
        self.hover(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).send_keys(nick_name)
        self.hover(*CanonizerManageNickNameIdentifiersPage.POP_UP_CREATE_BUTTON)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_CREATE_BUTTON).click()
        title = self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME_ERROR).text
        if title == message['Nick_name_tab']['NICK_NAME_ERROR']:
            return CanonizerManageNickNameTab(self.driver)
        else:
            print("Error message not found")

    def verify_entering_the_nick_name_with_space(self, DEFAULT_INVALID_NICK_NAME):
        self.verify_when_user_click_on_nick_name_tab()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.ADD_NEW_NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).click()
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_NICK_NAME).send_keys(DEFAULT_INVALID_NICK_NAME)
        self.find_element(*CanonizerManageNickNameIdentifiersPage.POP_UP_CREATE_BUTTON).click()

        return CanonizerManageNickNameTab(self.driver)

