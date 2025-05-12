import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_is_present(browser):
    browser.get(link)
    time.sleep(10)  # слип для проверки языка на кнопке
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert add_to_cart_button.is_displayed(), "Кнопка добавления в корзину не найдена на странице"
