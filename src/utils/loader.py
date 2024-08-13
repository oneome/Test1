import requests

class Loader:
    """
    Loader загружает данные из Google таблицы.
    """

    def load(self, link):
        response = requests.get(link)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to load data from {link}")

    def execute(self, link):
        return self.load(link)
