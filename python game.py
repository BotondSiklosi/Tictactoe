import random


def draw_matrix():
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            print(matrix[i][j], end=' ')
        print()
    print()

def menu():
    print("1 : 1 player game!")
    print("2 : 2 player game!")
    print("3 : options")
    print("4 : exit")
    menu_number = int(input("select: "))
    return menu_number


def options():
    set_map_size = int(input("Select map size: "))
    set_win_amount = int(input("select win amount: "))
    return set_map_size, set_win_amount


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def win_check():
    number = 0
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE-WIN_AMOUNT):
            if matrix[i][j] != 0:
                for k in range(WIN_AMOUNT):
                    if matrix[i][j] == matrix[i][j+k]:
                        number += 1
                        if number == WIN_AMOUNT:
                            return number
                    number = 0
    number = 0

    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            if matrix[i][j] != 0:
                for k in range(WIN_AMOUNT):
                    if matrix[i][j] == matrix[i-k][j]:
                        number += 1
                        if number == WIN_AMOUNT:
                            return number
                    number = 0
    number = 0

    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            if matrix[i][j] != 0:
                for k in range(WIN_AMOUNT):
                    if matrix[i][j] == matrix[i-k][j+k]:
                        number += 1
                        if number == WIN_AMOUNT:
                            return number
                    number = 0
    number = 0

    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            if matrix[i][j] != 0:
                for k in range(WIN_AMOUNT):
                    if matrix[i][j] == matrix[i-k][j-k]:
                        number += 1
                        if number == WIN_AMOUNT:
                            return number
                    number = 0
    


def turne(playerletter):
    if playerletter == "x":
        return "x"
    else:
        return "o"

def playermove():
    valt = []
    valt = list(input("move: "))
    valt1 = int(valt[0])
    valt2 = int(valt[1])
    matrix[valt1][valt2] = playerletter
    return valt1, valt2


def change_turn(turn):
    if turn == "player1":
        return "player2"
    else:
        return "player1"

print("Welcome in tic tac toe! ")
starter = 0
while starter == 0:
    MAP_SIZE = 3
    WIN_AMOUNT = 3
    while True:
        select = 0
        select = menu()
        if select == 1:
            print("Work in progress!")
            continue
        elif select == 2:
            break
        elif select == 3:
            MAP_SIZE, WIN_AMOUNT = options()
            continue
        elif select == 4:
            starter = 2
            break

        else:
            print("invalid number!")
            continue
    print(starter)
    matrix = [["⬚" for x in range (MAP_SIZE)]for y in range (MAP_SIZE)]
    player1letter, player2letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    playerletter = ""

    while True:
        playerletter = turne(playerletter)
        print ("player's "+ turn + " round! ")
        valt1, valt2 = playermove()
        win_check()
        if win_check() == WIN_AMOUNT:
            print(turn,"won the game!! ")
            break
        elif tie_check() == True:
            print ("Draw match! ")
            break
        else:
            turn = change_turn(turn)
            continue

    answer = input("would you like to restart?(yes or no) ")
    if answer == "y":
        continue
    else:
        break
      
        
print("thanks for the game!! :)")