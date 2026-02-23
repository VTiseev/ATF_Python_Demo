# 🚀 Python Test Automation Framework (ATF) Demo

This project is a demonstrative Automated Testing Framework (UI and API) built from scratch using Python. The primary goal is to showcase the implementation of modern design patterns, testing tools, and best practices in test automation.

[![Automated Tests](https://github.com/VTiseev/ATF_Python_Demo/actions/workflows/tests.yml/badge.svg)](https://github.com/VTiseev/ATF_Python_Demo/actions/workflows/tests.yml)
📊 **[View Latest Allure Report](https://VTiseev.github.io/ATF_Python_Demo/)**

## 🛠 Tech Stack

* **Language:** Python 3.11
* **Test Runner:** Pytest
* **UI Testing:** Playwright (implementing Page Object Model)
* **BDD Testing:** pytest-bdd (Behavior-Driven Development)
* **API Testing:** Requests (synchronous) and HTTPX (asynchronous)
* **Unit Testing:** pytest-mock (dependency isolation)
* **Data Generation:** Faker
* **Reporting:** Allure Report (with automated screenshot attachments)


## 📁 Project Structure

```text
ATF_Python_Demo/
├── pages/                        # Page Object классы
│   ├── base_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── tests/                        # Тестовые сценарии
│   ├── api/                      # API тесты (с проверкой OpenAPI/JSON схем)
│   ├── bdd/                      # BDD тесты (Behavior-Driven Development)
│   │   ├── features/             # Gherkin сценарии
│   │   └── test_bdd_login.py
│   ├── ui/                       # UI тесты (Playwright)
│   └── unit/                     # Unit и Архитектурные тесты
│       ├── test_architecture.py  # Проверка независимости слоев (Arch Unit)
│       └── test_utils_mock.py
├── utils/                        # Вспомогательные утилиты и схемы
├── .github/workflows/            # CI/CD Pipeline для GitHub Actions
├── Dockerfile                    # Рецепт сборки Docker-образа
├── .dockerignore                 # Файлы, исключаемые из Docker-контейнера
├── conftest.py                   # Фикстуры Pytest
├── pytest.ini                    # Конфигурационный файл Pytest
└── requirements.txt              # Зависимости проекта

* **Architecture Testing:** Native `ast` module (Arch Unit analog for Python) to verify project structural integrity.
* **Schema Validation:** `jsonschema` for API contract testing.
* **Containerization:** Docker (isolated Linux environment for test execution).

## 🐳 Running Tests in Docker

You can run the entire test suite in an isolated Linux container without installing Python or browsers on your local machine.

1. Build the Docker image:
   ```bash
   docker build -t atf-demo .

## ⚙️ Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/ВАШ_НИКНЕЙМ/ATF_Python_Demo.git](https://github.com/ВАШ_НИКНЕЙМ/ATF_Python_Demo.git)
cd ATF_Python_Demo
