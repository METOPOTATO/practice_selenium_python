from time import sleep
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By


chrome_options = uc.ChromeOptions()

chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument("--disable-popup-blocking")

chrome_options.add_argument("--profile-directory=Default")

chrome_options.add_argument("--ignore-certificate-errors")

chrome_options.add_argument("--disable-plugins-discovery")

chrome_options.add_argument("--incognito")

chrome_options.add_argument("user_agent=DN")

driver = uc.Chrome(options=chrome_options)

driver.delete_all_cookies()

# driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
driver.get("https://docs.google.com/spreadsheets/d/185BgOcBUFVwdhPivOSH7fV7cyDHnVPmIfUMRx-P2NFA/edit#gid=0")


txt_email = driver.find_element(
    By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
txt_email.send_keys("linhupdate6@gmail.com")

btn_next = driver.find_element(
    By.XPATH, '//*[@id="identifierNext"]/div/button/span')
btn_next.click()

sleep(1)
txt_pw = driver.find_element(
    By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
txt_pw.send_keys("1s2heaven@")

btn_next = driver.find_element(
    By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')

btn_next = driver.find_element(
    By.XPATH, '//*[@id="passwordNext"]/div/button')
btn_next.click()

sleep(20)
