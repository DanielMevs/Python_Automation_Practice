from selenium import webdriver

caps = {
    'browserName': 'firefox'
}

driver = webdriver.Remote(
    command_executor='http://localhost:4444',
    desired_capabilities=caps
)
driver.quit()