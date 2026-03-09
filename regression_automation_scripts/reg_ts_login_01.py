import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
driver.find_element(By.LINK_TEXT,"Log in").click()
driver.find_element(By.XPATH,"//input[@value='Register']").click()

driver.find_element(By.ID,"gender-male").click()

driver.find_element(By.ID,"FirstName").send_keys("John")
time.sleep(3)