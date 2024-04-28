from conftest import driver
import allure
from data import URL
from pages.order_pages import PagesPlacingAnOrder



class TestOrder1:

    @allure.title("Проверка оформления заказа")
    @allure.description("Оформляем заказ по позитивному сценарию с первым набором данных")
    def test_successful_ordering_1(self, driver):
        order_pages = PagesPlacingAnOrder(driver)
        order_pages.open_page(URL.YASCOOTER)

        order_pages.click_top_button()
        order_pages.input_short_name()
        order_pages.input_short_surname()
        order_pages.input_short_address()
        order_pages.click_input_subway()
        order_pages.click_list_subway_without_space()
        order_pages.input_phone_short_number()
        order_pages.click_next_button()
        order_pages.click_input_rent()
        order_pages.click_list_rent_one()
        order_pages.input_date_present_month()
        order_pages.finish_order_button()
        order_pages.yes_button()
        assert order_pages.info_successful_ordering()
