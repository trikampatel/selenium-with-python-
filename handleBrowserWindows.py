from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)

twobrowsers=driver.window_handles

for handle in twobrowsers:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        time.sleep(5)
        driver.close()

