from selenium import webdriver
import time
import unittest


try:
    def link_t(link):
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element_by_xpath("//div[contains(@class, 'first_block')]/div[contains(@class, 'first_class')]/input").send_keys("Ivan")
        browser.find_element_by_xpath("//div[contains(@class, 'first_block')]/div[contains(@class, 'second_class')]/input").send_keys("Petrov")
        browser.find_element_by_xpath("//div[contains(@class, 'first_block')]/div[contains(@class, 'third_class')]/input").send_keys("Smolensk")
        browser.find_element_by_css_selector("button.btn").click()

        time.sleep(1)
        return browser.find_element_by_tag_name("h1").text
    class TestReg(unittest.TestCase):
        def test_reg1(self):
            self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", "shtoto gouno")
        def test_reg2(self):
            self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!", "shtoto toje gouno")
    if __name__ == "__main__":
        unittest.main()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()
