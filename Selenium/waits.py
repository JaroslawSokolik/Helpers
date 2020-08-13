from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# wait for element to appear, then hover it
wait = WebDriverWait(driver, 10)
men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@data-tracking-id='men']")))
ActionChains(driver).move_to_element(men_menu).perform()

# wait for Fastrack menu item to appear, then click it
fastrack = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//a[@data-tracking-id='0_Fastrack']")))
fastrack.click()
#try few times

for x in range(0, 4):  # try 4 times
    try:
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "wait-for-offer")))
        assert element.is_displayed()

    except:
        sleep(2)
