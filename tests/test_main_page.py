import allure
import pytest
from urls import Urls
from data import ANSWERS
from page.main_page import MainPage


class TestMainPage:
    @allure.title('Проверка ответов на вопросы в разделе «Вопросы о важном»')
    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])

    def test_questions_and_answer(self, driver, num):
        main_page = MainPage(driver)
        driver.get(Urls.MAIN_PAGE)
        assert ANSWERS[num] == main_page.get_answer_text(num)
