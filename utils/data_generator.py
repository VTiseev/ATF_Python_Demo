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

    # --- НАШ НОВЫЙ МЕТОД ---
    def generate_users(self, count: int):
        """Создает список из указанного количества случайных пользователей."""
        users_list = []
        for _ in range(count):
            users_list.append(self.generate_user())
        return users_list