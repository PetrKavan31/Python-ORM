# O.O
# X.X
# .OX

board = [
    list("..."),
    list("..."),
    list("..."),
] # Model

def print_board(): # View
    i = 0
    while i < len(board):
        print("".join(board[i]))
        i+=1

def player_move(): # Controller and View
    count = 1
    while count < 10:    
        player = 'X' if count % 2 != 0 else 'O'
        position = int(input(f"Player {player} turn. Enter the position (1-9): "))
        if position > 9 or position < 1:
            print("Wrong number.")
            continue
        count += 1
        position_number(position, player)
        print_board()
    print("End of game.")

def position_number(position, player): # View
    if position == 1:
        board[0][0] = player
    elif position == 2:
        board[0][1] = player
    elif position == 3:
        board[0][2] = player
    elif position == 4:
        board[1][0] = player
    elif position == 5:
        board[1][1] = player
    elif position == 6:
        board[1][2] = player
    elif position == 7:
        board[2][0] = player
    elif position == 8:
        board[2][1] = player
    elif position == 9:
        board[2][2] = player

def play_game(): # View
    print_board()
    player_move()

play_game()