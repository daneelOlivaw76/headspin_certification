from os import path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC

# APP_ANDROID info
CUR_DIR = path.dirname(path.abspath("../../prep_work/*"))
APP_IOS = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'

CAPS_IOS = {
    'platformName': 'iOS',
    'plaformVersion': '16.4',
    'deviceName': 'iPhone 14',
    'automationName': 'XCUITest',
    'app': APP_IOS,
}

# LOGIN INFO
CORRECT_USERNAME = 'alice'
BAD_USERNAME = 'rui'
CORRECT_PASSWORD = 'mypassword'
BAD_PASSWORD = '1234567'

# ACESSIBILITY IDS
USERNAME_ID = '//XCUIElementTypeOther[@name="username"]'
PASSWORD_ID = '//XCUIElementTypeOther[@name="password"]'
LOGIN_ID = 'Login Screen'
LOGIN_BUTTON_ID = '(//XCUIElementTypeOther[@name="loginBtn"])[2]'
ALERT_MESSAGE_ID = 'Invalid login credentials, please try again'
# ALERT_MESSAGE_ID = '//XCUIElementTypeStaticText[@name="Invalid login credentials, please try again"]'
ALERT_OK_ID = 'OK'
GOOD_LOGIN_ID = f'You are logged in as {CORRECT_USERNAME}'
LOGOUT_BUTTON_ID = '//XCUIElementTypeOther[@label="Logout"]'

# TEST STRINGS
ALERT_MESSAGE_TXT = 'Invalid login credentials'


# UTIL FUNCTIONS
def login(driver, wait, value):
    if value:
        username = CORRECT_USERNAME
        password = CORRECT_PASSWORD
    else:
        username = BAD_USERNAME
        password = BAD_PASSWORD

    # Navigate to the Login Screen
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, LOGIN_ID)
    )).click()

    # Enter an incorrect username and password
    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, USERNAME_ID)
    )).send_keys(username)
    driver.find_element(MobileBy.XPATH,
                        PASSWORD_ID).send_keys(password)
    # print("Credentials inserted")


def click_login_btn(driver):
    driver.find_element(MobileBy.XPATH,
                        LOGIN_BUTTON_ID).click()
    # print("Login Button clicked")


def logout(driver):
    driver.find_element(MobileBy.XPATH,
                        LOGOUT_BUTTON_ID).click()
    # print("Logout button clicked")
