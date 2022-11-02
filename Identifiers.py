from builtins import object

import urllib3.packages.six
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
    LOGIN_TITLE = (By.XPATH, '//h2[@class="ant-typography Login_titles__nmC2y"]')
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
    BLANK_EMAIL_ERROR = (By.XPATH, '//div[text() = "Please input your Email!"]')
    BLANK_PASSWORD_ERROR = (By.XPATH, '//div[text() = "Please input your Password!"]')
    ONE_TIME_REQUEST_TITLE = (By.XPATH, '//h2[@class = "ant-typography Registration_titles__pUOnj"]')
    FORGET_PASSWORD = (By.XPATH, '//a[text()= "Forgot password"]')
    FORGET_PASSWORD_TITLE = (By.XPATH, '//h2[text()= "Forgot your password?"]')
    REGISTER_NOW_LINK = (By.ID, 'dont-account-link-tag')
    REQUEST_CODE = (By.ID, 'request-otp-btn')
    EMAIL_ERROR_MESSAGE = (By.XPATH, '//*[@id="login_form"]/div[1]/div[2]/div[2]/div')
    LOGIN_TITLE = (By.XPATH, '//*[@id="registration-title"]')
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
    CONFIRM_PASSWORD_ERROR = (By.XPATH, '//*[@id="changePassword"]/div[1]/div/div[3]/div/div[2]/div[2]')
    CURRENT_PASSWORD_ERROR = (By.XPATH, '//div[text() = "Please enter current password!"]')
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
    CHECK_BOX = (By.XPATH, '//*[@id="login_form_remember"]')
    TITLE = (By.XPATH, '(//div[@class="ant-message-custom-content ant-message-error"]//child::span)[1]')
    FORGET_PASSWORD = (By.XPATH, '//a[text()= "Forgot password"]')
    TITTLE1 = (By.XPATH, '//h2[text()= "Forgot your password?"]')


class ForgotPasswordIdentifiers(object):
    FORGOT_PASSWORD_LINK = (By.ID, 'forgot-password-link')
    LOGIN = (By.XPATH, '(//span[text()=" Log in"])[1]')
    FORGOT_PASSWORD = (By.XPATH, '//*[@id="login_form"]/div[3]/div/div/div/a')
    EMAIL = (By.ID, 'forgotPassword_email_id')
    SUBMIT_BUTTON = (By.XPATH, '(//span[text()="Submit "])[1]')
    OTP_PAGE_TITLE = (By.ID, 'forgot-password-title')
    FORGOT_PASSWORD_TITLE = (By.ID, 'forgot-password-title')
    INVALID_EMAIL = (By.XPATH, '//*[@id="forgotPassword"]/div[1]/div[2]/div[2]/div[2]/div')
    SUBMIT_OTP_BUTTON = (By.XPATH, '(//span[text()="Submit "])[1]')
    EMPTY_OTP = (By.XPATH, '//*[@id="otpverify"]/div[1]/div[2]/div/div[2]/div')
    OTP_ENTER = (By.XPATH, '//*[@id="otpverify_otp"]')
    INVALID_OTP = (By.XPATH, '//*[@id="otpverify"]/div[1]/div[2]/div/div[2]/div')
    CROSS_ICON_FORGOT_MODAL = (By.XPATH, '//*[@id="forgotPassword"]/button')
    CROSS_ICON_OTP_MODAL = (By.XPATH, '//*[@id="forgot-modal-close-btn"]/span/svg')
    CHANGE_PASSWORD_TITLE = (By.XPATH, '//h2[text()="Create new password"]')


