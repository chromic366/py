# Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках записаны N
# целых чисел Ai. Последняя строка содержит число X


# N = abs(int(input('Введите количество элементов списка: ')))
# element = input("Введите через пробел элементы списка: ").split()
# A_num = list(map(int, element))
# if len(A_num) != N:
#     print('Введенные элементы не соответствуют заявленному количеству!')
# else:
#     x = int(input('Введите число X, которое необходимо найти в списке: '))
#     count = 0
#     for i in range(N):
#         if A_num[i] == x:
#             count += 1
#     print(f'Число {x} встречается в списке  {count} раз')


# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai.
# Последняя строка  содержит число X

N = abs(int(input('Введите количество элементов списка: ')))
element= input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, element))
if len(A_num) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    x = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(x - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(x - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A_num[index]} в списке наиболее близко по величине к числу {x}')