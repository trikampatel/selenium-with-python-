from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
driver.get("G://trikam/upload.html")
driver.maximize_window()
time.sleep(5)



driver.find_element_by_id("icondemo").send_keys("C:/Users/Surajptl/Pictures/123.jpg")
