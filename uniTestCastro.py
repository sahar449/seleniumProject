import unittest
from selenium import webdriver
import time

class facebookPageTest (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium Drivers/chromedriver")
        cls.driver.get("https://www.castro.com/")
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_ifTheButtonExist(self):
        self.assertTrue(self.driver.find_element_by_xpath('//a [@class="toplinks-menu__account"]').is_displayed(),
                     "Element was not found or not displayed")


    def test_ifComboExist(self):
        self.driver.get("https://www.castro.com/he/MEN.html")
        self.assertTrue(self.driver.find_element_by_id("filter-title-fashion_line_filter").is_displayed(), "Element not found or displayed)")

    def test_sendKeys(self):
        self.driver.get("https://www.castro.com/he/MEN.html")





if __name__ == "__main__":
    unittest.main()
