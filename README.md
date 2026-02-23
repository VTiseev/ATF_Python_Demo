# 🚀 Python Test Automation Framework (ATF) Demo

This project is a demonstrative Automated Testing Framework (UI and API) built from scratch using Python. The primary goal is to showcase the implementation of modern design patterns, testing tools, and best practices in test automation.

[![Automated Tests](https://github.com/VTiseev/ATF_Python_Demo/actions/workflows/tests.yml/badge.svg)](https://github.com/VTiseev/ATF_Python_Demo/actions/workflows/tests.yml)
📊 **[View Latest Allure Report](https://VTiseev.github.io/ATF_Python_Demo/)**

## 🛠 Tech Stack

* **Language:** Python 3.11
* **Test Runner:** Pytest
* **UI Testing:** Playwright (implementing Page Object Model)
* **API Testing:** Requests (synchronous) and HTTPX (asynchronous)
* **Unit Testing:** pytest-mock (dependency isolation)
* **Data Generation:** Faker
* **Reporting:** Allure Report (with automated screenshot attachments on success/failure)


## 📁 Project Structure

```text
ATF_Python_Demo/
├── pages/                        # Page Object классы
│   └── login_page.py             # Логика и локаторы страницы авторизации
├── tests/                        # Тестовые сценарии
│   ├── api/                      # API тесты
│   │   └── test_api_dummyjson.py # Тесты для DummyJSON API
│   ├── ui/                       # UI тесты
│   │   └── test_ui_saucedemo.py  # Тесты интерфейса SauceDemo
│   └── unit/                     # Unit тесты
│       └── test_utils_mock.py    # Тестирование утилит с помощью моков
├── utils/                        # Вспомогательные утилиты
│   └── data_generator.py         # Генерация тестовых данных (например, Faker)
├── .gitignore                    # Файлы и папки, игнорируемые Git
├── README.md                     # Документация проекта
├── conftest.py                   # Фикстуры Pytest и настройки (например, Allure)
├── pytest.ini                    # Конфигурационный файл Pytest
└── requirements.txt              # Зависимости проекта

## ⚙️ Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/ВАШ_НИКНЕЙМ/ATF_Python_Demo.git](https://github.com/ВАШ_НИКНЕЙМ/ATF_Python_Demo.git)
cd ATF_Python_Demo
