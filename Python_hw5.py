# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# def sqr(a, b):
#     if b == 0:
#         return 1
#     elif b % 2 == 0:
#         return sqr(a * a, b // 2)
#     else:
#         return a * sqr(a, b - 1)
    
# a = int(input("Введите число A: "))
# b = int(input("Введите степень B: "))

# result = sqr(a, b)

# print(f'{a} * {b} = {result}')


# Напишите рекурсивную функцию sum(a, b), возвращающую 
# сумму двух целых неотрицательных чисел. Из всех а
# рифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)
    
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))  

result = sum(a, b)

print(f'{a} + {b} = {result}')