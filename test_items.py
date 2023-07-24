import time
from selenium.webdriver.common.by import By

def test_button_add_to_basket_exist_on_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #Время ожидания для проверки
    time.sleep(5)
    #Проверка наличия кнопки
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-lg.btn-primary.btn-add-to-basket")