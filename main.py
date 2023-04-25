from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(
    executable_path = './chromedriver.exe'
)
for i in range(0,2):
    driver.get("http://pyotrk6c.beget.tech/")
    element = driver.find_element(By.ID, "sec2")
    element.click()
    element = driver.find_element(By.CLASS_NAME, "slider-next")
    for i in range(0, 5):
        time.sleep(3)
        element.click()
    element = driver.find_element(By.CLASS_NAME, "slider-prev")
    for i in range(0, 5):
        time.sleep(3)
        element.click()
