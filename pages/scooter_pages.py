import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PagesLogoScooter(BasePage):
    TOP_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")

    @allure.step('кликаем на верхнюю кнопку Заказать')
    def click_top_button(self):
        top_button = self.wait_and_find_element(self.TOP_BUTTON)
        top_button.click()

    @allure.step('кликаем на лого Самокат')
    def click_logo_scooter(self):
        logo_scooter = self.wait_and_find_element(self.LOGO_SCOOTER)
        logo_scooter.click()