import unittest
from selenium.webdriver import Keys
from CanonizerBrowsePage import *
from CanonizerSupportValue import *
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
        result = CanonizerLoginPage(self.driver).login_with_valid_user(DEFAULT_USER, DEFAULT_PASS)
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/h3')))
        except TimeoutException:
            pass
        self.driver.maximize_window()

    def test_click_only_my_topics_button(self):
        #print("\n" + str(test_cases(23)))
        # Click on the Login Page and Create a Login Session and for further actions.
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).click_only_my_topics_button())


    def test_select_dropdown_value(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerBrowsePage(self.driver).select_dropdown_value())
                        
    def test_select_all_namespaces(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        CanonizerBrowsePage(self.driver).select_all_namespaces()
        result = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div/span[2]").text
        self.assertIn("All", result)

    def test_upload_file_with_user_login(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(10)
        self.assertTrue(CanonizerUploadFilePage(self.driver).upload_file_with_user_login())

    def test_upload_more_than_5mb_file_with_user_login(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(20)
        CanonizerUploadFilePage(self.driver).upload_more_than_5mb_file_with_user_login()
        result = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/form/div/div[2]/div[1]/span/div[2]/div/div/div/div/p").text
        self.assertIn("This file is exceeding the max limit and will not be uploaded", result)

    def test_upload_file_with_invalid_file_name_format(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(20)
        CanonizerUploadFilePage(self.driver).upload_file_with_invalid_file_name_format()
        result = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/form/div/div[2]/div[1]/span/div[2]/div/div/div/div/p").text
        self.assertIn("This file format is invalid", result)

                        
    def test_click_upload_button(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(20)
        CanonizerUploadFilePage(self.driver).click_upload_button()
        result = self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/nav/ul/li[2]").text
        self.assertIn("Upload File", result) 
        
    def test_support_value_new_topic(self):
        self.driver.implicitly_wait(30)
        self.login_to_canonizer_app()
        self.driver.maximize_window()

        self.assertTrue(CanonizerSupportValue(self.driver).support_value_new_topic())   
    def test_url_redirection(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)

        res = requests.get("http://canonizer3.canonizer.com/topic.asp/88-Theories-of-Consciousness/1-Agreement")
        res = str(res.status_code)
        print(res)
        if "200" == res:
           print("pass")
           self.driver.get("http://canonizer3.canonizer.com/topic.asp/88-Theories-of-Consciousness/1-Agreement")
           time.sleep(5)
           resp = self.driver.current_url
           print(resp)
        else:
           print("url does not exist")
        if resp == "/topic/88-Theories-of-Consciousness/1-Agreement":
            pass
        else:
            mailer.mailern()
            print("failed")


        self.assertIn("/topic/88-Theories-of-Consciousness/1-Agreement", resp)

    def test_unknown_topic(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)
        import string
        N = 10
        self.n = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        self.n = str(self.n)
        url = ("http://canonizer3.canonizer.com/topic/"+self.n)
        print(url)
        self.driver.get(url)
        resp = requests.get(url)
        resp = str(resp.status_code)
        print(resp)
        if resp == "404":
           pass
        
        else:
            mailer.mailern()
            print("failed")

        self.assertIn("404", resp)

    def test_asp_url_redirection(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)
        self.n = random.randint(0, 10000)
        self.n = str(self.n)
        self.driver.get("http://canonizer3.canonizer.com/topic.asp/"+self.n)
        time.sleep(5)

        resp = self.driver.current_url
        reslt = ("/topic/"+self.n)
        print(resp)
        print(reslt)
        if resp == reslt:
            pass
        else:
            mailer.mailern()
            print("failed")

        self.assertIn(reslt, resp)
    def test_video_url(self):
        self.login_to_canonizer_app()
        self.driver.implicitly_wait(30)
        res = requests.get("https://canonizer.com/videos/consciousness?chapter=representational_qualia_consensus")
        res = str(res.status_code)
        print(res)
        if "200" == res:
            url = ("https://"+"canonizer3"+".canonizer.com/videos/consciousness?chapter=representational_qualia_consensus")
            self.driver.get(url)
            if self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/video"):
               self.resp = "passed"
            #resp = self.driver.current_url
               print(self.resp)
        else:
            print("url does not exist")
        self.assertIn("passed", self.resp)  
    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test'))


