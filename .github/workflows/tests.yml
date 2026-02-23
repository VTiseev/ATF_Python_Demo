name: Automated Tests

# Когда запускать этот сценарий?
on:
  push:
    branches: [ "main" ] # Запускать при каждом пуше в ветку main
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    # Какой виртуальный компьютер нам нужен? Берем последнюю версию Ubuntu (Linux)
    runs-on: ubuntu-latest

    # Шаги, которые компьютер должен выполнить по порядку
    steps:
    # 1. Скачиваем твой код из репозитория
    - name: Checkout code
      uses: actions/checkout@v4

    # 2. Устанавливаем Python 3.11 (как у тебя в требованиях)
    - name: Set up Python 3.11
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"

    # 3. Устанавливаем все библиотеки (pytest, playwright, faker и т.д.)
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    # 4. Устанавливаем браузеры для UI тестов (Playwright)
    - name: Install Playwright browsers
      run: playwright install --with-deps chromium

    # 5. Запускаем все тесты!
    - name: Run tests
      run: pytest