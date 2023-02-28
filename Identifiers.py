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
    #SUBMIT = (By.ID, 'login-btn')
    SUBMIT = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/section/div/div[1]/div/form/div[4]/div/div/div/button[1]")
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


class BrowsePageIdentifiers(object):
    """
    Class to hold the Browse Page Identifiers
    """
    BROWSE = (By.XPATH, '//*[@id="__next"]/div/header/div[2]/nav/ul/li[1]/a')
    ONLY_MY_TOPICS = (By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/label/span[2]')
    NAMESPACE = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]')
    GENERAL = (By.ID, 'name-space-1')
    #CORPORATIONS = (By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[8]/div')
    CORPORATIONS = (By.ID, 'name-space-2')
    CRYPTOCURRENCY = (By.ID, 'name-space-3')
    FAMILY = (By.ID, 'name-space-4')
    FAMILYJESPERSON = (By.ID, 'name-space-5')
    OCCUPYWALLSTREET = (By.ID, 'name-space-6')
    ORGANIZATION = (By.ID, 'name-space-7')
    ORGANIZATIONCANONIZER = (By.ID, 'name-space-8')
    ORGANIZATIONCANONIZERHELP =  (By.ID, 'name-space-9')
    ORGANIZATIONMTA = (By.ID, 'name-space-10')
    ORGANIZATIONTV07 = (By.ID, 'name-space-11')
    ORGANIZATIONWTA = (By.ID, 'name-space-12')
    PERSONALATTRIBUTE = (By.ID, 'name-space-13')
    PERSONALREPUTATION = (By.ID, 'name-space-14')
    PROFESSIONALSERVICES = (By.ID, 'name-space-15')
    SANDBOX = (By.ID, 'name-space-16')
    TERMINOLOGY = (By.ID, 'name-space-17')
    WWW = (By.ID, 'name-space-18')
    SANDBOXTESTING = (By.ID, 'name-space-19')
    CRYPTOCURRENCYETHEREUM = (By.ID, 'name-space-21')
    VOID = (By.ID, 'name-space-22')
    MORMONCANONPROJECT = (By.ID, 'name-space-24')
    ORGANIZATIONUNITEDUTAHPARTY = (By.ID, 'name-space-25')
    GOVERNMENT = (By.ID, 'name-space-26')
    GOVERNMENTSANDYCITY = (By.ID, 'name-space-27')
    SPORT = (By.ID, 'name-space-28')
    SPORTSBCL = (By.ID, 'name-space-29')
    PLATEFORMOFTHEPEOPLE = (By.ID, 'name-space-30')
    FICTION = (By.ID, 'name-space-31')
    FICTIONLORDOFTHERINGS = (By.ID, 'name-space-32')
    FICTIONSTARWARS = (By.ID, 'name-space-33')
    FICTIONWORLDOFWARCRAFT = (By.ID, 'name-space-34')
    ALL = (By.ID, 'name-space-custom')

    UPLOADFILE = (By.XPATH, '//*[@id="__next"]/div/header/div[2]/nav/ul/li[2]/a')
    MENU_ITEM = (By.ID, 'namespace')
    TOPIC_NAME = (By.XPATH, '//*[@id="outline_127"]/a')
    UPLOAD = (By.XPATH, '//*[@id="__next"]/div/header/div[2]/nav/ul/li[2]/a')
    # SUB_TOPIC_NAME = (By.XPATH, '//*[@id="outline_127"]/a')
    #TITLE = (By.XPATH, '/html/body/div[1]/div[1]/h1')
    TITLE = (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/a[1]/span[1]/img[1]')
    HEADING = (By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div/h3/text()')
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


class HomePageIdentifiers:
    pass

    BODY = (By.ID, 'mainNav')
    LOGIN = (By.XPATH, '(//span[text()=" Log in"])[1]')
    #LOGIN = (By.XPATH, '/html/body/div[1]/div/header/div[3]/div[1]/button[1]/span')
    REGISTER = (By.XPATH, '//*[@id="navbarResponsive"]/ul[1]/li[2]/a[3]')
    WHATISCANONIZER = (By.XPATH, '//*[@id="exampleAccordion"]/ul[1]/li[2]/a')
    WHATISCANONIZERHEADING = (By.XPATH, '//*[@id="exampleAccordion"]/ul[1]/li[1]/a/span')
    EMAILLOGIN = (By.XPATH, '//*[@id="login_form_username"]')
    PASSWORD = (By.ID, 'login_form_password')
    LOGIN_SUBMIT = (By.XPATH,
                    '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/section/div/div[1]/div/form/div[4]/div/div/div/button[1]')
    ACCOUNT_HEADER = (By.XPATH, '(//div[@class="siteHeader_btnsLoginRegister__u9U7_"]//child::*)[13]')


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
    CAMP_FORUM_BUTTON = (By.XPATH, '(//button[contains(@class,"ant-btn ant-btn-primary")])[2]')
    BROWSE = (By.XPATH, '//*[@id="__next"]/div/header/div[2]/nav/ul/li[1]/a')
    SEARCH_TOPIC = (By.XPATH, '//input[@placeholder="Search by topic name"]')
    SEARCH_ICON = (By.XPATH, '(//span[@class="ant-input-group-addon"]//button)[2]')
    TOPIC_CLICK = (By.XPATH, '//a[@href="/topic/1118-Automated-Topic/1-Agreement"]')
    CAMP_FORUM_TITLE = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[1]')
    THREAD_BUTTON = (By.ID, 'all-thread-btn')


class UploadFileIdentifiers(object):
    """
    Class to hold the Browse Page Identifiers
    """
    UPLOADFILE = (By.XPATH, '//*[@id="__next"]/div/header/div[2]/nav/ul/li[2]/a')
    UPLOAD = (By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/form/div/div[2]/div[1]/span/div[1]/span/input')
    UPLOADBUTTON = (By.XPATH, '/html/body/div[1]/div/header/div[2]/nav/ul/li[2]/a')
    ERROR_FILE_NAME = "  "
    FIVE_MB_FILE = "/home/akashroshan/PycharmProjects/Test/5mb.jpg"
    VALID_FILE_NAME = "/home/akashroshan/PycharmProjects/Test/sample.csv"
    UPLOADED_OPTION = (By.ID, "threeDots")
    UPLOADED_IMAGE = (By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div/form/div/div[2]/div[2]/div[1]/div/div/div/div[2]")
    UPLOADED_IMAGE_VIEW = (By.XPATH, '/html/body/div[2]/div/div/ul/li[1]/span/span/span[2]')
