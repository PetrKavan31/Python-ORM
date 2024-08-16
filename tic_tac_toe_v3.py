board = list(".........")

def print_board():
    print("".join(board[:3]))
    print("".join(board[3:6]))
    print("".join(board[6:]))

def player_move():
    count = 1
    while count < 10:
        p = 'X' if count % 2 != 0 else 'O'
        position = int(input(f"Player {p} turn. Enter the position (1-9): "))
        if position > 9 or position < 1:
            print("Wrong number")
            continue
        count += 1
        print(count)
        position_number(position, p)
        print_board()
    print("End of game")

def position_number(position, p):
    for i in range((position-1),position):
        board[i] = p

player_move()