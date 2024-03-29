from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from os import path

APP_DIR = path.dirname(path.abspath("../prep_work/"))
APP = path.join(APP_DIR, 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'plaformVersion': '16.4',
    'deviceName': 'iPhone 14',
    'automationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

try:
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'messageInput'))).send_keys('Hello')
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn').click()
    saved = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'savedMessage').text
    assert saved == 'Hello'
    driver.back()

    wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    saved = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'savedMessage').text
    assert saved == 'Hello'
finally:
    driver.quit()
