import unittest
from subprocess import run

from selenium.webdriver import Keys
from termcolor import colored, cprint
import HtmlTestRunner

from CanonizerRegistrationPage import CanonizerRegisterPage

from unittest import result
from selenium.common.exceptions import TimeoutException
from CanonizerCreateNewTopicPage import CanonizerCreateNewTopic
from CanonizerLoginPage import CanonizerLoginPage
from CanonizerForgotPasswordPage import *
#from CanonizerTestCases import test_cases
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
        CanonizerLoginPage(self.driver).click_login_page_button()
        result = CanonizerLoginPage(self.driver).login_with_valid_user(DEFAULT_USER, DEFAULT_PASS).get_url()
        self.assertIn("", result)
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/h3')))
        except TimeoutException:
            pass

    # TC_CLICK_ON_REGISTER_BUTTON
    def test_click_browse_page_button(self):
        #print("\n" + str(test_cases(22)))
        # Click on the Login Page and Create a Login Session and for further actions.
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/header/div[2]/nav/ul/li[1]/a')))
        except TimeoutException:
            pass
        CanonizerBrowsePage(self.driver).click_browse_page_button()
        browse_url = self.driver.current_url
        print(browse_url)
        if browse_url == "https://canonizer3.canonizer.com/browse":
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
        # Click on the Browse link

    def test_click_only_my_topics_button(self):
        #print("\n" + str(test_cases(23)))
        # Click on the Login Page and Create a Login Session and for further actions.
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).click_browse_page_button()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]/input')))
        except TimeoutException:
            pass
        CanonizerBrowsePage(self.driver).click_only_my_topics_button()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]')))
        except TimeoutException:
            pass
        # Click on the Browse link and click on "Only My Topics"
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)

    def test_select_dropdown_value(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).click_browse_page_button()
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span')))
        except TimeoutException:
            pass
        CanonizerBrowsePage(self.driver).select_dropdown_value()
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.ID, 'rc_select_3_list_1')))
        except TimeoutException:
            pass
        if self.driver.find_element(By.ID, "rc_select_3_list_1"):
            result = "Passed"
        else:
            result = "Failed"

        self.assertIn("Passed", result)

    def test_select_by_value_general(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_general()
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]')))
        except TimeoutException:
            pass
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/span[2]"):
            result = "Passed"
        else:
            result = "Failed"

        self.assertIn("Passed", result)
    def test_select_by_value_general_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_general_only_my_topics()
        CanonizerBrowsePage(self.driver).click_only_my_topics_button()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]')))
        except TimeoutException:
            pass
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_corporations(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_corporations()

        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/div/ul/li/a/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_corporations_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_corporations_only_my_topics()

        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        self.assertIn("Passed", result)
    def test_select_by_value_crypto_currency(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_crypto_currency()
        sleep(3)
        if self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[3]/div"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
        sleep(3)

    def test_select_by_value_crypto_currency_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_crypto_currency_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)

    def test_select_by_value_family(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_family()
        if self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[4]/div"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_family_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_family_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)

    def test_select_by_value_family_jesperson_oscar_f(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_family_jesperson_oscar_f()
        if self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[5]/div"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_family_jesperson_oscar_f_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_family_jesperson_oscar_f_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)

    def test_select_by_value_occupy_wall_street(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_occupy_wall_street()
        if self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[6]/div"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_occupy_wall_street_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_occupy_wall_street_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)

    def test_select_by_value_organizations(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations()
        if self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[6]/div"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_canonizer(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_canonizer()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_canonizer_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_canonizer_only_my_topics()

    def test_select_by_value_organizations_canonizer_help(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_canonizer_help()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_canonizer_help_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_canonizer_help_only_my_topics()
        CanonizerBrowsePage(self.driver).click_only_my_topics_button()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_mta(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_mta()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_mta_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_mta_help_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_tv07(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_tv07()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_tv07_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_tv07_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_wta(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_wta()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_wta_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_wtaonly_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_personal_attributes(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_personal_attributes()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_personal_attributes_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_personal_attributes_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_personal_reputations(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_personal_reputations()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_personal_reputations_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_personal_reputations_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test'))


output = run("pwd", capture_output=True).stdout
print(output)
