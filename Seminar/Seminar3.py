# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

list_1  = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]

print(len(set(list_1)))

my_list = [1, 1, 2, 0, -1, 3, 4, 4, 3, -3, 0, 10, 11, 11]

for i in my_list:
    if my_list.count(i) > 1:
        for _ in range(my_list.count(i) - 1):
            my_list.remove(i)
print(len(my_list))