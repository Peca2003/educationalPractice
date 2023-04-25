import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
class MyTestCase(unittest.TestCase):
    driver.get("http://pyotrk6c.beget.tech/")

    def testSection2(self):
        self.section2 = driver.find_element(By.ID, "sec2")
        time.sleep(2)
        self.section2.click()

    def testNext(self):
        self.buttonNext = driver.find_element(By.CLASS_NAME, "slider-next")
        for i in range(0, 5):
            time.sleep(1)
            self.buttonNext.click()

    def testPrev(self):
        self.buttonPrev = driver.find_element(By.CLASS_NAME, "slider-prev")
        for i in range(0, 5):
            time.sleep(1)
            self.buttonPrev.click()
if __name__ == '__main__':
    unittest.main()
