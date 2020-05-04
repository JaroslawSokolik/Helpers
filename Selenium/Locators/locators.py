from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("input[name='name']").send_keys("Jarek") # two of them but selenium search from top to bottom
driver.find_element_by_name("email").send_keys("jirafolder@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("misiek69")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
