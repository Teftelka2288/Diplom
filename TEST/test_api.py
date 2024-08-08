import pytest
import requests

# Указываем базовый URL
BASE_URL = "https://market-delivery.yandex.ru/eats/v1/full-text-search/v1"

# Общие заголовки
HEADERS = {
    "location": "longitude=44.00585167153857&latitude=56.327056428014245",
    "Apikey": "c0d403ab-e5be-4049-908c-8122a58acf23",
    "latitude": "56.327056428014245",
    "longitude": "44.00585167153857",
    "Content-Type": "application/json"
}

# Тесты для каждого запроса

# 1. Запрос: "несколько слов в названии товара"
def test_search_multiple_words_in_product_name():
    payload = {
        "text": "кока-кола",
        "region_id": 17
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

# 2. Запрос: "Точное название товара"
def test_search_exact_product_name():
    payload = {
        "text": "сыр российский",
        "region_id": 17
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

# 3. Запрос: "Наличие товара по запросу"
def test_search_product_availability():
    payload = {
        "text": "молоко",
        "region_id": 17
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

# 4. Запрос: "Кириллица и латиница"
def test_search_cyrillic_and_latin():
    payload = {
        "text": "Pepsi",
        "region_id": 17
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

# 5. Запрос: "Найти товар по номеру"
def test_search_product_by_number():
    payload = {
        "text": "12345",
        "region_id": 17
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

# 6. Запрос: "Поиск по категориям"
def test_search_by_category():
    payload = {
        "text": "напитки",
        "region_id": 17
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

# 7. Запрос: "Поиск по частичному совпадению"
def test_search_partial_match():
    payload = {
        "text": "масл",
        "region_id": 17
    }
    
    response = requests.post(f"{BASE_URL}/search", headers=HEADERS, json=payload)
    assert response.status_code == 200
    
    json_response = response.json()
    assert "header" in json_response
    assert "blocks" in json_response
    assert len(json_response["blocks"]) > 0

if __name__ == "__main__":
    pytest.main()
