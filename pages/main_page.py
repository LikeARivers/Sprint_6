import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPageQuests(BasePage):
    QUEST_1 = (By.XPATH, "//div[@id = 'accordion__heading-0']")
    QUEST_2 = (By.XPATH, "//div[@id = 'accordion__heading-1']")
    QUEST_3 = (By.XPATH, "//div[@id = 'accordion__heading-2']")
    QUEST_4 = (By.XPATH, "//div[@id = 'accordion__heading-3']")
    QUEST_5 = (By.XPATH, "//div[@id = 'accordion__heading-4']")
    QUEST_6 = (By.XPATH, "//div[@id = 'accordion__heading-5']")
    QUEST_7 = (By.XPATH, "//div[@id = 'accordion__heading-6']")
    QUEST_8 = (By.XPATH, "//div[@id = 'accordion__heading-7']")

    @allure.step('скролл до Вопроса №1')
    def scroll_to_quest_1(self):
        quest_1 = (self.wait_and_find_element(self.QUEST_1))
        self.driver.execute_script("arguments[0].scrollIntoView();", quest_1)

    @allure.step('Ищем Вопрос №1 и кликаем на него')
    def find_and_click_quest_1(self):
        quest_1 = (self.wait_and_find_element(self.QUEST_1))
        quest_1.click()

    @allure.step('скролл до Вопроса №2')
    def scroll_to_quest_2(self):
        quest_2 = (self.wait_and_find_element(self.QUEST_2))
        self.driver.execute_script("arguments[0].scrollIntoView();", quest_2)

    @allure.step('Ищем Вопрос №2 и кликаем на него')
    def find_and_click_quest_2(self):
        quest_2 = (self.wait_and_find_element(self.QUEST_2))
        quest_2.click()

    @allure.step('скролл до Вопроса №3')
    def scroll_to_quest_3(self):
        quest_3 = (self.wait_and_find_element(self.QUEST_3))
        self.driver.execute_script("arguments[0].scrollIntoView();", quest_3)

    @allure.step('Ищем Вопрос №3 и кликаем на него')
    def find_and_click_quest_3(self):
        quest_3 = (self.wait_and_find_element(self.QUEST_3))
        quest_3.click()

    @allure.step('скролл до Вопроса №4')
    def scroll_to_quest_4(self):
        quest_4 = (self.wait_and_find_element(self.QUEST_4))
        self.driver.execute_script("arguments[0].scrollIntoView();", quest_4)

    @allure.step('Ищем Вопрос №4 и кликаем на него')
    def find_and_click_quest_4(self):
        quest_4 = (self.wait_and_find_element(self.QUEST_4))
        quest_4.click()

    @allure.step('скролл до Вопроса №5')
    def scroll_to_quest_5(self):
        quest_5 = (self.wait_and_find_element(self.QUEST_5))
        self.driver.execute_script("arguments[0].scrollIntoView();", quest_5)

    @allure.step('Ищем Вопрос №5 и кликаем на него')
    def find_and_click_quest_5(self):
        quest_5 = (self.wait_and_find_element(self.QUEST_5))
        quest_5.click()

    @allure.step('скролл до Вопроса №6')
    def scroll_to_quest_6(self):
        quest_6 = (self.wait_and_find_element(self.QUEST_6))
        self.driver.execute_script("arguments[0].scrollIntoView();", quest_6)

    @allure.step('Ищем Вопрос №6 и кликаем на него')
    def find_and_click_quest_6(self):
        quest_6 = (self.wait_and_find_element(self.QUEST_6))
        quest_6.click()

    @allure.step('скролл до Вопроса №7')
    def scroll_to_quest_7(self):
        quest_7 = (self.wait_and_find_element(self.QUEST_7))
        self.driver.execute_script("arguments[0].scrollIntoView();", quest_7)

    @allure.step('Ищем Вопрос №7 и кликаем на него')
    def find_and_click_quest_7(self):
        quest_7 = (self.wait_and_find_element(self.QUEST_7))
        quest_7.click()

    @allure.step('скролл до Вопроса №8')
    def scroll_to_quest_8(self):
        quest_8 = (self.wait_and_find_element(self.QUEST_8))
        self.driver.execute_script("arguments[0].scrollIntoView();", quest_8)

    @allure.step('Ищем Вопрос №8 и кликаем на него')
    def find_and_click_quest_8(self):
        quest_8 = (self.wait_and_find_element(self.QUEST_8))
        quest_8.click()

class MainPageAnswers(BasePage):
    ANSWER_1 = (By.XPATH, "//p[text() = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    ANSWER_2 = (By.XPATH, "//p[text() = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")
    ANSWER_3 = (By.XPATH, "//p[text() = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    ANSWER_4 = (By.XPATH, "//p[text() = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    ANSWER_5 = (By.XPATH, "//p[text() = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    ANSWER_6 = (By.XPATH, "//p[text() = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")
    ANSWER_7 = (By.XPATH, "//p[text() = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    ANSWER_8 = (By.XPATH, "//p[text() = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']")

    @allure.step('Ищем Ответ на Вопрос №1')
    def find_answer_1(self):
        answer_1 = (self.wait_and_find_element(self.ANSWER_1))
        return answer_1.is_displayed()

    @allure.step('Ищем Ответ на Вопрос №2')
    def find_answer_2(self):
        answer_2 = (self.wait_and_find_element(self.ANSWER_2))
        return answer_2.is_displayed()

    @allure.step('Ищем Ответ на Вопрос №3')
    def find_answer_3(self):
        answer_3 = (self.wait_and_find_element(self.ANSWER_3))
        return answer_3.is_displayed()

    @allure.step('Ищем Ответ на Вопрос №4')
    def find_answer_4(self):
        answer_4 = (self.wait_and_find_element(self.ANSWER_4))
        return answer_4.is_displayed()

    @allure.step('Ищем Ответ на Вопрос №5')
    def find_answer_5(self):
        answer_5 = (self.wait_and_find_element(self.ANSWER_5))
        return answer_5.is_displayed()

    @allure.step('Ищем Ответ на Вопрос №6')
    def find_answer_6(self):
        answer_6 = (self.wait_and_find_element(self.ANSWER_6))
        return answer_6.is_displayed()

    @allure.step('Ищем Ответ на Вопрос №7')
    def find_answer_7(self):
        answer_7 = (self.wait_and_find_element(self.ANSWER_7))
        return answer_7.is_displayed()

    @allure.step('Ищем Ответ на Вопрос №8')
    def find_answer_8(self):
        answer_8 = (self.wait_and_find_element(self.ANSWER_8))
        return answer_8.is_displayed()