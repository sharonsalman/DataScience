import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options , service=Service(ChromeDriverManager().install()))
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.send_keys("test")
search.send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()