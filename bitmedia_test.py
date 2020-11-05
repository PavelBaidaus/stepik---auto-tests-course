import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('clothesid', ['1', '2', '3', '4', '5', '6', '7'])
def test_guest_should_see_login_link(browser, clothesid):
    link = "http://automationpractice.com/index.php"
    browser.get(link)
    print(f"{clothesid}")
    browser.find_element_by_css_selector(f"a[data-id-product = '{clothesid}']").click()
    browser.find_element_by_css_selector("a[title = 'Proceed to checkout']").click()
    table = str.maketrans("", "", "\t\n\v\f\r!@#$%^&*_+|+:;[]{}<>")
    unit_price = browser.find_element_by_css_selector("span[class = 'price']").get_attribute('innerHTML').translate(table)
    quantity = browser.find_element_by_xpath("//*[contains(./@id, 'product')]/td[5]/input[2]").get_attribute('value')
    total_shipping = browser.find_element_by_css_selector("td[id = 'total_shipping']").get_attribute('innerHTML').translate(table)
    total_price = browser.find_element_by_id("total_price_without_tax").get_attribute('innerHTML').translate(table)
    assert float(unit_price)*float(quantity)+float(total_shipping) == float(total_price), "price is not right!!! "
    print(float(unit_price)*float(quantity)+float(total_shipping))
    print(float(total_price))
    time.sleep(4)
