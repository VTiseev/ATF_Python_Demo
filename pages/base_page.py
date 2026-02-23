from playwright.sync_api import Page


class BasePage:
    """
    Базовый класс для всех Page Object.
    Содержит общие методы для работы со страницами.
    """

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        """Открывает переданный URL."""
        self.page.goto(url)

    def get_text(self, locator) -> str:
        """Безопасно извлекает текстовое содержимое локатора."""
        return locator.text_content()

    # В будущем сюда можно добавить методы вроде wait_for_element,
    # switch_to_iframe, scroll_to_bottom и т.д.