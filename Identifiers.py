from builtins import object

from selenium.webdriver.common.by import By

"""
Objects are Separated in this module
 - ID is the preferable choice as it is unique in a web page
 - XPATH is the next best alternative and is also unique but it is cumbersome to fix 
   if the there are any changes in the layout of the Web page.
- Add the Identifiers in Tuple.
"""


class LoginPageIdentifiers(object):
    LOGIN_BUTTON = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/button[1]/span')
    EMAIL = (By.XPATH, '//*[@id="login_form_username"]')
    PASSWORD = (By.ID, 'login_form_password')
    SUBMIT = (By.XPATH, '//*[@id="login_form"]/div[4]/div/div/div/button[1]')
    CLOSE_BUTTON = (By.XPATH, '//span[@class = "anticon anticon-close-circle"]')
    CHECK_BOX = (By.XPATH, '//*[@id="login_form_remember"]')
    TITLE = (By.XPATH, '(//div[@class="ant-message-custom-content ant-message-error"]//child::span)[1]')
    FORGET_PASSWORD = (By.XPATH, '//a[text()= "Forgot password"]')
    TITTLE1 = (By.XPATH, '//h2[text()= "Forgot your password?"]')


class HomePageIdentifiers:
    pass

    BODY = (By.ID, 'mainNav')
    LOGIN = (By.XPATH, '(//span[text()=" Log in"])[1]')
    REGISTER = (By.XPATH, '//*[@id="navbarResponsive"]/ul[1]/li[2]/a[3]')
    WHATISCANONIZER = (By.XPATH, '//*[@id="exampleAccordion"]/ul[1]/li[2]/a')
    WHATISCANONIZERHEADING = (By.XPATH, '//*[@id="exampleAccordion"]/ul[1]/li[1]/a/span')
    EMAILLOGIN = (By.XPATH, '//*[@id="login_form_username"]')
    PASSWORD = (By.ID, 'login_form_password')
    LOGIN_SUBMIT =(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div/section/div/div[1]/div/form/div[4]/div/div/div/button[1]')
    ACCOUNT_HEADER =(By.XPATH, '(//div[@class="siteHeader_btnsLoginRegister__u9U7_"]//child::*)[13]')


class ForgotPasswordIdentifiers(object):
    FORGOT_PASSWORD_LINK = (By.ID, 'forgot-password-link')
    LOGIN = (By.XPATH, '(//span[text()=" Log in"])[1]')
    FORGOT_PASSWORD = (By.XPATH, '//*[@id="login_form"]/div[3]/div/div/div/a')
    EMAIL = (By.ID, 'forgotPassword_email_id')
    SUBMIT_BUTTON =(By.XPATH,'(//span[text()="Submit "])[1]')
    OTP_PAGE_TITLE = (By.ID, 'forgot-password-title')
    FORGOT_PASSWORD_TITLE = (By.ID, 'forgot-password-title')
    INVALID_EMAIL = (By.XPATH, '//*[@id="forgotPassword"]/div[1]/div[2]/div[2]/div[2]/div')
    SUBMIT_OTP_BUTTON =(By.XPATH,'(//span[text()="Submit "])[1]')
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
    TOPIC_CLICK = (By.XPATH, '//a[@href="/topic/1118-Automated-Topic/1-Agreement"]')
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
    THREAD_LINK = (By.ID, 'thread-name-th1q')
    POST_TITLE = (By.ID, 'card-title')
    POST_REPLY = (By.XPATH, '//*[@id="new_post"]/div/div[1]/div/div/div[2]/div[1]')
    POST_NICK_NAME = (By.XPATH, '//*[@id="new_post"]/div/div[2]/div/div[2]/div[1]/div/div')
    POST_SUBMIT = (By.ID, 'submit-btn')
    REPLY_FIELD = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]')
    EMPTY_REPLY_ERROR = (By.XPATH, '//span[@class="ant-typography ant-typography-danger"]')
    NICK_NAME_LINK_ON_POST_PAGE = (By.XPATH, '//*[@id="started-by-label"]/a')
    USER_PROFILE_TITLE = (By.XPATH, '//div[@class="ant-card-head-wrapper"]//div')
    EDIT_REPLY = (By.XPATH, '(//div[@class="ant-space-item"]//a)[3]')
    REPLY_UPDATED_MESSAGE = (By.XPATH, '//div[@class="ant-message-notice"]//div')


