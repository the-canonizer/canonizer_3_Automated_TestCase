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

DEFAULT_USER = "akash.roshan@iffort.com"
DEFAULT_PASS = "Iffort@1234"
DEFAULT_NAME = "test"
INVALID_NAME = "sai deekshith1"
INVALID_PASSWORD = "sfagf@@3 sfg gdahg"

FIRST_NAME = "test"
MIDDLE_NAME = "testing"
LAST_NAME = "automation"

# Registration Page Configuration Parameters
DEFAULT_FIRST_NAME = "test"
DEFAULT_LAST_NAME = "tester"
DEFAULT_EMAIL = "akash.roshan@iffort.com"
DEFAULT_PASSWORD = "Iffort@1234"
DEFAULT_CONFIRM_PASSWORD = "Iffort@1234"
INVALID_MOBILE_NUMBER = "12345"
DEFAULT_MOBILE_NUMBER = "1992936545"
DEFAULT_INVALID_EMAIL = "sai#222222gmail"

reg_list_1 = [
    "      ",
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    INVALID_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_2 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    INVALID_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_3 = [
    '',
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    INVALID_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_4 = [
    DEFAULT_FIRST_NAME,
    '',
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASSWORD,
    DEFAULT_CONFIRM_PASSWORD,
    ''
]
reg_list_5 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    '',
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_6 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    '',
    DEFAULT_PASS,
    ''
]
reg_list_7 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    'ab123',
    '1234567',
    ''
]
reg_list_8 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    'Sai@22222222222222',
    ''

]
reg_list_9 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_10 = [
    "first  @##$#$$$23",
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_11 = [
    DEFAULT_FIRST_NAME,
    "sai@@@@###@@",
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_12 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_13 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    'INVALID'
]
reg_list_14 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_INVALID_EMAIL,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''

]
reg_list_15 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
reg_list_16 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    INVALID_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]

# Login Page Configuration Parameters
# DEFAULT_USER = ""
# DEFAULT_PASS = ""
DEFAULT_USER = "sania.mohan@talentelgia.in"
DEFAULT_PASS = "Test@123"

# Forgot Password  Page Configuration Parameters
UNREGISTERED_EMAIL = "can@gmail.com"
INVALID_LONG_OTP = "7272727722"
# DEFAULT_EMAIL = "cano3@yopmail.com"
DEFAULT_USER_INVALID = "xcvxc"
# DEFAULT_PASS = "123456"

# Login Page Configuration Parameters
# DEFAULT_USER = "sania.mohan@talentelgia.in"
# DEFAULT_PASSWORD = "Test@123"
# DEFAULT_USER = "r_canonizer_user@yopmail.com"
# DEFAULT_PASS = "Rupali@12345"
DEFAULT_INVALID_USER = 'invaliduse22rgmail.com'
DEFAULT_INVALID_PASSWORD = "invalid_password"

# Account Setting page Configuration Parameters
DEFAULT_NICK_NAME = "saideekshith"
DEFAULT_NEW_PASSWORD = "Sai@199828"
DEFAULT_INVALID_NICK_NAME = "saideekshith"
DEFAULT_INVALID_CONFIRM_PASSWORD = "sai@   12333333"
INVALID_NEW_PASSWORD = "sai123333"
INVALID_CURRENT_PASSWORD = "sai@    12333"
DEFAULT_CONFIRM_PASSWORD = "Sai@166666"
DEFAULT_FIRST_NAME = "automation  testing"
DEFAULT_LAST_NAME = "testing  cases"
DEFAULT_MIDDLE_NAME = "test  case "

# support camps tab Configuration Parameters
DEFAULT_TOPIC_NAME = "automation 123"
# //input [@aria-activedescendant = 'PlacesAutocomplete__suggestion-ChIJVaU9EY4UrjsRIrtCkznuBEc']
DEFAULT_UNVERIFIED_PHONE_NUMBER = "1234567890"
DEFAULT_INVALID_PHONE_NUMBER = "1212121212"
DEFAULT_VALID_PHONE_NUMBER = ""
DEFAULT_INVALID_OTP = "123456789"
DEFAULT_INVALID_EMAIL_FORMAT = "test@test"

# Camp Forum Configuration Parameters
DEFAULT_TOPIC = "Automated Topic"

# Create New Topic Configuration Parameters
# DEFAULT_NICK_NAME = "sania_talentelgia"
# DEFAULT_TOPIC_NAME = "testing4546"
DEFAULT_NAMESPACE = ""
DEFAULT_SUMMARY = "Default note"
DUPLICATE_TOPIC_NAME = "Theories of Consciousness"
INVALID_TOPIC_NAME = "invalid @#$%^&(!(!(!"

