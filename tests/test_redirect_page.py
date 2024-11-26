import allure
from page.redirect_page import RedirectPage
from urls import Urls

class TestRedirectPage:
    @allure.title('Проверяем переход на главную страницу "Яндекс.Самокат" по клику на логотип "Самокат"')
    def test_logo_scooter_redirect(self, driver):
        redirect_page = RedirectPage(driver)
        driver.get(Urls.ORDER_PAGE)
        assert redirect_page.scooter_logo_redirect().is_displayed()

    @allure.title('Проверяем переход на "Дзен" по клику на логотип "Яндекса"')
    def test_ya_logo_redirect(self, driver):
        redirect_page = RedirectPage(driver)
        driver.get(Urls.MAIN_PAGE)
        assert redirect_page.yandex_logo_redirect().is_displayed()
