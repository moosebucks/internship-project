from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.find_element(By.ID,'twotabsearchtextbox')
driver.find_element(By.ID,'nav-search-submit-button')
driver.find_element((By.XPATH, "//select[@name='url']")
