import unittest
from selenium import webdriver
import time

class GmailPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium Drivers/chromedriver")
        cls.driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()

    def test_EmptyData(self):
        self.driver.find_element_by_id('identifierId').send_keys("")
        self.driver.find_element_by_xpath('//div[@class="VfPpkd-RLmnJb"]').click()
        time.sleep(5)
        errorData = self.driver.find_element_by_xpath('//div[@class="o6cuMc"]')
        self.assertTrue('הזן כתובת אימייל או מספר טלפון' in errorData.text, "Wrong error message")


if __name__ == "__main__":
    unittest.main()




# driver.get("https://www.castro.com/")
#driver.find_element_by_xpath('//a[@title="Twitter Castro"]').click()
#hanldesList = driver.window_handles
# currentTabId = driver.current_window_handle
# for tabId in hanldesList:
#     if tabId != currentTabId:
#         driver.switch_to.window(tabId)
#     print(driver.title)

