def test_cases(index):
    return testCases[index]


Critical = "Critical"
major = "Major"
moderate = "Moderate"
low = "Low"

testCases = {

    'TC_CLICK_ON_REGISTER_BUTTON': [Critical, 'In Home page,when user click "Register" button, user should see '
                                              'register page'],
    'TC_REGISTER_WITH_BLANK_FIRST_NAME': [moderate, 'In User Registration Page, When user doesn\'t put First Name, '
                                                    'user must see Error Message'],
    'TC_REGISTER_WITH_BLANK_LAST_NAME': [moderate, 'In User Registration Page, When user doesn\'t put Last Name, '
                                                   'user must see Error Message'],
    'TC_REGISTRATION_WITH_BLANK_EMAIL': [moderate, 'In User Registration Page, When user doesn\'t put Email, '
                                                   'user must see Error Message'],
    'TC_REGISTRATION_WITH_BLANK_PASSWORD': [moderate, 'In User Registration Page, When user puts blank password, '
                                                      'user must see Error Message'],
    'TC_REGISTRATION_WITH_INVALID_PASSWORD_LENGTH': [moderate, 'In User Registration Page, when user puts invalid '
                                                               'password,user must see Error Message'
                                                               'error message'],
    'TC_REGISTRATION_WITH_DIFFERENT_CONFIRM_PASSWORD': [moderate,
                                                        'In User Registration Page, when user puts different password '
                                                        'for confirmation,user must see Error Message'],
    'TC_REGISTER_WITH_BLANK_SPACES_FIRST_NAME': [Critical, 'In User Registration Page, when user puts blank spaces to '
                                                           'first name ,user must see Error Message'],

    'TC_REGISTRATION_WITH_INVALID_FIRST_NAME': [moderate, 'In User Registration Page, When user invalid put First '
                                                          'Name user must see Error Message'],
    'TC_REGISTRATION_WITH_INVALID_LAST_NAME': [moderate, 'In User Registration Page, When user put invalid Last Name, '
                                                         'user must see Error Message'],
    'TC_REGISTRATION_WITH_INVALID_EMAIL': [moderate, 'In User Registration Page, When user put invalid email, '
                                                     'user must see Error Message'],
    'TC_CHECK_LOGIN_PAGE_OPEN_CLICK_ON_LOGIN_HERE_LINK': [Critical, 'when user click on main page register but , '
                                                                    'user should see login link ,when user click on '
                                                                    'login link ,user should redirect to canonizer '
                                                                    'login page'],
    'TC_VERIFY_THE_FUNCTIONALITY_OF_REGISTERATION_WITH_MANDATORY_FIELDS': [Critical, 'when user fill all mandatary '
                                                                                     'fields on register page,'
                                                                                     'user able to create a accounton '
                                                                                     'canonizer'],

    'TC_VERIFYING_ACCOUNT_PROFILE': [Critical, 'When user should click on login dropdown button,user should see '
                                               'account setting page option'],
    'TC_CLICK_ON_LOGIN_BUTTON': [Critical, 'When user should click on login button with valid email and password,'
                                           'user should see main page'],
    'TC_VERIFY_LOGIN_PAGE': [Critical, 'When user should click on close on on login page, user should go to canonize '
                                       'main page'],
    'TC_CLICK_CLOSE_ICON_ON_LOGIN_PAGE': [Critical, 'When user should verify the tittle of "log in canonize page" in '
                                                    'login page,user should get '
                                                    'verified tittle'],
    'TC_LOGIN_WITH_REGISTERED_CREDENTIALS': [Critical, 'When user should try to login with registered credentials, '
                                                       'user should see main page'],
    'TC_LOGIN_WITH_INVALID_EMAIL': [Critical, 'When user should try to login with invalid email, user should see '
                                              'proper error message'],
    'TC_VERIFYING_REMEMBER_CHECK_BOX': [Critical, 'When user should click on checkbox on login page, user should see '
                                                  'marked with blue mark'],
    'TC_VERIFYING_EMPTY_SPACE_FOR_EMAIL_FILED': [Critical, 'When user should click on login button with empty fields, '
                                                           'user should see proper error message'],
    'TC_VERIFY_FORGET_PASSWORD': [Critical, 'When user should verify tittle of "forget password, user should get '
                                            'proper tittle'],
    'TC_CLICK_ON_REGISTER_NOW_LINK': [Critical, 'When user should click register now link button on login page ,'
                                                'user should redirect canonize register page'],
    'TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON': [Critical, 'When user should click one time verification code without '
                                                        'entering email, user should see proper error message'],
    'TC_CLICK_REQUEST_ONE_TIME_CODE_BUTTON_WITH_INVALID-EMAIL': [Critical, 'When user should click one time '
                                                                           'verification code with invalid email,user '
                                                                           'should see proper error message'],
    'TC_VERIFYING_SOCIAL LINKS': [Critical, 'when '],
    'Tc_verifying_facebook_link': [Critical, 'when user click on facebook link on login page ,user should see it '
                                             'redirect to facebook page'],
    'TC_VERIFYING_GOOGLE_LINK': [Critical, 'when user click on google link on login page, user should see it redirect '
                                           'to google chrome site'],
    'TC_VERIFYING_TWITTER_LINK': [Critical, 'when user click on twitter link on login page , user should see it '
                                            'redirect to twitter page'],
    'TC_VERIFYING_LINKEDIN_LINK': [Critical, 'when user click on linkedin link on login page, user should see it '
                                             'redirect to linkedin page'],
    'TC_VERIFYING_GITHUB_LINK': [Critical, 'when user should click on github link, user should see it redirect to '
                                           'github page'],
    'TC_VERIFYING_LOGIN_PLACEHOLDERS': [Critical, 'when  user used verify place holder on login page, suer should see '
                                                  'proper verfing place holders'],
    'TC_VERIFYING_ACCOUNT_PROFILE_PAGE': [Critical, 'When user should click on login drop down button ,user should '
                                                    'redirect to account setting page'],
    'TC-VERIFYING_SOCIAL_OAUTH_VERIFICATION': [Critical, 'when user click on account setting page, user should see '
                                                         'social oauth verification'],
    'TC_VERIFICATION_CHANGE_PASSWORD': [Critical, 'when user click on account setting page, user should see change '
                                                  'password button'],
    'TC_VERIFYING_NICK_NAME': [Critical, 'when user click on account setting page, user should see nick name button'],
    'TC_VERIFYING_SUPPORTED_CHANGES': [Critical, 'when user should click on account setting page , user should see '
                                                 'support camp changes'],
    'TC_VERIFYING_VALIDATION_FOR_PROFILE_INFO_PHONE_NUMBER': [Critical, 'when user try to give lessthan 10 digits '
                                                                        'profile info  phone number field,'
                                                                        'user should  see proper error message'],
    'TC_VERIFYING_VERIFY_BUTTON_WITH_BLANK_FIELDS': [Critical, 'when user click on verify button without entering any '
                                                               'data in mandatory fields, user should see proper '
                                                               'error message'],
    'TC_VERIFYING_CLICK_ON_MOBILE_CARRIER_DROP_DOWN': [Critical, 'when user click on mobile carrier , user should see '
                                                                 'droo down option'],
    'TC_VERIFYING_ALL_THE_FIELDS_ARE_PERSONAL_INFORMATION': [Critical, 'when user wants to verify the personal '
                                                                       'information fields  present are not, '
                                                                       'user click on profile info,then user can see '
                                                                       'personal information fields'],
    'TC_VERIFYING_FIRST_NAME_FIELD_WITHOUT_ENTERING_DATA': [Critical, 'when user click submit button without entering '
                                                                      'first name fields,user should see proper error'
                                                                      ' message'],
    'TC_UPDATE_THE_FIRST_NAME_AND_CHECK_IF_IT_IS_UPDATING_SAME_FOR_USERNAME': [Critical, 'when user updated first '
                                                                                         'name and user should see '
                                                                                         'it reflect to user name '
                                                                                         'also'],
    'TC_VERIFY_THE_FUNCTIONALITY_OF_RADIO_BUTTON_IN_SELECTING_THE_GENDER'
    'TC_VERIFY_THE_FUNCTIONALITY_OF_SELECTING_THE_DOB'
    'TC_VERIFY_WHEN_USER_UPDATE_THE_PERSONAL_INFORMATION_AND_LOGS_OUT_AND_LOGIN_AGAIN': [Critical,
                                                                                         'when user Update all the '
                                                                                         'Personal Information layout '
                                                                                         'field and Click on Update '
                                                                                         'button and user Logout '
                                                                                         'Again login and navigate to '
                                                                                         'account setting '],
    'TC_VERIFY_THE_SPACES_ARE_TRIMMED_IN_THE_FIRSTNAME_LASTNAME_MIDDLENAME_fields': [Critical, 'when user try to the '
                                                                                               'spaces are trimmed '
                                                                                               'in the first name, '
                                                                                               'lastname,middlename '
                                                                                               'fields,user should '
                                                                                               'see the spaces '
                                                                                               'should be trimmed '
                                                                                               'while saving the '
                                                                                               'entered  data'],
    'TC VERIFY_WHEN_USER_CLICK_ON_CHANGE_PASSWORD': [Critical, 'when user click on change password , user can see '
                                                               'current and new and confirm password fields'],
    'TC VERIFYING_CURRENT_PASSWORD_NEW_PASSWORD_CONFIRM_PASSWORD': [Critical, 'when user click on change password '
                                                                              'button,user can verify all fields are '
                                                                              'present'],
    'TC VERIFY_KEEPING_ALL_THE_FIELDS_EMPTY_AND_CLICK_ON_SAVE': [Critical, 'when user try to click on save button '
                                                                           'without entering any data  , user should '
                                                                           'see proper error message'],
    'TC VERIFY_ENTERING_THE_INVALID_CURRENT_PASSWORD': [Critical, 'when user click on save button entering '
                                                                  'current password with invalid data , user should '
                                                                  'see proper error message'],
    'TC VERIFY_ENTERING_THE_INVALID_NEW_PASSWORD': [Critical, 'when user click on save button with invalid new '
                                                              'password data user should see proper error message'],
    'TC VERIFY_ENTERING_THE_INVALID_CONFIRM_PASSWORD': [Critical, 'when user click on save button with invalid confirm '
                                                                  'password data,user should see proper error message'],
    'TC VERIFY_WHEN_BOTH_NEW_PASSWORD_AND_CONFIRM_PASSWORD_DOES_NOT_MATCH': [Critical, 'when user click on save '
                                                                                       'button when both new and '
                                                                                       'confirm password invalid,'
                                                                                       'user should see proper error '
                                                                                       'message'],
    'TC VERIFY_WHEN_USER_CLICK_ON_NICK_NAME_TAB': [Critical, 'when user click on nick name button , user should all '
                                                             'related fields for nick name'],
    'TC_VERIFY_WITH_ADD_NICKNAME_BUTTON_IS_PRESENT': [Critical,
                                                      'when user click on nick name button , user should see nick '
                                                      'name , nick name id'],
    'Tc_VERIFY_THE_FUNCTIONALITY_OF_ADD_NICKNAME_BUTTON': [Critical, 'when user click on add nick name button,user '
                                                                     'should see pop-up to fil the details of nick'
                                                                     '(or) create new nick name'],

}
