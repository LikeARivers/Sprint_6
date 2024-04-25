from conftest import driver
import allure
from data import URL
from pages.order_pages_2 import PagesPlacingAnOrder



class TestBottomButton:

    @allure.title("Проверка нижней кнопки Заказать")
    @allure.description("Проверяем что после клика на нижнюю кнопку заказать Происходит переход к форме заказа")
    def test_click_top_button(self, driver):
        order_pages = PagesPlacingAnOrder(driver)
        order_pages.open_page(URL.YASCOOTER)

        order_pages.scroll_to_bottom_button()
        order_pages.click_bottom_button()
        current_url = order_pages.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/order"