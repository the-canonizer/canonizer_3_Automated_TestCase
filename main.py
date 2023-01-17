import unittest
from subprocess import run
from selenium.webdriver import Keys
from termcolor import colored, cprint
import HtmlTestRunner
from CanonizerBrowsePage import *
from CanonizerUploadFilePage import *
from Config import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import string
import random
import HtmlTestRunner
import time
from time import sleep


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from subprocess import run
from termcolor import colored, cprint
import HtmlTestRunner

from CanonizerRegistrationPage import CanonizerRegisterPage

from unittest import result
from selenium.common.exceptions import TimeoutException
from CanonizerCreateNewTopicPage import CanonizerCreateNewTopic
from CanonizerLoginPage import CanonizerLoginPage
from CanonizerForgotPasswordPage import *
from CanonizerTestCases import test_cases
from Config import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import string
import random
import HtmlTestRunner


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestPages(unittest.TestCase):
    def setUp(self):
        """
            Initialize the Things
            :return:
        """
        driver_location = DEFAULT_CHROME_DRIVER_LOCATION
        options = webdriver.ChromeOptions()

        options.binary_location = DEFAULT_BINARY_LOCATION

        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(DEFAULT_BASE_URL)

    def login_to_canonizer_app(self):
        """
            This Application will allow you to login to canonizer App on need basis
        :param flag:
        :return:
        """
        #result = CanonizerLoginPage(self.driver).click_login_page_button().login_with_valid_user(DEFAULT_USER, DEFAULT_PASS).get_url()
        self.driver.implicitly_wait(10)
        CanonizerLoginPage(self.driver).click_login_page_button()
        result = CanonizerLoginPage(self.driver).login_with_valid_user(DEFAULT_USER, DEFAULT_PASS).get_url()
        self.assertIn("", result)
        self.driver.maximize_window()

    def test_click_browse_page_button(self):
        #print("\n" + str(test_cases(22)))
        # Click on the Login Page and Create a Login Session and for further actions.
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        CanonizerBrowsePage(self.driver).click_browse_page_button()
        browse_url = self.driver.get_url
        self.assertIn("/browse", result)
