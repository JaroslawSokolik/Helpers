from selenium import webdriver
from time import sleep


list = []
list_summary = []

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
sleep(2)
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

veggies = driver.find_elements_by_css_selector("h4[class='product-name']")
for veg in veggies:
    list.append(veg.text)
print(list)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()

veggies_summary = driver.find_elements_by_css_selector("p.product-name")
for veg_summary in veggies_summary:
    list_summary.append(veg_summary.text)
print(list_summary)

assert list in list_summary