from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# Указываем путь к нашему feature-файлу
scenarios('features/login.feature')

# --- ШАГИ (Steps) ---

@given("I open the login page")
def open_login(page: Page):
    """Шаг: Открытие страницы."""
    login_p = LoginPage(page)
    login_p.navigate()

# parsers.parse позволяет нам вытаскивать слова в кавычках как переменные!
@when(parsers.parse('I login as "{username}" with password "{password}"'))
def login_step(page: Page, username, password):
    """Шаг: Ввод логина и пароля."""
    login_p = LoginPage(page)
    # Используем метод из нашего Page Object!
    login_p.login(username, password)

@then("I should see the inventory page")
def verify_inventory(page: Page):
    """Шаг: Проверка результата."""
    # Убеждаемся, что мы перешли на нужную страницу
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@then(parsers.parse('I should see an error message containing "{error_text}"'))
def verify_error_message(page: Page, error_text):
    """Шаг: Проверка текста ошибки при логине."""
    login_p = LoginPage(page)
    # Берем текст ошибки со страницы и проверяем, что в нем есть ожидаемый текст
    assert error_text in login_p.get_error_text()