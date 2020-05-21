from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()
driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
sleep(5)
driver.find_element_by_class_name("promoBtn").click()