from CanonizerBase import Page
from Identifiers import CanonizerSupportCampIdentifiersPage


class CanonizerSupportCampsTab(Page):

    def click_account_settings_page(self):
        self.hover(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.ACCOUNT_SETTING_BUTTON).click()

        return CanonizerSupportCampsTab(self.driver)

    def click_on_supported_camp_tab(self):
        self.hover(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMPS).click()

        return CanonizerSupportCampsTab(self.driver)

    def verify_user_is_navigating_to_supported_camp_page_when_clicks_on_supported_camps_tab(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()

        return CanonizerSupportCampsTab(self.driver)

    def verify_direct_supported_camps(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.hover(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS)
        self.hover(*CanonizerSupportCampIdentifiersPage.DELEGATED_SUPPORT_CAMPS)

        return CanonizerSupportCampsTab(self.driver)

    def verify_the_search_bar_is_present_next_the_delegate_support_camp_tab(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORT_CAMP_SEARCH_BAR).click()

        return CanonizerSupportCampsTab(self.driver)

    def verify_the_functionality_of_direct_support_camp(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS).click()

        return CanonizerSupportCampsTab(self.driver)

    def verify_the_functionality_of_delegate_support_camp_tab(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.DELEGATED_SUPPORT_CAMPS).click()

        return CanonizerSupportCampsTab(self.driver)

    def verify_the_search_functionality_in_supported_camps_page(self, DEFAULT_TOPIC_NAME):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORT_CAMP_SEARCH_BAR).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORT_CAMP_SEARCH_BAR).send_keys(DEFAULT_TOPIC_NAME)

        return CanonizerSupportCampsTab(self.driver)

    def verify_topic_name_and_agreement_camp_name_is_present_in_direct_support_camp_tab(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS).click()

        return CanonizerSupportCampsTab(self.driver)


    def topic_name_and_camp_name_is_clickable(self):
        self.click_account_settings_page()
        self.click_on_supported_camp_tab()
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICKING_ON_TOPIC_NAME).CLICK()
        title = self.find_element(*CanonizerSupportCampIdentifiersPage.TOPIC_NAME_TITLE).text
        if title == 'Topic: automation 123':
            return CanonizerSupportCampsTab(self.driver)
        else:
            print("title not found")

    def verify_remove_support_button_functionality(self):
        self.hover(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.ACCOUNT_SETTING_BUTTON).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECET_SUPPORTED_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.CLICK_ON_REMOVE_SUPPORT)
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICK_ON_REMOVE_SUPPORT).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.REMOVE_ON_POP_UP_BUTTON).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.REMOVE_TITLE)
        title = self.find_element(*CanonizerSupportCampIdentifiersPage.REMOVE_TITLE).text
        if title == 'Remove Support':
            return CanonizerSupportCampsTab(self.driver)
        else:
            print('title not found')