class TicTacToe:
    def __init__(self):
        self.board = ["."] * 9
        self.player_on_turn = 'X'

    def is_over(self):
        # TODO - proper game logic
        return self.board.count('.') == 0

    def make_move(self):
        while not self.is_over():
            position = self.ask_player_position()
            if position not in range(1,10):
                print("Wrong number.")
                continue
            if self.board[position - 1] == '.':
                self.board[position - 1] = self.player_on_turn
            else: 
                print("The position is covered, make a move to another position.")
                continue
            self.player_on_turn = 'X' if self.player_on_turn == 'O' else 'O'
            self.print_board()
        print("End of game.")

    def print_board(self):
        for i in range(0,9,3):
            print("".join(self.board[i:(i+3)]))

    def ask_player_position(self):
        player_on_turn = self.player_on_turn
        return int(input(f"Player {player_on_turn} turn. Enter the position (1-9): "))

def main():
    game = TicTacToe()
    game.print_board()
    game.make_move()

if __name__ == "__main__":
    main()
