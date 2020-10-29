import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-features=NetworkService")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-features=VizDisplayCompositor")

driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrome_options)


class account:
    login = 'YOUR LOGIN CODE HERE'
    password = 'YOUR PASS PIN HERE'

def log(msg):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time, msg)

if __name__ == "__main__":
    driver.get("https://app.tangerino.com.br")
    time.sleep(2)
    log("opening tangerino")
    driver.get("https://app.tangerino.com.br/Tangerino/?wicket:interface=:1:loginForm:loginFuncionario::ILinkListener::")
    time.sleep(2)
    driver.find_element_by_xpath("//input[@type='text']").send_keys(account.login)
    time.sleep(1)
    driver.find_element_by_xpath("//input[@placeholder='PIN']").send_keys(account.password)
    time.sleep(1)
    driver.find_element_by_xpath("//input[@type='submit']").click()
    log("logged in tangerino")
    time.sleep(5)
    
    driver.switch_to_frame(0)
    driver.find_element_by_xpath("//input[@placeholder='PIN']").send_keys(account.password)
    time.sleep(1)
    driver.find_element_by_xpath("//button[@id='registraPonto']").click()
    log("point successfully registered")
    time.sleep(10)
    driver.quit()