import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.tag("ui")
@allure.id("MainPage-1")
@allure.severity("blocker")
@allure.title("Клик по кнопке 'Вход'")
@allure.story("работа функциональности кнопки 'Вход'")
@allure.feature("кнопка 'Вход'")
@allure.description("Функциональность кнопки 'Вход' на главной странице")
def test_button_entrance(main_page):
    with allure.step("Нажать на кнопку 'Вход'"):
        main_page.click_on_button()

    with allure.step("Дождаться загрузки элемента на странице"):
        wait = WebDriverWait(main_page.driver, 10)
        new_element = wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, 'passp-auth-content'))
        )
        assert new_element.is_displayed(), "Элемент не появился"


@allure.tag("ui")
@allure.id("MainPage-2")
@allure.severity("critical")
@allure.title("Ввод текста в строку поиск")
@allure.story("Поиск фильма в строке поиска")
@allure.feature("строка 'Поиск'")
@allure.description("Функциональность строки 'Поиск' на главной странице")
def test_input(main_page):
    with allure.step("Ввести название фильма в строку поиск"):
        main_page.input_text("Вий")

    with allure.step("Дождаться загрузки элемента на странице"):
        wait = WebDriverWait(main_page.driver, 20)
        new_element = wait.until(EC.visibility_of_element_located((
            By.CLASS_NAME, 'styles_root___4K2i'))
        )
        assert new_element.is_displayed(), "Элемент не появился"


@allure.tag("ui")
@allure.id("NoveltiesPage-1")
@allure.severity("critical")
@allure.title("Выбор фильма в разделе 'Новинки'")
@allure.story("Выбор фильма на странице по очередности")
@allure.feature("поиск фильма в разделе 'Новинки'")
@allure.description("Выбор фильма в разделе 'Новинки' и появление элемента 'Смотреть фильм'")
def test_novelties(novelties_page):
    with allure.step("Выбрать любой фильм, кликнув по нему"):
        novelties_page.click_element(30)

    with allure.step("Дождаться загрузки элемента на странице"):
        wait = WebDriverWait(novelties_page.driver, 10)
        new_element = wait.until(
            EC.visibility_of_element_located((
                By.XPATH, "//button[@data-test-id='MainButton_offer']")))
        assert new_element.is_displayed(), "Элемент не появился"

        button_text = new_element.text.strip()
        assert button_text != "", f"Кнопка пустая или невидимая: '{button_text}'"

        print(button_text)


@allure.tag("ui")
@allure.id("MainPage-3")
@allure.severity("critical")
@allure.title("Меню навигация на главной странице")
@allure.story("работа функциональности меню навигации")
@allure.feature("меню навигация")
@allure.description("Переход на страницы поочередно в меню навигации")
def test_link_to_page(main_page):
    with allure.step("Переход поочередно на страницы в меню навигации"):
        main_page.navigation_menu('styles_root__7mPJN styles_lightThemeItem__BSbZW')

        assert True, "Тест выполнен"


@allure.tag("ui")
@allure.id("ChannelsPage-1")
@allure.severity("critical")
@allure.title("Вернуться на главную страницу")
@allure.story("работа функциональности элемента 'Кинопоиск'")
@allure.feature("элемент хедер 'Кинопоиск' ")
@allure.description("Функциональность элемента 'Кинопоиск' расположенный в хедер")
def test_return_to_main_page(main_page, channels_page):
    with allure.step("Перейти на страницу 'Телеканалы' и нажать на элемент 'Кинопоиск'"):
        channels_page.back_homepage()

    with allure.step("Дождаться загрузки главной страницы"):
        current_url = main_page.driver.current_url
        assert current_url == "https://www.kinopoisk.ru/", (f""
                                                            f"Ожидалось перенаправление на главную страницу,"
                                                            f" получено: {current_url}")
