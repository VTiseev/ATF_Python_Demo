from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Класс для страницы авторизации SauceDemo."""

    def __init__(self, page: Page):
        super().__init__(page)  # Вызываем конструктор BasePage

        # Локаторы
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        # Используем метод open() из родительского BasePage
        self.open("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self):
        # Используем безопасный метод get_text() из родительского BasePage
        return self.get_text(self.error_message)