
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

driver.implicitly_wait(5)

driver.get("https://www.travolook.in/")


time.sleep(2)
#driver.find_elements(By.ID, "flying_from_N").send_keys("Delhi").click()
driver.find_elements_by_id("flying_frin_N").send_keys("Delhi").click()
time.sleep(2)
driver.find_elements(By.ID, "flying_to_N").send_keys("Mumbai")
time.sleep(2)



time.sleep(2)

#driver.find_elements_by_id(By.ID, "//*[@id="searchengine_btn"]").click()
driver.find_elements_by_xpath("//*[@id='searchengine_btn']").click()


driver.quit()
