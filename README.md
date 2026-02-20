# 🚀 Python Test Automation Framework (ATF) Demo

This project is a demonstrative Automated Testing Framework (UI and API) built from scratch using Python. The primary goal is to showcase the implementation of modern design patterns, testing tools, and best practices in test automation.

## 🛠 Tech Stack

* **Language:** Python 3.11
* **Test Runner:** Pytest
* **UI Testing:** Playwright (implementing Page Object Model)
* **API Testing:** Requests (synchronous) and HTTPX (asynchronous)
* **Unit Testing:** pytest-mock (dependency isolation)
* **Data Generation:** Faker
* **Reporting:** Allure Report (with automated screenshot attachments on success/failure)

## 📁 Project Structure

* `pages/` — Page Object classes for web pages (encapsulating locators and methods).
* `tests/api/` — REST API tests (using DummyJSON).
* `tests/ui/` — UI automated tests (using SauceDemo).
* `tests/unit/` — Unit tests verifying helper utilities (using mocks).
* `utils/` — Helper classes and mock data generators.
* `conftest.py` — Pytest configuration and hooks for Allure reporting.

## ⚙️ Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/ВАШ_НИКНЕЙМ/ATF_Python_Demo.git](https://github.com/ВАШ_НИКНЕЙМ/ATF_Python_Demo.git)
cd ATF_Python_Demo