from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.headless = True

driver = webdriver.Chrome("/usr/bin/chromedriver_linux64", options=options)

driver.get("https://google.com/")
print(driver.title)
driver.quit()