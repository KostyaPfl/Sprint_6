import allure
from locators.order_page_locator import OrderPageLocators
from page.base_page import BasePage
from helper import generate_after_tomorrow_date, generate_phone_number
from data import UserData


class OrderPage(BasePage):

    @allure.step('Нажимаем на кнопку "Далее" на первой странице оформления заказа')
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем первую страницу формы заказа')
    def filling_order_form(self, name, surname):
        self.find_element_with_wait(OrderPageLocators.ORDER_HEADER)
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_FIELD, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, UserData.STREET)
        self.add_text_to_element(OrderPageLocators.METRO_STATION_FIELD, UserData.METRO_STATION)
        self.click_on_element(OrderPageLocators.ADD_STATION)
        self.add_text_to_element(OrderPageLocators.TELEPHONE_FIELD, generate_phone_number())

    @allure.step('Заполняем вторую страницу формы заказа')
    def filling_order_form_next(self):
        self.find_element_with_wait(OrderPageLocators.ABOUT_RENT)
        self.click_on_element(OrderPageLocators.DATA_FIELD)
        self.add_text_to_element(OrderPageLocators.DATA_FIELD, generate_after_tomorrow_date())
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocators.PERIOD_BUTTON)

    @allure.step('нажимаем на кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('нажимаем на кнопку "Да" во всплывающем окне подтверждения заказа')
    def click_yes_button(self):
        self.find_element_with_wait(OrderPageLocators.CONFIRMATION_WINDOW_HEADER)
        self.click_on_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Оформляем заказ')
    def create_order(self, name, surname):
        self.filling_order_form(name, surname)
        self.click_next_button()
        self.filling_order_form_next()
        self.click_order_button()
        self.click_yes_button()

    @allure.step('Проверяем окно оформленного заказа')
    def page_create_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_PLACED)
