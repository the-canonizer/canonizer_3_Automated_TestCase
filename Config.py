import os
import platform

"""
Set All Basic Configuration required for testing Framework
"""

DEFAULT_BASE_URL = "https://canonizer3.canonizer.com/"

"""
    Identify the Default Chrome Binary Location for different OS 
"""
DEFAULT_BINARY_LOCATION = ''

if platform.system() == 'Darwin':
    DEFAULT_BINARY_LOCATION = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    DEFAULT_CHROME_DRIVER_LOCATION = os.getcwd() + "/Webdrivers/chromedriver"
elif platform.system() == 'Windows':
    DEFAULT_BINARY_LOCATION = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    DEFAULT_CHROME_DRIVER_LOCATION = os.getcwd() + "/Webdrivers/chromedriver"
elif platform.system() == 'Linux':
    DEFAULT_BINARY_LOCATION = "/usr/bin/google-chrome"
    DEFAULT_CHROME_DRIVER_LOCATION = os.getcwd() + "/Webdrivers/chromedriver"
else:
    print("Unknown OS")
    exit(1)

# Forgot Password  Page Configuration Parameters
UNREGISTERED_EMAIL = "can@gmail.com"
INVALID_LONG_OTP ="7272727722"
DEFAULT_EMAIL = "cano3@yopmail.com"
DEFAULT_USER_INVALID = "xcvxc"
DEFAULT_PASS = "123456"

# Login Page Configuration Parameters
DEFAULT_USER = "sania.mohan@talentelgia.in"
DEFAULT_PASSWORD = "Test@123"
# DEFAULT_USER = "r_canonizer_user@yopmail.com"
# DEFAULT_PASS = "Rupali@12345"
DEFAULT_INVALID_USER = 'invaliduser@gmail.com'
DEFAULT_INVALID_PASSWORD = "invalid_password"
DEFAULT_UNVERIFIED_PHONE_NUMBER = "1234567890"
DEFAULT_INVALID_PHONE_NUMBER = "1212121212"
DEFAULT_VALID_PHONE_NUMBER = ""
DEFAULT_INVALID_OTP = "123456789"
DEFAULT_INVALID_EMAIL_FORMAT = "test@test"


# Create New Topic Configuration Parameters
DEFAULT_NICK_NAME = "sania_talentelgia"
DEFAULT_TOPIC_NAME = "testing4546"
DEFAULT_NAMESPACE = ""
DEFAULT_SUMMARY = "Default note"
DUPLICATE_TOPIC_NAME = "Theories of Consciousness"
INVALID_TOPIC_NAME = "@#$%^&(!(!(!"

# Camp Forum Configuration Parameters
DEFAULT_TOPIC = "Automated Topic"
DUPLICATE_THREAD_TITLE = "Automated thread"





