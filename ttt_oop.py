class TicTacToe:
    def __init__(self):
        self.board = ["."] * 9
        self.player_on_turn = 'X'

    def is_over(self):
        # TODO - proper game logic
        return self.board.count('.') == 0

    def make_move(self, player_on_turn, board):
        while not game.is_over():
            position = self.ask_player_position()
            if position not in range(1,10):
                print("Wrong number.")
                continue
            if board[position - 1] == '.':
                board[position - 1] = player_on_turn
            else: 
                print("The position is covered, make a move to another position.")
                continue
            player_on_turn = 'X' if player_on_turn == 'O' else 'O'
            game.print_board(game.board)
        print("End of game.")

    def print_board(self, board):
        for i in range(0,9,3):
            print("".join(board[i:(i+3)]))

    def ask_player_position(self):
        player_on_turn = game.player_on_turn
        return int(input(f"Player {player_on_turn} turn. Enter the position (1-9): "))

game = TicTacToe()

draw_board = game.board
game.print_board(draw_board)

play = game.player_on_turn
game.make_move(play, draw_board)