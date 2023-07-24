import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Выбор браузера по параметру
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru', help="Choose language")

@pytest.fixture(scope='function')
def browser(request):
    # В переменную browser_name передается параметр из командной строки
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    # Передаем параметр из командной строки в зависимости от браузера
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()