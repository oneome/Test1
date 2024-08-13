import json

class Settings:
    """
    Класс Settings загружает и хранит настройки из config.json.
    """

    def __init__(self, config_file='.\config.json'):
        with open(config_file, 'r') as file:
            self.cfg = json.load(file)

    def get(self, key):
        return self.cfg.get(key)

    def get_mail_server(self):
        return self.cfg.get('mail-server')
