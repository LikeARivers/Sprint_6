import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPageQuestsAndAnswers(BasePage):
    QUEST_1 = (By.XPATH, "//div[@id = 'accordion__heading-0']")
    QUEST_2 = (By.XPATH, "//div[@id = 'accordion__heading-1']")
    QUEST_3 = (By.XPATH, "//div[@id = 'accordion__heading-2']")
    QUEST_4 = (By.XPATH, "//div[@id = 'accordion__heading-3']")
    QUEST_5 = (By.XPATH, "//div[@id = 'accordion__heading-4']")
    QUEST_6 = (By.XPATH, "//div[@id = 'accordion__heading-5']")
    QUEST_7 = (By.XPATH, "//div[@id = 'accordion__heading-6']")
    QUEST_8 = (By.XPATH, "//div[@id = 'accordion__heading-7']")
    ANSWER_1 = (By.XPATH, "//p[text() = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    ANSWER_2 = (By.XPATH, "//p[text() = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")
    ANSWER_3 = (By.XPATH, "//p[text() = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    ANSWER_4 = (By.XPATH, "//p[text() = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    ANSWER_5 = (By.XPATH, "//p[text() = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    ANSWER_6 = (By.XPATH, "//p[text() = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")
    ANSWER_7 = (By.XPATH, "//p[text() = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    ANSWER_8 = (By.XPATH, "//p[text() = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']")

    @allure.step('скролл до Вопроса')
    def scroll_to_quest(self, quest_element):
        quest = self.wait_and_find_element(quest_element)
        self.scroll_into_view(quest)

    @allure.step('Ищем Вопрос и кликаем на него')
    def find_and_click_quest(self, quest_element):
        quest = self.wait_and_find_element(quest_element)
        quest.click()

    @allure.step('Ищем Ответ на Вопрос')
    def find_answer(self, answer_element):
        answer = self.wait_and_find_element(answer_element)
        return answer.is_displayed()