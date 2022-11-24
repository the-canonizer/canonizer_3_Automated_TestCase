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
        if self.driver.find_element(By.ID, 'name-space-1'):
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

        if self.driver.find_element(By.ID, 'name-space-2'):
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
        if self.driver.find_element(By.ID, 'name-space-3'):
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
        if self.driver.find_element(By.ID, 'name-space-4'):
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
        if self.driver.find_element(By.ID, 'name-space-5'):
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
        if self.driver.find_element(By.ID, 'name-space-6'):
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
        if self.driver.find_element(By.ID, 'name-space-7'):
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
        if self.driver.find_element(By.ID, 'name-space-8'):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_canonizer_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_canonizer_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_canonizer_help(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_canonizer_help()
        if self.driver.find_element(By.ID, 'name-space-9'):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_canonizer_help_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_canonizer_help_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_mta(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_mta()
        if self.driver.find_element(By.ID, 'name-space-10'):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_mta_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_mta_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_tv07(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_tv07()
        if self.driver.find_element(By.ID, 'name-space-11'):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_tv07_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_tv07_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"

        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_wta(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_wta()
        if self.driver.find_element(By.ID, 'name-space-12'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_wta_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_wta_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_personal_attributes(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_personal_attributes()
        if self.driver.find_element(By.ID, 'name-space-13'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_personal_attributes_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_personal_attributes_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_personal_reputations(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_personal_reputations()
        if self.driver.find_element(By.ID, 'name-space-14'):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_personal_reputations_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_personal_reputations_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_professional_services(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_professional_services()
        if self.driver.find_element(By.ID, 'name-space-15'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_professional_services_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_professional_services_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_sandbox(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_sandbox()
        if self.driver.find_element(By.ID, 'name-space-16'):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_sandbox_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_sandbox_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_terminology(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_terminology()
        if self.driver.find_element(By.ID, 'name-space-17'):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_terminology_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_terminology_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_www(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_www()
        if self.driver.find_element(By.ID, "name-space-18"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_www_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_www_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_sandbox_testing(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_sandbox_testing()
        if self.driver.find_element(By.ID, 'name-space-19'):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_sandbox_testing_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_sandbox_testing_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_crypto_currency_ethereum(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_crypto_currency_ethereum()
        if self.driver.find_element(By.ID, 'name-space-21'):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_crypto_currency_ethereum_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_crypto_currency_ethereum_only_my_topics()
        if self.driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        print(result)
        self.assertIn("Passed", result)
    def test_select_by_value_void(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_void()
        if self.driver.find_element(By.ID, 'name-space-22'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_void_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_void_only_my_topics()
        if self.driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_mormon_canon_project(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_mormon_canon_project()
        if self.driver.find_element(By.ID, 'name-space-24'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_mormon_canon_project_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_mormon_canon_project_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_united_utah_party(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_united_utah_party()
        if self.driver.find_element(By.ID, 'name-space-25'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_organizations_united_utah_party_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_organizations_united_utah_party_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_government(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_government()
        if self.driver.find_element(By.ID, 'name-space-26'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_government_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_government_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_government_sandy_city(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_government_sandy_city()
        if self.driver.find_element(By.ID, 'name-space-27'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_government_sandy_city_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_government_sandy_city_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_sports(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_sports()
        if self.driver.find_element(By.ID, 'name-space-28'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_sports_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_sports_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_sports_sbcl(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_sports_sbcl()
        if self.driver.find_element(By.ID, 'name-space-29'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_sports_sbcl_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_sports_sbcl_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_plateform_of_the_people(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_plateform_of_the_people()
        if self.driver.find_element(By.ID, 'name-space-30'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_plateform_of_the_people_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_plateform_of_the_people_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_fiction(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_fiction()
        if self.driver.find_element(By.ID, 'name-space-31'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_fiction_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_fiction_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_fiction_lord_of_the_ring(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_fiction_lord_of_the_ring()
        if self.driver.find_element(By.ID, 'name-space-32'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_fiction_lord_of_the_ring_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_fiction_lord_of_the_ring_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_fiction_star_wars(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_fiction_star_wars()
        if self.driver.find_element(By.ID, 'name-space-33'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_fiction_star_wars_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_fiction_star_wars_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_fiction_world_of_warcraft(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_fiction_world_of_warcraft()
        if self.driver.find_element(By.ID, 'name-space-34'):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_fiction_world_of_warcraft_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_fiction_world_of_warcraft_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_select_by_value_all(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_all()
        if self.driver.find_element(By.ID, 'name-space-custom'):
            result = "Passed"
        else:
            result = "Failed"
    def test_select_by_value_all_only_my_topics(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerBrowsePage(self.driver).select_by_value_all_only_my_topics()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[1]"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_support_value(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/div/ul/li[1]/a/span[2]')))
        except TimeoutException:
            pass
        CanonizerBrowsePage(self.driver).click_browse_page_button()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/div/ul/li[1]/a/span[2]')))
        except TimeoutException:
            pass
        namespace = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/div/ul/li[1]/a/span[2]")
        namespace = float(namespace.text)
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/div/ul/li[1]/a/span[2]')))
        except TimeoutException:
            pass
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/div/ul/li[1]/a/span[2]").click()
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[1]/span[3]/span/div/div/span[2]')))
        except TimeoutException:
            pass
        value = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[1]/span[3]/span/div/div/span[2]")
        value = float(value.text)
        if namespace == value:
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def test_support_value_new_topic(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        #sleep(3)
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/header/div[2]/nav/ul/li[1]')))
        except TimeoutException:
            pass
        CanonizerSupportValue(self.driver).support_value_new_topic()
        self.topic_score = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[1]/span[3]/span/div/div/span[2]")
        self.topic_score = float(self.topic_score.text)
        '''self.topic_value = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[1]/span[3]/span/div")
        print(self.topic_value.text)
        self.topic_value = float(self.topic_value.text)
        print(self.topic_value)'''
        self.camp1_score = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[2]/span[3]/span/div/div/span[2]")
        self.camp1_score = float(self.camp1_score.text)
        self.camp2_score = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[3]/span[3]/span/div/div/span[2]")
        self.camp2_score = float(self.camp2_score.text)
        self.camp_sum = self.camp1_score + self.camp2_score
        self.camp_sum = float(self.camp_sum)
        self.camp_sum = ("%.2f" % self.camp_sum)
        self.camp_sum = float(self.camp_sum)
        if self.topic_score == self.camp_sum:
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
        def test_upload_file_with_user_login(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        sleep(3)
        CanonizerUploadFilePage(self.driver).upload_file_with_user_login()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/form/div/div[2]/div[1]/span/div[2]/div/div/div/div/div/div[1]/div/span"):
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)

    def test_upload_more_than_5mb_file_with_user_login(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        sleep(3)
        CanonizerUploadFilePage(self.driver).upload_more_than_5mb_file_with_user_login()
        if self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/form/div/div[2]/div[1]/span/div[2]/div/div/div/div/div/div[1]/div/span"):
            result = "Failed"
        else:
            result = "Passed"
        self.assertIn("Failed", result)

    def test_open_uploaded_file(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        sleep(3)
        CanonizerUploadFilePage(self.driver).open_uploaded_file()
        if self.driver.find_element(By.ID, "modalImageId"):
            result = "Failed"
        else:
            result = "Passed"
        self.assertIn("Failed", result)

    def test_verify_uploaded_image_file_format(self):
        self.login_to_canonizer_app()
        self.driver.maximize_window()
        CanonizerUploadFilePage(self.driver).verify_uploaded_image_file_format()
        self.error_message = self.driver.find_element(*UploadFileIdentifiers.UPLOADED_IMAGE).text
        print("Main" + self.error_message)
        if "png" in self.error_message:
            result = "Passed"
        else:
            result = "Failed"
        self.assertIn("Passed", result)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test'))


output = run("pwd", capture_output=True).stdout
print(output)
