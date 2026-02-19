import pytest
import allure
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect


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


@allure.feature("UI Testing")
@allure.story("Login Scenarios")
def test_add_to_cart_positive(page: Page):
    """Позитивный тест: Добавление товара в корзину."""
    login_p = LoginPage(page)
    login_p.navigate()
    login_p.login("standard_user", "secret_sauce")

    # Прямое взаимодействие (для простоты примера без PageObject инвентаря)
    page.locator("#add-to-cart-sauce-labs-backpack").click()

    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")


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

    assert "Username and password do NOT match" in login_p.get_error_text()