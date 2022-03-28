import unittest
from CanonizerHomePage import *

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



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
