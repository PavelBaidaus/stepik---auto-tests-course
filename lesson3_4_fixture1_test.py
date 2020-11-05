from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"
class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nclassmetod setup1")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("classmetod teardown 2 ")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")
        print("3")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("4")

class TestMainPage2():

    def setup_method(self):
        print(" setup 5")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("teardown 6")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")
        print("7")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("8")
