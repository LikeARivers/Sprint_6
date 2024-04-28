from conftest import driver
import allure
from data import URL
from pages.order_pages import PagesPlacingAnOrder



class TestOrder2:

    @allure.title("Проверка оформления заказа")
    @allure.description("Оформляем заказ по позитивному сценарию со вторым набором данных")
    def test_successful_ordering_1(self, driver):
        order_pages = PagesPlacingAnOrder(driver)
        order_pages.open_page(URL.YASCOOTER)

        order_pages.scroll_to_bottom_button()
        order_pages.click_bottom_button()
        order_pages.input_long_name()
        order_pages.input_long_surname()
        order_pages.input_long_address()
        order_pages.click_input_subway()
        order_pages.click_list_subway_with_space()
        order_pages.input_phone_long_number()
        order_pages.click_next_button()
        order_pages.click_input_rent()
        order_pages.click_list_rent_two()
        order_pages.input_date_next_month()
        order_pages.click_black_checkbox()
        order_pages.input_comment()
        order_pages.finish_order_button()
        order_pages.yes_button()
        assert order_pages.info_successful_ordering()