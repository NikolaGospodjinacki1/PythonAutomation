from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="/usr/bin/chromedriver")


def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def main():
    driver = get_driver()
    driver.find_element(by=By.ID, value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by=By.ID, value="id_password").send_keys("automatedautomated" +
    Keys.RETURN)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="/html/body/nav/div/a").click()
    print(driver.current_url)
    time.sleep(2)
print(main())