###########################################
# MODEL (attributes) + CONTROLLER (methods)

class TicTacToe:
    def __init__(self):
        self.board = ["."] * 9
        self.player_on_turn = 'X'

    def is_over(self):
        # TODO - proper game logic
        return self.board.count('.') == 0

    def make_move(self, position: int):
        # position is number 0-8
        # position = self.ask_player_position()
        # if position not in range(1,10):
        #     return True
        # update game state - mark position in board
        # change player on turn
        # TODO dodelej
        pass

    def is_number_valid(self, position):
        position = self.ask_player_position()
        if position not in range(1,10):
            return True


    def is_move_valid(self, position: int) -> bool:
        # position is number 0-8
        if self.board[position - 1] == '.':
            self.board[position - 1] = self.player_on_turn
            return True
            # print("Wrong number.")
            # continue
        #pass

    def ask_player_position(self):
        player_on_turn = self.player_on_turn
        return int(input(f"Player {player_on_turn} turn. Enter the position (1-9): "))

######################################
# VIEW

# def draw_board(board: list[str]):
    def draw_board(self):
        for i in range(0,9,3):
            print("".join(self.board[i:(i+3)]))


def get_user_input(game: TicTacToe) -> int:    # return number in the range 0 - 8
    # only return valid input
    while True:
        # print prompt "zadej"
        position = game.ask_player_position()
        # get input
        game.make_move(position)
        #game.is_move_valid(position)

        # check that input is a number between 1 - 9
        if not game.is_number_valid(position):
            print("Wrong number.")
            continue

        # check that the tile is not taken
        if not game.is_move_valid(position):
            print("The position is covered, make a move to another position.")
            continue

        self.player_on_turn = 'X' if self.player_on_turn == 'O' else 'O'
        # return if valid


def main():
    game = TicTacToe()
    while not game.is_over():
        # draw board - view
        game.draw_board()
        # TODO - dodelej kresleni

        # get user input - view
        position = get_user_input(game)

        # process input - pass user input to controller, controller updates model state
        game.make_move(position)


if __name__ == "__main__":
    main()