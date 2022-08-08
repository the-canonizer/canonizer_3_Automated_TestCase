def test_cases(index):
    return testCases[index]


Critical = "Critical"
major = "Major"
moderate = "Moderate"
low = "Low"

testCases = {


    'TC_CLICK_FORGOT_PASSWORD_LINK': [Critical, 'User should see forgot password link'],
    'TC_SUBMIT_BUTTON_WITH_VALID_EMAIL_AND_CHECK_OTP_SCREEN': [Critical, 'User must see OTP screen on submit button'],
    'TC_SUBMIT_BUTTON_WITH_INVALID_EMAIL': [Critical, 'User must see error message with invalid email'],
    'TC_SUBMIT_BUTTON_WITH_EMPTY_EMAIL': [Critical, 'User must see error message when email is left empty'],
    'TC_SUBMIT_EMPTY_OTP': [Critical, 'User must see error message when OTP is left empty'],
    'TC_SUBMIT_INVALID_LENGTH_OTP': [Critical, 'User must see error message when submit invalid length OTP'],
    'TC_SUBMIT_BUTTON_WITH_UNREGISTERED_EMAIL': [Critical, 'User must see error message for email which is unregistered'],
    'TC_CROSS_ICON_ON_FORGOT_MODAL': [Critical, ' User must be able to click cross icon and modal should close'],
    'TC_CROSS_ICON_ON_OTP_MODAL': [Critical, 'User must be able to click cross icon and modal should close'],
    'TC_ENTER_VALID_OTP': [Critical, ' User must enter valid OTP and must see change password page'],
    'TC_CLICK_CREATE_TOPIC_WITH_USER_LOGIN': [Critical, 'User must be able to click Create topic button on login'],
    'TC_CLICK_CREATE_TOPIC_WITHOUT_USER_LOGIN': [Critical, 'User must see login page when click create topic button '
                                                           'when not logged in'],
    'TC_CREATE_TOPIC_WITH_BLANK_TOPIC_NAME': [Critical, ' User must not be able to create topic with blank name'],
    'TC_CREATE_TOPIC_WITH_VALID_DATA': [Critical, 'User must be able to create a new topic with valid data'],
    'TC_CREATE_TOPIC_WITH_BLANK_SPACES_TOPIC_NAME': [Critical, ' User must see error message when enter blank spaces'],
    'TC_CREATE_NEW_TOPIC_WITH_ENTER_KEY': [Critical, 'User must be able to create new topi when press EnterKey'],
    'TC_CREATE_NEW_TOPIC_WITH_TRAILING_SPACES': [Critical, 'Trailing spaces must be removed '
                                                 'and new topic is created'],
    'TC_CREATE_TOPIC_WITH_DUPLICATE_NAME': [Critical, 'Duplicate topic name must not be created'],
    'TC_CREATE_NEW_TOPIC_WITH_SPECIAL_CHARS': [Critical, 'Topic must not be created when invalid data is entered'],
    'TC_CREATE_NEW_WITHOUT_MANDATORY_FIELDS_DATA': [Critical, 'User must not be able to create a topic '
                                                    'when mandatory fields are blank'],
    'TC_CREATE_NEW_TOPIC_ENTERING_DATA_ONLY_IN_MANDATORY_FIELDS': [Critical, ' User must be able to create a new '
                                                                   'topic when enter data only in mandatory fields'],
    'TC_CLICK_ON_CANCEL_BUTTON': [Critical, 'User must not be able to create a topic on click '
                                  'cancel button instead redirect to home page'],
    'TC_TOPIC_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK': [Critical, 'User must see mandatory fields marked '
                                                                'with asterisk'],
    'TC_CHECK_NO_THREAD_AVAILABILITY': [Critical, 'User must see no data found message'],
    'TC_CLICK_CAMP_FORUM_BUTTON': [Critical, 'User must be able to click on camp forum button'],
    'TC_CLICK_CREATE_THREAD_BUTTON': [Critical, 'User must be able to click on create thread button'],
    'TC_LOAD_ALL_THREADS_PAGE': [Critical, 'User must see all threads under all threads section'],
    'TC_LOAD_MY_THREADS_PAGE': [Critical, 'User must see only their threads when click my threads button'],
    'TC_LOAD_MY_PARTICIPATION_PAGE': [Critical, 'User must see participation page on click the button'],
    'TC_LOAD_TOP_10_THREADS_PAGE': [Critical, 'User must see top 10 threads on this page'],
    'TC_CREATE_THREAD_WITH_VALID_DATA': [Critical, 'User must be able to create a thread'],
    'TC_CREATE_THREAD_WITH_BLANK_TITLE': [Critical, 'User must not be able to create thread and see error message'],
    'TC_CREATE_THREAD_WITH_SPECIAL_CHARS': [Critical, 'User must be able to create thread when enter special chars'],
    'TC_CREATE_THREAD_WITH_BLANK_MANDATORY_FIELDS': [Critical, 'User must not be able to create thread '
                                                               'and see error message'],
    'TC_CREATE_THREAD_WITH_DUPLICATE_TITLE': [Critical, 'User must not be able to create thread'],
    'TC_CREATE_THREAD_WITH_VALID_DATA_WITH_ENTER_KEY': [Critical, 'User must be able to create thread with enter key'],
    'TC_CREATE_THREAD_WITH_TRAILING_SPACES': [Critical, 'User must be able to create a top with trailing spaces'],
    'TC_THREAD_PAGE_MANDATORY_FIELDS_ARE_MARKED_WITH_ASTERISK': [Critical, 'User must see asterisk symbol '
                                                                 'for mandatory fields'],
    'TC_LOAD_EDIT_THREAD_PAGE': [Critical, 'User must be able to see edit thread page on click edit icon'],
    'TC_CLICK_ON_BACK_BUTTON': [Critical, 'User must redirect to camp forum page on click back button'],
    'TC_UPDATE_THREAD': [Critical, 'User must be able to edit and update thread on submit button'],
    'TC_EDIT_THREAD_WITH_SPECIAL_CHARS': [Critical, 'Thread title should be updated if entered special chars'],
    'TC_CLICK_ON_EDIT_BACK_BUTTON': [Critical, 'On click back button user must redirect to camp forum page'],
    'TC_LOAD_THREAD_POSTS_PAGE': [Critical, 'User must be redirected tp thread post page on click thread link'],
    'TC_THREAD_POST_WITH_VALID_DATA': [Critical, 'User must be able to reply to a thread with all valid data'],
    'TC_THREAD_POST_WITH_EMPTY_REPLY': [Critical, 'User must see error message if reply field is left blank'],
    'TC_CLICK_ON_POST_BACK_BUTTON': [Critical, 'User must be navigated to camp forum page on click back button'],
    'TC_VERIFY_NICK_NAME_LINK_ON_POST_PAGE': [Critical, 'User must be navigated to the profile on  '
                                              'click the nick name link'],
    'TC_VERIFY_EDIT_REPLY_TO_THREAD': [Critical, 'User must be able to edit reply n click edit icon']










}
