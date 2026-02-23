import pytest

from utils.data_generator import UserGenerator


def test_generate_user_mocked(mocker):
    """
    Unit тест с использованием Mock.
    Мы подменяем реальный метод faker.first_name и faker.job,
    чтобы проверить логику нашего класса UserGenerator, а не библиотеки Faker.
    """
    # Arrange (Подготовка)
    generator = UserGenerator()

    # Mocker - это фикстура из pytest-mock.
    # Мы говорим: когда вызывается first_name, верни 'Alice'
    mocker.patch.object(generator.faker, 'first_name', return_value='Alice')
    mocker.patch.object(generator.faker, 'job', return_value='Tester')

    # Act (Действие)
    user = generator.generate_user()

    # Assert (Проверка)
    assert user['name'] == 'Alice'
    assert user['job'] == 'Tester'
    # Проверяем, что результат действительно словарь
    assert isinstance(user, dict)


@pytest.mark.parametrize("count", [0, 1, 5])
def test_generate_users_count(count):
    """
    Параметризованный тест: проверяем, что метод generate_users
    возвращает список правильной длины.
    Мы запустим этот тест 3 раза: для 0, 1 и 5 пользователей.
    """
    generator = UserGenerator()

    # Действие: генерируем нужное количество пользователей
    users = generator.generate_users(count)

    # Проверка: длина списка должна совпадать с запрошенным числом
    assert len(users) == count
    # Проверяем, что возвращается именно список (list)
    assert isinstance(users, list)