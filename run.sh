python -m pytest --alluredir allure-result
allure serve allure-result # сгенерировать результат тестов в отчет

pytest --alluredir=./reports
allure serve ./reports