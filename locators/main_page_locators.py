from selenium.webdriver.common.by import By


class MainPageLocators:
    # надпись "Самокат на пару дней" на главной странице сайта Яндекс Самокат
    HOME_HEADER = By.XPATH, '//*[contains(@class, Home_Header)]'

    # кнопка "Заказать" вверху страницы сайта Яндекс Самокат
    ORDER_BUTTON_HEADER = By.XPATH, '//button[text() = "Статус заказа"]/preceding-sibling::button[text() = "Заказать"]'

    # кнопка "Заказать" внизу главной страницы сайта Яндекс Самокат
    ORDER_BUTTON_DOWN = By.XPATH, './/button[contains(@class, Button_UltraBig) and text() = "Заказать"]'

    # поля с вопросами в блоке "Вопросы о важном"
    QUESTION = By.XPATH, '//*[@id="accordion__heading-{}"]'

    # выпадающие строки с ответами "Вопросы о важном"
    ANSWER = By.XPATH, '//*[@id="accordion__panel-{}"]'

    # последний вопрос в блоке "Вопросы о важном"
    LAST_QUESTION = By.XPATH, '//*[@id="accordion__heading-7"]'