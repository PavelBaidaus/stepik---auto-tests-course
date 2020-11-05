from selenium import webdriver
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    Fname = 'Kirill'
    Lname = 'Konik'
    Email = 'kirillkonik@gmail.com'

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys(Fname)
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys(Lname)
    input3 = browser.find_element_by_name("email")
    input3.send_keys(Email)


    # получаем путь к директории текущего исполняемого
    right_dir = os.path.abspath(os.path.dirname(__file__)) #__file__ даёт доступ к той же дериктории где хранится файл
    # добавляем к этому пути имя файла
    file_path = os.path.join(right_dir, 'testfile.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
