# 🚀 ATF Python Demo (Automated Testing Framework)

[![Tests](https://github.com/ВАШ_НИКНЕЙМ/ATF_Python_Demo/actions/workflows/tests.yml/badge.svg)](https://github.com/ВАШ_НИКНЕЙМ/ATF_Python_Demo/actions/workflows/tests.yml)
[![Allure Report](https://img.shields.io/badge/Allure%20Report-deployed-success)](https://ВАШ_НИКНЕЙМ.github.io/ATF_Python_Demo/)

A comprehensive test automation framework built with Python. It covers UI, API, BDD, Unit, and Architectural testing to ensure the highest quality of the application.

## 🛠 Tech Stack

* **Language:** Python 3.11
* **Test Runner:** Pytest
* **UI Testing:** Playwright (implementing Page Object Model)
* **BDD Testing:** pytest-bdd (Behavior-Driven Development)
* **API Testing:** Requests (synchronous) and HTTPX (asynchronous)
* **Architecture Testing:** Native `ast` module (Arch Unit analog for Python) to verify project structural integrity
* **Schema Validation:** `jsonschema` for API contract testing
* **Containerization:** Docker (isolated Linux environment for test execution)
* **Unit Testing:** pytest-mock (dependency isolation)
* **Data Generation:** Faker
* **Reporting:** Allure Report (with automated screenshot attachments)

## 📁 Project Structure

```text
ATF_Python_Demo/
├── pages/                        # Page Object classes
│   ├── base_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── tests/                        # Test Scenarios
│   ├── api/                      # API tests (with OpenAPI/JSON schema validation)
│   ├── bdd/                      # BDD tests (Behavior-Driven Development)
│   │   ├── features/             # Gherkin scenarios
│   │   └── test_bdd_login.py     # Step definitions
│   ├── ui/                       # UI tests (Playwright)
│   └── unit/                     # Unit and Architecture tests
│       ├── test_architecture.py  # Layer independence checks (Arch Unit)
│       └── test_utils_mock.py
├── utils/                        # Utilities and schemas
├── .github/workflows/            # CI/CD Pipeline for GitHub Actions
├── Dockerfile                    # Recipe for building the Docker image
├── .dockerignore                 # Files excluded from the Docker container
├── conftest.py                   # Pytest fixtures and hooks
├── pytest.ini                    # Pytest configuration
└── requirements.txt              # Project dependencies
```

## 🐳 Running Tests in Docker

You can run the entire test suite in an isolated Linux container without installing Python or browsers on your local machine.

1. Build the Docker image:
   ```bash
   docker build -t atf-demo .
   ```
2. Run the tests:
   ```bash
   docker run --rm atf-demo
   ```

## ⚙️ Local Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/VTiseev/ATF_Python_Demo.git](https://github.com/VTiseev/ATF_Python_Demo.git)
cd ATF_Python_Demo
```

**2. Create and activate a virtual environment:**
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Install Playwright browsers:**
```bash
playwright install chromium
```

## ▶️ Running Tests Locally

You can run the whole suite or specific parts of it:

* **All tests:** `pytest`
* **UI tests only:** `pytest tests/ui/`
* **API tests only:** `pytest tests/api/`
* **BDD tests only:** `pytest tests/bdd/`
* **Architecture & Unit tests:** `pytest tests/unit/`

## 📊 Reporting (Allure)

To generate and view the Allure report:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```