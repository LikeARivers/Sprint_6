from conftest import driver
import allure
from data import URL
from pages.yandex_pages import PagesLogoYandex
import time




class TestClickLogoYandex:

    @allure.title("Проверка перехода по лого Яндекса")
    @allure.description("Проверяем что после клика на лого Яндекса происходит переход на главную страницу Яндекс Дзен")
    def test_click_logo_yandex(self, driver):
        pages_logo_yandex = PagesLogoYandex(driver)
        pages_logo_yandex.open_page(URL.YASCOOTER)

        pages_logo_yandex.click_logo_yandex()
        all_tabs = driver.window_handles

        # Переключиться на последнюю (новую) вкладку
        new_tab = all_tabs[-1]
        driver.switch_to.window(new_tab)
        pages_logo_yandex.wait_yandex_page()
        # Получить текущий URL в новой вкладке
        current_url = driver.current_url
        assert current_url == URL.YANDEX_ZEN