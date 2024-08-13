class Beautifier:
    """
    Beautifier удаляет лишние пробелы и точки в начале и конце слова.
    """

    def beautify(self, word):
        return word.strip().strip('.')

    def execute(self, word):
        return self.beautify(word)
