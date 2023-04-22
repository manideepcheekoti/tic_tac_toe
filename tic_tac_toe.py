import numpy as np
Board = np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
p1S = 'X'
p2S = 'O'


def check_rows(symbol):
    for r in range(3):  # for 3 rows
        count = 0
        for c in range(3):  # for iterating each cell # total 3 cells
            if Board[r][c] == symbol:
                count = count + 1
            if count == 3:
                print(symbol, "Won")
                return True
    return False


def check_cols(symbol):
    for c in range(3):  # for 3 coulmns
        count = 0
        for r in range(3):
            if Board[r][c] == symbol:
                count = count + 1
            if count == 3:
                print(symbol, "Won")
                return True
    return False


def check_diagonals(symbol):
    if Board[0][2] == Board[1][1] and Board[1][1] == Board[2][0] and Board[1][1] == symbol:
        print(symbol, "Won")
        return True
    if Board[0][0] == Board[1][1] and Board[1][1] == Board[2][2] and Board[1][1] == symbol:
        print(symbol, "Won")
        return True
    return False


def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)


def place(symbol):
    print(np.matrix(Board))
    while(1):
        row = int(input("Enter row - 1 or 2 or 3:"))
        col = int(input("Enter column - 1 or 2 or 3:"))
        if row > 0 and row < 4 and col > 0 and col < 4 and Board[row - 1][col - 1] == '-':
            break
        else:
            print("Invalid input. Please enter again")
    Board[row - 1][col - 1] = symbol


def play():
    for turn in range(9):
        if turn % 2 == 0:
            print("X turn.")
            place(p1S)
            if won(p1S):
                break
        else:
            print("O turn.")
            place(p2S)
            if won(p2S):
                break
    if not(won(p1S)) and not(won(p2S)):
        print("Draw.")


play()
