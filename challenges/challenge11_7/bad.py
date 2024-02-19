import time
from appium import webdriver

APP = 'path to your app'
APPIUM = 'http://localhost:4723'
CAPS = {
    'platformName': '?',
    'platformVersion': '?',
    'deviceName': '?',
    'automationName': '?',
    'app': APP,
}

# start session
driver = webdriver.Remote(APPIUM, CAPS)

# Test 1: test login works
time.sleep(4)  # wait for app to load
driver.find_element('?', '?').click()  # get to login screen
time.sleep(2)  # wait for login screen to load
driver.find_element('?', '?').send_keys('alice')  # enter valid username
driver.find_element('?', '?').send_keys('mypassword')  # enter valid password
driver.find_element('?', '?').click()  # click login button
time.sleep(4)  # wait for secret area to load
driver.find_element('?', '?')  # check that the correct username is displayed


# Test 2: test logout works
driver.find_element('?', '?').click()  # click logout button
time.sleep(2)  # wait for login page to load
driver.find_element('?', '?')  # check we're on the login page to prove logout was successful

# Quit session
driver.quit()