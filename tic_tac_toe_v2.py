# O.O
# X.X
# .OX

board = [
    list("..."),
    list("..."),
    list("..."),
] # Model

def print_board(): # View
    for i in board:
        print("".join(i))
    
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
    board[(position - 1) // 3][(position - 1) % 3] = player
    
def play_game(): # View
    print_board()
    player_move()

play_game()