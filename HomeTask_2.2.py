# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример: Для n=4 -> [2, 2.25, 2.37, 2.44]  Сумма 9.06

n = int(input(f'введите количество чисел последовательности n: '))
my_list = []
for num in range(1, n+1):
    number = (1+1/num)**num
    my_list.append(number)   
print(my_list)
print(f'сумма элементов равна: {sum(my_list)}')  