class CreateTopicIdentifiers(object):
    CREATE_NEW_TOPIC = (By.XPATH, '(//span[text()=" Create New Topic"])[1]')
    LOGIN_PAGE = (By.XPATH, '//h2[text() = "Login to Canonizer"]')
    TOPIC_PAGE_TITLE = (By.XPATH, '(//span[text()="Create New Topic"])[1]')
    TOPIC_NAME = (By.ID, 'create_new_topic_topic_name')
    NICK_NAME = (By.ID, 'create_new_topic_nick_name')
    NAMESPACE = (By.ID, 'create_new_topic_namespace')
    EDIT_SUMMARY = (By.ID, 'create_new_topic_edit_summary')
    CREATE_TOPIC_BUTTON = (By.ID, 'create-topic-btn')
    TOPIC_PAGE = (By.XPATH, '//h3[text()="Canonizer Sorted Camp Tree"]')
    ERROR_TOPIC_NAME = (By.XPATH, '//*[@id="create_new_topic"]/div/div[1]/div[2]/div[2]/div[2]/div')
    ERROR_DUPLICATE_TOPIC_NAME = (By.XPATH, '//*[@id="create_new_topic"]/div/div[1]/div[2]/div[2]/div[2]/div')
    INVALID_TOPIC_NAME = (By.XPATH, '//*[@id="create_new_topic"]/div/div[1]/div[2]/div[2]/div[2]/div')
    CANCEL_BUTTON = (By.ID, 'cancel-btn')
    MAIN_PAGE = (By.XPATH, '//h3[text()="Select Namespace"]')
    NICK_NAME_ASTERISK = (By.XPATH, '(//span[@class = "required"])')
    TOPIC_NAME_ASTERISK = (By.XPATH, '(//span[@class = "required"])[2]')
    NAMESPACE_ASTERISK = (By.XPATH, '(//span[@class = "required"])[3]')


