import allure
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.feature("UI Testing")
@allure.story("Login Scenarios")
def test_login_standard_user_positive(page: Page):
    """Позитивный тест: Успешный логин."""
    login_p = LoginPage(page)

    with allure.step("Open Login Page"):
        login_p.navigate()

    with allure.step("Login as standard user"):
        login_p.login("standard_user", "secret_sauce")

    with allure.step("Verify redirect to inventory"):
        # Проверяем, что URL изменился на страницу товаров
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


# Не забудь добавить импорт InventoryPage в самом верху файла test_ui_saucedemo.py:
# from pages.inventory_page import InventoryPage

@allure.feature("UI Testing")
@allure.story("Login Scenarios")
def test_add_to_cart_positive(page: Page):
    """Позитивный тест: Добавление товара в корзину."""
    # 1. Инициализируем страницы
    login_p = LoginPage(page)
    inventory_p = InventoryPage(page)

    # 2. Логинимся
    with allure.step("Open Login Page and Login"):
        login_p.navigate()
        login_p.login("standard_user", "secret_sauce")

    # 3. Добавляем товар (теперь через Page Object!)
    with allure.step("Add backpack to cart"):
        inventory_p.add_backpack_to_cart()

    # 4. Проверяем результат
    with allure.step("Verify cart badge shows 1 item"):
        assert inventory_p.get_cart_items_count() == "1"


@allure.feature("UI Testing")
@allure.story("Negative Login Scenarios")
def test_login_locked_out_user_negative(page: Page):
    """Негативный тест: Заблокированный пользователь."""
    login_p = LoginPage(page)
    login_p.navigate()
    login_p.login("locked_out_user", "secret_sauce")

    assert "Sorry, this user has been locked out" in login_p.get_error_text()


@allure.feature("UI Testing")
@allure.story("Negative Login Scenarios")
def test_login_invalid_password_negative(page: Page):
    """Негативный тест: Неверный пароль."""
    login_p = LoginPage(page)
    login_p.navigate()
    login_p.login("standard_user", "wrong_pass")

    assert "Username and password do not match" in login_p.get_error_text()