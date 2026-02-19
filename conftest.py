import pytest
import allure
from playwright.sync_api import Page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Нас интересует только основной этап выполнения теста (call), игнорируем setup и teardown
    if report.when == "call":
        # Проверяем, использует ли тест фикстуру 'page' (то есть, является ли он UI-тестом)
        page = item.funcargs.get("page")
        if page:
            # Если тест упал
            if report.failed:
                allure.attach(
                    page.screenshot(full_page=True),
                    name="Screenshot on Failure",
                    attachment_type=allure.attachment_type.PNG
                )
            # Если тест прошел успешно
            elif report.passed:
                allure.attach(
                    page.screenshot(full_page=True),
                    name="Screenshot on Success",
                    attachment_type=allure.attachment_type.PNG
                )