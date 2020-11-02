import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

class AlljobsPageTest (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium Drivers/chromedriver", options=options)
        cls.driver.get('https://www.alljobs.co.il')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_empty(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@eventlabel="התחבר"]').click()
        self.driver.find_element_by_xpath('//input[@placeholder = "מייל:"]').send_keys("")
        self.driver.find_element_by_xpath('//input[@placeholder = "סיסמה:"]').send_keys("")
        self.driver.find_element_by_xpath('//button[@ng-click="LogIn.LogIn()"]').click()
        mailerrorElement = self.driver.find_element_by_id('lb-error-e')
        passErrorLElement = self.driver.find_element_by_id('lb-error-p')
        self.assertTrue("אופס.. שכחת למלא את המייל" in mailerrorElement.text , "error wrong message")
        self.assertTrue("עצור, סיסמה" in passErrorLElement.text , "error wrong message" )



if __name__ == "__main__":
    unittest.main()
