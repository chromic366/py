# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# list_1  = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
#
# print(len(set(list_1)))
#
# my_list = [1, 1, 2, 0, -1, 3, 4, 4, 3, -3, 0, 10, 11, 11]
#
# for i in my_list:
#     if my_list.count(i) > 1:
#         for _ in range(my_list.count(i) - 1):
#             my_list.remove(i)
# print(len(my_list))

# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

# lst = [1, 2, 3, 4, 5]
# k = 2
# for i in range(k):
#     lst.insert(0, lst.pop())
# print(lst)
#
# lst = [1, 2, 3, 4, 5]
# a1 = lst[-k:]
# a2 = lst[:-k]
# print(a1 + a2)


# Напишите программу для печати всех уникальных
# значений в словаре.

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
          {" VIII":" S007 "}]

set_n = set()

for dct in list_1:
    set_n.add(str(*dct.values()).strip())

print(set_n)