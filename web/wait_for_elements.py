from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
ff_options = Options()
ff_options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

chr_options = Options()
chr_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# driver = webdriver.Firefox(options=ff_options, executable_path=r"C:\Users\daniel.mevs\Documents"
#                                                             "\Python_Refresher_Automation\drivers\geckodriver.exe")
# chr_options = Options()
# chr_options
# driver = webdriver.Firefox(options=ff_options)
driver = webdriver.Chrome()

# driver = webdriver.Firefox()

# driver = webdriver.Firefox(executable_path=r'C:\Users\daniel.mevs\Documents\Python_Refresher_Automation\drivers\geckodriver.exe')
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))
    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/'))
finally:
    time.sleep(5)
    driver.quit()
