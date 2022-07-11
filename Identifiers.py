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


class ProfileInfoIdentifiersPage(object):
    CLICK_ON_DROPDOWN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/div/div/div[2]/div/div[3]/a')
    # CLICK_ON_DROPDOWN = (By.CLASS_NAME, 'ant-space ant-space-horizontal ant-space-align-center ant-dropdown-trigger')
    PROFILE_BUTTON = (By.XPATH, '//*[@id="rc-tabs-1-tab-profile_info"]')
    ACCOUNT_SETTING_BUTTON = (By.XPATH, '(//span[@class="ant-dropdown-menu-title-content"])[1]')
    SOCIAL_OAUTH_VERIFICATION = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[2]')
    CHANGE_PASSWORD = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[3]')
    SUPPORTED_CAMPS = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[5]')
    NICK_NAME = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[4]')
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
    ADDRESS_LINE = (By.ID, 'profileInfo_address_1')
    ALGORITHM_FIELD = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[5]/div')
    ALGORITHM_DROP_DOWN = (By.XPATH, '(//div[@class="ant-select-item-option-content"])[1]')


class CanonizerSupportCampIdentifiersPage(object):
    CLICK_ON_DROPDOWN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/div/div/div[2]/div/div[3]/a')
    ACCOUNT_SETTING_BUTTON = (By.XPATH, '(//span[@class="ant-dropdown-menu-title-content"])[1]')
    SUPPORTED_CAMPS = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[5]')
    DIRECET_SUPPORTED_CAMPS = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div['
                                         '1]/div[1]/div/div[1]')
    DELEGATED_SUPPORT_CAMPS = (By.XPATH, '(//div[@class = "ant-tabs-tab ant-tabs-tab-active"])[2]')
    SUPPORT_CAMP_SEARCH_BAR = (By.XPATH, '//div [@class = "Settings_search_users__sjo27"]')
    CLICKING_ON_TOPIC_NAME = (By.XPATH, '(//div [@class = "DirectSupportedCamps_card_heading_title__qF4nl"])[1]')
    TOPIC_NAME_TITLE = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div[1]/div[1]/div[1]')
    CLICK_ON_REMOVE_SUPPORT = (By.XPATH, '//div[@class="ant-card-extra"]//child::div')
    REMOVE_ON_POP_UP_BUTTON = (By.XPATH, '(//div[@class="ant-form-item-control-input-content"]//child::button)[1]')
    REMOVE_TITLE = (By.XPATH, '//div[@class="ant-modal-title"]')


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
    CURRENT_ASTRK = (By.XPATH, '(//span[@class = "required"])[1]')
    NEW_ASTRK = (By.XPATH, '(//span[@class = "required"])[2]')
    CONFIRM_ASTRK = (By.XPATH, '(//span[@class = "required"])[3]')


class CanonizerManageNickNameIdentifiersPage(object):
    CLICK_ON_DROPDOWN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/div/div/div[2]/div/div[3]/a')
    ACCOUNT_SETTING_BUTTON = (By.XPATH, '(//span[@class="ant-dropdown-menu-title-content"])[1]')
    NICK_NAME = (By.XPATH, '(//div[@class="ant-tabs-tab-btn"])[4]')
    NICK_NAME_ID = (By.XPATH, '(//thead[@class="ant-table-thead"]//child::th[2])')
    VISIBILITY_STATUS = (By.XPATH, '(//thead[@class="ant-table-thead"]//child::th[4])')
    ADD_NEW_NICK_NAME = (By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn ant-btn-orange ant-btn-lg"]')
    ADD_NEW_NICK_NAME_TITLE = (By.XPATH, '//div[text()="Add New Nick Name"]')
    POP_UP_NICK_NAME = (By.ID, 'enterNickName')
    POP_UP_CREATE_BUTTON = (By.ID, 'addEditBtn')
    POP_UP_NICK_NAME_ERROR = (By.XPATH, '//div[text()="Please Enter Nick Name!"]')
    SERIAL_NUMBER = (By.XPATH, '(//thead[@class="ant-table-thead"]//child::th[1])')


class BrowsePageIdentifiers(object):
    CLICK_ON_BROWSE = (By.XPATH, '//*[@id="__next"]/div/header/div[2]/nav/ul/li[1]/a')
    SELECT_NAME_SPACE = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div['
                                   '1]/div/span[2]')
    ONLY_MY_TOPICS = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/label/span['
                                '1]/input')


class HomePageIdentifiers(object):
    FACEBOOK_LINK = (By.XPATH, '//*[@id="__next"]/div/footer/div[1]/div/div[3]/div[1]/div/a[1]/span/img')
    INSTA_LINK = (By.XPATH, '//*[@id="__next"]/div/footer/div[1]/div/div[3]/div[1]/div/a[2]/span/img')
    TWITTER_LINK = (By.XPATH, '//*[@id="__next"]/div/footer/div[1]/div/div[3]/div[1]/div/a[3]/span/img')
    YOUTUBE_LINK = (By.XPATH, '//*[@id="__next"]/div/footer/div[1]/div/div[3]/div[1]/div/a[4]/span/img')
    LINKEDIN_LINK = (By.XPATH, '//*[@id="__next"]/div/footer/div[1]/div/div[3]/div[1]/div/a[5]/span/img')
    PRIVACY_POLICY = (By.XPATH, '//a[text() = "Privacy Policy"]')
    TERMS_AND_SERVICES = (By.XPATH, '//a[text() = "Terms & Services"]')
    BROWSE = (By.XPATH, '//i[@class = "icon-angle-right"]')
    CREATE_NEW_TOPIC = (By.XPATH, '(//i[@class = "icon-angle-right"])[4]')
    UPLOAD_FILE = (By.XPATH, '(//i[@class = "icon-angle-right"])[5]')
    HELP = (By.XPATH, '(//i[@class = "icon-angle-right"])[6]')
    WHITE_PAPER = (By.XPATH, '(//i[@class = "icon-angle-right"])[7]')
    BLOG = (By.XPATH, '(//i[@class = "icon-angle-right"])[8]')
    JOBS = (By.XPATH, '(//i[@class = "icon-angle-right"])[9]')
    CANONIZER_LOGO = (By.XPATH, '//*[@id="__next"]/div/footer/div[1]/div/div[1]/div/a/span/img')
    SUPPORT_CANONIZER = (By.XPATH, 'icon-envelope')
    ALGORITHM_DROP_DOWN = (By.XPATH,
                           '//div[@class="ant-select ant-select-lg topicListFilter_algoSelect__VRCVF '
                           'ant-select-single ant-select-show-arrow"]')


class SocialOauthVerificationPageIdentifiers(object):
    CLICK_ON_DROPDOWN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/div/div/div[2]/div/div[3]/a')
    ACCOUNT_SETTING_BUTTON = (By.XPATH, '(//span[@class="ant-dropdown-menu-title-content"])[1]')
    GOOGLE_LINK = (By.XPATH, '(//div[@class = "Social_content__qPKaX"])[1]')
    SOCIAL_OAUTH_VERIFICATION = (By.XPATH, '(//div[@class = "ant-tabs-tab ant-tabs-tab-active"]')
