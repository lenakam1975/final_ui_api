import requests
import allure


@allure.epic("КиноПоиск")
@allure.suite("SearchApi")
class SearchApi:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    def get_search_to_name(self, name_movi) -> dict:
        """ Метод реализует получение результата
            поиска фильма по его названию через API
        """
        path = (
            "{url}v1.4/movie/search?page=1&limit=1&query={name}".
            format(url=self.base_url, name=name_movi)
        )
        headers = {
            "X-API-KEY": self.token,
            "accept": "application/json"
        }

        response = requests.get(path, headers=headers)
        return response.json()

    def get_search_to_data(self, data_realse) -> dict:
        """ Метод используется для получения случайных фильмов,
            выпущенных в указанный период (data_realse), через API
        """
        path = ("{url}v1.4/movie/random?premiere.russia={data}".
                format(url=self.base_url, data=data_realse))
        headers = {
            "X-API-KEY": self.token,
            "accept": "application/json"
        }
        params = {
            "page": "1",
            "limit": "3",
        }
        response = requests.get(path, params=params, headers=headers)
        return response.json()

    def get_search_to_age(self) -> dict:
        """ Метод осуществляет запрос к API
            для получения списка фильмов
            с рейтингом возраста, отличным от 18+
        """
        path = "{url}v1.4/movie".format(url=self.base_url)
        headers = {
            "X-API-KEY": self.token,
            "accept": "application/json"
        }
        params = {
            "page": "1",
            "limit": "10",
            "ageRating": "!18"
        }
        response = requests.get(path, params=params, headers=headers)
        return response.json()

    def get_search_to_year(self) -> dict:
        """ Метод получает список фильмов,
            выпущенных в конкретный год (в данном примере — 2025),
            используя API
        """
        params = {
            "page": "1",
            "limit": "10",
            "year": "2025"
        }
        path = "{url}v1.4/movie".format(url=self.base_url)
        headers = {"X-API-KEY": self.token}
        response = requests.get(path, params=params, headers=headers)
        return response.json()

    def get_search_to_rating(self) -> dict:
        """ Метод выполняет запрос к API
            для получения списка фильмов
            с определенным диапазоном рейтинга (от 7 до 10 баллов по Кинопоиску)
        """
        params = {
            "page": "1",
            "limit": "10",
            "rating.kp": "7-10"
        }
        path = "{url}v1.4/movie".format(url=self.base_url)
        headers = {"X-API-KEY": self.token}
        response = requests.get(path, params=params, headers=headers)
        return response.json()
