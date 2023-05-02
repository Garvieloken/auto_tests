from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    
    driver = webdriver.Chrome()
    driver.get(link)
    '''    
    # EXAMPLE
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)
    '''
    driver.find_element(By.NAME, 'firstname').send_keys('fuck')
    driver.find_element(By.NAME, 'lastname').send_keys('fuck')
    driver.find_element(By.NAME, 'email').send_keys('fuck@fuck.com')
    

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'txt.txt')
    input_file = driver.find_element(By.ID, 'file').send_keys(file_path)
    
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    
finally:
    
    time.sleep(15)
    driver.quit()