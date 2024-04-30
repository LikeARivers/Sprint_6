from conftest import driver
import allure
from data import URL
from pages.scooter_pages import PagesLogoScooter



class TestClickLogoScooter:

    @allure.title("Проверка перехода по лого Самоката")
    @allure.description("Проверяем что после клика на лого Самоката происходит переход на главную страницу Яндекс Самокат")
    def test_click_logo_scooter(self, driver):
        logo_scooter_pages = PagesLogoScooter(driver)
        logo_scooter_pages.open_page(URL.YASCOOTER)

        logo_scooter_pages.click_top_button()
        logo_scooter_pages.click_logo_scooter()
        current_url = logo_scooter_pages.get_current_url()
        assert current_url == URL.YASCOOTER