import allure
import pytest

# Импортируем наш новый клиент

BASE_URL = "https://dummyjson.com"


@allure.feature("API Testing")
@allure.story("Synchronous Requests (Requests lib)")
# Передаем api_client в скобки функции! Pytest сам подставит сюда объект из conftest.py
def test_add_product_positive(api_client):
    """Позитивный тест: Добавление продукта (POST)."""

    with allure.step("Send POST request to add product"):
        # Используем api_client напрямую, мы его больше не создаем руками!
        response = api_client.add_product(title="Test Product", price=150)

    with allure.step("Verify status code is 200 or 201"):
        assert response.status_code in [200, 201]

    data = response.json()
    assert data["title"] == "Test Product"
    assert "id" in data


@allure.feature("API Testing")
@allure.story("Negative Scenarios")
# То же самое делаем для второго теста
def test_login_unsuccessful_negative(api_client):
    """Негативный тест: Авторизация с неверными данными."""

    with allure.step("Try to login with invalid credentials"):
        response = api_client.login("invalid_user", "wrong_password")

    assert response.status_code == 400
    assert "message" in response.json()


@allure.feature("API Testing")
@allure.story("Async Requests (HTTPX lib)")
@pytest.mark.asyncio
async def test_get_products_async_positive(async_api_client):  # Передаем новую фикстуру!
    """Позитивный асинхронный тест: Получение списка продуктов."""

    # Больше никакого 'async with httpx...' в самом тесте.
    # Просто вызываем понятный метод клиента:
    response = await async_api_client.get_products(limit=5)

    assert response.status_code == 200
    assert len(response.json()["products"]) > 0


@allure.feature("API Testing")
@allure.story("Negative Scenarios")
@pytest.mark.asyncio
async def test_product_not_found_async_negative(async_api_client):
    """Негативный асинхронный тест: Продукт не найден."""

    # Запрашиваем продукт с несуществующим ID через клиент
    response = await async_api_client.get_product(product_id=999999)

    assert response.status_code == 404