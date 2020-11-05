import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1(object):

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

        #pytest -s -v -m smoke lesson3_5_fixture8_test.py   ---for starting
        #маркировки регестрируются в файле pytest.ini
        #pytest -s -v -m "not smoke" lesson3_5_fixture8_test.py     ---инверсия, запускается все кроме смоук
        #pytest -s -v -m "smoke or regression ----Для запуска тестов с разными метками можно использовать логическое ИЛИ.
        #pytest -s -v -m "smoke and win10" ----Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:
        #Итак, чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip:
