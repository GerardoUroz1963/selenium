from lib2to3.pgen2 import driver
from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\DriverChrome\chromedriver.exe")
driver.get("https://gmail.com")

usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("elchaca2007@gmail.com")
usuario.send_keys(Keys.ENTER)

clave = driver.find_element_by_name("password")
clave.send_keys("tupasswordpersonal")
clave.send_keys(Keys.ENTER)


