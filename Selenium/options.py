from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.biznesradar.pl/")
print(driver.title)