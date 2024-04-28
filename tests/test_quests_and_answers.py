import allure
import pytest
from conftest import driver
from data import URL
from pages.main_page import MainPageQuestsAndAnswers

class TestQuestsAndAnswers:

    @allure.title("Проверка Вопроса {quest_number}")
    @allure.description("Проверяем что каждый вопрос раскрывается при нажатии на него")
    @pytest.mark.parametrize("quest_number, quest_element, answer_element, answer_text", [
        (1, MainPageQuestsAndAnswers.QUEST_1, MainPageQuestsAndAnswers.ANSWER_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (2, MainPageQuestsAndAnswers.QUEST_2, MainPageQuestsAndAnswers.ANSWER_2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (3, MainPageQuestsAndAnswers.QUEST_3, MainPageQuestsAndAnswers.ANSWER_3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (4, MainPageQuestsAndAnswers.QUEST_4, MainPageQuestsAndAnswers.ANSWER_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (5, MainPageQuestsAndAnswers.QUEST_5, MainPageQuestsAndAnswers.ANSWER_5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (6, MainPageQuestsAndAnswers.QUEST_6, MainPageQuestsAndAnswers.ANSWER_6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (7, MainPageQuestsAndAnswers.QUEST_7, MainPageQuestsAndAnswers.ANSWER_7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (8, MainPageQuestsAndAnswers.QUEST_8, MainPageQuestsAndAnswers.ANSWER_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ])

    def test_click_quest(self, driver, quest_number, quest_element, answer_element, answer_text):
        main_page_quest_and_answers = MainPageQuestsAndAnswers(driver)

        main_page_quest_and_answers.open_page(URL.YASCOOTER)
        main_page_quest_and_answers.scroll_to_quest(quest_element)
        main_page_quest_and_answers.find_and_click_quest(quest_element)

        assert main_page_quest_and_answers.find_answer(answer_element)