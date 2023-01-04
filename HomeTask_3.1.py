# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = int(input(f'введите количество чисел в списке n: '))
my_list = []
for num in range(1, n+1):
    my_list.append(num)   
print(my_list)
a = sum(my_list[i] for i in range(1, len(my_list), 2))
print(f'сумма элементов с нечетным индексом равна: {a}')