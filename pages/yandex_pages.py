import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PagesLogoYandex(BasePage):
    LOGO_YANDEX = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    LOGO_YANDEX_ZEN = 'https://dzen.ru/?yredirect=true&is_autologin_ya=true'

    @allure.step('кликаем на лого Яндекс')
    def click_logo_yandex(self):
        logo_yandex = (self.wait_and_find_element(self.LOGO_YANDEX))
        logo_yandex.click()

    @allure.step('ждем загрузку Яндекс Дзен')
    def wait_yandex_page(self):
        yandex_page = (self.wait_and_find_url(self.LOGO_YANDEX_ZEN))
        return yandex_page