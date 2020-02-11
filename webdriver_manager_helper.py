from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.udemy.com/course/kurs-selenium-python/learn/lecture/14519262#overview")
driver.close()