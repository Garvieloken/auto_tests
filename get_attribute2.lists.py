from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

def sum(x, y):
  return (x + y)

try:

    driver = webdriver.Chrome()
    driver.get(link)

    num1 = driver.find_element(By.CSS_SELECTOR, '#num1')
    x = int(num1.text)
    num2 = driver.find_element(By.CSS_SELECTOR, '#num2')
    y = int(num2.text)
    
    z = sum(x, y)
    print(z)
    
    select = Select(driver.find_element(By.ID, "dropdown"))
    
    select.select_by_value(str(z))
    
    submit = driver.find_element(By.CLASS_NAME, "btn").click()
    
finally:
   
    time.sleep(10)
    driver.quit()

