from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get(link)

try:
    value = driver.find_element(By.ID, 'input_value')
    x = value.text
    y = calc(x)
    
    driver.execute_script("window.scrollBy(0, 100);")
    
    input = driver.find_element(By.ID, 'answer').send_keys(y)
    
    checkbox = driver.find_element(By.ID, 'robotCheckbox').click()
    radioButton = driver.find_element(By.ID, 'robotsRule').click()
    submit = driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    
finally:
    
    time.sleep(10)
    driver.quit()