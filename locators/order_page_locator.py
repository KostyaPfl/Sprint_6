from selenium.webdriver.common.by import By


class OrderPageLocators:
    # надпись "Для кого самокат" на первой станице формы заказа
    ORDER_HEADER = By.XPATH, '// div[text()="Для кого самокат"]'

    # поле "Имя" на первой станице формы заказа
    NAME_FIELD = By.XPATH, "// input[@placeholder = '* Имя']"

    # поле "Фамилия" на первой станице формы заказа
    SURNAME_FIELD = By.XPATH, "// input[@placeholder = '* Фамилия']"

    # поле "Адрес" на первой станице формы заказа
    ADDRESS_FIELD = By.XPATH, "// input[@placeholder = '* Адрес: куда привезти заказ']"

    # поле "Станция метро" на первой станице формы заказа
    METRO_STATION_FIELD = By.XPATH, "//input[@placeholder = '* Станция метро']"

    # выпадающий список станций метро на первой станице формы заказа
    ADD_STATION = By.XPATH, '// div[@class = "select-search__select"]'

    # поле "Телефон" на первой станице формы заказа
    TELEPHONE_FIELD = By.XPATH, "// input[@placeholder = '* Телефон: на него позвонит курьер']"

    # кнопка "Далее" на первой станице формы заказа
    NEXT_BUTTON = By.XPATH, "// button[text() = 'Далее']"

    # надпись "Про аренду" на второй станице формы заказа
    ABOUT_RENT = By.XPATH, '// div[text()="Про аренду"]'

    # поле "Когда привезти самокат" на второй станице формы заказа
    DATA_FIELD = By.XPATH, "// input[@placeholder = '* Когда привезти самокат']"

    # поле "Срок аренды" на второй станице формы заказа
    RENTAL_PERIOD_FIELD = By.XPATH, "//span[@class ='Dropdown-arrow']"

    # строка выподающего списка "Срок аренды" на второй станице формы заказа
    PERIOD_BUTTON = By.XPATH, "// div[text() = 'двое суток']"

    # кнопка "Заказать" на второй станице формы заказа
    ORDER_BUTTON = By.XPATH, '//button[contains(@class, "Button_Middle") and text() = "Заказать"]'

    # надпись "Хотите оформить заказ?" на всплывающем окне подтверждения заказа
    CONFIRMATION_WINDOW_HEADER = By.XPATH, "// div[text() = 'Хотите оформить заказ?']"

    # кнопка "Да" на всплывающем окне подтверждения заказа
    YES_BUTTON = By.XPATH, '//button[text() = "Да"]'

    # надпись "Заказ оформлен" на всплывающем окне статуса заказа
    ORDER_PLACED = By.XPATH, "// div[text() = 'Заказ оформлен']"