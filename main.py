from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/admin/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?f_WT=2%2C1%2C3&geoId=100752109&keywords=junior%20developer&location='
           'Scotland%2C%20United%20Kingdom')

signin_button = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
signin_button.click()

