from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path="C:/Selenium Drivers/chromedriver")



driver.get("https://he-il.facebook.com/")
emailElement = driver.find_element_by_id("email")
emailElement.send_keys("Sahar@test.com")

passElement = driver.find_element_by_id("pass")
passElement.send_keys("123456")

driver.find_element_by_id("u_0_b").click()


driver.get("https://is.hit.ac.il/nidp/idff/sso?id=HITUserPassword&sid=0&option=credential&sid=0&target=https%3A%2F%2Fportal.hit.ac.il%2F")
userNameElement = driver.find_element_by_id("username")
userNameElement.send_keys("Name")

passElement = driver.find_element_by_id("password")
passElement.send_keys("1234")
driver.find_element_by_xpath('//input[@type="submit"]').click()
#-----------------------

driver.get("https://friends.walla.co.il/register")
userNameElement = driver.find_element_by_id("username")
userNameElement.send_keys("Sahar")

passElement = driver.find_element_by_xpath('//input[@type="password"]')
passElement.send_keys("123456")

fisrtNameElement = driver.find_element_by_id("fname")
fisrtNameElement.send_keys("First Name")

lastNameElement = driver.find_element_by_id("sname")
lastNameElement.send_keys("Sure Name")

cellphone = driver.find_element_by_id("postfix")
cellphone.send_keys("8008000")

prefixCombo = Select(driver.find_element_by_xpath('//select[@formcontrolname="prefix"]'))
prefixCombo.select_by_visible_text("052")

driver.find_element_by_id("gender-input-1").click()

driver.find_element_by_id("disclaimer").click()


driver.find_element_by_id("submit-button").click()




driver.get("https://www.alljobs.co.il/")
userNameElement = driver.find_element_by_xpath('//input[@type="text"][@ng-keyup="LogIn.GetSearchContent($event)"]')
userNameElement.send_keys("Name")

passElement = driver.find_element_by_xpath('//input[@type="password"]')
passElement.send_keys("1234")
driver.find_element_by_xpath('//button[@ng-click="LogIn.LogIn()"]').click()



driver.close()

