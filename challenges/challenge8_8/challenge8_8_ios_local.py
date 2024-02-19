from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium import webdriver
from headspin_certification.challenges.challenge8_8 import constants8_8_ios_local as const

# DRIVER
driver = webdriver.Remote(const.APPIUM, const.CAPS_IOS)

try:
    wait = WebDriverWait(driver, 10)

    const.login(driver, wait, False)

    # Attempt to log in
    const.click_login_btn(driver)

    # Assert that the alert which pops up has the text "Invalid login credentials"
    alert_message = wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, const.ALERT_MESSAGE_ID)
    )).text

    assert const.ALERT_MESSAGE_TXT in alert_message

    # Dismiss the alert
    driver.find_element(MobileBy.ACCESSIBILITY_ID,
                        const.ALERT_OK_ID).click()
    driver.back()
    driver.back()

    # Enter the correct username and password (username: alice, password: mypassword)
    const.login(driver, wait, True)

    # Attempt to log in
    const.click_login_btn(driver)

    # Assert that the resulting view mentions the user's username
    logged_message = wait.until(ec.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, const.GOOD_LOGIN_ID)
    )).text

    assert const.CORRECT_USERNAME in logged_message

    # Log out
    const.logout(driver)

    # Assert that the username field is now visible again
    assert wait.until(ec.presence_of_element_located(
        (MobileBy.XPATH, const.USERNAME_ID)
    ))

finally:
    driver.quit()
