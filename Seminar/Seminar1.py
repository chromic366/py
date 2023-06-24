# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

# n = int(input())
# m = int(input())2
#
# print((m + n - 1) // n)


# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них

# a = int(input())
# b = int(input())
# c = int(input())
#
# part_a = a // 2 + a % 2
# part_b = b // 2 + b % 2
# part_c = c // 2 + c % 2
#
# print(part_a + part_b + part_c)


# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.


# i = int(input("Введите число "))
# j = int(input("Введите число "))
#
# if i == j:
#     print("Не хватает данных")
# else:
#     print(i + j - 1)


# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400


# year = int(input())
#
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("yes")
# else:
#     print("no")


# Шахматный король ходит по горизонтали, вертикали и диагонали,
# но только на 1 клетку. Даны две различные клетки шахматной доски,
# определите, может ли  король попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие
# номер столбца и номер строки сначала для первой клетки,
# потом для второй клетки. Программа должна вывести YES,
# если из первой клетки ходом короля можно попасть во вторую или NO
# в противном случае. # В случае, если хотя бы одно из введенных
# чисел не лежит в диапазоне от 1 до 8, выведите строку "Ошибка!".

# king_v = int(input())
# king_g = int(input())
#
# next_turn_v = int(input())
# next_turn_g = int(input())
#
# def chekInput(king_v, king_g, next_turn_v, next_turn_g):
#     if(king_v in range(1, 9) and
#         king_v in range(1, 9) and
#         next_turn_v in range(1, 9) and
#         next_turn_g in range(1, 9)):
#         return True
#     else:
#         return False
#
# def cheas(king_v, king_g, next_turn_v, next_turn_g):
#
#     if(chekInput(king_v, king_g, next_turn_v, next_turn_g)):
#         if(abs(next_turn_v - king_v) <= 1 and abs(next_turn_g - king_g) <= 1):
#             print("yes")
#         else:
#             print("no")
#
#     else:
#         print("no")
#
# cheas(king_v, king_g, next_turn_v, next_turn_g)


# Треугольник существует только тогда, когда сумма любых двух
# его сторон больше третьей. Дано a, b, c - стороны
# предполагаемого треугольника. Требуется сравнить длину
# каждого отрезка-стороны с суммой двух других. Если хотя
# бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")