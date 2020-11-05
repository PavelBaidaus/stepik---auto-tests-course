from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration1.html"
#link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()
browser.get(link)
# заполняются только обязательные для регистрации поля
browser.find_element_by_css_selector('.first_block  *  .form-control.first').send_keys('TEST')
browser.find_element_by_css_selector('.first_block  *  .form-control.second').send_keys('TEST')
browser.find_element_by_css_selector('.first_block  *  .form-control.third').send_keys('TEST')

browser.find_element_by_css_selector('button[type=submit]').click()

time.sleep(10)
browser.quit()
