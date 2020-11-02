import unittest
from selenium import webdriver
import time


class GoogleSearchTest(unittest.TestCase):

    @classmethod  # נקרא פעם אחת לפני תחילת הטסט
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium Drivers/chromedriver")
        cls.driver.get("https://google.com")
        time.sleep(5)

    @classmethod # נקרא פעחת אחת לפני סוף הטסט
    def tearDownClass(cls):
        cls.driver.quit()

    def test_checkIfSearchExists(self):
        self.assertTrue(self.driver.find_element_by_id("fakebox-input").is_displayed(), "Error msg")



if __name__ == "__main__":
    unittest.main()