class CampForumIdentifiers(object):
    VIEW_ALL = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div[3]/div/div/a/span')
    CAMP_FORUM_BUTTON = (By.XPATH, '//div[@class="topicDetails_topicDetailContentHead_Right__Vc37F"]//button[1]')
    BROWSE = (By.XPATH, '//*[@id="__next"]/div/header/div[2]/nav/ul/li[1]/a')
    SEARCH_TOPIC = (By.XPATH, '//input[@placeholder="Search by topic name"]')
    SEARCH_ICON = (By.XPATH, '(//span[@class="ant-input-group-addon"]//button)[2]')
    TOPIC_CLICK = (By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/div/ul/li/a')
    CAMP_FORUM_TITLE = (By.XPATH, '//span[text()="Camp Forum"]')
    MY_PARTICIPATION = (By.ID, 'participate-btn')
    TOP_10_THREADS = (By.ID, 'most-rep-btn')
    NO_THREAD_STATEMENT = (By.XPATH, '//div[text()="No Data"]')
    ALL_THREADS_BUTTON = (By.ID, 'all-thread-btn')
    MY_THREADS_BUTTON = (By.ID, 'my-thread-btn')
    THREAD_BUTTON = (By.ID, 'all-thread-btn')
    CREATE_THREAD_BUTTON = (By.ID, 'create-btn')
    CREATE_THREAD_TITLE = (By.XPATH, '//span[text()="Create a new thread"]')
    THREAD_TITLE = (By.ID, 'create_new_thread_thread_title')
    NICK_NAME = (By.XPATH, '//div[text()="sania_talentelgia"]')
    SUBMIT_THREAD = (By.ID, 'submit-btn')
    THREAD_BACK = (By.ID, 'back-btn')
    ERROR_BLANK_TITLE = (By.XPATH, '//*[@id="create_new_thread"]/div/div/div[1]/div[2]/div[2]/div')
    DUPLICATE_TITLE_ERROR = (By.XPATH, '/html/body/div[2]/div/div/div/div')
    THREAD_TITLE_ASTERISK = (By.XPATH, '(//span[@class = "required"])')
    NICK_NAME_ASTERISK = (By.XPATH, '(//span[@class = "required"])[2]')
    BACK_BUTTON = (By.ID, 'back-btn')
    EDIT_THREAD_ICON = (By.XPATH, '//*[@id="thread-name-new"]/a/span')
    EDIT_THREAD_PAGE_TITLE = (By.XPATH, '//span[text()="Edit title of the thread"]')
    THREAD_LINK = (By.ID, 'thread-label-1')
    POST_TITLE = (By.ID, 'card-title')
    POST_REPLY = (By.XPATH, '//*[@id="new_post"]/div/div[1]/div/div/div[2]/div[1]')
    POST_NICK_NAME = (By.XPATH, '//*[@id="new_post"]/div/div[2]/div/div[2]/div[1]/div/div')
    POST_SUBMIT = (By.ID, 'submit-btn')
    REPLY_FIELD = (By.CLASS_NAME, 'ql-editor')
    EMPTY_REPLY_ERROR = (By.XPATH, '//span[@class="ant-typography ant-typography-danger"]')
    NICK_NAME_LINK_ON_POST_PAGE = (By.XPATH, '//*[@id="started-by-label"]/a')
    USER_PROFILE_TITLE = (By.XPATH, '//div[@class="ant-card-head-wrapper"]//div')
    EDIT_REPLY = (By.XPATH, '(//div[@class="ant-space-item"]//a)[3]')
    REPLY_UPDATED_MESSAGE = (By.XPATH, '//div[@class="ant-message-notice"]//div')
    DELETE_REPLY = (By.XPATH, '//a[@id="post-delete-icon-1938"]')
    BUTTON2 = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div[2]/button[2]')


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


class ProfileInfoIdentifiersPage(object):
        CLICK_ON_DROPDOWN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/div/div/div[2]/div/div[3]/a')
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


class CreateCampIdentifiers(object):
    CREATE_NEW_CAMP_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/aside/div[1]/div[1]/button[2]')
    NEW_CAMP_TITLE = (By.ID, 'card-title')
    NICK_NAME_ASTERISK = (By.XPATH, '(//span[@class = "required"])')
    PARENT_CAMP_ASTERISK = (By.XPATH, '(//span[@class="required"])[2]')
    CAMP_NAME_ASTERISK = (By.XPATH, '(//span[@class = "required"])[3]')
    CAMP_NICKNAME = (By.XPATH, '//span[text()="sania_talentelgia"]')
    PARENT_CAMP = (By.XPATH, '(//div[@class="ant-select-selector"])[2]')
    CAMP_NAME = (By.ID, 'create_new_camp_camp_name')
    CAMP_EDIT_SUMMARY = (By.ID, 'create_new_camp_note')
    CAMP_ABOUT_URL = (By.ID, 'create_new_camp_camp_about_url')
    KEYWORDS = (By.ID, 'create_new_camp_key_words')
    CAMP_ABOUT_NICK_NAME = (By.XPATH, '(//div[@class="ant-select-selector"])[3]')
    CREATE_CAMP_BUTTON = (By.ID, 'crate-camp-btn')
    CAMP_CANCEL_BUTTON = (By.ID, 'cancel-btn')


class AddNewsIdentifiers(object):
    ADD_NEWS_LINK = (By.XPATH, '//div[@class="ant-checkbox-wrapper"]//a[1]')
    ADD_NEWS_PAGE_TITLE = (By.XPATH, '//div[text()="Add News"]')
    DISPLAY_TEXT = (By.ID, 'display_text')
    LINK = (By.ID, 'link')
    NICKNAME = (By.XPATH, '//span[@title="sania_talentelgia"]')
    CREATE_NEWS_BUTTON = (By.ID, 'create-news-btn')
    CANCEL_BUTTON = (By.ID, 'cancel-news-btn')
    DISPLAY_TEXT_ASTERISK = (By.XPATH, '(//span[@class = "required"])')
    LINK_ASTERISK = (By.XPATH, '(//span[@class="required"])[2]')
    NICKNAME_ASTERISK = (By.XPATH, '(//span[@class = "required"])[3]')
    NEWS_ADDED = (By.XPATH, '//h4[text()="News added by sania_talentelgia"]')
    BLANK_LINK_ERROR = (By.CLASS_NAME, "ant-form-item-explain-error")
    BLANK_DISPLAY_TEXT_ERROR = (By.XPATH, '//div[@class="ant-form-item-explain-error"]')
    TOPIC_PAGE = (By.XPATH, '//h3[text()="Canonizer Sorted Camp Tree"]')
    AVAILABLE_FOR_CHILD_CAMP = (By.ID, 'available_for_child')
    INVALID_LINK = (By.XPATH, '//span[text()="Link is invalid. (Example: https://www.example.com?post=1234)."]')
    EDIT_NEWS = (By.XPATH, '//div[@class="ant-checkbox-wrapper"]//button[1]')
    EDIT_ICON = (By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[1]/aside/div[3]/div/div[2]/div/ul/li[1]/div/button')
    EDIT_NEWS_TITlE = (By.XPATH, '//div[text()="Edit News"]')
    EDIT_CANCEL_BUTTON = (By.ID, 'cancel-news-btn')


class LogoutIdentifiers(object):
    LOGOUT = (By.XPATH, '//span[text()="Log Out"]')
    CLICK_ON_DROPDOWN = (By.XPATH, '(//div[contains(@class,"ant-space ant-space-horizontal")])[3]')


class CampStatementIdentifiers(object):
    ADD_STATEMENT_BUTTON = (By.XPATH, '//button[@type="button"]//a')
    ADD_STATEMENT_TITLE = (By.XPATH, '//div[text()="Add Camp Statement"]')
    NICK_NAME = (By.XPATH, '//div[text()="sania_talentelgia"]')
    STATEMENT = (By.ID, 'statement')
    EDIT_SUMMARY = (By.ID, 'edit_summary')
    SUBMIT_STATEMENT_BUTTON = (By.XPATH, '//div[@class="ant-form-item-control-input-content"]//button[1]')
    CANCEL_BUTTON = (By.XPATH, '//button[contains(@class,"ant-btn ant-btn-ghost")]')
    CAMP_STATEMENT_HISTORY = (By.XPATH, '//h4[@class="ant-typography"]')
    NICK_NAME_ASTERISK = (By.XPATH, '//span[@class="required"]')
    STATEMENT_ASTERISK = (By.XPATH, '(//span[@class="required"])[2]')
    STATEMENT_FIELD_ERROR = (By.XPATH, 'ant-form-item-explain-error')
    TOPIC_PAGE = (By.XPATH, '//h3[text()="Canonizer Sorted Camp Tree"]')
    PREVIEW_PAGE = (By.XPATH, '(//button[contains(@class,"ant-btn ant-btn-primary")])[2]')
    SUBMIT_PREVIEW = (By.XPATH, '//button[@class="ant-btn ant-btn-primary"]')
    PREVIEW_MODAL_TITLE = (By.ID, 'rc_unique_0')
    EDIT_CAMP_STATEMENT_BUTTON = (By.XPATH, '//a[@href="/statement/history/610-Automated-Topic/1-Agreement"]')
    CAMP_HISTORY_TITLE = (By.XPATH, '//h4[@class="ant-typography"]')
    SUBMIT_STATEMENT_UPDATE = (By.XPATH, '//span[text()="Submit Statement Update Based on This"]')
    SUBMIT_UPDATE = (By.XPATH, '(//button[@type="submit"])[2]')
    VIEW_THIS_VERSION_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div[3]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/button[2]')
    OBJECTED_COLOR = (By.XPATH, '//div[@id="__next"]/div[1]/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]')
    LIVE_COLOR = (By.XPATH, '//div[@id="__next"]/div[1]/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]')
    IN_REVIEW = (By.XPATH, '//div[@id="__next"]/div[1]/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]')
    OLD = (By.XPATH, '//div[@id="__next"]/div[1]/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]')
    COMPARE_STATEMENT2 = (By.XPATH, '(//input[@type="checkbox"])[2]')
    COMPARE_STATEMENT1 = (By.XPATH, '(//input[@type="checkbox"])')
    COMPARE_STATEMENT_BUTTON = (By.XPATH, '(//button[contains(@class,"ant-btn ant-btn-primary")])[2]')
    STATEMENT_COMPARE_HISTORY_TITLE = (By.XPATH, '//h4[@class="ant-typography"]')


class CampHistoryIdentifiers(object):
    TOPIC_EDIT_BUTTON = (By.XPATH, '//a[@href="/topic/history/173-Software-Testing"]')
    CAMP_EDIT_BUTTON = (By.XPATH, '//a[@href="/camp/history/173-Software-Testing/1-Agreement"]')
    TOPIC_HISTORY_TITLE = (By.XPATH, '//h4[@class="ant-typography"]')
    HISTORY_TOPIC = (By.XPATH, '//a[@href="/topic/173-Software-Testing/1-Agreement"]')
    NAMESPACE_ALL = (By.XPATH, '//div[@title="All"]//div[1]')
    NAMESPACE = (By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div')






