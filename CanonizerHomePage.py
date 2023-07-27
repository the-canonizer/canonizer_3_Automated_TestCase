from CanonizerBase import Page
from Identifiers import *
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class CanonizerHomePage(Page):
    """
    Class Name: CanonizerHomePage
    Description: Verify test cases for Canonizer Home Page.

    Attributes: None
    """

    def verify_the_facebook_link(self):
        self.hover(*HomePageIdentifiers.FACEBOOK_LINK)
        self.find_element(*HomePageIdentifiers.FACEBOOK_LINK).click()
        return CanonizerHomePage(self.driver)

    def verify_the_insta_link(self):
        self.hover(*HomePageIdentifiers.INSTA_LINK)
        self.find_element(*HomePageIdentifiers.INSTA_LINK).click()
        return CanonizerHomePage(self.driver)

    def verify_the_twitter_link(self):
        self.hover(*HomePageIdentifiers.TWITTER_LINK)
        self.find_element(*HomePageIdentifiers.TWITTER_LINK).click()
        return CanonizerHomePage(self.driver)

    def verify_the_youtube_link(self):
        self.hover(*HomePageIdentifiers.YOUTUBE_LINK)
        self.find_element(*HomePageIdentifiers.YOUTUBE_LINK).click()
        return CanonizerHomePage(self.driver)

    def verify_the_linkedin_link(self):
        self.hover(*HomePageIdentifiers.LINKEDIN_LINK)
        self.find_element(*HomePageIdentifiers.LINKEDIN_LINK).click()
        return CanonizerHomePage(self.driver)


class CanonizerTermsAndPrivacyPolicy(Page):

    def driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def verify_privacy_policy_page(self):
        self.hover(*HomePageIdentifiers.PRIVACY_POLICY)
        self.find_element(*HomePageIdentifiers.PRIVACY_POLICY).click()
        return CanonizerHomePage(self.driver)

    def verify_terms_and_services_page(self):
        self.hover(*HomePageIdentifiers.TERMS_AND_SERVICES)
        self.find_element(*HomePageIdentifiers.TERMS_AND_SERVICES).click()
        return CanonizerHomePage(self.driver)

    def verify_browse_button(self):
        self.hover(*HomePageIdentifiers.BROWSE)
        self.find_element(*HomePageIdentifiers.BROWSE).click()
        return CanonizerHomePage(self.driver)

    def verify_create_new_topic(self):
        self.hover(*HomePageIdentifiers.CREATE_NEW_TOPIC)
        self.find_element(*HomePageIdentifiers.CREATE_NEW_TOPIC).click()
        return CanonizerHomePage(self.driver)

    def verify_upload_file(self):
        self.hover(*HomePageIdentifiers.UPLOAD_FILE)
        self.find_element(*HomePageIdentifiers.UPLOAD_FILE).click()
        return CanonizerHomePage(self.driver)

    def verify_the_help(self):
        self.hover(*HomePageIdentifiers.HELP)
        self.find_element(*HomePageIdentifiers.HELP).click()
        return CanonizerHomePage(self.driver)

    def verify_the_white_paper(self):
        self.hover(HomePageIdentifiers.WHITE_PAPER)
        self.find_element(*HomePageIdentifiers.WHITE_PAPER).click()
        return CanonizerHomePage(self.driver)

    def verify_the_blog(self):
        self.hover(*HomePageIdentifiers.BLOG)
        self.find_element(*HomePageIdentifiers.BLOG).click()
        return CanonizerHomePage(self.driver)

    def verify_the_jobs(self):
        self.hover(*HomePageIdentifiers.JOBS)
        self.find_element(*HomePageIdentifiers.JOBS).click()
        return CanonizerHomePage(self.driver)

    def click_on_canonizer_logo(self):
        self.hover(*HomePageIdentifiers.CANONIZER_LOGO)
        self.find_element(*HomePageIdentifiers.CANONIZER_LOGO).click()
        return CanonizerHomePage(self.driver)

    def click_on_support_canonizer(self):
        self.hover(*HomePageIdentifiers.SUPPORT_CANONIZER)
        self.find_element(*HomePageIdentifiers.SUPPORT_CANONIZER).click()
        return CanonizerTermsAndPrivacyPolicy(self.driver)

    def click_on_algorithm_dropdown_button(self):
        self.hover(*HomePageIdentifiers.ALGORITHM_DROP_DOWN)
        self.find_element(*HomePageIdentifiers.ALGORITHM_DROP_DOWN).click()
        return CanonizerTermsAndPrivacyPolicy(self.driver)
    def tree_toggle_button(self, topic_name):

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'siteHeader_navWrap__yilWi false')))
        except TimeoutException:
            pass

        # Browse to Browse Page
        self.hover(*CampForumIdentifiers.BROWSE)
        self.find_element(*CampForumIdentifiers.BROWSE).click()

        # Click on Search Topic
        self.hover(*CampForumIdentifiers.SEARCH_TOPIC)
        self.find_element(*CampForumIdentifiers.SEARCH_TOPIC).send_keys("Test")
        self.hover(*CampForumIdentifiers.SEARCH_ICON)
        self.find_element(*CampForumIdentifiers.SEARCH_ICON).click()
        self.hover(*CampForumIdentifiers.TOPIC_CLICK)
        self.find_element(*CampForumIdentifiers.TOPIC_CLICK).click()
        # Click on Manage/edit Topic
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-btn ant-btn-default btn-green')))
        except TimeoutException:
            pass
        return CanonizerHomePage(self.driver)
