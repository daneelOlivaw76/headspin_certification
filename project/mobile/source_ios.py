import time
from os import path
from appium import webdriver

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'
CAPS = {
    'platformName': 'iOS',
    'platformVersion': '13.6',
    'deviceName': 'iPhone 11',
    'automationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(APPIUM, CAPS)
try:
    time.sleep(4)
    print(driver.page_source)
finally:
    driver.quit()
