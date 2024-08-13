import os

class Git:
    """
    Git отвечает за добавление данных в файл и их коммит.
    """

    def add(self, data):
        with open('words.in', 'a') as file:
            file.write(f"{data}\n")

    def commit(self):
        os.system('./commit.sh')

    def execute(self, data):
        print(f'git execute {data}')
        self.add(data)
        self.commit()
