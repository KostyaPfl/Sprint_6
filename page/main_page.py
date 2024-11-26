import allure
from locators.main_page_locators import MainPageLocators
from page.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Кликаем на вопрос')
    def click_on_question(self, num):
        self.find_element_with_wait(MainPageLocators.HOME_HEADER)
        self.scroll_to_element(MainPageLocators.LAST_QUESTION)
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION, num)
        self.click_on_element(locator_q_formatted)

    @allure.step('Получаем ответ на вопрос')
    def get_answer(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверяем ответ')
    def get_answer_text(self, num):
        self.click_on_question(num)
        return self.get_answer(num)


    @allure.step(' Кликаем на кнопку "Заказать" в вверху страницы')
    def click_header_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step(' Кликаем на кнопку "Заказать" внизу страницы')
    def click_order_down_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_DOWN)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_DOWN)
