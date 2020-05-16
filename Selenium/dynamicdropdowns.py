from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("DEL")
sleep(2)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
for city in cities:
    # print(city.text) if you want to print them
    # print(len(cities)) to know how many of them are there
    if city.text =="Del Rio, United States":
        city.click()
        break #to break because it has been found and we dont have to iterate other ones