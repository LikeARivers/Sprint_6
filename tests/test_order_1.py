from conftest import driver
import allure
from data import URL
from pages.order_pages_1 import PagesPlacingAnOrder1



class TestOrder1:

    @allure.title("Проверка оформления заказа")
    @allure.description("Оформляем заказ по позитивному сценарию с первым набором данных")
    def test_successful_ordering_1(self, driver):
        order_pages = PagesPlacingAnOrder1(driver)
        order_pages.open_page(URL.YASCOOTER)

        order_pages.click_top_button()
        order_pages.input_name()
        order_pages.input_surname()
        order_pages.input_address()
        order_pages.click_input_subway()
        order_pages.click_list_subway()
        order_pages.input_phone_number()
        order_pages.click_next_button()
        order_pages.click_input_rent()
        order_pages.click_list_rent()
        order_pages.input_date()
        order_pages.finish_order_button()
        order_pages.yes_button()
        assert order_pages.info_successful_ordering()
