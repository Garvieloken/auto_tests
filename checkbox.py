from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)

    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text # КУСОК КОДА ИЩЕТ ЗНАЧЕНИЕ ПРИСВОЕННОЕ В ТЕКСТЕ!!!!!!!!
    y = calc(x)

    input_field = driver.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    checkbox_button = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    rabio_button = driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    
    submit_button = driver.find_element(By.XPATH, '//button').click()

    time.sleep(20)

finally:
   
   time.sleep(10)

   driver.quit()


