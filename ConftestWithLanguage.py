import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#@pytest.fixture(scope="function")
#def browser():
#    print("\nstart browser for test..")
#    browser = webdriver.Chrome()
#    browser.implicitly_wait(5)
#    yield browser
#    print("\nquit browser..")
#    browser.quit()


#options = Options()
#options.add_experimental_option('prefs',\
#                                {'intl.accept_languages': user_language})
#browser = webdriver.Chrome(options=options)
#Для Firefox объявление нужного языка будет выглядеть немного иначе:
#fp = webdriver.FirefoxProfile()
#fp.set_preference("intl.accept_languages", user_language)
#browser = webdriver.Firefox(firefox_profile=fp)




def pytest_addoption(parser):
    parser.addoption('--browser_name', \
                     action='store', \
                     default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language',\
                     action='store',\
                     default=None,\
                     help="choose leaguage: ru, en, es...(etc.)"

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_lenguage = request.config.getoption("language")
        if browser_name == "chrome":
        options = Options()0
        options.add_experimental_option('prefs', \
                                        {'intl.accept_languages':user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set)set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser <browser_name> still is not implemented")
    yield browser
    print("\nquit browser..")
    browser.quit()
