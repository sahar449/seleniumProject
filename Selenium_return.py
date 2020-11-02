from selenium import webdriver
import unittest

class jobnetLoginPage (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium Drivers/chromedriver")
        cls.driver.get("https://www.alljobs.co.il/")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_empty_username(self):
        self.driver.find_element_by_id("in-pass-c").send_keys("")
        self.driver.find_element_by_xpath('//button[text () = "כניסה "]').click()
        error_data = self.driver.find_element_by_xpath('//div[text () =" אופס.. שכחת למלא את המייל"]')
        self.assertTrue(" אופס.. שכחת למלא את המייל" in error_data.text, "Wrong error message")

        
if __name__ == "__main__":
    unittest.main()