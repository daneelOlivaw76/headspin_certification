from os import path
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CUR_DIR = path.dirname(path.abspath("../prep_work/"))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'
MESSAGE = 'Hello'
CAPS = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
    'app': APP,
}

driver = webdriver.Remote(APPIUM, CAPS)
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'messageInput'))).send_keys(MESSAGE)
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn').click()
    saved = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, MESSAGE))).text
    assert saved == MESSAGE
    driver.back()

    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    saved = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, MESSAGE))).text
    assert saved == MESSAGE

finally:
    driver.quit()
