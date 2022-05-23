from builtins import object

from selenium.webdriver.common.by import By

"""
Objects are Separated in this module
 - ID is the preferable choice as it is unique in a web page
 - XPATH is the next best alternative and is also unique but it is cumbersome to fix 
   if the there are any changes in the layout of the Web page.
- Add the Identifiers in Tuple.
"""


class RegistrationPageIdentifiers(object):
    """
    This class holds the User Registration Page Identifiers
    """
    REGISTER = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/button[2]/span')
    FIRST_NAME = (By.XPATH, '//*[@id="registration_first_name"]')
    LAST_NAME = (By.ID, 'registration_last_name')
    ERROR_LAST_NAME =(By.XPATH,'//*[@id="registration"]/div[1]/div/div[2]/div/div[2]/div[2]/div')
    EMAIL = (By.ID, 'registration_email')
    PASSWORD = (By.ID, 'registration_password')
    CONFIRM_PASSWORD = (By.ID, 'registration_confirm')
    CLOSE_ICON = (By.XPATH, '//*[@id="registration"]/button')
    CAPTCHA = (By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
    ERROR = (By.XPATH, '//div[@class="ant-form-item-explain-error"]')
    LOGIN = (By.XPATH, '//*[@id="registration"]/span/a')
    FORGET_PASSWORD = (By.XPATH, '//*[@id="login_form"]/div[3]/div/div/div/a')
    TITLE = (By.XPATH, '//h2[text()="Register Now on Canonizer"]')
    FNAME = (By.XPATH, '//label[@title="First Name (Limit 100 Chars)"]')
    FNAME_HEADING = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[1]/div/div[1]/label')
    ERROR_FIRST_NAME = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[1]/div/div[2]/div[2]/div')
    CREATE_ACCOUNT = (By.XPATH, '//span[text()="Register Now "]')
    ERROR_PASSWORD = (By.XPATH,
                      '//*[@id="registration"]/div[1]/div/div[5]/div/div[2]/div[2]/div')
    ERROR_CONFIRMATION = (By.XPATH, '//div[text()="Confirm Password does not match!"]')
    ERROR_EMAIL = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[3]/div/div[2]/div[2]/div')
    ERROR_CAPTCHA = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[7]/div/div/div[2]/div')
    LOGIN_TITTLE = (By.XPATH, '//h2[text() ="Log in to Canonizer"]')


class LoginPageIdentifiers(object):
    LOGIN_BUTTON = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/button[1]/span')
    EMAIL = (By.XPATH, '//*[@id="login_form_username"]')
    PASSWORD = (By.ID, 'login_form_password')
    SUBMIT = (By.XPATH, '//*[@id="login_form"]/div[4]/div/div/div/button[1]')
    CLOSE_BUTTON = (By.XPATH, '//span[@class = "anticon anticon-close-circle"]')
    CHECK_BOX = (By.XPATH, '//*[@id="login_form_remember"]')
    TITTLE = (By.XPATH, '(//div[@class="ant-message-custom-content ant-message-error"]//child::span)[1]')
    FORGET_PASSWORD = (By.XPATH, '//a[text()= "Forgot password"]')
    TITTLE1 = (By.XPATH, '//h2[text()= "Forgot your password?"]')
    REGISTER_NOW_LINK = (By.XPATH, '//*[@id="login_form"]/span/a')
    REQUEST_CODE = (By.XPATH, '//*[@id="login_form"]/div[4]/div/div/div/button[2]/span')
    EMAIL_ERROR_MESSAGE = (By.XPATH, '//*[@id="login_form"]/div[1]/div[2]/div[2]/div')
    LOGIN_TITTLE = (By.XPATH, '//h2[text() = "Log in to Canonizer"]')
    SOCIAL_LINKS = (By.XPATH, '//div[@class="social-login_btn_group__BQdOr"]//child::button')


class AccountSettingPageIdentifier(object):
    CLICK_ON_DROPDOWN = (By.XPATH, '(//div[@class="siteHeader_btnsLoginRegister__u9U7_"]//child::*)[13]')
    #CLICK_ON_DROPDOWN = (By.CLASS_NAME, 'ant-space ant-space-horizontal ant-space-align-center ant-dropdown-trigger')
    PROFILE_BUTTON = (By.XPATH, '//*[@id="rc-tabs-1-tab-profile_info"]')
    ACCOUNT_SETTING_BUTTON = (By.XPATH, '(//span[@class="ant-dropdown-menu-title-content"])[1]')
    SOCIAL_OAUTH_VERIFICATION = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[2]')
    CHANGE_PASSWORD = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[3]')
    NICK_NAME = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[4]')
    SUPPORTED_CAMPS = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[5]')
    PHONE_NUMBER = (By.ID, 'verifyNumber_phone_number')
    PHONE_NUMBER_ERROR = (By.XPATH, '//div[text()="Phone number must be at least 10 digits!"]')
    MOBILE_CARRIER = (By.XPATH, '//*[@id="verifyNumber"]/div/div[1]/div[2]/div/div[2]/div/div/div/div/span[2]')
    VERIFY_BUTTON = (By.XPATH, '//*[@id="verifyNumber"]/div/div[2]/div/div/div/button')
    FIRST_NAME = (By.ID, 'profileInfo_first_name')
    MIDDLE_NAME = (By.ID, 'profileInfo_middle_name')
    LAST_NAME = (By.ID, 'profileInfo_last_name')
    GENDER = (By.XPATH, '//*[@id="profileInfo_gender"]/div/div[1]/label')
    DATA_BIRTH = (
        By.XPATH, '//*[@id="profileInfo"]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/span/div[1]/div/div/div/div')
    UPDATE_BUTTON = (By.XPATH, '//span[text() = "Update"]')
    LOGOUT = (By.XPATH, '(//span[@class="ant-dropdown-menu-title-content"])[3]')
    CURRENT_PASSWORD = (By.ID, 'changePassword_current_password')
    NEW_PASSWORD = (By.ID, 'changePassword_new_password')
    CONFIRM_PASSWORD = (By.ID, 'changePassword_confirm_password')
    SAVE_BUTTON = (By.XPATH, '//*[@id="changePassword"]/div[2]/div/div/div/button/span')
    CONFIRM_PASSWORD_ERROR = (By.XPATH, '//div[text() = "Confirm Password does not match."]')
    CURRENT_PASSWORD_ERROR = (By.XPATH, '//div[text() = "Incorrect Current Password"]')
    NEW_PASSWORD_ERROR = (By.XPATH, '//*[@id="changePassword"]/div[1]/div/div[2]/div/div[2]/div[2]/div')
    SERIAL_NUMBER = (By.XPATH, '(//thead[@class="ant-table-thead"]//child::th[1])')
    NICK_NAME_ID = (By.XPATH, '(//thead[@class="ant-table-thead"]//child::th[2])')
    NICK_NAME1 = (By.XPATH, '(//thead[@class="ant-table-thead"]//child::th[3])')
    VISIBILITY_STATUS = (By.XPATH, '(//thead[@class="ant-table-thead"]//child::th[4])')
    ADD_NEW_NICK_NAME = (By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn ant-btn-orange ant-btn-lg"]')
    ADD_NEW_NICK_NAME_TITTLE = (By.XPATH, '//div[text()="Add New Nick Name"]')
    POP_UP_NICK_NAME = (By.ID, 'add_edit_form_nick_name')
    POPO_UP_CREATE_BUTTON = (By.XPATH, '//*[@id="add_edit_form"]/div[3]/div/div/div/button')
    POP_UP_NICK_NAME_ERROR = (By.XPATH, '//div[text()="Please Enter Nick Name!"]')


class BrowsePageIdentifiers(object):
    CLICK_ON_BROWSE = (By.XPATH, '//*[@id="__next"]/div/header/div[2]/nav/ul/li[1]/a')
    SELECT_NAME_SPACE = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div['
                                   '1]/div/span[2]')
    ONLY_MY_TOPICS = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/label/span['
                                '1]/input')


class HomePageIdentifiers:
    pass