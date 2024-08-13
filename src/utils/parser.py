import csv
from io import StringIO

class Parser:
    def parse(self, data):
        result = []
        reader = csv.DictReader(StringIO(data))
        
        # Добавляем отладочный вывод
        for row in reader:
            print(row)  # Выводим каждую строку для проверки
            mail = row['mail']
            words = row['words'].split(',')
            result.append((mail, words))
        
        return result

    def execute(self, data):
        return self.parse(data)
