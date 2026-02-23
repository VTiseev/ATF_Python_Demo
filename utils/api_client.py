import httpx  # Добавили импорт для асинхронных запросов
import requests


class DummyJsonClient:
    """Класс-клиент для работы с API DummyJSON (Синхронный)."""
    def __init__(self):
        self.base_url = "https://dummyjson.com"

    def add_product(self, title: str, price: int):
        payload = {"title": title, "price": price}
        return requests.post(f"{self.base_url}/products/add", json=payload)

    def login(self, username, password):
        payload = {"username": username, "password": password}
        return requests.post(f"{self.base_url}/auth/login", json=payload)


class AsyncDummyJsonClient:
    """Асинхронный клиент для работы с API DummyJSON."""
    def __init__(self):
        self.base_url = "https://dummyjson.com"

    async def get_products(self, limit: int = 5):
        """Асинхронно получает список продуктов."""
        # Прячем работу с httpx внутрь метода
        async with httpx.AsyncClient() as client:
            return await client.get(f"{self.base_url}/products?limit={limit}")

    async def get_product(self, product_id: int):
        """Асинхронно получает один продукт по его ID."""
        async with httpx.AsyncClient() as client:
            return await client.get(f"{self.base_url}/products/{product_id}")