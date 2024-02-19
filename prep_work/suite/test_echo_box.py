from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_echo_box(driver_ios):
    wait = WebDriverWait(driver_ios, 10)
    wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'messageInput'))).send_keys('Hello')
    driver_ios.find_element(MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn').click()
    saved = driver_ios.find_element(MobileBy.ACCESSIBILITY_ID, 'savedMessage').text
    assert saved == 'Hello'
    driver_ios.back()

    wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    saved = driver_ios.find_element(MobileBy.ACCESSIBILITY_ID, 'savedMessage').text
    assert saved == 'Hello'
