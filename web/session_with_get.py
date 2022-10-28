from selenium import webdriver

driver = webdriver.Firefox()
try:
    driver.get('https://the-internet.herokuapp.com')
finally:
    driver.quit()