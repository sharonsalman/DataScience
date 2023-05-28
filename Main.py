import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options , service=Service(ChromeDriverManager().install()))
driver.get('https://www.nadlan.gov.il/')

search = driver.find_element(By.ID, 'SearchString')
search.send_keys("חיפה")
search_box = driver.find_element(By.ID, 'submitSearchBtn')
search_box.send_keys(Keys.RETURN)
print(driver.page_source)
try:
    marging_container = WebDriverWait(driver , 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "marging-container"))
    )
    print(marging_container.page_source)
except:
    driver.quit()


driver.quit()