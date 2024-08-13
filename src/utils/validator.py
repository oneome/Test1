import re

class Validator:
    """
    Validator проверяет валидность слов.
    """

    def validate(self, word):
        if len(word) <= 3:
            return False, "Длина слова меньше или равна 3"
        if not re.match(r'^[a-zA-Z0-9.]+$', word):
            return False, "Недопустимые символы в слове"
        if '..' in word:
            return False, "Две точки подряд"
        return True, "Валидное слово"

    def execute(self, word):
        return self.validate(word)
