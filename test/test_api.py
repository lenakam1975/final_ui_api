import pytest
import allure


@pytest.mark.parametrize("expected_status", [200])
@allure.id("Api-1")
@allure.severity("critical")
@allure.title("Поиск фильма по названию")
@allure.feature("API. Поиск фильма")
@allure.description("API тестирование.Поиск фильма по названию")
def test_get_search_to_name(expected_status, auth_api):
    with allure.step("Отправляем GET запрос. Поиск фильма по названию"):
        search_to_name = auth_api.get_search_to_name("Вий")

    with allure.step("Ожидаем статус == 200"):
        assert expected_status == 200

    with allure.step("Ожидаемый результат должен быть словарь dict"):
        assert isinstance(search_to_name, dict)

    with allure.step("Логируем полученные данные"):
        print(f"Полученные данные: {search_to_name}, "
              f"Статус: {expected_status}")


@pytest.mark.parametrize("expected_status", [200])
@allure.id("Api-2")
@allure.severity("Major")
@allure.title("Поиск фильма по дате премьеры в России")
@allure.feature("API. Поиск фильма")
@allure.description("API тестирование.Поиск фильма дате премьеры в России")
def test_get_search_to_data(expected_status, auth_api):
    with allure.step("Отправляем GET запрос. "
                     "Поиск фильма по дате премьеры в России"):
        search_to_data = auth_api.get_search_to_data("01.01.1997")

    with allure.step("Ожидаем статус == 200"):
        assert expected_status == 200

    with allure.step("Ожидаемый результат должен быть словарь dict"):
        assert isinstance(search_to_data, dict)
        assert len(search_to_data) > 0

    with allure.step("Логируем полученные данные"):
        print(f"Полученные данные: {search_to_data}, "
              f"Статус: {expected_status}")


@pytest.mark.parametrize("expected_status", [200])
@allure.id("Api-3")
@allure.severity("critical")
@allure.title("Поиск фильма по возрастному рейтингу")
@allure.feature("API. Поиск фильма")
@allure.description("API тестирование.Поиск фильма по возрастному рейтингу")
def test_get_search_to_age(expected_status, auth_api):
    with allure.step("Отправляем GET запрос. "
                     "Поиск фильма по возрастному рейтингу"):
        search_to_age = auth_api.get_search_to_age()

    with allure.step("Ожидаем статус == 200"):
        assert expected_status == 200

    with allure.step("Ожидаемый результат должен быть словарь dict"):
        assert isinstance(search_to_age, dict)
        assert len(search_to_age) > 0

    with allure.step("Логируем полученные данные"):
        for movie in search_to_age['docs']:
            print(
                f"Статус: {expected_status}, "
                f"Полученные данные: (ID: {movie['id']}, "
                f"Название: {movie['name'] or movie['alternativeName']}, "
                f"Год: {movie['year']}, "
                f"Рейтинг KP: {movie['rating']['kp']})"
            )


@pytest.mark.parametrize("expected_status", [200])
@allure.id("Api-4")
@allure.severity("Minor")
@allure.title("Поиск фильма по году")
@allure.feature("API. Поиск фильма")
@allure.description("API тестирование.Поиск фильма по году")
def test_get_search_to_year(expected_status, auth_api):
    with allure.step("Отправляем GET запрос. "
                     "Поиск фильма по году"):
        search_to_year = auth_api.get_search_to_year()

    with allure.step("Ожидаем статус == 200"):
        assert expected_status == 200

    with allure.step("Ожидаемый результат должен быть словарь dict"):
        assert isinstance(search_to_year, dict)
        assert len(search_to_year) > 0

    with allure.step("Логируем полученные данные"):
        print(f"Полученные данные: {search_to_year}, "
              f"Статус: {expected_status}")


@pytest.mark.parametrize("expected_status", [200])
@allure.id("Api-5")
@allure.severity("critical")
@allure.title("Поиск фильма по рейтингу Кинопоиск")
@allure.feature("API. Поиск фильма")
@allure.description("API тестирование.Поиск фильма по рейтингу Кинопоиск")
def test_get_search_to_rating(expected_status, auth_api):
    with allure.step("Отправляем GET запрос. "
                     "Поиск фильма по рейтингу Кинопоиск"):
        search_to_rating = auth_api.get_search_to_rating()

    with allure.step("Ожидаем статус == 200"):
        assert expected_status == 200

    with allure.step("Ожидаемый результат должен быть словарь dict"):
        assert isinstance(search_to_rating, dict)
        assert len(search_to_rating) > 0

    with allure.step("Логируем полученные данные"):
        for movie in search_to_rating['docs']:
            print(
                f"Статус: {expected_status}, "
                f"Полученные данные: (ID: {movie['id']}, "
                f"Название: {movie['name'] or movie['alternativeName']} "
                f"Рейтинг KP: {movie['rating']['kp']})"
            )
