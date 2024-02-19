from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import warnings
warnings.simplefilter("ignore")

APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'appium:options': {
        'platformVersion': '16.4',
        'deviceName': 'iPhone 14 Plus',
        'automationName': 'XCUITest',
    },
    'browserName': 'Safari'
}

url = 'https://the-internet.herokuapp.com/'
login_url = 'https://the-internet.herokuapp.com/login'

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

try:
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    # driver.find_element(By.LINK_TEXT, 'Form Authentication')
    form_auth_link = wait.until(ec.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))
    form_auth_link.click()

    username = wait.until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#username')
    ))
    username.send_keys('tomsmith')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('SuperSecretPassword!')

    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    wait.until(ec.presence_of_element_located(
        (By.LINK_TEXT, 'Logout')
    )).click()

    wait.until(ec.url_to_be(login_url))

    flash = wait.until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#flash')
    ))

    assert 'logged out' in flash.text

    els = driver.find_elements(By.TAG_NAME, 'a')
    print(f'There were {len(els)} anchor elements')

    els = driver.find_elements(By.TAG_NAME, 'foo')
    print(f'There were {len(els)} anchor elements')

finally:
    driver.quit()
