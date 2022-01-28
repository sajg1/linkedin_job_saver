from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os

EMAIL = os.environ.get('LINKEDIN_EMAIL')
PASSWORD = os.environ.get('LINKEDIN_PASSWORD')

chrome_driver_path = '/Users/admin/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?f_WT=2%2C1%2C3&geoId=100752109&keywords=junior%20developer&location='
           'Scotland%2C%20United%20Kingdom')

# SIGNIN AND MAXIMISE WINDOW
signin_button_one = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
signin_button_one.click()
driver.maximize_window()
time.sleep(3)

email = driver.find_element(By.NAME, 'session_key')
password = driver.find_element(By.NAME, 'session_password')
signin_button_page_two = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
signin_button_page_two.click()

# CLOSE MESSAGING POP UP
message_pop_up = driver.find_element(By.CLASS_NAME, 'msg-overlay-bubble-header__details')
message_pop_up.click()
time.sleep(2)

# ACCESS ALL JOBS ON LEFT HAND SIDE
jobs = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')

for job in jobs:
    job.click()
    time.sleep(2)

    # SAVE JOB POST
    job_save_button = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
    job_save_button.click()
    time.sleep(2)

    # DISMISS NOTIFICATION BOTTOM LEFT
    toast = driver.find_element(By.CLASS_NAME, 'artdeco-toast-item__dismiss')
    toast.click()

    # SCROLL TO COMPANY SECTION OF JOB DESCRIPTION AND FOLLOW COMPANY
    time.sleep(3)
    job_description = driver.find_element(By.CLASS_NAME, 'jobs-search__right-rail')
    job_description.click()
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    html.send_keys(Keys.PAGE_UP)
    time.sleep(2)
    try:
        company_follow = driver.find_element(By.CLASS_NAME, 'follow')
        company_follow.click()
    except NoSuchElementException:
        continue
    time.sleep(2)

    # DISMISS NOTIFICATION BOTTOM LEFT
    toast = driver.find_element(By.CLASS_NAME, 'artdeco-toast-item__dismiss')
    toast.click()







