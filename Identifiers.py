from builtins import object

from selenium.webdriver.common.by import By

"""
Objects are Separated in this module
 - ID is the preferable choice as it is unique in a web page
 - XPATH is the next best alternative and is also unique but it is cumbersome to fix 
   if the there are any changes in the layout of the Web page.
- Add the Identifiers in Tuple.
"""


class HomePageIdentifiers(object):
    """
    This Class holds the Home Page Element Identifiers.
    """
    BODY = (By.ID, 'mainNav')
    LOGIN = (By.XPATH, '//*[@id="navbarResponsive"]/ul[1]/li[2]/a[2]')
    REGISTER = (By.XPATH, '//*[@id="navbarResponsive"]/ul[1]/li[2]/a[3]')
    WHATISCANONIZER = (By.XPATH, '//*[@id="exampleAccordion"]/ul[1]/li[2]/a')
    WHATISCANONIZERHEADING = (By.XPATH, '//*[@id="exampleAccordion"]/ul[1]/li[1]/a/span')
    CANONIZER_LOGO = (By.XPATH, '//*[@id="__next"]/div/header/div[1]/a/span/img')


class RegisterPageIdentifiers(object):
    CLICK_REGISTER_BUTTON = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/button[2]/span')
    FIRST_NAME = (By.XPATH, '//*[@id="registration_first_name"]')
    LAST_NAME = (By.ID, 'registration_last_name')
    EMAIL = (By.ID, 'registration_email')
    PASSWORD = (By.ID, 'registration_password')
    CONFIRM_PASSWORD = (By.ID, 'registration_confirm')
    REGISTER_NOW = (By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-block login-form-button"]')
    CLOSE_ICON = (By.XPATH, '//*[@id="registration"]/button')
    CAPTCHA = (By.XPATH, '//div[@class="rc-anchor-logo-img rc-anchor-logo-img-portrait"]')
    ERROR = (By.XPATH, '//div[@class="ant-form-item-explain-error"]')
    LOGIN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/button[1]/span')
    FORGET_PASSWORD = (By.XPATH, '//*[@id="login_form"]/div[3]/div/div/div/a')
    TITLE = (By.XPATH, '//h2[text()="Register Now on Canonizer"]')
    FNAME = (By.XPATH, '//label[@title="First Name (Limit 100 Chars)"]')
    FNAME_HEADING = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[1]/div/div[1]/label')
    ERROR_FIRST_NAME = (By.XPATH, '//div[@class="ant-form-item-explain-error"]')
    error = (By.XPATH, '//div[@class="ant-form-item-explain ant-form-item-explain-connected"]')
    FIRST_NAME_ERROR = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[1]/div/div[2]/div[2]/div')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/button[2]/span')
    INVALID_PASSWORD_ERROR = (By.XPATH,
                              '//div[text()="Password must be contain small, capital letter, number and special '
                              'character like Abc@1234."]')
    INVALID_CONFIRM_PASSWORD_ERROR = (By.XPATH, '//div[text()="Confirm Password does not match!"]')
    EMAIL_INVALID_ERROR = (By.XPATH, '//div[text()="The input is not valid E-mail!"]')
    CAPTCHA_ERROR_MESSAGE = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[7]/div/div/div[2]/div')


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

