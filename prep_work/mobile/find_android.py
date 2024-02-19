from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path

APP_DIR = path.dirname(path.abspath("../prep_work/"))
APP = path.join(APP_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Login Screen')
    ))

    driver.find_element(MobileBy.CLASS_NAME, 'android.widget.TextView')
    driver.find_element(
        MobileBy.XPATH, '//android.widget.TextView[@text="Webview Demo"]')
finally:
    driver.quit()
