# Базовый цикл событий мог бы выглядеть следующим образом:
# Данный код, всего лишь условность, реальный цикл событий выглядеть куда длинее и запутанее
from time import sleep


# fruits = ['apple', 'banana', 'cherry']
# fruits.pop(1) # deletes banana :(
# print(*fruits)

class SimpleEventLoop:
    def __init__(self):
        self.tasks = [] # Очередь задач

    def add_task(self, task):
        self.tasks.append(task) # Добавляем задачи в очередь

    def run_forever(self):
        while self.tasks: # Выполнять, пока есть задачи
            task = self.tasks.pop(0) # получить первую задачу
            task() # выполнить задачу
            # sleep(1)
            # self.tasks.append(task)


# Пример функций-задач
def task1():
    print('Выполняется задача 1')

def task2():
    print('Выполняется задача 2')

# Создание и использование цикла событий
loop = SimpleEventLoop()
loop.add_task(task1) # Добавить задачу 1 в цикл событий
loop.add_task(task2) # Добавить задачу 2 в цикл событий
loop.run_forever() # Запустить цикл событий



