from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

page = 'https://the-internet.herokuapp.com/'
headspin_url = 'https://dev-id-jk-0.headspin.io:9095/v0/a98cacf6d76d479c8bc2c10edf704ab6/wd/hub'

caps = {
    "headspin:capture": True,  # False if session not to be persisted
    "headspin:initialScreenSize": {
        "width": 1920,
        "height": 1080
    },
    "browserName": "firefox",
    "browserVersion": "79.0"
}

driver = webdriver.Remote(
    command_executor=headspin_url,
    desired_capabilities=caps
)


def get_elements():
    els = driver.find_elements(By.XPATH, '//*[@id="elements"]//*')
    return els


def add_element():
    new_element = driver.find_element(
        By.CSS_SELECTOR, '.example > button').click()

    return new_element


def delete_elements(position=0):
    numElements = len(get_elements()) - 1
    get_elements()[numElements - position].click()


try:
    wait = WebDriverWait(driver, 10)
    driver.get(page)

    # Add Remove Elements
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/add_remove_elements/"]')
    )).click()

    content = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="elements"]')
    ))

    assert len(get_elements()) == 0
    add_element()
    assert len(get_elements()) == 1
    add_element()
    assert len(get_elements()) == 2

    delete_elements(1)
    assert len(get_elements()) == 1
    delete_elements(0)
    assert len(get_elements()) == 0

    driver.back()

    # Dynamic Loading
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/dynamic_loading"]')
    )).click()

    driver.find_element(
        By.CSS_SELECTOR, 'a[href="/dynamic_loading/2"]').click()

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'button')
    )).click()

    dynamic_element = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#finish > h4')
    ))

    assert dynamic_element.text == 'Hello World!'

    driver.back()
    driver.back()

    # Frames
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/frames"]')
    )).click()

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/iframe"]')
    )).click()

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.tox-mbtn__select-label')
    )).click()

    driver.find_element(By.CSS_SELECTOR, '.tox-collection__item-label').click()
    iframe = driver.find_element(By.CSS_SELECTOR, '#mce_0_ifr')
    driver.switch_to.frame(iframe)
    text_box = driver.find_element(By.XPATH, '//*[@id="tinymce"]')
    text_box.send_keys('Hello from automation!')
    assert text_box.text == 'Hello from automation!'

    driver.switch_to.default_content()
    driver.back()
    driver.back()
finally:
    driver.quit()
