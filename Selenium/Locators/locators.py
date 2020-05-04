from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("input[name='name']").send_keys("Jarek")
driver.find_element_by_id("exampleCheck1").click()
