from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# wait for element to appear, then hover it
wait = WebDriverWait(driver, 10)
men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@data-tracking-id='men']")))
ActionChains(driver).move_to_element(men_menu).perform()

# wait for Fastrack menu item to appear, then click it
fastrack = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//a[@data-tracking-id='0_Fastrack']")))
fastrack.click()
