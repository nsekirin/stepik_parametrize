import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Импортируем Options


@pytest.fixture(scope="function")
def browser(request, language):
    print("\nstart browser for test in incognito mode..")

    language = request.config.getoption("language")

    # Создаем объект Options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Добавляем параметр инкогнито
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})

    # Указываем опции при инициализации WebDriver
    browser = webdriver.Chrome(options=chrome_options)  # Передаем options
    yield browser
    print("\nquit browser..")
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Set the interface language (e.g., en, fr, es)"
    )


@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("--language")
