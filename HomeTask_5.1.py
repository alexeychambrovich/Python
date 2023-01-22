
import random 

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28:  "))
    if x < 1 or x > 28:
        x = int(input(f" {name}, введите корректное количество конфет:  "))
    return x
    
def p_print(name, k, count, value):
    print(f"Ходил {name}, он взял {k} конфет, теперь у него {count} конфет. На столе осталось {value} конфет")



value = random.randint(29, 300)
print(f"На столе лежало: {value}")

Player1 = input ("Введите имя первого игрока: ")
print("Свами будет играть бот Федя")
Player2 = str('Бот Федя')
flag = random.randint(0, 2)
# print(flag)
if flag == 1:
    print(f"Первый ходит {Player1}")
else:
    print(f"Первый ходит {Player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(Player1)
        counter1 += k
        value -= k
        flag = False
        p_print(Player1, k, counter1, value)
    else:
        k = random.randint(1, 29)
        counter2 += k
        value -= k
        flag = True
        p_print(Player2, k, counter2, value)

if flag:
    print(f"Выиграл {Player1}")
else:
    print(f"Выиграл {Player2}")
