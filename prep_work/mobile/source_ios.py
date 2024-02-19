import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path
import sys

APP_DIR = path.dirname(path.abspath("../prep_work/"))
APP = path.join(APP_DIR, 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'plaformVersion': '16.4',
    'deviceName': 'iPhone 14 Pro',
    'automationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

try:
    time.sleep(5)
    with open('page_source.xml', 'w') as f:
        print(driver.page_source, file=f)

finally:
    driver.quit()
