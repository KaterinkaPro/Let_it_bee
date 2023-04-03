# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# first_element = int(input('Введите первую цифру: '))
# difference = int(input('Введите разность: '))
# numberOfElements = int(input('Введите количество элементов: '))


# for i in range(first_element, numberOfElements):
#     print(first_element + (i - 1) * difference)





# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
from random import randint

list = []

min = int(input('Введите минимальное число: '))
max = int(input('Введите максимальное число: '))

list = [randint(-21, 21) for i in range(10)]
print(list)

for i in range(len(list)):
    if min <= list[i] <= max:
        print(list[i], end=' ')