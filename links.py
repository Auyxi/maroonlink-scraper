from selenium import webdriver
from dotenv import load_dotenv
import os
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

f = open('organizations.in', 'w+')

load_dotenv(dotenv_path='info.env')

# open browser
driver = webdriver.Chrome()
driver.get("https://maroonlink.tamu.edu/organizations")

# tell orgs list to load everything
load_more = driver.find_element_by_xpath('//*[@id="react-app"]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/button/div/div/span')

while len(driver.find_elements_by_xpath('//*[@id="react-app"]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/button/div/div/span')) > 0:
    load_more.click()
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-app"]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/button/div/div/span')))
    except TimeoutException:
        break   

time.sleep(1)

orgs_list = driver.find_elements_by_css_selector('a[style*="display: block; text-decoration: none; margin-bottom: 20px;"')

# write orgs links to file
for org in orgs_list:
    f.write(org.get_attribute('href') + '\n')

f.close()