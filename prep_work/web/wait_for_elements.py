from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

page = 'https://the-internet.herokuapp.com/'

driver = webdriver.Firefox()

try:
    wait = WebDriverWait(driver, 10)

    driver.get(page)

    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))

    wait.until(EC.url_to_be(page))
finally:
    driver.quit()
