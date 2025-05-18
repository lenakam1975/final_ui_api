import requests


class SearchApi:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token


    def get_search_to_name(self) -> dict:
        path = "{url}v1.4/movie/search?page=1&limit=1&query=1+1".format(url=self.base_url)
        headers = {"X-API-KEY": self.token}
        resp = requests.get(path, headers=headers)
        return resp.json()

    def get_search_to_data(self):
        path = "{url}v1.4/movie/random?premiere.russia=01.01.1997".format(url=self.base_url)
        headers = {"X-API-KEY": self.token}
        resp = requests.get(path, headers=headers)
        return resp.json()

    def get_search_to_age(self):
        params = {
            "page": "1",
            "limit": "10",
            "ageRating": "!18"
        }
        path = "{url}v1.4/movie".format(url=self.base_url)
        headers = {"X-API-KEY": self.token}
        resp = requests.get(path, params=params, headers=headers)
        return resp.json()

    def get_search_to_year(self):
        params = {
            "page": "1",
            "limit": "1",
            "year": "2025"
        }
        path = "{url}v1.4/movie".format(url=self.base_url)
        headers = {"X-API-KEY": self.token}
        resp = requests.get(path, params=params, headers=headers)
        return resp.json()

    def get_search_to_rating(self):
        params = {
            "page": "1",
            "limit": "10",
            "rating.kp": "7-10"
        }
        path = "{url}v1.4/movie".format(url=self.base_url)
        headers = {"X-API-KEY": self.token}
        resp = requests.get(path, params=params, headers=headers)
        return resp.json()



