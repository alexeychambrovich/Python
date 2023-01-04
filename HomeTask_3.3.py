# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19



import random
import math
my_list = []
my_list_new = []
for _ in range(10):
    amount = random.randint(0,2)
    number = round(random.uniform(0, 10), amount)
    if number == int(number):
        my_list_new.append(int(number))
    else:
        f, _= math.modf(number)
        my_list_new.append(number)
        my_list.append((f))
        
print(my_list_new)
print(f'разница между максимальным и минимальным значением дробной части элементов равна: {max(my_list) - min(my_list)}')
