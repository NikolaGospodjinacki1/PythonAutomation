
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt


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


def clean_text(text):
   """ Extract only the temperature from text"""
   output = float(text.split(": ")[1])
   return output

def write_file(text):
    ### Format used for file names ###
    now= dt.now()
    format = "%d_%m_%y_%H_%M_%S"
    suffix = ".txt"
    now_formatted= now.strftime(format)
    ### Write the current avg data to the newly made file ###
    with open(f"{now_formatted}.{suffix}", 'w') as f:
        f.write(text) 

def main():
    
    ### Enter credentials on login page and go to homepage ### 
    driver = get_driver()
    driver.find_element(by=By.ID, value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by=By.ID, value="id_password").send_keys("automatedautomated" +
    Keys.RETURN)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="/html/body/nav/div/a").click()
    time.sleep(2)
    ### Continuously scrape the current avg temp info and put it in a separate file
    while True:
        time.sleep(2)
    ### Get current value ###
        element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/h1[2]").text
    ### Write to file using the function write_file after converting to string ###
        text = str(clean_text(element))
        write_file(text)

        
print(main()) 