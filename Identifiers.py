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
    CLICK_REGISTER_BUTTON =(By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/button[2]/span')
    FIRST_NAME = (By.XPATH, '//*[@id="registration_first_name"]')
    LAST_NAME =(By.ID, 'registration_last_name')
    EMAIL = (By.ID, 'registration_email')
    PASSWORD =(By.ID, 'registration_password')
    CONFIRM_PASSWORD = (By.ID, 'registration_confirm')
    REGISTER_NOW = (By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-block login-form-button"]')
    CLOSE_ICON = (By.XPATH, '//*[@id="registration"]/button')
    CAPTCHA = (By.XPATH, '//div[@class="rc-anchor-logo-img rc-anchor-logo-img-portrait"]')
    ERROR = (By.XPATH, '//div[@class="ant-form-item-explain-error"]')
    LOGIN = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/button[1]/span')
    FORGET_PASSWORD = (By.XPATH, '//*[@id="login_form"]/div[3]/div/div/div/a')
    TITLE = (By.XPATH, '//*[@id="forgotPassword"]/h2')
    FNAME = (By.XPATH, '//label[@title="First Name (Limit 100 Chars)"]')
    FNAME_HEADING = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[1]/div/div[1]/label')
    ERROR_FIRST_NAME = (By.XPATH, '//div[@class="ant-form-item-explain-error"]')
    error = (By.XPATH, '//div[@class="ant-form-item-explain ant-form-item-explain-connected"]')
    FIRST_NAME_ERROR = (By.XPATH, '//*[@id="registration"]/div[1]/div/div[1]/div/div[2]/div[2]/div')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="__next"]/div/header/div[3]/div[1]/button[2]/span')
    Register_now = (By.XPATH, '//*[@id="registration"]/div[2]/div/div/div/button/span[1]')
    INVALID_PASSWORD_ERROR = (By.XPATH,'//div[text()="Password must be contain small, capital letter, number and special character like Abc@1234."]')



