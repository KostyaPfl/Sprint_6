import allure
from locators.redirect_locators import RedirectLocators
from page.base_page import BasePage


class RedirectPage(BasePage):

    @allure.step('переход на главную страницу нажатием на логотип самокат "Самокат"')
    def scooter_logo_redirect(self):
        self.click_on_element(RedirectLocators.SCOOTER_LOGO)
        return self.find_element_with_wait(RedirectLocators.SCOOTER_BLUEPRINT)


    @allure.step('переход на "Дзен" нажимаем на логотип "Яндекс"')
    def yandex_logo_redirect(self):
        self.click_on_element(RedirectLocators.YANDEX_LOGO)
        self.switch_to_window()
        return self.find_element_with_wait(RedirectLocators.DZEN_LOGO)
