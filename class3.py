from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="C:/Selenium Drivers/chromedriver")

# driver.get("https://www.wallashops.co.il/")
# wait = WebDriverWait(driver, 5)
# searchBar = wait.until(EC.element_to_be_clickable((By.ID, "search-input")))
# searchBar.click()


driver.get("http://testautomationpractice.blogspot.com/")
alertButton = driver.find_element_by_xpath('//button[@onclick="myFunction()"]').click()
WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()
# driver.switch_to_alert().accept()   -- DEPRECATED


driver.get("https://www.renuar.co.il/he/men.html")
driver.find_element_by_xpath("//a[text() = 'פייסבוק']").click()

hanldesList = driver.window_handles
currentTabId = driver.current_window_handle
for tabId in hanldesList:
    if tabId != currentTabId:
        driver.switch_to.window(tabId)
    print(driver.title)

