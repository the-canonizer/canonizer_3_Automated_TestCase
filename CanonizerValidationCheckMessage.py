import os
import platform

"""
Set All Text Values in this class
"""
message = {
    'RegisterPage': {
        'FIRST_NAME_ERROR': 'Please input your first name!',
        'LAST_NAME_ERROR': 'Please input your last name!',
        'BLANK_EMAIL_ERROR': 'Please input your E-mail!',
        'BLANK_PASSWORD_ERROR': 'Please input your password!',
        'INVALID_PASSWORD_ERR0R': 'Password must contain small, capital letter, number and special character like '
                                  'Abc@1234.',
        'INVALID_FIRST_NAME_ERROR': 'The first name should only contain alphabets and spaces.',
        'INVALID_LAST_NAME_ERROR': 'The last name should only contain alphabets and spaces.',
        'INVALID_EMAIL_ERROR': 'The input is not valid E-mail!',
        'MOBILE_NUMBER_ERROR': 'Phone number must be at least 10 digits!',
        'LOGIN_TITLE': 'Login to Canonizer',
        'REGISTER_BUTTON_TITLE': 'Register Now on Canonizer'

    },
    'LoginPage': {
        'LOGIN_PAGE_TITLE': 'Login to Canonizer',
        'INVALID_EMAIL': 'Input is not valid!',
        'BLANK_EMAIL': 'Please input your Email!',
        'BLANK_PASSWORD': 'Please input your Password!',
        'FORGOT_PASSWORD': 'Forgot your password?',
        'REGISTER_PAGE_TITLE': 'Register Now on Canonizer',
        'ONE_TIME_REQUEST_CODE_WITH_INVALID_EMAIL': 'Input is not valid!',
        'ONE_TIME_REQUEST_CODE_WITH_INVALID_PASSWORD': 'Log in One Time Verification Code',
        'FACEBOOK_TITLE': 'Log in to Facebook',
        'TWITTER_TITLE': 'Authorize the_canonizer to access your account?',
        'EMAIL_ERROR_MESSAGE': 'Please input your Email!'
    }

}
