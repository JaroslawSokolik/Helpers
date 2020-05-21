from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()