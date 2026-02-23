import allure
import pytest

from utils.api_client import DummyJsonClient, AsyncDummyJsonClient


@pytest.fixture
def api_client():
    """Фикстура для создания синхронного API-клиента."""
    return DummyJsonClient()

# Добавляем новую фикстуру:
@pytest.fixture
def async_api_client():
    """Фикстура для создания асинхронного API-клиента."""
    return AsyncDummyJsonClient()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        page = item.funcargs.get("page")
        if page:
            if report.failed:
                allure.attach(
                    page.screenshot(full_page=True),
                    name="Screenshot on Failure",
                    attachment_type=allure.attachment_type.PNG
                )
            elif report.passed:
                allure.attach(
                    page.screenshot(full_page=True),
                    name="Screenshot on Success",
                    attachment_type=allure.attachment_type.PNG
                )

# --- НАША НОВАЯ ФИКСТУРА ---
@pytest.fixture
def api_client():
    """Фикстура для создания API-клиента."""
    return DummyJsonClient()