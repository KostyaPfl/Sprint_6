import allure
from urls import Urls
from page.order_page import OrderPage
from page.main_page import MainPage
from data import UserData


class TestOrderPage:
    @allure.title("Тест оформления заказа по клику на кнопку 'Заказать' вверху страницы")

    def test_place_an_order_one(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        driver.get(Urls.MAIN_PAGE)
        main_page.click_header_order_button()
        order_page.create_order(UserData.NAME_1, UserData.SURNAME_1)
        assert 'Заказ оформлен' in order_page.page_create_order()

    @allure.title("Тест оформления заказа по клику на кнопку 'Заказать' внизу страницы")

    def test_down_an_order_one(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        driver.get(Urls.MAIN_PAGE)
        main_page.click_order_down_button()
        order_page.create_order(UserData.NAME_2, UserData.SURNAME_2)
        assert 'Заказ оформлен' in order_page.page_create_order()
