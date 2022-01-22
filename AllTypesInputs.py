from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#browser exposes an executable file

#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

driver.implicitly_wait(10)
# to maximize the browser window
driver.maximize_window()

#get method to launch the URL
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

#to refresh the browser
driver.refresh()
time.sleep(1)

driver.find_element_by_name("firstname").send_keys("Trikam")
time.sleep(2)

driver.find_element_by_name("lastname").send_keys("Patel")
time.sleep(2)

driver.find_element_by_xpath("//input[@value='Male']").click()
time.sleep(2)

driver.find_element_by_xpath("//input[@value='7']").click()
time.sleep(5)

#identifying the checkbox with xpath, then clck
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[6]/td[2]/span[2]/input")\
    .click()
time.sleep(2)

s = driver.find_element_by_xpath("//input[@type='file']")
#file path specified with send_keys
s.send_keys("G:\\trikam\\trikamphoto.png")
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[8]/td[2]/span[3]/input")\
    .click()
time.sleep(2)

select = Select(driver.find_element_by_name('continents'))
select.select_by_visible_text('Antartica')
time.sleep(2)

# upto this its fine
select = Select(driver.find_element_by_name('selenium_commands'))
select.select_by_visible_text('WebElement Commands')
time.sleep(5)

driver.find_element_by_name("submit").click()
