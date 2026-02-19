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