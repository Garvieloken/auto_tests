from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

driver = webdriver.Chrome()
driver.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    book = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    
    btn = driver.find_element(By.ID, 'book').click()

    input_value = driver.find_element(By.ID, 'input_value')
    x = input_value.text
    y = calc(x)

    input = driver.find_element(By.ID, 'answer').send_keys(y)

    solve_btn = driver.find_element(By.ID, 'solve').click()


finally:

    time.sleep(10)
    driver.quit()