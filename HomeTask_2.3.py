# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random
n = int(input(f'введите количество значений для создания списка: '))
my_list = []
for num in range(1, n+1):
    my_list.append(num) 
print(f'сформированный список: {my_list}')

def mix_list(my_list): # Создаем копию, поскольку мы не должны изменять оригинал
    list = my_list[:]   # Цикл от 0 до длины списка -1
    list_length = len(my_list)
    for i in range(list_length): # Получение случайного индекса
        index = random.randint(0, list_length - 1) # Замена
        temp = list[i]
        list[i] = list[index]
        list[index] = temp # Возвращаем список
    return list

print(f'перемешанный список: {mix_list(my_list)}')


