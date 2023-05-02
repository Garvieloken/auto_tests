from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
browser.switch_to.window(window_name)

Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

new_window = browser.window_handles[1]

'''


link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    booking = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element(By.ID, '#price'), '$100')
    
    booking.click()
    button = driver.find_element(By.ID, 'book').click()
    
    driver.execute_script("window.scrollBy(0, 100);")
    
    value = driver.find_element(By.ID, 'input_value')
    x = value.text
    y = calc(x)
    print(y)
    driver.find_element(By.ID, 'answer').send_keys(y)
    solve_button = driver.find_element(By.ID, 'solve').click()
    
    
    
finally:
    
    time.sleep(20)
    driver.quit