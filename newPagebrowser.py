from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time

'''
browser.switch_to.window(window_name)

Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

new_window = browser.window_handles[1]

'''


link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)
    
    driver.find_element(By.CLASS_NAME, 'trollface').click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    
    value = driver.find_element(By.ID, 'input_value')
    x = value.text
    y = calc(x)
    
    print(y)
    
    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    
finally:
    
    time.sleep(20)
    driver.quit