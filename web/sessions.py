from selenium import webdriver

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# options = webdriver.EdgeOptions()
#options.use_chromium = True
#driver = webdriver.Edge(options=options)
driver.quit()