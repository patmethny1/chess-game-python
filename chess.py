import numpy as np
from piece import ChessPiece


'''
TODO: 
    user_input:
        - exd4 (read-in moves taking another piece)
        - Nce4 (read-in moves where two pieces can go to same square, Knight on c to e4)
    - convert moves to 2d array coordinates (a1 --> (0, 7))
'''
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
            # Reading user input
            if user_input in ["O-O-O", "O-O"]: # If user gives castling (WARNING: does not check whether castling is available)
                if user_input == "O-O-O":
                    castling = "Q" # Q for Queenside castling
                elif user_input == "O-O":
                    castling = "K" # K for Kingside castling
            else: # If user isn't castling
                if len(user_input) == 2: # if user only gives coordinates (WARNING: does not check if user_input is of invalid type)
                    piece_type = "P" # Piece type is pawn
                elif len(user_input) > 2:
                    piece_type = user_input[0]
                coordinate = user_input[-2:]
                print(coordinate) # DEBUG
            
            # Print Board
            for row in self.board:
                print(' '.join(row))
            break # remove

