import allure
from selenium.webdriver.common.by import By


@allure.epic("КиноПоиск")
@allure.suite("MainPage")
class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.kinopoisk.ru/"

    def open(self):
        self.driver.get(self.url)

    def click_on_button(self):
        button = self.driver.find_element(
            By.CLASS_NAME, 'styles_loginButton__LWZQp')
        button.click()

    def input_text(self, text):
        input_text = self.driver.find_element(By.CSS_SELECTOR, "input")
        input_text.click()
        input_text.clear()
        input_text.send_keys(text)

    def navigation_menu(self, class_names):
        elements = self.driver.find_elements(By.CLASS_NAME, class_names)
        for element in elements:
            element.click()
        self.driver.back()

    def go_any_page(self, selector):
        element_img = self.driver.find_element(By.XPATH, selector)
        element_img.click()
