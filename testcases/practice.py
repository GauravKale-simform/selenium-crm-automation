import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ui.cogmento.com/")
driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys('gauravkale.sinhgad@gmail.com')
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('Royal@12345')
driver.find_element(By.XPATH,"//div[@class='ui fluid large blue submit button']").click()
time.sleep(5)
hover_element = driver.find_element(By.XPATH,"//span[normalize-space()='Companies']")
action = ActionChains(driver)
action.move_to_element(hover_element).perform()
clickable_element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/button[1]/i[1]")))
clickable_element.click()
driver.find_element(By.XPATH,"//label[normalize-space()='Phone']").click()
time.sleep(2)
# driver.find_element(By.XPATH,"//span[normalize-space()='Companies']").click()
driver.find_element(By.XPATH,"//div[@name='hint']//input[@type='text']").send_keys("India")
driver.find_element(By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='India']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='Number']").send_keys("8888929274")
time.sleep(10)
#element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ui.active.visible.fluid.multiple.search.selection.dropdown")))
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='search icon']")))
element.send_keys("technology")
#driver.execute_script("window.scrollBy(0,1000);")
#time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,".ui.active.visible.fluid.multiple.search.selection.dropdown").send_keys("technology")
# time.sleep(2)
# driver.find_element(By.XPATH,"//span[@class='text'][normalize-space()='technology']").click()
# time.sleep(20)
driver.find_element(By.XPATH,"//div[@name='channel_type']").click() #social channel
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='three fields']//div[@class='ui field']//div[3]").click()
time.sleep(15)
driver.find_element(By.XPATH, "//div[@class='ui field'][.//label[normalize-space()='Social channels']]//div[@class='ui input']//input[@name='value']").send_keys("gauravkale")
time.sleep(5)
driver.find_element(By.XPATH,"//body/div[@id='ui']/div[@class='ui fluid container']/div[@class='ui fluid container']/div[@id='main-content']/div[@class='ui fluid container ']/div[@class='ui fluid container main-content']/form[@class='ui form segment custom-form-container']/div[7]/div[2]/div[1]/div[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='visible menu transition']//div[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@name='status']//i[@class='dropdown icon']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='visible menu transition']//div[7]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@name='source']//i[@class='dropdown icon']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='visible menu transition']//div[11]").click()
time.sleep(2)
file_input = driver.find_element(By.XPATH,"//input[@name='image']")
file_path = "C:/Users/gaurav/Downloads/indian_flag.png"
file_input.send_keys(file_path)
time.sleep(10)















