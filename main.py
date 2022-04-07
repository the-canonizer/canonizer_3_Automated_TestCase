import unittest

from selenium.webdriver.remote.webelement import WebElement

from CanonizerHomePage import *
from CanonizerRegistrationPage import CanonizerRegisterPage

from CanonizerTestCases import test_cases
from Config import *
from selenium import webdriver


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

        self.driver = webdriver.Chrome(driver_location, options=options)
        self.driver.get(DEFAULT_BASE_URL)

    # 01
    def test_canonizer_home_page_load(self):
        print("\n" + str(test_cases(0)))
        self.assertTrue(CanonizerMainPage(self.driver).check_home_page_loaded())

    # 02
    def test_canonizer_click_register_page(self):
        result = CanonizerRegisterPage(self.driver).click_register_button().get_url()
        self.assertIn("", result)

    # 03
    def test_click_register_page_entering_fields_with_valid_data(self):
        result = CanonizerRegisterPage(self.driver).click_register_page_and_enter_fields_with_valid_data('kumar',
                                                                                                         'file',
                                                                                                         'saideekshith@zibtek.in',
                                                                                                         'Sai@1998',
                                                                                                         'Sai@1998').get_url()
        self.assertIn("", result)

    # 04
    def test_click_on_register_page_and_click_on_close_icon(self):
        result = CanonizerRegisterPage(self.driver).click_on_close_icon_register_page().get_url()
        self.assertIn("", result)

    # 05
    def test_create_register_page_without_entering_data(self):
        result = CanonizerRegisterPage(self.driver).craete_canonizer_register_page_without_entering_data("", "", "", "",
                                                                                                         "").get_url()
        self.assertIn("//canonizer3.canonizer.com/", result)

    # 06
    def test_create_register_page_entering_invalid_data(self):
        result = CanonizerRegisterPage(self.driver).create_canonizer_register_page_entering_with_invalid_data(
            'kumar_sai', 'file    1', 'saideekshith@zibtek.in', 'Sai@1998', 'Sai@1998').get_url()
        self.assertIn("", result)

    # 07
    def test_create_registration_page_with_existed_data(self):
        result = CanonizerRegisterPage(self.driver).create_canonizer_page_with_existed_data('kumar', 'file',
                                                                                            'saideekshith@zibtek.in',
                                                                                            'Sai@1998',
                                                                                            'Sai@1998').get_url()
        self.assertIn("", result)

    # 08
    def test_create_registration_page_without_entering_in_one_mandatary_field(self):
        result = CanonizerRegisterPage(self.driver).create_registration_page_without_entering_in_one_mandatary_field(
            'kumar', 'saideekshith@zibtek.in', 'Sai@1998', 'Sai@1998').get_url()
        self.assertIn("", result)

    # 09
    def test_registration_title_identification(self):
        print("\n" + str(test_cases(4)))
        result = CanonizerRegisterPage(self.driver).registration_title_identification().get_url()
        print(result)

    # 10
    def test_verify_firstname_empty(self):
        print("\n" + str(test_cases(5)))
        result = CanonizerRegisterPage(self.driver).verify_firstname_empty('').get_url()
        print(result)

    # 11
    def test_verify_all_fields_empty(self):
        print("\n" + str(test_cases(6)))
        result = CanonizerRegisterPage(self.driver).verify_all_fields_empty().get_url()
        print(result)

    # 12
    def test_verify_invalid_password_format(self):
        result = CanonizerRegisterPage(self.driver).verify_invalid_password_format("A","bn","son12@zibtek.in","Sonali@zibtek.in",).get_url()
        print(result)

    # 13



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
