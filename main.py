from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

EMAIL = os.environ.get('LINKEDIN_EMAIL')
PASSWORD = os.environ.get('LINKEDIN_PASSWORD')

chrome_driver_path = '/Users/admin/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?f_WT=2%2C1%2C3&geoId=100752109&keywords=junior%20developer&location='
           'Scotland%2C%20United%20Kingdom')

signin_button_one = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
signin_button_one.click()

time.sleep(5)

email = driver.find_element(By.NAME, 'session_key')
password = driver.find_element(By.NAME, 'session_password')
signin_button_page_two = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
signin_button_page_two.click()




