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
    EMAIL = (By.ID, 'registration_email')
    PASSWORD = (By.ID, 'registration_password')
    CONFIRM_PASSWORD = (By.ID, 'registration_confirm')
    CLOSE_ICON = (By.XPATH, '//*[@id="registration"]/button')
    CAPTCHA = (By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
    LOGIN_HERE = (By.XPATH, '//*[@id="registration"]/span/a')
    FORGET_PASSWORD = (By.XPATH, '//*[@id="login_form"]/div[3]/div/div/div/a')
    TITLE = (By.XPATH, '//h2[text()="Register Now on Canonizer"]')
    LOGIN_TITLE = (By.XPATH, '//h2[@class= "ant-typography Login_titles__nmC2y"]')
    CREATE_ACCOUNT = (By.XPATH, '//span[text()="Register Now "]')
    ERROR_FIRST_NAME = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[1]/div/div[2]/div[2]/div')
    ERROR_LAST_NAME = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[2]/div/div[2]/div[2]/div')
    ERROR = (By.XPATH, '//div[@class="ant-form-item-explain-error"]')
    ERROR_PASSWORD = (By.XPATH,
                      '//*[@id="registration"]/div[1]/div/div[5]/div/div[2]/div[2]/div')
    ERROR_CONFIRMATION_PASSWORD = (By.XPATH, '//div[text()="Confirm Password does not match!"]')
    ERROR_EMAIL = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[3]/div/div[2]/div[2]/div')
    ERROR_CAPTCHA = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[7]/div/div/div[2]/div')


class LoginPageIdentifiers(object):
    LOGIN_BUTTON = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/button[1]/span')
    EMAIL = (By.XPATH, '//*[@id="login_form_username"]')
    PASSWORD = (By.ID, 'login_form_password')
    SUBMIT = (By.XPATH, '//*[@id="login_form"]/div[4]/div/div/div/button[1]')
    CLOSE_BUTTON = (By.XPATH, '//span[@class = "anticon anticon-close-circle"]')
    CHECK_BOX = (By.XPATH, '//*[@id="login_form_remember"]')
    INVALID_EMAIL_TITLE = (By.XPATH, '(//div[@class="ant-message-custom-content ant-message-error"]//child::span)[1]')
    FORGET_PASSWORD = (By.XPATH, '//a[text()= "Forgot password"]')
    FORGET_PASSWORD_TITLE = (By.XPATH, '//h2[text()= "Forgot your password?"]')
    REGISTER_NOW_LINK = (By.XPATH, '//*[@id="login_form"]/span/a')
    REQUEST_CODE = (By.XPATH, '//*[@id="login_form"]/div[4]/div/div/div/button[2]/span')
    EMAIL_ERROR_MESSAGE = (By.XPATH, '//*[@id="login_form"]/div[1]/div[2]/div[2]/div')
    LOGIN_TITLE = (By.XPATH, '//h2[text() = "Log in to Canonizer"]')
    SOCIAL_LINKS = (By.XPATH, '//div[@class="social-login_btn_group__BQdOr"]//child::button')
    FACEBOOK_LINK = (By.XPATH, '//*[@id="login_form"]/div[5]/div/div/div/div/div/button[1]')
    FACEBOOK_TITLE = (By.XPATH, '//*[@id="header_block"]/span/div')
    GOOGLE_LINK = (By.XPATH, '//*[@id="login_form"]/div[5]/div/div/div/div/div/button[2]')
    TWITTER_LINK = (By.XPATH, '//*[@id="login_form"]/div[5]/div/div/div/div/div/button[3]')
    TWITTER_TITLE = (By.XPATH, '//h2[text() = "Authorize the_canonizer to access your account?"]')
    LINKEDIN_LINK = (By.XPATH, '//*[@id="login_form"]/div[5]/div/div/div/div/div/button[4]')
    LINKEDIN_TITLE = (By.XPATH, '//*[@id="app__container"]/main/div[2]/div[2]')
    GITHUB_LINK = (By.XPATH, '//*[@id="login_form"]/div[5]/div/div/div/div/div/button[5]')
    GITHUB_TITLE = (By.XPATH, '//*[@id="js-pjax-container"]/div/div[1]/h2')


class AccountSettingPageIdentifier(object):
    CLICK_ON_DROPDOWN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/div/div/div[2]/div/div[3]/a')
    # CLICK_ON_DROPDOWN = (By.CLASS_NAME, 'ant-space ant-space-horizontal ant-space-align-center ant-dropdown-trigger')
    PROFILE_BUTTON = (By.XPATH, '//*[@id="rc-tabs-1-tab-profile_info"]')
    ACCOUNT_SETTING_BUTTON = (By.XPATH, '(//span[@class="ant-dropdown-menu-title-content"])[1]')
    SOCIAL_OAUTH_VERIFICATION = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[2]')
    CHANGE_PASSWORD = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[3]')
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



class CanonizerSupportCampIdentifiersPage(object):
    CLICK_ON_DROPDOWN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/div/div/div[2]/div/div[3]/a')
    ACCOUNT_SETTING_BUTTON = (By.XPATH, '(//span[@class="ant-dropdown-menu-title-content"])[1]')
    SUPPORTED_CAMPS = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[5]')
    DIRECET_SUPPORTED_CAMPS = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div['
                                         '1]/div[1]/div/div[1]')
    DELEGATED_SUPPORT_CAMPS = (By.XPATH, '//*[@id="rc-tabs-10-tab-2"]')
    SUPPORT_CAMP_SEARCH_BAR = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/input')
    CLICKING_ON_TOPIC_NAME = (By.XPATH, '//*[@id="rc-tabs-5-panel-1"]/div[2]/div[1]/div[1]/div/div[1]/div/span/a')
    TOPIC_NAME_TITLE = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div[1]/div[1]/div[1]')
    CLICK_ON_REMOVE_SUPPORT = (By.XPATH, '//div[@class="ant-card-extra"]//child::div')
    REMOVE_ON_POP_UP_BUTTON = (By.XPATH, '(//div[@class="ant-form-item-control-input-content"]//child::button)[1]')
    REMOVE_TITLE = (By.XPATH, '//div[@class="ant-modal-title"]')

class CanonizerChangePasswordIdentifierPage(object):
    CLICK_ON_DROPDOWN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/div/div/div[2]/div/div[3]/a')
    ACCOUNT_SETTING_BUTTON = (By.XPATH, '(//span[@class="ant-dropdown-menu-title-content"])[1]')
    CHANGE_PASSWORD =  (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[3]')
    CURRENT_PASSWORD = (By.XPATH, '//*[@id="currentPassword"]')
    NEW_PASSWORD = (By.XPATH, '//*[@id="newPassword"]')
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="confirmPassword"]')
    SAVE_BUTTON = (By.XPATH, '//*[@id="changePassword"]/div[2]/div/div/div/button/span')
    CONFIRM_PASSWORD_ERROR = (By.XPATH, '//div[text() = "Confirm Password does not match."]')
    CURRENT_PASSWORD_ERROR = (By.XPATH, '//div[text() = "Incorrect Current Password"]')
    NEW_PASSWORD_ERROR = (By.XPATH, '//*[@id="changePassword"]/div[1]/div/div[2]/div/div[2]/div[2]/div')


class CanonizerManageNickNameIdentifiersPage(object):
    CLICK_ON_DROPDOWN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/div/div/div[2]/div/div[3]/a')
    ACCOUNT_SETTING_BUTTON = (By.XPATH, '(//span[@class="ant-dropdown-menu-title-content"])[1]')
    NICK_NAME = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[4]')
    NICK_NAME_ID = (By.XPATH, '(//thead[@class="ant-table-thead"]//child::th[2])')
    VISIBILITY_STATUS = (By.XPATH, '(//thead[@class="ant-table-thead"]//child::th[4])')
    ADD_NEW_NICK_NAME = (By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn ant-btn-orange ant-btn-lg"]')
    ADD_NEW_NICK_NAME_TITLE = (By.XPATH, '//div[text()="Add New Nick Name"]')
    POP_UP_NICK_NAME = (By.ID, 'add_edit_form_nick_name')
    POP_UP_CREATE_BUTTON = (By.XPATH, '//*[@id="add_edit_form"]/div[3]/div/div/div/button')
    POP_UP_NICK_NAME_ERROR = (By.XPATH, '//div[text()="Please Enter Nick Name!"]')
    SERIAL_NUMBER = (By.XPATH, '(//thead[@class="ant-table-thead"]//child::th[1])')


class BrowsePageIdentifiers(object):
    CLICK_ON_BROWSE = (By.XPATH, '//*[@id="__next"]/div/header/div[2]/nav/ul/li[1]/a')
    SELECT_NAME_SPACE = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div['
                                   '1]/div/span[2]')
    ONLY_MY_TOPICS = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/label/span['
                                '1]/input')


class HomePageIdentifiers(object):
    pass
