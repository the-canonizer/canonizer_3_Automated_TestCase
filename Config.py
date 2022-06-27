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
    DEFAULT_CHROME_DRIVER_LOCATION = os.getcwd() + "/Webdrivers/chromedriver_mac_m1"
elif platform.system() == 'Windows':
    DEFAULT_BINARY_LOCATION = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    DEFAULT_CHROME_DRIVER_LOCATION = os.getcwd() + "/Webdrivers/chromedriver"
elif platform.system() == 'Linux':
    DEFAULT_BINARY_LOCATION = "/usr/bin/google-chrome"
    DEFAULT_CHROME_DRIVER_LOCATION = os.getcwd() + "/Webdrivers/chromedriver"
else:
    print("Unknown OS")
    exit(1)

DEFAULT_USER = "saideekshith@zibtek.in"
DEFAULT_PASS = "Deekshith@123"
DEFAULT_NAME = "saideekshith"
INVALID_NAME = "sai deekshith1"

FIRST_NAME = "test"
MIDDLE_NAME = "testing"
LAST_NAME = "automation"

# Registration Page Configuration Parameters
DEFAULT_FIRST_NAME = "kumar"
DEFAULT_LAST_NAME = "file"
DEFAULT_EMAIL = "saideekshith@zibtek"
DEFAULT_PASSWORD = "Sai@1998"
DEFAULT_CONFIRM_PASSWORD = "Sai@1998"
INVALID_MOBILE_NUMBER = "12345"
DEFAULT_MOBILE_NUMBER = "1992936545"
DEFAULT_INVALID_EMAIL = "sai#222222gmail"


REG_LIST_1 = [
    "           ",
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    INVALID_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_2 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    INVALID_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_3 = [
    '',
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    INVALID_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_4 = [
    DEFAULT_FIRST_NAME,
    '',
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASSWORD,
    DEFAULT_CONFIRM_PASSWORD,
    ''
]
REG_LIST_5 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    '',
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_6 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    '',
    DEFAULT_PASS,
    ''
]
REG_LIST_7 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    'ab123',
    '1234567',
    ''
]
REG_LIST_8 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    'Sai123',
    ''

]
REG_LIST_9 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_10 = [
    "first @##$#$$$23",
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_11 = [
    DEFAULT_FIRST_NAME,
    "sai@@@@###@@",
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_12 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_13 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    'INVALID'
]
REG_LIST_14 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_INVALID_EMAIL,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''

]
REG_LIST_15 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_MOBILE_NUMBER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_16 = [
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
DEFAULT_USER = "saideekshith@zibtek.in"
DEFAULT_PASS = "Deekshith@123"
# DEFAULT_USER = "r_canonizer_user@yopmail.com"
# DEFAULT_PASS = "Rupali@12345"
DEFAULT_INVALID_USER = 'invaliduser@gmail'
DEFAULT_INVALID_PASSWORD = "invalid_password"

# Account Setting page Configuration Parameters
DEFAULT_NICK_NAME = "saideekshith"
DEFAULT_INVALID_NICK_NAME = "sai___   deekshith"
DEFAULT_NEW_PASSWORD = "Sai@199828"
DEFAULT_INVALID_CONFIRM_PASSWORD = "sai@   12333333"
INVALID_NEW_PASSWORD = "sai@    123333"
INVALID_CURRENT_PASSWORD = "sai@    12333"
DEFAULT_CONFIRM_PASSWORD = "Sai@166666"
DEFAULT_FIRST_NAME = "automation  testing"
DEFAULT_LAST_NAME = "testing  cases"
DEFAULT_MIDDLE_NAME = "test  case "


# support camps tab Configuration Parameters
DEFAULT_TOPIC_NAME = "automation 123"
#//input [@aria-activedescendant = 'PlacesAutocomplete__suggestion-ChIJVaU9EY4UrjsRIrtCkznuBEc']
