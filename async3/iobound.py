#########
# IO bound tasks


# reading file
with open('file.txt', 'r') as f:
    data = f.read()

# writing file
with open('file.txt', 'w') as f:
    f.write('Hello, world!')

###########################
import requests

# sending GET request
response = requests.get('http://www.python.org')

# sending POST request
response2 = requests.post('http://www.python.org', data={'key': 'value'})

########################
# Reading input from keyboard
name = input('Input your name: ')

# Output information
print(f'Hi {name}')

####################
import os

# Getting list of files in directory
files = os.listdir('/path/to/directory')

# Launching system command
os.system('ls -l')

####################
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('example.db')

# Создание курсора
c = conn.cursor()

# Выполнение SQL-запроса
c.execute("SELECT * FROM stocks WHERE symbol = 'RHAT'")

######################
import serial

# Открытие последовательного порта
ser = serial.Serial('/dev/ttyUSB0')

# Чтение данных из порта
data = ser.read(100)

######################3
from selenium import webdriver

# Открытие веб-браузера
driver = webdriver.Firefox()

# Переход на веб-сайт
driver.get('http://www.python.org')

