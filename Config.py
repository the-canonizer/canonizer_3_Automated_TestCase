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
DEFAULT_PASS = "Sai@1998"

# Registration Page Configuration Parameters
DEFAULT_FIRST_NAME = "kumar"
DEFAULT_LAST_NAME = "file"
DEFAULT_EMAIL = "saideekshith@zibtek"
DEFAULT_PASSWORD = "Sai@1998"
DEFAULT_CONFIRM_PASSWORD = "Sai@1998"


REG_LIST_1 = [
    "first  @123",
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_2 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_3 = [
    '',
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_4 = [
    DEFAULT_FIRST_NAME,
    '',
    DEFAULT_USER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_5 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    '',
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_6 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    '',
    'DEFAULT_PASS',
    ''
]
REG_LIST_7 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    '123',
    '12345',
    ''
]
REG_LIST_8 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    'Test@1234567',
    'Test@123456',
    ''
]
REG_LIST_9 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_10 = [
    "first @##$#$$$23",
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_11 = [
    DEFAULT_FIRST_NAME,
    "sai@@@@###@@",
    DEFAULT_USER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_12 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_13 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    'INVALID'
]
REG_LIST_14 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
REG_LIST_15 = [
    DEFAULT_FIRST_NAME,
    DEFAULT_LAST_NAME,
    DEFAULT_USER,
    DEFAULT_PASS,
    DEFAULT_PASS,
    ''
]
