from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\DriverChrome\chromedriver.exe")
driver.get("http://python.org")
driver.close