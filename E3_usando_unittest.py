from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver  = webdriver.Chrome(executable_path=r"C:\DriverChrome\chromedriver.exe")

    def test_buscar(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google",driver.title, "no esta el titulo")

        element = driver.find_element("name", "q")
        
        element.send_keys("selenium")
        element.send_keys(Keys.ENTER)
        time.sleep(5)
        assert "No encontro el elementos: " not in driver.page_source

    def tearDown(self):
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()
        




