from os import path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC

# APP_ANDROID info
CUR_DIR = path.dirname(path.abspath("../../prep_work/*"))
APP_ANDROID = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'https://dev-us-pao-0.headspin.io:7045/v0/39d8b4a2a37146ef8c83ecbe8f96e816/wd/hub'

#Webdriver URL
# https://dev-us-pao-0.headspin.io:7045/v0/39d8b4a2a37146ef8c83ecbe8f96e816/wd/hub

# CAPS
CAPS_ANDROID = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'appium:appPackage': 'com.appiumpro.the_app',
    'appium:appActivity': '.MainActivity',
    'deviceName': 'SM-A715F',
    'udid': 'R58N92C0XEZ',
    'headspin:capture': True,
    'headspin:controlLock': True
}

# LOGIN INFO
CORRECT_USERNAME = 'alice'
BAD_USERNAME = 'rui'
CORRECT_PASSWORD = 'mypassword'
BAD_PASSWORD = '1234567'

# ACESSIBILITY IDS
USERNAME_ID = 'username'
PASSWORD_ID = 'password'
LOGIN_ID = 'Login Screen'
LOGIN_BUTTON_ID = 'loginBtn'
ALERT_MESSAGE_ID = '//android.widget.TextView[@text="Invalid login credentials, please try again"]'
ALERT_OK_ID = '//android.widget.Button[@text="OK"]'
GOOD_LOGIN_ID = f'//android.widget.TextView[@text="You are logged in as {CORRECT_USERNAME}"]'
LOGOUT_BUTTON_ID = '//android.widget.TextView[@text="Logout"]'

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
        (MobileBy.ACCESSIBILITY_ID, USERNAME_ID)
    )).send_keys(username)
    driver.find_element(MobileBy.ACCESSIBILITY_ID,
                        PASSWORD_ID).send_keys(password)


def click_login_btn(driver):
    driver.find_element(MobileBy.ACCESSIBILITY_ID,
                        LOGIN_BUTTON_ID).click()


def logout(driver):
    driver.find_element(MobileBy.XPATH,
                        LOGOUT_BUTTON_ID).click()
