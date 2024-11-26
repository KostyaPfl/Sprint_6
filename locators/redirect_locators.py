from selenium.webdriver.common.by import By


class RedirectLocators:
    # логотип "Яндекс" сверху страницы "Яндекс.Самокат"
    YANDEX_LOGO = By.XPATH, './/a[@href="//yandex.ru"]'

    # логотип "самокат" сверху страницы "Яндекс.Самокат"
    SCOOTER_LOGO = By.XPATH, '// a[contains(@class, "Header_LogoScooter")]'

    # логотип "Дзен" на главной стрранице "Яндекс.дзен"
    DZEN_LOGO = By.XPATH, '// header[@id = "dzen-header"]'

    # чертеж самоката на главной странице "Яндекс.Самокат"
    SCOOTER_BLUEPRINT = By.XPATH, '// div[contains(@class, "Home_BluePrint")]'

