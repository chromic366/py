# Напишите программу, которая на вход принимает два числа A и B, и
# возводит число А в целую степень B с помощью рекурсии.

# def power(num1, num2):
#     if num2 == 0:
#         return 1
#
#     return num1 * power(num1, num2 - 1)
#
#
# num = power(int(input('number: ')), int(input('degree: ')))
# print(f'number is {num}')


# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы

def summ(a, b):

    if b == 0:
        return a

    return summ(a + 1, b - 1)

summa = summ(int(input('a:')), int(input('b:')))
print(f'sum is {summa}')