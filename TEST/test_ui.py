import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Настройка WebDriver (например, Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_input_russian(driver: WebDriver):
    # Шаг 1: Открыть сайт
    driver.get("https://market-delivery.yandex.ru/")

    # Шаг 2: Найти поле ввода по атрибуту data-testid
    search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-input"]'))
    )

    # Шаг 3: Ввести тестовые данные в поле ввода
    test_input = "Пицца"
    search_field.send_keys(test_input)

    # Шаг 4: Проверить, что данные были введены правильно
    entered_value = search_field.get_attribute("value")
    assert entered_value == test_input, f"Ожидалось '{test_input}', но было '{entered_value}'"

def test_input_english(driver: WebDriver):
    # Шаг 1: Открыть сайт
    driver.get("https://market-delivery.yandex.ru/")

    # Шаг 2: Найти поле ввода по атрибуту data-testid
    search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-input"]'))
    )

    # Шаг 3: Ввести тестовые данные в поле ввода
    test_input = "Pizza"
    search_field.send_keys(test_input)

    # Шаг 4: Проверить, что данные были введены правильно
    entered_value = search_field.get_attribute("value")
    assert entered_value == test_input, f"Ожидалось '{test_input}', но было '{entered_value}'"

def test_input_mixed_case(driver: WebDriver):
    # Шаг 1: Открыть сайт
    driver.get("https://market-delivery.yandex.ru/")

    # Шаг 2: Найти поле ввода по атрибуту data-testid
    search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-input"]'))
    )

    # Шаг 3: Ввести тестовые данные в поле ввода
    test_input = "APPlE"
    search_field.send_keys(test_input)

    # Шаг 4: Проверить, что данные были введены правильно
    entered_value = search_field.get_attribute("value")
    assert entered_value == test_input, f"Ожидалось '{test_input}', но было '{entered_value}'"

def test_input_special_characters(driver: WebDriver):
    # Шаг 1: Открыть сайт
    driver.get("https://market-delivery.yandex.ru/")

    # Шаг 2: Найти поле ввода по атрибуту data-testid
    search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-input"]'))
    )

    # Шаг 3: Ввести тестовые данные в поле ввода
    test_input = "♣☺♂"
    search_field.send_keys(test_input)

    # Шаг 4: Проверить, что данные были введены правильно
    entered_value = search_field.get_attribute("value")
    assert entered_value == test_input, f"Ожидалось '{test_input}', но было '{entered_value}'"

def test_input_numeric_text(driver: WebDriver):
    # Шаг 1: Открыть сайт
    driver.get("https://market-delivery.yandex.ru/")

    # Шаг 2: Найти поле ввода по атрибуту data-testid
    search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="search-input"]'))
    )

    # Шаг 3: Ввести тестовые данные в поле ввода
    test_input = "5 яблок"
    search_field.send_keys(test_input)

    # Шаг 4: Проверить, что данные были введены правильно
    entered_value = search_field.get_attribute("value")
    assert entered_value == test_input, f"Ожидалось '{test_input}', но было '{entered_value}'"
