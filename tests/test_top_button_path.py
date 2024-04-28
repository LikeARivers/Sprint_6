from conftest import driver
import allure
from data import URL
from pages.order_pages import PagesPlacingAnOrder



class TestTopButton:

    @allure.title("Проверка верхней кнопки Заказать")
    @allure.description("Проверяем что после клика на верхнюю кнопку заказать Происходит переход к форме заказа")
    def test_click_top_button(self, driver):
        order_pages = PagesPlacingAnOrder(driver)
        order_pages.open_page(URL.YASCOOTER)

        order_pages.click_top_button()
        current_url = order_pages.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/order"