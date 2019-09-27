# This file contains the function to run the Chess Emulator
# Code is written assuming the initial position has a piece already present to move.

from board import Board 
from piece import Piece
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from queen import Queen
from rook import Rook
from king import King

def player_move(board_obj, initial, final, color):
    row, col = board_obj.chess_to_matrix_translator(final)
    obj = board_obj.board[row][col]

    if obj.piece_type == 'none':
        capture = False
    else:
        capture = True

    # print(capture)
    row2, col2 = board_obj.chess_to_matrix_translator(initial)   
    obj_to_move = board_obj.board[row2][col2] 

    if obj_to_move.move(initial, final, capture):
        board_obj.place(obj_to_move)
        board_obj.place(Piece(initial, color))

    return

b = Board()

b.place(Pawn('a2', 'White'))
b.place(Pawn('b2', 'White'))
b.place(Pawn('c2', 'White'))
b.place(Pawn('d2', 'White'))
b.place(Pawn('e2', 'White'))
b.place(Pawn('f2', 'White'))
b.place(Pawn('g2', 'White'))
b.place(Pawn('h2', 'White'))
b.place(Pawn('a7', 'Black'))
b.place(Pawn('b7', 'Black'))
b.place(Pawn('c7', 'Black'))
b.place(Pawn('d7', 'Black'))
b.place(Pawn('e7', 'Black'))
b.place(Pawn('f7', 'Black'))
b.place(Pawn('g7', 'Black'))
b.place(Pawn('h7', 'Black'))
b.place(Rook('a1', 'White'))
b.place(Rook('h1', 'White'))
b.place(Rook('a8', 'Black'))
b.place(Rook('h8', 'Black'))
b.place(Knight('b1', 'White'))
b.place(Knight('g1', 'White'))
b.place(Knight('b8', 'Black'))
b.place(Knight('g8', 'Black'))
b.place(Bishop('c1', 'White'))
b.place(Bishop('f1', 'White'))
b.place(Bishop('c8', 'Black'))
b.place(Bishop('f8', 'Black'))
b.place(King('e1', 'White'))
b.place(Queen('d1', 'White'))
b.place(Queen('d8', 'Black'))
b.place(King('e8', 'Black'))

b.disp()
print("\n")

cnt = 0

while True:
    pos = input()
    pos = pos.split(" ")
    initial = pos[0]
    final = pos[1]

    if cnt%2 == 0:
        player_move(b, initial, final, 'White')
    else:
        player_move(b, initial, final, 'Black')
    
    b.disp()
    print("\n")
    cnt += 1








