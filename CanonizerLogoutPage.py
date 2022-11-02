from CanonizerBase import Page
from Identifiers import LogoutIdentifiers, LoginPageIdentifiers
from CanonizerValidationCheckMessages import message


class CanonizerLogoutPage(Page):

    def click_log_out_page_button(self):
        self.hover(*LogoutIdentifiers.CLICK_ON_DROPDOWN)
        self.find_element(*LogoutIdentifiers.CLICK_ON_DROPDOWN).click()
        self.hover(*LogoutIdentifiers.LOGOUT)
        self.find_element(*LogoutIdentifiers.LOGOUT).click()
        self.hover(*LoginPageIdentifiers.LOGIN_BUTTON)
        title = self.find_element(*LoginPageIdentifiers.LOGIN_BUTTON).text
        if title == message['Logout']['LOGIN']:
            return CanonizerLogoutPage(self.driver)
        else:
            print("Title not found or not matching")

