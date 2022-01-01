import numpy as np
from piece import ChessPiece

class Main:
    def __init__(self):        
        # Some variables
        char_pawn = "P"
        char_row = ["R", "Kn", "B", "Q", "K", "B", "N", "R"]
        board = np.empty((8, 8), dtype=str)
        board.fill("0")
        board[1,:] = board[6,:] = char_pawn
        board[0,:] = board[7,:] = char_row
        self.board = board
    def run_game(self):
        turn = "White"
        while True:
            user_input = input(f"{turn}: Please make your move\n") # Stores user's move in <type><location> form: e.g. Rd4
            # Switch sides after every move
            if turn == "White":
                turn = "Black"
            elif turn == "Black":
                turn = "White"
            
            # Print Board
            for row in self.board:
                print(' '.join(row))

game = Main()
game.run_game()