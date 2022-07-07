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
    FIRST_NAME = (By.ID, 'registration_first_name')
    LAST_NAME = (By.ID, 'registration_last_name')
    EMAIL = (By.ID, 'registration_email')
    PASSWORD = (By.ID, 'registration_password')
    MOBILE_NUMBER = (By.ID, 'registration_phone')
    CONFIRM_PASSWORD = (By.ID, 'registration_confirm')
    CLOSE_ICON = (By.ID, 'register-modal-close-btn')
    CAPTCHA = (By.ID, 'rc-anchor-container')
    LOGIN_HERE = (By.ID, 'already-text-link')
    TITLE = (By.ID, 'registration-title')
    LOGIN_TITLE = (By.XPATH, '//h2[@class= "ant-typography Login_titles__nmC2y"]')
    REGISTER_NOW = (By.ID, 'register-btn')
    ERROR_FIRST_NAME = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[1]/div/div[2]/div[2]/div')
    ERROR_LAST_NAME = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[2]/div/div[2]/div[2]/div')
    ERROR = (By.XPATH, '//div[@class="ant-form-item-explain-error"]')
    ERROR_PASSWORD = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[5]/div/div[2]/div[2]/div')
    ERROR_MOBILE_NUMBER = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[4]/div/div[2]/div[2]/div')
    ERROR_CONFIRMATION_PASSWORD = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[6]/div/div[2]/div[2]/div')
    ERROR_EMAIL = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[3]/div/div[2]/div[2]/div')
    ERROR_CAPTCHA = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[7]/div/div/div[2]/div')
    FIRST_NAME_ASTRK = (By.XPATH, '(//span[@class = "required"])[1]')
    LAST_NAME_ASTRK = (By.XPATH, '(//span[@class = "required"])[2]')
    EMAIL_ASTRK = (By.XPATH, '(//span[@class = "required"])[3]')
    PASSWORD_ASTRK = (By.XPATH, '(//span[@class = "required"])[4]')
    CONFIRM_PASSWORD_ASTRK = (By.XPATH, '(//span[@class = "required"])[5]')


class LoginPageIdentifiers(object):
    EMAIL_ASTRK = (By.XPATH, '//span[@class = "required"]')
    PASSWORD_ASTRK = (By.XPATH, '(//span[@class = "required"])[2]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/button[1]/span')
    EMAIL = (By.ID, 'login_form_username')
    PASSWORD = (By.ID, 'login_form_password')
    SUBMIT = (By.ID, 'login-btn')
    CLOSE_BUTTON = (By.XPATH, '//span[@class = "anticon anticon-close-circle"]')
    CHECK_BOX = (By.ID, 'login_form_remember')
    INVALID_EMAIL_TITLE = (By.XPATH, '//*[@id="login_form"]/div[1]/div[2]/div[2]/div')
    FORGET_PASSWORD = (By.XPATH, '//a[text()= "Forgot password"]')
    FORGET_PASSWORD_TITLE = (By.XPATH, '//h2[text()= "Forgot your password?"]')
    REGISTER_NOW_LINK = (By.ID, 'dont-account-link-tag')
    REQUEST_CODE = (By.ID, 'request-otp-btn')
    EMAIL_ERROR_MESSAGE = (By.XPATH, '//*[@id="login_form"]/div[1]/div[2]/div[2]/div')
    LOGIN_TITLE = (By.XPATH, '//h2[text() = "Log in to Canonizer"]')
    SOCIAL_LINKS = (By.XPATH, '//div[@class="social-login_btn_group__BQdOr"]//child::button')
    FACEBOOK_LINK = (By.ID, 'facebook-link')
    FACEBOOK_TITLE = (By.ID, 'header_block')
    GOOGLE_LINK = (By.ID, 'google-link')
    TWITTER_LINK = (By.ID, 'twitter-link')
    TWITTER_TITLE = (By.XPATH, '//h2[text() = "Authorize the_canonizer to access your account?"]')
    LINKEDIN_LINK = (By.ID, 'linkedin-link')
    LINKEDIN_TITLE = (By.XPATH, '//*[@id="app__container"]/main/div[2]/div[2]')
    GITHUB_LINK = (By.ID, 'github-link')
    GITHUB_TITLE = (By.XPATH, '//*[@id="js-pjax-container"]/div/div[1]/h2')


class CanonizerChangePasswordIdentifierPage(object):
    CLICK_ON_DROPDOWN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/div/div/div[2]/div/div[3]/a')
    ACCOUNT_SETTING_BUTTON = (By.XPATH, '(//span[@class="ant-dropdown-menu-title-content"])[1]')
    CHANGE_PASSWORD = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[3]')
    CURRENT_PASSWORD = (By.ID, 'currentPassword')
    NEW_PASSWORD = (By.ID, 'newPassword')
    CONFIRM_PASSWORD = (By.ID, 'confirmPassword')
    SAVE_BUTTON = (By.ID, 'saveBtn')
    CONFIRM_PASSWORD_ERROR = (By.XPATH, '//div[text() = "Confirm Password does not match."]')
    CURRENT_PASSWORD_ERROR = (By.XPATH, '//div[text() = "Incorrect Current Password"]')
    NEW_PASSWORD_ERROR = (By.XPATH, '//*[@id="changePassword"]/div[1]/div/div[2]/div/div[2]/div[2]/div')
