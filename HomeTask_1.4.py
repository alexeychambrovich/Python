# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


a = int(input(f'введите номер четверти от 1 до 4: '))

if  a == 1:
    print(f'координаты точки Х > 0 и Y > 0')
elif  a == 2:
    print(f'координаты точки Х < 0 и Y > 0')
elif a == 3:
    print(f'координаты точки Х < 0 и Y < 0')
elif a == 4:
    print(f'координаты точки Х > 0 и Y < 0')
else:
    print(f'вы ввели недопустимое значение, введите номер четверти от 1 до 4')

