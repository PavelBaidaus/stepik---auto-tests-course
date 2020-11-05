from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text

    y_element = browser.find_element_by_id("num2")
    y = y_element.text

    z = str (int(x)+int(y))

    
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(z)
      

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
