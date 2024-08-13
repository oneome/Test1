class Conveyor:
    """
    Класс Conveyor реализует конвейерную обработку задач.
    """

    def __init__(self, settings):
        self.settings = settings
        self.q = []

    def add_task(self, task, *args):
        self.q.append((task, args))

    def run(self):
        result = None
        while self.q:
            task, args = self.q.pop(0)
            if result is not None:
                args = (result,) + args  # Передаем результат предыдущей задачи как первый аргумент
            result = task(*args)  # Сохраняем результат выполнения задачи
        print(result)

# Пример добавления задач в конвейер:
# conveyor.add_task(Parser().execute, data)
# conveyor.add_task(Beautifier().execute, word)
