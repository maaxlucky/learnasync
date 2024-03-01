# Арифметические операции
result = (3 + 4) * 5 / 2

# Логические операции
is_true = (5 > 3) and (2 < 4)


# Цикл for
for i in range(10):
    print(i)

# Цикл while
i = 0
while i < 10:
    print(i)
    i += 1


# Условные операторы
x = 10
if x > 5:
    print('x больше 5')
elif x < 5:
    print('x меньше 5')
else:
    print('x равно 5')
    
# Определение функции
def square(x):
    return x ** 2

# Вызов функции
result = square(5)


# Сортировка списка
numbers = [5, 2, 3, 1, 4]
numbers.sort()

# Поиск в списке
index = numbers.index(3)


from PIL import Image

# Открытие изображения
img = Image.open('image.jpg')

# Применение фильтра
img = img.filter(ImageFilter.BLUR)

# Сохранение изображения
img.save('blurred_image.jpg')


from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Загрузка данных
iris = load_iris()
X, y = iris.data, iris.target

# Обучение модели
clf = RandomForestClassifier()
clf.fit(X, y)


import numpy as np

# Создание массива
x = np.array([1, 2, 3, 4, 5])

# Вычисление синуса для каждого элемента массива
y = np.sin(x)


from cryptography.fernet import Fernet

# Генерация ключа
key = Fernet.generate_key()

# Создание объекта шифрования
cipher = Fernet(key)

# Шифрование сообщения
message = b"Hello, World!"
encrypted_message = cipher.encrypt(message)