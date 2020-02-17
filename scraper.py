from selenium import webdriver
from dotenv import load_dotenv
import os
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import json

load_dotenv(dotenv_path='info.env')

# setup browser
driver = webdriver.Chrome()
driver.get('https://maroonlink.tamu.edu/organizations')

# sign in process
sign_in = driver.find_elements_by_xpath('//*[@id="discovery-bar"]/div/header[1]/div/a[2]')[0]
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
# you have 10 seconds to manually click the button for duo and sign in


# setup data for loading
f = open('organizations.in', 'r')
links = f.readlines()
f.close()
orgs = []

# begin loading data
for org in links:
    driver.get(org)

    x = {}

    x["name"] = driver.find_element_by_css_selector("h1[style*='padding: 13px 0px 0px 85px;'").text
    try:
        x["desc"] = driver.find_element_by_xpath("//*[@id='react-app']/div/div[1]/div/div/div[1]/div[1]/div/div[2]/p").text
    except NoSuchElementException:
        x["desc"] = ""
    x["people"] = []

    time.sleep(1)

    menus = driver.find_elements_by_css_selector('span[style*="position: relative; opacity: 1; font-size: 16px; letter-spacing: 0px; text-transform: uppercase; font-weight: 500; margin: 0px; user-select: none; padding-left: 16px; padding-right: 16px; color: rgb(0, 0, 0);"')
    if len(menus) == 1:
        menus[0].click()
    else:
        menus[1].click()
        
    time.sleep(1)

    while len(driver.find_elements_by_css_selector('span[style*="position: relative; opacity: 1; font-size: 16px; letter-spacing: 0px; text-transform: uppercase; font-weight: 500; margin: 0px; user-select: none; padding-left: 16px; padding-right: 16px; color: rgb(0, 0, 0);"')) > 0:
        driver.find_element_by_css_selector('span[style*="position: relative; opacity: 1; font-size: 16px; letter-spacing: 0px; text-transform: uppercase; font-weight: 500; margin: 0px; user-select: none; padding-left: 16px; padding-right: 16px; color: rgb(0, 0, 0);"').click()
        try:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[style*="position: relative; opacity: 1; font-size: 16px; letter-spacing: 0px; text-transform: uppercase; font-weight: 500; margin: 0px; user-select: none; padding-left: 16px; padding-right: 16px; color: rgb(0, 0, 0);"')))
        except TimeoutException:
            break   

    people_list = driver.find_elements_by_css_selector('div[style="font-size: 16px; overflow: hidden; text-overflow: ellipsis;"')

    for person in people_list:
        x["people"].append(person.text)

    orgs.append(x)
    print(x)

# write out json data
f = open('org_data.json', 'w+')
f.write(json.dumps(orgs))
f.close()