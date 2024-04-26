import allure
import pytest
from conftest import driver
from data import URL
from pages.main_page import MainPageQuests, MainPageAnswers

class TestQuestsAndAnswers:

    @allure.title("Проверка Вопроса {quest_number}")
    @allure.description("Проверяем что Вопрос {quest_number} раскрывается при нажатии на него")
    @pytest.mark.parametrize("quest_number, quest_element, answer_element, answer_text", [
        (1, MainPageQuests.QUEST_1, MainPageAnswers.ANSWER_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (2, MainPageQuests.QUEST_2, MainPageAnswers.ANSWER_2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (3, MainPageQuests.QUEST_3, MainPageAnswers.ANSWER_3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (4, MainPageQuests.QUEST_4, MainPageAnswers.ANSWER_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (5, MainPageQuests.QUEST_5, MainPageAnswers.ANSWER_5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (6, MainPageQuests.QUEST_6, MainPageAnswers.ANSWER_6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (7, MainPageQuests.QUEST_7, MainPageAnswers.ANSWER_7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (8, MainPageQuests.QUEST_8, MainPageAnswers.ANSWER_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ])
    def test_click_quest(self, driver, quest_number, quest_element, answer_element, answer_text):
        main_page_quest = MainPageQuests(driver)
        main_page_quest.open_page(URL.YASCOOTER)

        # Находим элемент
        quest = main_page_quest.wait_and_find_element(quest_element)

        # Скроллируем до вопроса и кликаем на него
        main_page_quest.scroll_into_view(quest)
        quest.click()

        main_page_answer = MainPageAnswers(driver)

        # Проверяем наличие ответа и его текст
        answer = main_page_answer.wait_and_find_element(answer_element)
        assert answer.text == answer_text