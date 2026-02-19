from faker import Faker


class UserGenerator:
    """Класс для генерации тестовых данных пользователя."""

    def __init__(self):
        self.faker = Faker()

    def generate_user(self):
        """Создает случайного пользователя с именем и работой."""
        return {
            "name": self.faker.first_name(),
            "job": self.faker.job()
        }