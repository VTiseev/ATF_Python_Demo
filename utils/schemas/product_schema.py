# utils/schemas/product_schema.py

"""
Здесь мы описываем OpenAPI/JSON схему для нашего ответа.
Мы требуем, чтобы в ответе обязательно были id, title и price,
и строго проверяем их типы данных (что id - это число, а не строка).
"""

PRODUCT_ADD_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        # Можно даже описать вложенные объекты или массивы!
    },
    "required": ["id", "title", "price"] # Эти поля обязательны
}