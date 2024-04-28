import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PagesPlacingAnOrder(BasePage):
    TOP_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    BOTTOM_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    INPUT_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    INPUT_SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    INPUT_SUBWAY = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    LIST_SUBWAY = [By.XPATH, f'.//div[@class = "select-search__select"]//div[text()="Сокольники"]']
    INPUT_PHONE_NUMBER = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    INPUT_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    INPUT_RENT = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    LIST_RENT = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    BLACK_CHECKBOX = (By.ID, "black")
    INPUT_COMMENT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    FINISH_ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[contains(text(), 'Заказать')]")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    INFO_SUCCESSFUL_ORDERING = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")


    @allure.step('кликаем на верхнюю кнопку Заказать')
    def click_top_button(self):
        top_button = self.wait_and_find_element(self.TOP_BUTTON)
        top_button.click()

    @allure.step('скролл до нижней кнопки Заказать')
    def scroll_to_bottom_button(self):
        bottom_button = self.wait_and_find_element(self.BOTTOM_BUTTON)
        self.scroll_into_view(bottom_button)

    @allure.step('кликаем на нижнюю кнопку Заказать')
    def click_bottom_button(self):
        bottom_button = self.wait_and_find_element(self.BOTTOM_BUTTON)
        bottom_button.click()

    @allure.step('в поле Имя вводим Ян')
    def input_short_name(self):
        name = self.wait_and_find_element(self.INPUT_NAME)
        name.send_keys('Ян')

    @allure.step('в поле Имя вводим Константин')
    def input_long_name(self):
        name = self.wait_and_find_element(self.INPUT_NAME)
        name.send_keys('Константин')

    @allure.step('в поле Фамилия вводим Ки')
    def input_short_surname(self):
        surname = self.wait_and_find_element(self.INPUT_SURNAME)
        surname.send_keys('Ки')

    @allure.step('в поле Фамилия вводим Константинов')
    def input_long_surname(self):
        surname = self.wait_and_find_element(self.INPUT_SURNAME)
        surname.send_keys('Константинов')

    @allure.step('в поле Адрес вводим Улица')
    def input_short_address(self):
        address = self.wait_and_find_element(self.INPUT_ADDRESS)
        address.send_keys('Улица')

    @allure.step('в поле Адрес вводим Улица-Улица-Улица')
    def input_long_address(self):
        address = self.wait_and_find_element(self.INPUT_ADDRESS)
        address.send_keys('Улица-Улица-Улица')

    @allure.step('кликаем на поле Станция метро')
    def click_input_subway(self):
        input_subway = self.wait_and_find_element(self.INPUT_SUBWAY)
        input_subway.click()

    @allure.step('кликаем на станцию Сокольники в выпадающем списке')
    def click_list_subway_without_space(self):
        list_subway = self.wait_and_find_element(self.LIST_SUBWAY)
        list_subway.click()

    @allure.step('кликаем на станцию Преображенская площадь в выпадающем списке')
    def click_list_subway_with_space(self):
        list_subway = self.wait_and_find_element(self.LIST_SUBWAY)
        list_subway.click()

    @allure.step('в поле Телефон вводим +7123456789')
    def input_phone_short_number(self):
        phone_number = self.wait_and_find_element(self.INPUT_PHONE_NUMBER)
        phone_number.send_keys('+7123456789')

    @allure.step('в поле Телефон вводим +712312312312')
    def input_phone_long_number(self):
        phone_number = self.wait_and_find_element(self.INPUT_PHONE_NUMBER)
        phone_number.send_keys('+712312312312')

    @allure.step('кликаем на кнопку Далее')
    def click_next_button(self):
        next_button = self.wait_and_find_element(self.NEXT_BUTTON)
        next_button.click()

    @allure.step('в поле Когда привезти самокат вводим 30.04.2024')
    def input_date_present_month(self):
        date = self.wait_and_find_element(self.INPUT_DATE)
        date.send_keys('30.04.2024')

    @allure.step('в поле Когда привезти самокат вводим 02.05.2024')
    def input_date_next_month(self):
        date = self.wait_and_find_element(self.INPUT_DATE)
        date.send_keys('27.04.2024')

    @allure.step('кликаем на поле Срок аренды')
    def click_input_rent(self):
        input_rent = self.wait_and_find_element(self.INPUT_RENT)
        input_rent.click()

    @allure.step('из выпадающего списка выбираем сутки')
    def click_list_rent_one(self):
        list_rent = self.wait_and_find_element(self.LIST_RENT)
        list_rent.click()

    @allure.step('из выпадающего списка выбираем двое суток')
    def click_list_rent_two(self):
        list_rent = self.wait_and_find_element(self.LIST_RENT)
        list_rent.click()

    @allure.step('нажимаем чек-бокс черный жемчуг')
    def click_black_checkbox(self):
        black_checkbox = self.wait_and_find_element(self.BLACK_CHECKBOX)
        black_checkbox.click()

    @allure.step('в поле комментарий вводим Позвони по номеру телефона')
    def input_comment(self):
        comment = self.wait_and_find_element(self.INPUT_COMMENT)
        comment.send_keys('Позвони по номеру телефона')

    @allure.step('кликаем на кнопку Заказать')
    def finish_order_button(self):
        finish_order_button = self.wait_and_find_element(self.FINISH_ORDER_BUTTON)
        finish_order_button.click()

    @allure.step('кликаем на кнопку Да')
    def yes_button(self):
        yes_button = self.wait_and_find_element(self.YES_BUTTON)
        yes_button.click()

    @allure.step('ищем текст Заказ оформлен')
    def info_successful_ordering(self):
        successful_ordering = self.wait_and_find_element(self.INFO_SUCCESSFUL_ORDERING)
        return successful_ordering.is_displayed()