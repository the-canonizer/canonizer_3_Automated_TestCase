def test_cases(index):
    return testCases[index]


critical = "Critical"
major = "Major"
moderate = "Moderate"
low = "Low"

testCases = {

    0: [critical, 'When user goes to Canonize main page, page should be loaded Properly'],
    1: [critical, 'In Home page,when user click "Register" button, user should see register page'],
    2: [critical, 'When user fill all fields in register page, user should see canonize main page'],
    3: [critical, 'In Login Page, when user click on close icon in login pop_up page, user should see Home Page'],
    4: [critical, 'when user try to create registration with empty fields , user should see proper error message'],
    5: [critical, 'When user should try to create account with invalid data,user should see proper error message'],
    6: [critical, 'When user should try to create registration with already existed dats, user should see proper '
                  'error message'],
    7: [critical, 'When user should try to create registration without entering mandatory field,user should see proper '
                  'error message'],
    8: [critical, 'When user should verify the registration tittle identification,user should get the tittle'],
    9: [critical, 'When user should try to register with first name empty,user should get proper error message'],
    10: [critical,
         'When suer should try to register without entering fields inputs,user should get proper error message'],
    11: [critical, 'When user should try to register with invalid password,user should see proper error message'],
    12: [critical,
         'When user should try to register with invalid confirm password,user should see proper error message'],
    13: [critical, 'When user should try to register with invalid email,user should should see proper error message'],
    14: [critical, 'When user should try to register without entering captcha,user should see proper error message'],
    15: [critical, 'When user should click on login dropdown button,user should see account setting page option'],
    16: [critical, 'When user should click on login button with valid email and password,user should see main page'],
    17: [critical, 'When user should click on close on on login page, user should go to canonize main page'],
    18: [critical, 'When user should verify the tittle of "log in canonize page" in login page,user should get '
                   'verified tittle'],
    19: [critical, 'When user should try to login with registered credentials, user should see main page'],
    20: [critical, 'When user should try to login with invalid email, user should see proper error message'],
    21: [critical, ' When user should click on checkbox on login page, user should see marked with blue mark'],
    22: [critical, 'When user should click on login button with empty fields, user should see proper error message'],
    23: [critical, 'When user should verify tittle of "forget password, user should get proper tittle'],
    24: [critical, 'When user should click register now link button on login page ,user should redirect canonize '
                   'register page'],
    25: [critical, 'When user should click one time verification code without entering email, user should see proper '
                   'error message'],
    26: [critical, 'When user should click one time verification code with invalid email,user should see proper error '
                   'message'],
    27: [critical, 'when '],
    28: [critical, 'When user should click on login drop down button ,user should redirect to account setting page'],

}
