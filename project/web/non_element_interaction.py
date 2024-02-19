from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# caps = {
    # "browserName": "firefox",
# }
# driver = webdriver.Remote(
    # command_executor='https://dev-us-pao-0.headspin.io:9093/v0/5a2cc04759594618b01a9aa8b9cbc2ac/wd/hub',
    # desired_capabilities=caps
# )
try:
    driver.get('https://the-internet.herokuapp.com')

    driver.save_screenshot('screen.png')

    cur_handle = driver.current_window_handle
    handles = driver.window_handles
    driver.switch_to.window(handles[0])
    driver.switch_to.window(cur_handle)

    driver.get('https://the-internet.herokuapp.com/iframe')
    frame = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(frame)
    driver.find_element(By.CSS_SELECTOR, '#tinymce').send_keys('in iframe')
    driver.switch_to.default_content()

    driver.back()
    driver.refresh()
    driver.find_element(By.LINK_TEXT, 'JavaScript Alerts').click()

    driver.find_element(By.XPATH, '//button[. = "Click for JS Alert"]').click()
    driver.switch_to.alert.accept()

    driver.maximize_window()
finally:
    driver.quit()
