# Игра "Крестики-нолики"

board = list(range(1, 10))
win_cod = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def GameFild():
    print("\n")
    print("\t_____ _____ _____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}  ".format(board[0], board[1], board[2]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}  ".format(board[3], board[4], board[5]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}  ".format(board[6], board[7], board[8]))
    print("\t_____|_____|_____")

def take_input(player):
    while True:
        print("\n")
        value = input('Куда поставить:  '+ player +'?')
        if not (value in '123456789'):
            print('Ошибочный ввод. Повторите ход')
            continue
        value = int(value)
        if str(board[value-1]) in 'XO':
           print("\n")
           print('Эта клетка уже занята')
           continue
        board[value-1] = player
        break

def check_win():
    for each in win_cod:
        if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
            return board[each[1]-1]
    else:
        return False


def main():
    counter = 0
    while True:
        GameFild()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = check_win()
            if winner:
              GameFild()
              print("\n")
              print(winner, 'Выиграл')
              break 
        counter +=1
        if counter > 8:
            GameFild()
            print("\n")
            print('Ничья!')
            break


main()

