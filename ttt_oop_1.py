class TicTacToe:
    def __init__(self):
        self.board = ["."] * 9
        self.player_on_turn = 'X'

    def is_over(self):
        # TODO - proper game logic
        return self.board.count('.') == 0

    def make_move(self, position: int):
        assert 0 <= position <= 8
        assert self.is_move_valid(position)
        self.board[position] = self.player_on_turn
        self.player_on_turn = 'X' if self.player_on_turn == 'O' else 'O'

    def is_move_valid(self, position: int) -> bool:
        assert 0 <= position <= 8
        return self.board[position] == '.'

######################################
# VIEW

def draw_board(board: list[str]):
    for i in range(0,9,3):
        print("".join(board[i:(i+3)]))
    # pass


def get_user_input(game: TicTacToe) -> int:    # return number in the range 0 - 8
    # only return valid input

    while True:
        # print prompt "zadej"
        # get input
        player_on_turn = game.player_on_turn
        position = int(input(f"Player {player_on_turn} turn. Enter the position (1-9): "))
   
       
        # check that input is a number between 1 - 9
        if position not in range(1, 10):
            draw_board(game.board)
            print("Wrong number.")
            continue

        # check that the tile is not taken
        if not game.is_move_valid(position - 1):
            draw_board(game.board)
            print("The position is covered, make a move to another position.")
            continue

        # return if valid
        return position - 1



def main():
    game = TicTacToe()
    while not game.is_over():
        # draw board - view
        draw_board(game.board)
        # TODO - dodelej kresleni

        # get user input - view
        position = get_user_input(game)

        # process input - pass user input to controller, controller updates model state
        game.make_move(position)
    
    draw_board(game.board)
    print("End of game.")

if __name__ == "__main__":
    main()