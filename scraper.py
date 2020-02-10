from selenium import webdriver
from dotenv import load_dotenv
import os
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

load_dotenv(dotenv_path='info.env')

# open browser
driver = webdriver.Chrome()
driver.get("https://maroonlink.tamu.edu/organizations")

# sign in process
""" sign_in = driver.find_elements_by_xpath('//*[@id="discovery-bar"]/div/header[1]/div/a[2]')[0]
sign_in.click()

# username
user = os.getenv("USER")

user_login = driver.find_elements_by_xpath('//*[@id="username"]')[0]
user_login.send_keys(user)

user_submit = driver.find_elements_by_xpath('//*[@id="fm1"]/button')[0]
user_submit.click()

# password
password = os.getenv("PASS")

password_login = driver.find_elements_by_xpath('//*[@id="password"]')[0]
password_login.send_keys(password)

password_submit = driver.find_elements_by_xpath('//*[@id="fm1"]/button')[0]
password_submit.click()

# duo page
WebDriverWait(driver, 10).until(EC.title_contains("Organizations"))
# you have 10 seconds to manually click the button for duo and sign in """


# tell orgs list to load everything
""" load_more = driver.find_element_by_xpath('//*[@id="react-app"]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/button/div/div/span')

while len(driver.find_elements_by_xpath('//*[@id="react-app"]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/button/div/div/span')) > 0:
    load_more.click()
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-app"]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/button/div/div/span')))
    except TimeoutException:
        break """

load_more = driver.find_element_by_xpath('//*[@id="react-app"]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/button/div/div/span')
load_more.click()

time.sleep(1)

# print(len(driver.find_elements_by_css_selector('a[style*="display: block; text-decoration: none; margin-bottom: 20px;"')))

orgs_list = driver.find_elements_by_css_selector('a[style*="display: block; text-decoration: none; margin-bottom: 20px;"')

for org in orgs_list:
    print(org.get_attribute('href'))

