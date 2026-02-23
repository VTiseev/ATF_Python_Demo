from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Класс для страницы списка товаров (Inventory) SauceDemo."""

    def __init__(self, page: Page):
        super().__init__(page)  # Наследуем возможности BasePage

        # Локаторы (адреса элементов на странице)
        self.add_backpack_btn = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_backpack_to_cart(self):
        """Метод для добавления рюкзака в корзину."""
        self.add_backpack_btn.click()

    def get_cart_items_count(self) -> str:
        """Метод для получения количества товаров на значке корзины."""
        return self.get_text(self.cart_badge)
