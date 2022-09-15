import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome (executable_path=r"C:\DriverChrome\chromedriver.exe")

    def test_usando_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)
        select = driver.find_element("xpath", "//*[@id='main']/div[3]/div[1]/select")
        '''
        opcion = select.find_elements(TAG_NAME, 'option')  
        #.find_element("By_TAG_NAME", "opcion")
        time.sleep(3)

        for option in opcion:
            print("Valores: %s" % option.get_attribute("value"))
            option.click()
            time.sleep(1)
        '''
        seleccionar = Select(driver.find_element("xpath", "//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")

        time.sleep(10)

if __name__ == '__main__':
    unittest.main()    