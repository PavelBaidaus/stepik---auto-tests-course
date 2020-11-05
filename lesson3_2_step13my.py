from selenium import webdriver
import time
import unittest
try:
    class TestReg (unittest.TestCase):
        def test_reg1(self):
            #link = "http://suninjuly.github.io/registration2.html"
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            browser.find_element_by_xpath("//div[contains(@class, 'first_block')]/div[contains(@class, 'first_class')]/input").send_keys("Ivan")
            browser.find_element_by_xpath("//div[contains(@class, 'first_block')]/div[contains(@class, 'second_class')]/input").send_keys("Petrov")
            browser.find_element_by_xpath("//div[contains(@class, 'first_block')]/div[contains(@class, 'third_class')]/input").send_keys("Smolensk")
            browser.find_element_by_css_selector("button.btn").click()
            time.sleep(1)
            welcome_text = browser.find_element_by_tag_name("h1").text
            self.assertEqual(welcome_text,"Congratulations! You have successfully registered!", "ERRRRRROOOORRRRR!!!!")
        def test_reg2(self):
            link = "http://suninjuly.github.io/registration2.html"
            #link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            browser.find_element_by_xpath("//div[contains(@class, 'first_block')]/div[contains(@class, 'first_class')]/input").send_keys("Ivan")
            browser.find_element_by_xpath("//div[contains(@class, 'first_block')]/div[contains(@class, 'second_class')]/input").send_keys("Petrov")
            browser.find_element_by_xpath("//div[contains(@class, 'first_block')]/div[contains(@class, 'third_class')]/input").send_keys("Smolensk")
            browser.find_element_by_css_selector("button.btn").click()
            time.sleep(1)
            welcome_text = browser.find_element_by_tag_name("h1").text
            self.assertEqual(welcome_text,"Congratulations! You have successfully registered!", "ERRRRRROOOORRRRR!!!!")

    if __name__=="__main__":
        unittest.main()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
