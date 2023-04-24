from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(
    executable_path = './chromedriver.exe'
)
while(45645):
    driver.get("http://pyotrk6c.beget.tech/")
    element = driver.find_element(By.ID, "sec2")
    element.click()
    element1 = driver.find_element(By.CLASS_NAME, "slider-next")
    for i in range(0, 5):
        element1.click()
        time.sleep(1)
    element2 = driver.find_element(By.CLASS_NAME, "slider-prev")
    for i in range(0, 5):
        element2.click()
        time.sleep(1)
