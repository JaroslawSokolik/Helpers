from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
sleep(2)
dropdown.select_by_index(0)





# SELECT to be used only with select tag- you can choose what is inside by index, visible test, value.