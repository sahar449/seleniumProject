from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome(executable_path="C:/Selenium Drivers/chromedriver")
from selenium.webdriver.support.select import Select

# driver.get("https://www.jobmaster.co.il/code/korot/password.asp")
#
# # print the title the page (the tab name)
# print(driver.title)
#
# emailElement = driver.find_element_by_name("pemail")
# passwordElement = driver.find_element_by_xpath('//input[@name="password"]')
#
# emailElement.send_keys("name")
# passwordElement.send_keys("12345")
#
# # talk a screenshot of the page
# driver.get_screenshot_as_file("C:/Users/סהר/Desktop/pic.png")


#---------------------------------
# driver.get("https://www.ynet.co.il")
# time.sleep(3)
# driver.get("https://www.mako.co.il")
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()



# driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
# button1 = driver.find_element_by_xpath("//button[@onClick = 'myAlertFunction()']")
# print("isDisplayed:", button1.is_displayed())
# print("isEnabled:", button1.is_enabled())

#----------
# driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
# toggelButton = driver.find_element_by_xpath('//button[@onclick="myFunction()"]')
# clickMeButton = driver.find_element_by_id("myDIV")
# print("display : " , clickMeButton.is_displayed())
# toggelButton.click()
# print("display : " , clickMeButton.is_displayed())
# # כדי לבחור כפתור בצ'ק בוקס משתמשים בפונקציה is selected
# #------------------

# driver.get("https://www.jobmaster.co.il/code/korot/password.asp")
# userNameElement = driver.find_element_by_xpath('//input[@name="pemail"]')
# userNameElement.send_keys("name")
# passElement = driver.find_element_by_xpath('//input[@name="password"]')
# passElement.send_keys("1234")
# driver.find_element_by_xpath('//input[@value="התחבר"]').click()

#--------------------------------------

# driver.get('https://www.wallashops.co.il/RegisterCustomer')
# print(driver.title)
# userNameElement = driver.find_element_by_xpath('//input[@name="FirstName"]')
# userNameElement.send_keys("name")
# LastNameElement = driver.find_element_by_xpath('//input[@name="LastName"]')
# LastNameElement.send_keys("Last")
# geder = driver.find_element_by_id("genderRadioMale").click()
# driver.get_screenshot_as_file("C:/Users/סהר/Desktop/pic.png")

#----------------------------
# driver.get("https://www.wallashops.co.il/")
# time.sleep(3)
# driver.get("https://www.youtube.com/watch?v=oQbh5Kvet04&list=RDzEf423kYfqk&index=4")
# time.sleep(5)
# driver.back()
# time.sleep(5)
# driver.forward()

#---------------
# driver.get("https://www.youtube.com/watch?v=aJXd_64QHqo&list=RDzEf423kYfqk&index=9")
# searchButton = driver.find_element_by_id('img')
# print("The button is display : " , searchButton.is_displayed())
# print("The button is enabled" , searchButton.is_enabled())

#---------------------
# driver.get('https://www.renuar.co.il/he/storelocator/')
# city = Select (driver.find_element_by_id("area-select"))
# city.select_by_visible_text("מרכז")
#--------------------
# driver.get("https://www.renuar.co.il/he/storelocator/")
# city = Select (driver.find_element_by_id("area-select"))
# chooseCity = driver.find_element_by_xpath('//option[@value="דרום"]')
# print("display : " , chooseCity.is_displayed())
# chooseCity.click()
# print("display : " , chooseCity.is_displayed())




# driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
# toggelButton = driver.find_element_by_xpath('//button[@onclick="myFunction()"]')
# clickMeButton = driver.find_element_by_id("myDIV")
# print("display : " , clickMeButton.is_displayed())
# toggelButton.click()
# print("display : " , clickMeButton.is_displayed())

#-------------------------
# driver.get("https://www.google.com/")
# #
# # keyboardButton = driver.find_element_by_xpath('//span[@class="hOoLGe"]')
# # searchButton = driver.find_element_by_xpath('//body[@class="hp vasq"]')
# # print("display : " , searchButton.is_displayed())
# # keyboardButton.click()
# # print("display : " , searchButton.is_displayed())

#-----------------------


