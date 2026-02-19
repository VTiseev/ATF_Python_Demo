import pytest
import requests
import httpx
import allure

BASE_URL = "https://dummyjson.com"


@allure.feature("API Testing")
@allure.story("Synchronous Requests (Requests lib)")
def test_add_product_positive():
    """Позитивный тест: Добавление продукта (POST)."""
    payload = {"title": "Test Product", "price": 150}

    with allure.step("Send POST request to add product"):
        response = requests.post(f"{BASE_URL}/products/add", json=payload)

    with allure.step("Verify status code is 200 or 201"):
        # DummyJSON может возвращать 200 или 201 при успешном создании
        assert response.status_code in [200, 201]

    data = response.json()
    assert data["title"] == "Test Product"
    assert "id" in data


@allure.feature("API Testing")
@allure.story("Async Requests (HTTPX lib)")
@pytest.mark.asyncio
async def test_get_products_async_positive():
    """Позитивный асинхронный тест: Получение списка продуктов."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/products?limit=5")

    assert response.status_code == 200
    assert len(response.json()["products"]) > 0


@allure.feature("API Testing")
@allure.story("Negative Scenarios")
def test_login_unsuccessful_negative():
    """Негативный тест: Авторизация с неверными данными."""
    payload = {"username": "invalid_user", "password": "wrong_password"}

    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    assert response.status_code == 400
    assert "message" in response.json()


@allure.feature("API Testing")
@allure.story("Negative Scenarios")
@pytest.mark.asyncio
async def test_product_not_found_async_negative():
    """Негативный асинхронный тест: Продукт не найден."""
    async with httpx.AsyncClient() as client:
        # Запрашиваем продукт с несуществующим ID
        response = await client.get(f"{BASE_URL}/products/999999")

    assert response.status_code == 404