from conftest import driver
import allure
from data import URL
from pages.main_page import MainPageQuests, MainPageAnswers


class TestQuest1:

    @allure.title("Проверка Вопроса 1")
    @allure.description("Проверяем что Вопрос 1 раскрывается при нажатии на него")
    def test_click_quest_1(self, driver):
        main_page_quest = MainPageQuests(driver)
        main_page_quest.open_page(URL.YASCOOTER)

        main_page_quest.scroll_to_quest_1()
        main_page_quest.find_and_click_quest_1()

        main_page_answer = MainPageAnswers(driver)
        assert main_page_answer.find_answer_1()





