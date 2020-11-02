import unittest
from selenium import webdriver


class Wallashops_page(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium Drivers/chromedriver")
        cls.driver.get("https://www.wallashops.co.il/Login")


    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_fake_login(self):
        self.driver.find_element_by_id('txtPassword').send_keys('')
        self.driver.find_element_by_id('btnSubmit').click()
        errorData = self.driver.find_element_by_xpath('//span [text() = "אי אפשר להכנס בלי סיסמה..."]')
        self.assertTrue("אי אפשר להכנס בלי סיסמה..." in errorData.text, "Wrong error message")

if __name__ == "__main__":
    unittest.main()
