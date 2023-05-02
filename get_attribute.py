from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    driver = webdriver.Chrome()
    driver.get(link)

    img = driver.find_element(By.CSS_SELECTOR, "#treasure")
    
    attribute = img.get_attribute("valuex")

    x = attribute # КУСОК КОДА ИЩЕТ ЗНАЧЕНИЕ ПРИСВОЕННОЕ В ТЕКСТЕ!!!!!!!!
    y = calc(x)

    input_field = driver.find_element(By.ID, "answer").send_keys(y)

    checkbox_button = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    rabio_button = driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    
    submit_button = driver.find_element(By.XPATH, '//button').click()

    driver.implicitly_wait(10)

finally:
   
    time.sleep(10)
    driver.quit()

