# O.O
# X.X
# .OX

board = ["."] * 9 # Model

def print_board(): # View
    for i in range(3):
        print("".join(board[(i * 3):((i + 1) * 3)]))

def player_move(): # Controller and View
    count = 1
    while count < 10:
        player = 'X' if count % 2 != 0 else 'O'
        position = int(input(f"Player {player} turn. Enter the position (1-9): "))
        if position not in range(1,10):
            print("Wrong number.")
            continue
        count += 1
        position_number(position, player)
        print_board()
    print("End of game.")

def position_number(position, player): # View
    board[(position - 1)] = player  

def play_game(): # View
    print_board()
    player_move()

play_game()