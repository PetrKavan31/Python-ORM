# O.O
# X.X
# .OX

board = [
    list("..."),
    list("..."),
    list("..."),
]
def print_board():
    i = 0
    while i < len(board):
        print("".join(board[i]))
        i+=1

def player_move():
    count = 1
    while count < 10:    
        p = 'X' if count % 2 != 0 else 'O'
        position = int(input(f"Player {p} turn. Enter the position (1-9): "))
        count += 1
        position_number(position, p)
        print_board()

def position_number(position, p):
    if position == 1:
        board[0][0] = p
    elif position == 2:
        board[0][1] = p
    elif position == 3:
        board[0][2] = p
    elif position == 4:
        board[1][0] = p
    elif position == 5:
        board[1][1] = p
    elif position == 6:
        board[1][2] = p
    elif position == 7:
        board[2][0] = p
    elif position == 8:
        board[2][1] = p
    elif position == 9:
        board[2][2] = p

print_board()
player_move()