from settings import Settings
from conveyor import Conveyor
from utils.loader import Loader
from utils.parser import Parser
from utils.beautifier import Beautifier
from utils.validator import Validator
from utils.notifier import Notifier
from utils.git import Git

def main():
    # Загрузка настроек
    settings = Settings()

    # Инициализация конвейера
    conveyor = Conveyor(settings)

    # 1. Загрузка данных из Google таблицы
    conveyor.add_task(Loader().execute, settings.get('table'))

    # 2. Парсинг данных
    conveyor.add_task(Parser().execute)

    # 3. Обработка каждого слова из списка слов (Beautify, Validate)
    
    # 3. Обработка каждого слова из списка слов (Beautify, Validate)
    def process_parsed_data(parsed_data):
        for mail, words in parsed_data:
            beautified_words = [Beautifier().execute(word) for word in words]
            validated_words = [(word, Validator().execute(word)) for word in beautified_words]
            print(validated_words)
            
            conveyor.add_task(Notifier(settings.get_mail_server()).execute, mail, validated_words)
    # Добавляем обработку данных после парсинга в очередь
    conveyor.add_task(process_parsed_data)
        
    conveyor.run()
if __name__ == "__main__":
    main()
