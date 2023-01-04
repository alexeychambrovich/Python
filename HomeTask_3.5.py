# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.[Негафибоначи]
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


f1 = 1
f2 = 1
list = [1, 1, ]
n = int(input('Введите число:  '))
my_listA = []
my_listB = []
def fibbonachi(n):
    i = 2
    f1 = 1
    f2 = 1
    while i < n:
        f1, f2 = f2, f2 + f1
        my_listA.append(f2)
        i += 1
    return(my_listA)   

def negafibbonachi(n):
    i = 0
    f1 = 1
    f2 = 1
    while i < n + 1:
        f1, f2 = f2, f1 - f2
        my_listB.append(f2)
        i += 1
    my_listB.reverse()
    return(my_listB)
negafibbonachi(n)
fibbonachi(n)
print(my_listB + list + my_listA)
  
    