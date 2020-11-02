from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Selenium Drivers/chromedriver")
driver.get('https://www.ynet.co.il/home/0,7340,L-8,00.html')
driver.get_screenshot_as_file("C:\screen shot/pic.png")
driver.save_screenshot("C:\screen shot/pic1.png")