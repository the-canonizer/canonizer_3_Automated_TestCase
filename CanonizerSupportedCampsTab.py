from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CanonizerBase import Page
from CanonizerValidationCheckMessages import message
from Identifiers import CanonizerSupportCampIdentifiersPage


class CanonizerSupportCampsTab(Page):

    def click_account_settings_page(self):
        self.hover(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.ACCOUNT_SETTING_BUTTON).click()

    def click_on_supported_camp_dropdown(self):
        self.hover(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN)
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICK_ON_DROPDOWN).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMP_DROPDOWN)
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMP_DROPDOWN).click()

    def verify_user_is_navigating_to_supported_camp_page_when_clicks_on_supported_camps_tab(self):
        self.click_on_supported_camp_dropdown()
        try:
            WebDriverWait(self.driver, 6).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'Settings_notes__KNmaY')))
        except TimeoutException:
            pass
        self.hover(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMP_TITLE)
        title = self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMP_TITLE).text
        if title == message['Supported_camps']['SUPPORTED_CAMP_TITLE']:
            return CanonizerSupportCampsTab(self.driver)
        else:
            print("title not found")

    def verify_the_search_bar_is_present_next_the_delegate_support_camp_tab(self):
        self.click_on_supported_camp_dropdown()
        self.hover(*CanonizerSupportCampIdentifiersPage.SUPPORT_CAMP_SEARCH_BAR)
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORT_CAMP_SEARCH_BAR).click()

        return CanonizerSupportCampsTab(self.driver)

    def verify_the_functionality_of_direct_support_camp(self):
        self.click_on_supported_camp_dropdown()
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMPS).click()

        return CanonizerSupportCampsTab(self.driver)

    def verify_the_search_functionality_in_supported_camps_page(self, DEFAULT_TOPIC_NAME):
        self.click_on_supported_camp_dropdown()
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORT_CAMP_SEARCH_BAR).click()
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORT_CAMP_SEARCH_BAR).send_keys(DEFAULT_TOPIC_NAME)

        return CanonizerSupportCampsTab(self.driver)

    def verify_the_functionality_of_delegate_support_camp_tab(self):
        self.click_on_supported_camp_dropdown()
        self.find_element(*CanonizerSupportCampIdentifiersPage.DELEGATED_SUPPORT_CAMPS).click()

        return CanonizerSupportCampsTab(self.driver)

    def verify_topic_name_link_in_direct_support_camp_tab(self):
        self.click_on_supported_camp_dropdown()
        self.hover(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMPS).click()

        return CanonizerSupportCampsTab(self.driver)

    def topic_name_and_camp_name_is_clickable(self):
        self.click_on_supported_camp_dropdown()
        self.hover(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.CLICKING_ON_TOPIC_NAME)
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICKING_ON_TOPIC_NAME).click()

        return CanonizerSupportCampsTab(self.driver)

    def verify_remove_support_button_functionality(self):
        self.click_on_supported_camp_dropdown()
        self.hover(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORTED_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.CLICK_ON_REMOVE_SUPPORT)
        self.find_element(*CanonizerSupportCampIdentifiersPage.CLICK_ON_REMOVE_SUPPORT).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.REMOVE_ON_POP_UP_BUTTON)
        self.find_element(*CanonizerSupportCampIdentifiersPage.REMOVE_ON_POP_UP_BUTTON).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.REMOVE_TITLE)
        title = self.find_element(*CanonizerSupportCampIdentifiersPage.REMOVE_TITLE).text
        if title == message['Supported_camps']['REMOVE_BUTTON_TITLE']:
            return CanonizerSupportCampsTab(self.driver)
        else:
            print("title not found")

    def verify_nick_name_link_on_delegated_tab(self):
        self.click_on_supported_camp_dropdown()
        self.hover(*CanonizerSupportCampIdentifiersPage.DELEGATED_SUPPORT_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.DELEGATED_SUPPORT_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.NICK_NAME_LINK)
        text = self.find_element(*CanonizerSupportCampIdentifiersPage.NICK_NAME_LINK).text
        self.find_element(*CanonizerSupportCampIdentifiersPage.NICK_NAME_LINK).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.NICK_NAME_COMPARE)
        text2 = self.find_element(*CanonizerSupportCampIdentifiersPage.NICK_NAME_COMPARE).text
        if text == text2:
            return CanonizerSupportCampsTab(self.driver)
        else:
            print("Text not matching")

    def verify_support_delegated_to_user_link(self):
        self.click_on_supported_camp_dropdown()
        self.hover(*CanonizerSupportCampIdentifiersPage.DELEGATED_SUPPORT_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.DELEGATED_SUPPORT_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.SUPPORT_DELEGATED_TO_LINK)
        text = self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORT_DELEGATED_TO_LINK).text
        self.find_element(*CanonizerSupportCampIdentifiersPage.SUPPORT_DELEGATED_TO_LINK).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.NICK_NAME_COMPARE)
        text2 = self.find_element(*CanonizerSupportCampIdentifiersPage.NICK_NAME_COMPARE).text
        if text == text2:
            return CanonizerSupportCampsTab(self.driver)
        else:
            print("Text not matching")

    def verify_current_supported_camp_link(self):
        self.click_on_supported_camp_dropdown()
        self.hover(*CanonizerSupportCampIdentifiersPage.DELEGATED_SUPPORT_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.DELEGATED_SUPPORT_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.CURRENT_SUPPORTED_CAMP)
        text = self.find_element(*CanonizerSupportCampIdentifiersPage.CURRENT_SUPPORTED_CAMP).text
        self.find_element(*CanonizerSupportCampIdentifiersPage.CURRENT_SUPPORTED_CAMP).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.AGREEMENT_CAMP)
        text2 = self.find_element(*CanonizerSupportCampIdentifiersPage.AGREEMENT_CAMP).text
        if text == text2:
            return CanonizerSupportCampsTab(self.driver)
        else:
            print("Text not matching")

    def verify_topic_link_on_direct_supported_tab(self):
        self.click_on_supported_camp_dropdown()
        self.hover(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.TOPIC_LINK)
        text = self.find_element(*CanonizerSupportCampIdentifiersPage.TOPIC_LINK).text
        self.find_element(*CanonizerSupportCampIdentifiersPage.TOPIC_LINK).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMP_LINK)
        text2 = self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMP_LINK).text
        if text == text2:
            return CanonizerSupportCampsTab(self.driver)
        else:
            print("Text not matching")

    def verify_agreement_support_link_on_direct_supported_tab(self):
        self.click_on_supported_camp_dropdown()
        self.hover(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMPS)
        self.find_element(*CanonizerSupportCampIdentifiersPage.DIRECT_SUPPORTED_CAMPS).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.AGREEMENT_DIRECT_SUPPORT_LINK)
        text = self.find_element(*CanonizerSupportCampIdentifiersPage.AGREEMENT_DIRECT_SUPPORT_LINK).text
        self.find_element(*CanonizerSupportCampIdentifiersPage.AGREEMENT_DIRECT_SUPPORT_LINK).click()
        self.hover(*CanonizerSupportCampIdentifiersPage.AGREEMENT_CAMP)
        text2 = self.find_element(*CanonizerSupportCampIdentifiersPage.AGREEMENT_CAMP).text
        if text == text2:
            return CanonizerSupportCampsTab(self.driver)
        else:
            print("Text not matching")




