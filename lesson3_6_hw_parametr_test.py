import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

final = ''

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
    print(final)

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904",  "236905"])
#@pytest.mark.parametrize('number', ["236898"])
def test_guest_should_see_login_link(browser, number):
    global final
    answer = str(math.log(int(time.time())))
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    browser.find_element_by_css_selector(".textarea").send_keys(answer)
    browser.find_element_by_class_name("submit-submission").click()
    #buttom = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(By.className, "submit-submission")).click() #(By.CSS_SELECTOR, "pre")
    #WebDriverWait(browser, 5).until(
    #    EC.text_to_be_present_in_element((By.CLASS_NAME, "smart-hints__hint"), "Correct!")
    #)
    #correct = WebDriverWait(browser, 5).until(
    #    EC.visibility_of((By.CLASS_NAME, "smart-hints__hint"))
    #)
    correct = browser.find_element_by_class_name("smart-hints__hint").text
    #correct = browser.find_element((By.CLASS_NAME, "smart-hints__hint"), "Correct!")
    try:
        assert "Correct!" == correct
    except AssertionError:
        final += correct  # собираем ответ про Сов с каждой ошибкой
