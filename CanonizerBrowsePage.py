from time import sleep

from CanonizerBase import Page
from Identifiers import BrowsePageIdentifiers


class CanonizerBrowsePage(Page):

    def click_browse_page_button(self):
        """
        This function is to click on the Browse link
        -> Hover to the Browse link
        -> Find the element and click it

        :return:
            Return the result to the main page.
        """
    def Verify_Browse_page_is_opening_when_you_click_on_Browse(self):
        self.hover(*BrowsePageIdentifiers.CLICK_ON_BROWSE)
        self.find_element(*BrowsePageIdentifiers.CLICK_ON_BROWSE).click()
        return CanonizerBrowsePage(self.driver)

    def Verify_all_the_specified_fields_are_present_on_the_Browse_page(self):
        self.Verify_Browse_page_is_opening_when_you_click_on_Browse()
        sleep(2)
        self.hover(*BrowsePageIdentifiers.SELECT_NAME_SPACE)
        self.find_element(*BrowsePageIdentifiers.SELECT_NAME_SPACE).click()
        self.find_element(*BrowsePageIdentifiers.ONLY_MY_TOPICS).click()
        return CanonizerBrowsePage(self.driver)

    def Check_for_the_validation_of_Select_Namespace_drop_down(self):
        sleep(3)
        self.Verify_Browse_page_is_opening_when_you_click_on_Browse()
        sleep(3)
        self.find_element(*BrowsePageIdentifiers.SELECT_NAME_SPACE).click()
        return CanonizerBrowsePage(self.driver)
