# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
start_list = [2, -5, 8, 9, -25, 25, 4]
i = 0
sqrt_list = []
while i < len(start_list):
    if start_list[i] >= 0:
        a = math.sqrt(start_list[i])
        if a == int(a):
            sqrt_list.append(int(a))
    i += 1
print("Новый список с корнями: ", sqrt_list)
print("-------------------------------------------------------------")
# # Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# # Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# # Склонением пренебречь (2000 года, 2010 года)
#
date = input("Введите дату в формате dd.mm.yyyy: ")
#date = "25.09.1992"
day = date[0:2]
month = date[3:5]
year = date[6:]


day = int(day)
month = int(month)
day_string10 = ""
month_string = ["января", "февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]
if day > 31 or month > 12:
    print("Такой даты не существует")
    exit(0)
if day > 20 and day < 30:
    day_string10 = "двадцать"
    day = day - 20
if day == 30:
    day_string = "тридцатое"
if day == 31:
    day_string = "тридцать первое"

if day <= 20:
    if day == 1:
        day_string = "первое"
    elif day == 2:
        day_string = "второе"
    elif day == 3:
        day_string = "третье"
    elif day == 4:
        day_string = "четвёртое"
    elif day == 5:
        day_string = "пятое"
    elif day == 6:
        day_string = "шестое"
    elif day == 7:
        day_string = "седьмое"
    elif day == 8:
        day_string = "восьмое"
    elif day == 9:
        day_string = "девятое"
    elif day == 10:
        day_string = "десятое"
    elif day == 11:
        day_string = "одиннадцатое"
    elif day == 12:
        day_string = "двенадцатое"
    elif day == 13:
        day_string = "тринадцатое"
    elif day == 14:
        day_string = "четырнадцатое"
    elif day == 15:
        day_string = "пятнадцатое"
    elif day == 16:
        day_string = "шестнадцатое"
    elif day == 17:
        day_string = "семнадцатое"
    elif day == 18:
        day_string = "восемнадцатое"
    elif day == 19:
        day_string = "девятнадцатое"
    elif day == 20:
        day_string = "дведцатое"

print("Буквенная запись даты: ",day_string10,day_string,month_string[month-1],year,"года")
print("-------------------------------------------------------------")

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
n = int(input("Введите чило элементов списка: "))
random_list = []
i = 0
while i < n:
    m = random.randint(-100, 100)
    random_list.append(m)
    i += 1
print(random_list)
print("-------------------------------------------------------------")
# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random
n = 10
random_list = []
i = 0
while i < n:
    m = random.randint(0, 6)
    random_list.append(m)
    i += 1
a = set(random_list)
print("Исходный список: ",random_list)
a = list(a)
print("Задание а: ",a)

b = []
j = 0
while j < len(a):
    n = 0
    i = 0
    while i < len(random_list):
        if a[j] == random_list[i]:
            n += 1
        i += 1
    if n == 1:
        b.append(a[j])
    j += 1
print("Задание б: ",b)
