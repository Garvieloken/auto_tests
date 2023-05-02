'''
alert = browser.switch_to.alert
alert.accept()

Чтобы получить текст из alert, используйте свойство text объекта alert:

alert = browser.switch_to.alert
alert_text = alert.text

confirm = browser.switch_to.alert
confirm.accept()

Для confirm-окон можно использовать следующий метод для отказа:

confirm.dismiss()

Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
'''
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)
    
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    confirm = driver.switch_to.alert
    confirm.accept()
    
    value = driver.find_element(By.ID, 'input_value')
    x = value.text
    y = calc(x)
    
    print(y)
    
    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    
finally:
    
    time.sleep(20)
    driver.quit