def test_cases(index):
    return testCases[index]


critical = "Critical"
major = "Major"
moderate = "Moderate"
low = "Low"

testCases = {

    0: [critical, 'When user goes to Canonizer main page, page should be loaded Properly'],
    1: [critical, 'In Home page, when user click "Register" button, User should see User Registration Page'],
    2: [critical, 'In Home page, when user click "Login" button,  User should see Login Page'],
    3: [critical, 'In Login Page, when user login with a valid user, he should see Home Page'],

}
