from conftest import driver
import allure
from data import URL
from pages.yandex_pages import PagesLogoYandex




class TestClickLogoYandex:

    @allure.title("Проверка перехода по лого Яндекса")
    @allure.description("Проверяем что после клика на лого Яндекса происходит переход на главную страницу Яндекс Дзен")
    def test_click_logo_yandex(self, driver):
        pages_logo_yandex = PagesLogoYandex(driver)
        pages_logo_yandex.open_page(URL.YASCOOTER)

        pages_logo_yandex.click_logo_yandex()
        pages_logo_yandex.switch_to_new_tab()
        pages_logo_yandex.wait_yandex_page()

        current_url = pages_logo_yandex.get_current_url()
        assert current_url == URL.YANDEX_ZEN