# Click on the Browse link and click on "Only My Topics"
    def test_click_only_my_topics_button(self):
        #print("\n" + str(test_cases(23)))
        # Click on the Login Page and Create a Login Session and for further actions.
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        CanonizerBrowsePage(self.driver).click_browse_page_button()
        self.assertTrue(CanonizerBrowsePage(self.driver).click_only_my_topics_button())


    def test_select_dropdown_value(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        CanonizerBrowsePage(self.driver).click_browse_page_button()
        self.assertTrue(CanonizerBrowsePage(self.driver).select_dropdown_value())

    def test_select_by_value_general(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_general())
        
    def test_select_by_value_general_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_general_only_my_topics())
    def test_select_by_value_corporations(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_corporations())
    def test_select_by_value_corporations_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_corporations_only_my_topics())
    def test_select_by_value_crypto_currency(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_crypto_currency())

    def test_select_by_value_crypto_currency_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_crypto_currency_only_my_topics())

    def test_select_by_value_family(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_family())
    def test_select_by_value_family_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_family_only_my_topics())

    def test_select_by_value_family_jesperson_oscar_f(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_family_jesperson_oscar_f())
        
    def test_select_by_value_family_jesperson_oscar_f_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_family_jesperson_oscar_f_only_my_topics())

    def test_select_by_value_occupy_wall_street(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_occupy_wall_street()
                        
    def test_select_by_value_occupy_wall_street_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_occupy_wall_street_only_my_topics())

    def test_select_by_value_organizations(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations())
                        
    def test_select_by_value_organizations_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_only_my_topics())

    def test_select_by_value_organizations_canonizer(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_canonizer())

    def test_select_by_value_organizations_canonizer_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_canonizer_only_my_topics())
                        
    def test_select_by_value_organizations_canonizer_help(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_canonizer_help())
                        
    def test_select_by_value_organizations_canonizer_help_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_canonizer_help_only_my_topics())

    def test_select_by_value_organizations_mta(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_mta())

    def test_select_by_value_organizations_mta_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_mta_only_my_topics())

    def test_select_by_value_organizations_tv07(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_tv07())

    def test_select_by_value_organizations_tv07_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_tv07_only_my_topics())

    def test_select_by_value_organizations_wta(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_wta())

    def test_select_by_value_organizations_wta_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_wta_only_my_topics())
                        
    def test_select_by_value_personal_attributes(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_personal_attributes())

    def test_select_by_value_personal_attributes_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_personal_attributes_only_my_topics())
                        
    def test_select_by_value_personal_reputations(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_personal_reputations())

    def test_select_by_value_personal_reputations_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_personal_reputations_only_my_topics())

    def test_select_by_value_professional_services(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_professional_services())

    def test_select_by_value_professional_services_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_professional_services_only_my_topics())

    def test_select_by_value_sandbox(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_sandbox())

    def test_select_by_value_sandbox_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_sandbox_only_my_topics())

    def test_select_by_value_terminology(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_terminology())

    def test_select_by_value_terminology_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_terminology_only_my_topics())

    def test_select_by_value_www(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_www())

    def test_select_by_value_www_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_www_only_my_topics())

    def test_select_by_value_sandbox_testing(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_sandbox_testing())

    def test_select_by_value_sandbox_testing_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_sandbox_testing_only_my_topics())

    def test_select_by_value_crypto_currency_ethereum(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_crypto_currency_ethereum())

    def test_select_by_value_crypto_currency_ethereum_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_crypto_currency_ethereum_only_my_topics())

    def test_select_by_value_void(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_void())

    def test_select_by_value_void_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_void_only_my_topics())

    def test_select_by_value_mormon_canon_project(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_mormon_canon_project())

    def test_select_by_value_mormon_canon_project_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_mormon_canon_project_only_my_topics())

    def test_select_by_value_organizations_united_utah_party(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_united_utah_party())

    def test_select_by_value_organizations_united_utah_party_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_organizations_united_utah_party_only_my_topics())

    def test_select_by_value_government(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_government())

    def test_select_by_value_government_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_government_only_my_topics())
                        
    def test_select_by_value_government_sandy_city(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_government_sandy_city())

    def test_select_by_value_government_sandy_city_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_government_sandy_city_only_my_topics())

    def test_select_by_value_sports(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_sports())

    def test_select_by_value_sports_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_sports_only_my_topics())

    def test_select_by_value_sports_sbcl(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_sports_sbcl())

    def test_select_by_value_sports_sbcl_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_sports_sbcl_only_my_topics())

    def test_select_by_value_plateform_of_the_people(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_plateform_of_the_people())

    def test_select_by_value_plateform_of_the_people_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_plateform_of_the_people_only_my_topics())

    def test_select_by_value_fiction(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_fiction())

    def test_select_by_value_fiction_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_fiction_only_my_topics())

    def test_select_by_value_fiction_lord_of_the_ring(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_fiction_lord_of_the_ring())

    def test_select_by_value_fiction_lord_of_the_ring_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_fiction_lord_of_the_ring_only_my_topics())

    def test_select_by_value_fiction_star_wars(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_fiction_star_wars())

    def test_select_by_value_fiction_star_wars_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_fiction_star_wars_only_my_topics())

    def test_select_by_value_fiction_world_of_warcraft(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_fiction_world_of_warcraft())

    def test_select_by_value_fiction_world_of_warcraft_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_fiction_world_of_warcraft_only_my_topics())

    def test_select_by_value_all(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue( CanonizerBrowsePage(self.driver).select_by_value_all())
                        
    def test_select_by_value_all_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_by_value_all_only_my_topics())

    def test_support_value(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        CanonizerBrowsePage(self.driver).click_browse_page_button()
        namespace = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/div/ul/li[1]/a/span[2]")
        namespace = float(namespace.text)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/div/ul/li[1]/a/span[2]").click()
        value = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[1]/span[3]/span/div/div/span[2]")
        result = float(value.text)
        self.assertIn(namespace, result)
 
    def test_support_value_new_topic(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        CanonizerSupportValue(self.driver).support_value_new_topic()
        self.topic_score = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[1]/span[3]/span/div/div/span[2]")
        self.topic_score = float(self.topic_score.text)
        self.camp1_score = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[2]/span[3]/span/div/div/span[2]")
        self.camp1_score = float(self.camp1_score.text)
        self.camp2_score = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[3]/span[3]/span/div/div/span[2]")
        self.camp2_score = float(self.camp2_score.text)
        self.camp_sum = self.camp1_score + self.camp2_score
        self.camp_sum = float(self.camp_sum)
        self.camp_sum = ("%.2f" % self.camp_sum)
        result = float(self.camp_sum)
        self.assertIn(self.topic_score, result)
                        
    def test_upload_file_with_user_login(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerUploadFilePage(self.driver).upload_file_with_user_login())

    def test_upload_more_than_5mb_file_with_user_login(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerUploadFilePage(self.driver).upload_more_than_5mb_file_with_user_login())

    def test_open_uploaded_file(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerUploadFilePage(self.driver).open_uploaded_file())

    def test_verify_uploaded_image_file_format(self):
        self.login_to_canonizer_app()
        CanonizerUploadFilePage(self.driver).verify_uploaded_image_file_format()
        result = self.driver.find_element(*UploadFileIdentifiers.UPLOADED_IMAGE).text
        self.assertIn("png", result)
                        
    def test_click_upload_button(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerUploadFilePage(self.driver).click_upload_button())       
   
    def test_upload_file_with_size_zero_bytes(self):
        self.login_to_canonizer_app()
        CanonizerUploadFilePage(self.driver).upload_file_with_size_zero_bytes()
        self.driver.implicitly_wait(10)
        result = self.driver.find_element(*UploadFileIdentifiers.ZERO_BYTE_FILE).text
        self.assertIn("zero_byte_file.csv", result)
    
    def test_select_all_namespaces(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)        
        self.assertTrue(CanonizerBrowsePage(self.driver).select_all_namespaces()) 
                        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test'))


output = run("pwd", capture_output=True).stdout
print(output)
